"""Geometry helpers: render context, hand-drawn displacement, lattice sampling, clipping."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import shapely
from shapely.geometry import MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry

from . import rand as R

MAX_CELLS = 600_000  # safety valve for absurd texture densities


@dataclass
class Ctx:
    """Everything a generator needs to know about the drawing.

    ``u`` is the map scale as *map units per paper millimetre* (1:500 in metres
    -> 0.5). Generators multiply paper sizes by ``u`` to get ground sizes.
    ``period`` (width, height in map units) switches all randomness to be
    periodic so the output tiles seamlessly.
    """

    u: float = 1.0
    lod: int = 2
    seed: int = 0
    wobble: float = 1.0
    period: tuple | None = None

    def mm(self, v):
        return v * self.u

    # -- periodic fitting -------------------------------------------------
    def fit(self, size: float, axis: int = 0, even: bool = False) -> tuple[float, int | None]:
        """Snap a lattice step (map units) so it divides the tile; returns (step, count)."""
        if self.period is None:
            return size, None
        n = max(2 if even else 1, round(self.period[axis] / size))
        if even and n % 2:
            n += 1
        return self.period[axis] / n, n

    def noise(self, x, y, cell_mm: float, salt: int = 0) -> np.ndarray:
        """Smooth noise field in [-1, 1]; features about ``cell_mm`` wide on paper."""
        cx, nx = self.fit(cell_mm * self.u, 0)
        if self.period is None:
            return R.noise2(x, y, cx, self.seed, salt)
        cy, ny = self.fit(cell_mm * self.u, 1)
        # noise2 has one cell size; stretch y so its cells are cy tall
        return R.noise2(x, np.asarray(y) * (cx / cy), cx, self.seed, salt, period=(nx, ny))

    def rand_at(self, x, y, salt: int = 0, grain_mm: float = 0.41) -> np.ndarray:
        """Uniform [0,1) keyed on position: equal positions give equal values."""
        gx, nx = self.fit(grain_mm * self.u, 0)
        gy, ny = self.fit(grain_mm * self.u, 1)
        # the offsets keep regular pattern lattices off the cell borders, where rounding would decide the cell
        i = np.floor(np.asarray(x, dtype=np.float64) / gx + 0.3183098861).astype(np.int64)
        j = np.floor(np.asarray(y, dtype=np.float64) / gy + 0.7320508075).astype(np.int64)
        if nx is not None:
            i, j = i % nx, j % ny
        return R.rand(i, j, self.seed, salt)


# --------------------------------------------------------------------------- basics

def polygons_of(geom: BaseGeometry) -> list[Polygon]:
    if geom is None or geom.is_empty:
        return []
    if isinstance(geom, Polygon):
        return [geom]
    if isinstance(geom, MultiPolygon):
        return [g for g in geom.geoms if not g.is_empty]
    if hasattr(geom, "geoms"):
        out: list[Polygon] = []
        for g in geom.geoms:
            out.extend(polygons_of(g))
        return out
    return []


def _signed_area(r: np.ndarray) -> float:
    return 0.5 * float(np.sum(r[:-1, 0] * r[1:, 1] - r[1:, 0] * r[:-1, 1]))


def rings_of(geom: BaseGeometry) -> list[np.ndarray]:
    """All rings of a polygonal geometry as (N, 2) arrays: shells counter-clockwise, holes clockwise.

    With this orientation the even-odd and the non-zero fill rule give the same
    picture, so SVG, Matplotlib and QGIS agree on where the holes are.
    """
    rings = []
    for poly in polygons_of(geom):
        ext = np.asarray(poly.exterior.coords)[:, :2]
        rings.append(ext if _signed_area(ext) >= 0 else ext[::-1])
        for hole in poly.interiors:
            h = np.asarray(hole.coords)[:, :2]
            rings.append(h if _signed_area(h) <= 0 else h[::-1])
    return rings


def lines_of(geom: BaseGeometry) -> list[np.ndarray]:
    if geom is None or geom.is_empty:
        return []
    t = geom.geom_type
    if t in ("LineString", "LinearRing"):
        return [np.asarray(geom.coords)[:, :2]]
    if t in ("Polygon", "MultiPolygon"):
        return rings_of(geom)
    if hasattr(geom, "geoms"):
        out = []
        for g in geom.geoms:
            out.extend(lines_of(g))
        return out
    return []


def points_of(geom: BaseGeometry) -> np.ndarray:
    if geom is None or geom.is_empty:
        return np.empty((0, 2))
    t = geom.geom_type
    if t == "Point":
        return np.array([[geom.x, geom.y]])
    if t == "MultiPoint":
        return np.array([[g.x, g.y] for g in geom.geoms])
    c = geom.representative_point() if t in ("Polygon", "MultiPolygon") else geom.centroid
    return np.array([[c.x, c.y]])


def inset(region: BaseGeometry, dist: float) -> BaseGeometry:
    if dist <= 0:
        return region
    return region.buffer(-dist, join_style="mitre")


def rotate(xy: np.ndarray, angle_deg: float) -> np.ndarray:
    if not angle_deg:
        return xy
    a = math.radians(angle_deg)
    c, s = math.cos(a), math.sin(a)
    return np.column_stack([xy[:, 0] * c - xy[:, 1] * s, xy[:, 0] * s + xy[:, 1] * c])


def main_angle(poly: BaseGeometry) -> float:
    """Direction (degrees, 0..180) of the long side of the minimum rotated rectangle."""
    try:
        rect = poly.minimum_rotated_rectangle
        c = np.asarray(rect.exterior.coords)
    except Exception:
        return 0.0
    e1, e2 = c[1] - c[0], c[2] - c[1]
    e = e1 if np.hypot(*e1) >= np.hypot(*e2) else e2
    return math.degrees(math.atan2(e[1], e[0])) % 180.0


# --------------------------------------------------------------------------- hand-drawn line

def densify(coords: np.ndarray, step: float, ctx: "Ctx | None" = None) -> np.ndarray:
    """Insert points along a polyline at ground-anchored positions, at most ``step`` apart.

    The inserted points sit where the distance along each segment's supporting
    line, measured from the map origin, is a multiple of ``step``. They depend
    on the line only, not on where a segment starts or ends, so a shared edge
    is sampled identically from both sides, from a longer or shorter piece of
    the same line, and in every pattern tile. Original vertices are kept.
    """
    p = np.asarray(coords, dtype=np.float64)
    m = len(p) - 1
    if m < 1 or step <= 0:
        return p
    a, d = p[:-1], np.diff(p, axis=0)
    ln = np.hypot(d[:, 0], d[:, 1])
    ok = ln > 0
    e = np.zeros_like(d)
    e[ok] = d[ok] / ln[ok, None]
    st = np.full(m, float(step))
    if ctx is not None and ctx.period is not None:
        proj = ctx.period[0] * np.maximum(np.abs(e[:, 0]), np.abs(e[:, 1]))
        good = proj > 0
        st[good] = proj[good] / np.maximum(1.0, np.round(proj[good] / step))
    sa = np.einsum("ij,ij->i", a, e)
    eps = 1e-7 * st
    k0 = np.floor((sa + eps) / st).astype(np.int64) + 1
    k1 = np.ceil((sa + ln - eps) / st).astype(np.int64) - 1
    n = np.where(ok, np.maximum(0, k1 - k0 + 1), 0)
    total = int(n.sum())
    if total == 0 or total > 2_000_000:
        return p
    starts = np.cumsum(n) - n
    idx = np.repeat(np.arange(m), n)
    within = np.arange(total) - np.repeat(starts, n)
    s_at = (np.repeat(k0, n) + within) * st[idx]
    pts = a[idx] + (s_at - sa[idx])[:, None] * e[idx]
    out = np.empty((m + 1 + total, 2))
    vpos = np.arange(m + 1) + np.concatenate([[0], np.cumsum(n)])
    out[vpos] = p
    out[vpos[idx] + 1 + within] = pts
    return out


def wobble(coords: np.ndarray, ctx: Ctx, amp: float = 0.09, wave: float = 7.0,
           step: float = 1.1, salt: int = 0) -> np.ndarray:
    """Hand-drawn version of a polyline.

    Points are displaced by a smooth noise *field* anchored to the ground, not
    by noise along the line. Two polygons that share an edge therefore get the
    identical wobbly edge, and corners stay sharp. ``amp`` is the maximum length
    of the displacement in paper millimetres; at the default (0.09 mm on a
    0.18 mm outline) the ink always covers the true edge.
    """
    a = amp * ctx.wobble
    if a <= 0:
        return np.asarray(coords, dtype=np.float64)
    p = densify(coords, step * ctx.u, ctx)
    x, y = p[:, 0], p[:, 1]
    dx = ctx.noise(x, y, wave, 7001 + salt) + 0.35 * ctx.noise(x, y, wave * 0.45, 7003 + salt)
    dy = ctx.noise(x, y, wave, 7002 + salt) + 0.35 * ctx.noise(x, y, wave * 0.45, 7004 + salt)
    d = np.column_stack([dx, dy]) / 1.35
    d /= np.maximum(np.hypot(d[:, 0], d[:, 1]), 1.0)[:, None]  # bound the length, not each axis
    return p + (a * ctx.u) * d


# --------------------------------------------------------------------------- lattice sampling

def scatter(region: BaseGeometry, ctx: Ctx, spacing: float, *, salt: int = 0,
            jitter: float = 0.42, stagger: bool = True, keep: float = 1.0,
            inset_mm: float = 0.0, clump: float = 0.0, aspect: float = 1.0):
    """Jittered lattice points inside ``region``.

    ``spacing`` is in paper mm. Returns ``x, y, stream`` where ``stream`` hands
    out further independent random arrays for the accepted points. The lattice
    is anchored to the map origin, so it does not depend on the polygon.
    """
    empty = (np.empty(0), np.empty(0), R.Stream(np.empty(0, np.int64), np.empty(0, np.int64), ctx.seed, salt))
    target = inset(region, inset_mm * ctx.u) if inset_mm > 0 else region
    if target.is_empty:
        return empty
    sx, nx = ctx.fit(spacing * ctx.u, 0)
    sy, ny = ctx.fit(spacing * ctx.u * aspect * (0.8660254 if stagger else 1.0), 1, even=stagger)
    minx, miny, maxx, maxy = target.bounds
    i0, i1 = math.floor(minx / sx) - 1, math.ceil(maxx / sx) + 1
    j0, j1 = math.floor(miny / sy) - 1, math.ceil(maxy / sy) + 1
    if (i1 - i0) * (j1 - j0) > MAX_CELLS:
        f = math.sqrt((i1 - i0) * (j1 - j0) / MAX_CELLS)
        return scatter(region, ctx, spacing * f * 1.01, salt=salt, jitter=jitter, stagger=stagger,
                       keep=keep, inset_mm=inset_mm, clump=clump, aspect=aspect)
    I, J = np.meshgrid(np.arange(i0, i1 + 1, dtype=np.int64), np.arange(j0, j1 + 1, dtype=np.int64))
    I, J = I.ravel(), J.ravel()
    hi, hj = (I % nx, J % ny) if nx is not None else (I, J)
    base = salt * 1000
    x = (I + 0.5 + (0.5 * (J & 1) if stagger else 0.0) + jitter * R.rand_pm(hi, hj, ctx.seed, base + 1)) * sx
    y = (J + 0.5 + jitter * R.rand_pm(hi, hj, ctx.seed, base + 2)) * sy
    m = shapely.contains_xy(target, x, y)
    if keep < 1.0 or clump > 0:
        p = np.full(len(x), keep)
        if clump > 0:
            p = p * (1.0 + clump * ctx.noise(x, y, 22.0, base + 3))
        m &= R.rand(hi, hj, ctx.seed, base + 4) < p
    return x[m], y[m], R.Stream(hi[m], hj[m], ctx.seed, salt)


# --------------------------------------------------------------------------- clipping

def _to_linestrings(lines) -> np.ndarray:
    if isinstance(lines, np.ndarray) and lines.ndim == 3:
        return shapely.linestrings(lines) if len(lines) else np.empty(0, dtype=object)
    lines = [l for l in lines if len(l) >= 2]
    if not lines:
        return np.empty(0, dtype=object)
    counts = np.fromiter((len(l) for l in lines), dtype=np.int64, count=len(lines))
    coords = np.concatenate(lines)
    return shapely.linestrings(coords, indices=np.repeat(np.arange(len(lines)), counts))


def _split(geoms: np.ndarray) -> list[np.ndarray]:
    if len(geoms) == 0:
        return []
    coords, idx = shapely.get_coordinates(geoms, return_index=True)
    if len(coords) == 0:
        return []
    cuts = np.flatnonzero(np.diff(idx)) + 1
    return np.split(coords, cuts)


def clip_lines(lines: list[np.ndarray], region: BaseGeometry, whole_only: bool = False) -> list[np.ndarray]:
    """Clip polylines to a polygon. With ``whole_only`` lines that cross the edge are dropped."""
    geoms = _to_linestrings(lines)
    if len(geoms) == 0:
        return []
    shapely.prepare(region)
    inside = shapely.contains_properly(region, geoms)
    out = _split(geoms[inside])
    if whole_only:
        return out
    rest = geoms[~inside]
    if len(rest):
        rest = rest[shapely.intersects(region, rest)]
    if len(rest):
        parts = shapely.get_parts(shapely.intersection(rest, region))
        parts = parts[(shapely.get_type_id(parts) == 1) & ~shapely.is_empty(parts)]
        out.extend(_split(parts))
    return out


def segments(x0, y0, x1, y1) -> list[np.ndarray]:
    """Arrays of endpoints -> list of 2-point polylines."""
    a = np.stack([np.column_stack([x0, y0]), np.column_stack([x1, y1])], axis=1)
    return list(a)

"""From features to a display list: fills, textures, outlines, lines and point symbols."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from typing import Any, Iterable

import numpy as np
from shapely.geometry import box, shape
from shapely.geometry.base import BaseGeometry

from .. import colormath as C
from ..catalog import Catalog, Element
from . import geom as G
from . import rand as R
from .geom import Ctx
from .ir import LINE, QUAD, SMOOTH, Dots, Group, Paths
from .motifs import MOTIFS, crown_items, params_for

#: scale denominators at which the level of detail changes (LOD 3 | 2 | 1 | 0)
LOD_BREAKS = (750, 2500, 10000)

#: drawing order of line features and of roads/paths given as centre lines: above all
#: land cover, water and wetland (z <= 33), below buildings (60). Areas of equal z are
#: drawn largest first, so smaller areas stacked on larger ones stay visible.
STRIP_Z = 35

#: attribute names that give a tree's crown diameter in metres
SIZE_FIELDS = ("crown_diameter", "diameter_crown", "kronendurchmesser", "kronenbreite", "crown_m", "crown",
               "kronendurchm", "kr_durchm")
#: attribute names that give the stem diameter in metres
STEM_FIELDS = ("stem_diameter", "trunk_diameter", "stammdurchmesser", "stammdurchm", "dbh_m")
#: attribute names that give the stem circumference in centimetres (German tree surveys: Stammumfang)
GIRTH_FIELDS = ("stammumfang", "stu", "circumference", "girth_cm", "stammumfang_cm")
#: attribute names that give the width in metres of a road or path mapped as a centre line
WIDTH_FIELDS = ("width", "width_m", "breite", "est_width")


@dataclass
class Feature:
    geometry: BaseGeometry
    element: str
    props: dict = field(default_factory=dict)


@dataclass
class Options:
    """How to draw. All lengths are paper millimetres."""

    seed: int = 0
    handdrawn: float = 1.0        # 0 = exact geometry, 1 = house style, 2 = very sketchy
    outline_width: float = 0.18   # ISO 128 line-width series
    outline_wobble: float = 0.09  # stays below half the line width: the ink always covers the true edge
    textures: bool = True
    wash: bool = True
    lod: int | None = None        # None = from scale
    min_texture_area: float = 3.0  # mm2 on paper; smaller polygons stay flat
    fallback: str | None = "unknown"
    outline_contrast: float | None = None  # e.g. 3.0 darkens outlines to WCAG non-text contrast
    ink_contrast: float | None = None      # e.g. 3.0 darkens texture marks the same way
    symbol_scale: float = 1.0              # enlarges pictograms (legends, posters); crowns stay to scale

    @classmethod
    def accessible(cls, **kw) -> "Options":
        """High-contrast variant: outlines and texture marks reach 3:1 against their fill (WCAG 1.4.11)."""
        return cls(**{"outline_contrast": 3.0, "ink_contrast": 3.0, "outline_width": 0.25, **kw})


def lod_for_scale(scale: float) -> int:
    """Level of detail for a map scale denominator (1:500 -> 3, 1:5000 -> 1)."""
    a, b, c = LOD_BREAKS
    return 3 if scale <= a else 2 if scale <= b else 1 if scale <= c else 0


def lod_for_zoom(zoom: float, latitude: float = 50.0) -> int:
    """Level of detail for a web-map zoom level (256 px tiles, 96 dpi)."""
    return lod_for_scale(559082264.028 * math.cos(math.radians(latitude)) / 2**zoom)


# --------------------------------------------------------------------------- input

def as_features(data: Any, by: str = "element", mapping: dict | None = None) -> list[Feature]:
    """Accept a GeoDataFrame, a GeoJSON FeatureCollection, dicts with a ``geometry`` or (geometry, element) pairs."""
    if isinstance(data, list) and (not data or isinstance(data[0], Feature)):
        return data
    out: list[Feature] = []

    def cls(value):
        return mapping.get(value, value) if mapping else value

    if hasattr(data, "geometry") and hasattr(data, "columns"):  # GeoDataFrame
        if by not in data.columns:
            raise KeyError(f"column {by!r} not found; available: {', '.join(map(str, data.columns))}")
        cols = [c for c in data.columns if c != data.geometry.name]
        for geom, row in zip(data.geometry.values, data[cols].to_dict("records")):
            if geom is not None and not geom.is_empty:
                out.append(Feature(geom, cls(row[by]), row))
        return out
    if isinstance(data, dict) and data.get("type") == "FeatureCollection":
        for f in data["features"]:
            props = f.get("properties") or {}
            if f.get("geometry"):
                out.append(Feature(shape(f["geometry"]), cls(props.get(by)), props))
        return out
    for item in data:
        if isinstance(item, dict):                      # {"geometry": ..., "element": ..., **properties}
            out.append(Feature(item["geometry"], cls(item.get(by)), item))
            continue
        geom, el, *rest = item
        out.append(Feature(geom, cls(el), rest[0] if rest else {}))
    return out


def bounds_of(features: Iterable[Feature]) -> tuple[float, float, float, float]:
    b = np.array([f.geometry.bounds for f in features])
    return float(b[:, 0].min()), float(b[:, 1].min()), float(b[:, 2].max()), float(b[:, 3].max())


# --------------------------------------------------------------------------- drawing

def _hand(ring: np.ndarray, ctx: Ctx, opts: Options) -> np.ndarray:
    return G.wobble(ring, ctx, amp=opts.outline_wobble)


def draw_polygon(geom: BaseGeometry, el: Element, ctx: Ctx, opts: Options) -> Group:
    items: list = []
    rings = [_hand(r, ctx, opts) for r in G.rings_of(geom)]
    if el.fill:
        items.append(Paths(rings, fill=el.fill, closed=True, opacity=el.fill_opacity))
    if opts.textures and ctx.lod >= 1:
        for poly in G.polygons_of(geom):
            if poly.area / ctx.u**2 < opts.min_texture_area:
                continue
            if el.wash and opts.wash and el.fill and ctx.lod >= 2:
                wctx = Ctx(ctx.u, ctx.lod, R.stable_seed(opts.seed, el.id, "wash"), ctx.wobble, ctx.period)
                spec = {"ink": C.lighten(el.fill, 0.035), "ink2": C.darken(el.fill, 0.035)}
                items += MOTIFS["wash"](poly, params_for("wash", spec, ctx.lod), wctx)
            for k, tex in enumerate(el.textures):
                tctx = Ctx(ctx.u, ctx.lod, R.stable_seed(opts.seed, el.id, k), ctx.wobble, ctx.period)
                spec = params_for(tex["motif"], tex, ctx.lod)
                if opts.ink_contrast and el.fill:
                    for key in ("ink", "ink2", "stem", "branch"):
                        if spec.get(key):
                            spec[key] = C.ensure_contrast(spec[key], el.fill, opts.ink_contrast)
                items += MOTIFS[tex["motif"]](poly, spec, tctx)
    if el.outline and opts.outline_width > 0:
        col = el.outline
        if opts.outline_contrast:
            col = C.ensure_contrast(col, el.fill or "#F5F5F1", opts.outline_contrast)
        items.append(Paths(rings, stroke=col, width=el.outline_width or opts.outline_width, closed=True,
                           dash=el.outline_dash, cap="butt" if el.outline_dash else "round"))
    if el.border and ctx.lod >= 1:
        # border signature ("Randsignatur"): marks along the inside of the outline.
        # Shells run counter-clockwise and holes clockwise, so "left" is always inside.
        items += _line_marks(rings, {"side": "left", **el.border}, el, ctx, opts)
    return Group(items, element=el.id)


def _paper_width(spec: dict, ctx: Ctx, key: str = "width") -> float:
    """Line width in mm: a ground width (``width_m``) clamped to a readable range, or a fixed one."""
    if f"{key}_m" in spec:
        mm = spec[f"{key}_m"] / ctx.u
        return min(max(mm, spec.get(f"{key}_min", 0.25)), spec.get(f"{key}_max", 1e9))
    return spec.get(key, 0.3)


def draw_line(geom: BaseGeometry, el: Element, ctx: Ctx, opts: Options) -> Group:
    spec = el.line or {"color": el.outline or el.fill or "#505B61", "width": 0.3}
    lines = [G.wobble(ln, ctx, amp=opts.outline_wobble * spec.get("wobble", 1.0)) for ln in G.lines_of(geom)]
    w = _paper_width(spec, ctx)
    items: list = []
    if spec.get("casing"):
        items.append(Paths(lines, stroke=spec["casing"], width=w + 2 * spec.get("casing_width", 0.18),
                           cap=spec.get("cap", "round")))
    if spec.get("color"):
        items.append(Paths(lines, stroke=spec["color"], width=w, dash=spec.get("dash"),
                           cap="butt" if spec.get("dash") else spec.get("cap", "round")))
    marks = spec.get("marks")
    if marks and ctx.lod >= 1:
        items += _line_marks(lines, marks, el, ctx, opts)
    return Group(items, element=el.id)


def _along(lines: list[np.ndarray], step: float, start: float = 0.5):
    """Points every ``step`` along polylines: (xy, unit tangent)."""
    pts, tan = [], []
    for ln in lines:
        d = np.diff(ln, axis=0)
        seg = np.hypot(d[:, 0], d[:, 1])
        total = seg.sum()
        if total <= 0:
            continue
        cum = np.concatenate([[0.0], np.cumsum(seg)])
        at = np.arange(step * start, total, step)
        if not len(at):
            at = np.array([total / 2])
        k = np.clip(np.searchsorted(cum, at, side="right") - 1, 0, len(seg) - 1)
        t = ((at - cum[k]) / np.maximum(seg[k], 1e-12))[:, None]
        pts.append(ln[k] + d[k] * t)
        tan.append(d[k] / np.maximum(seg[k], 1e-12)[:, None])
    if not pts:
        return np.empty((0, 2)), np.empty((0, 2))
    return np.concatenate(pts), np.concatenate(tan)


def _pos_stream(xy: np.ndarray, seed: int) -> R.Stream:
    return R.Stream(np.round(xy[:, 0] * 100).astype(np.int64), np.round(xy[:, 1] * 100).astype(np.int64), seed)


def _line_marks(lines, marks: dict, el: Element, ctx: Ctx, opts: Options) -> list:
    """Marks repeated along lines: ticks, dots, rings, T-ticks, crosses, slope hachures, crowns.

    ``side`` is ``"both"`` (centred), ``"left"`` or ``"right"`` of the drawing
    direction; ``offset`` moves dots and rings off the line (paper mm).
    """
    kind = marks.get("kind", "ticks")
    u = ctx.u
    seed = R.stable_seed(opts.seed, el.id, "marks")
    if kind == "crowns":
        dia = min(max(marks.get("crown_m", 1.5) / u, marks.get("crown_min", 1.2)), marks.get("crown_max", 1e9)) * u
        xy, _ = _along(lines, dia * marks.get("pack", 0.8))
        if not len(xy):
            return []
        s = _pos_stream(xy, seed)
        r = 0.5 * dia * (0.8 + 0.4 * s.next())
        p = params_for("canopy", marks, ctx.lod)
        return crown_items(xy[:, 0], xy[:, 1], r, s, p, ctx)
    step = marks.get("step", 2.4) * u
    xy, tan = _along(lines, step)
    if not len(xy):
        return []
    nrm = np.column_stack([-tan[:, 1], tan[:, 0]])
    side = marks.get("side", "both")
    sgn = -1.0 if side == "right" else 1.0
    ln = marks.get("length", 0.9) * u
    col, w = marks.get("color") or el.outline or "#505B61", marks.get("width", 0.2)
    off = marks.get("offset", 0.0) * u * (0.0 if side == "both" else sgn)
    if kind == "dots":
        return [Dots(xy + nrm * off, marks.get("r", 0.3), col)]
    if kind == "rings":
        from .motifs import _circles

        c = xy + nrm * off
        return [Paths(_circles(c[:, 0], c[:, 1], marks.get("r", 0.4) * u, 16), stroke=col, width=w,
                      fill=marks.get("fill"), closed=True, kind=SMOOTH, fill_rule="nonzero")]
    if kind == "cross":
        a = np.stack([xy - (tan + nrm) * ln * 0.5, xy + (tan + nrm) * ln * 0.5], axis=1)
        b = np.stack([xy - (tan - nrm) * ln * 0.5, xy + (tan - nrm) * ln * 0.5], axis=1)
        return [Paths(np.concatenate([a, b]), stroke=col, width=w)]
    if kind == "tees":  # PlanZV 13.1: T-shaped ticks pointing to one side
        tip = xy + nrm * ln * sgn
        stem = np.stack([xy, tip], axis=1)
        bar = np.stack([tip - tan * ln * 0.38, tip + tan * ln * 0.38], axis=1)
        return [Paths(np.concatenate([stem, bar]), stroke=col, width=w, cap="butt")]
    if kind == "hachure":  # slope ticks on the downhill (right-hand) side, alternating long and short
        f = np.where(np.arange(len(xy)) % 2 == 0, 1.0, 0.5)[:, None]
        return [Paths(np.stack([xy, xy - nrm * ln * f], axis=1), stroke=col, width=w)]
    if side == "both":
        a, b = xy - nrm * ln * 0.5, xy + nrm * ln * 0.5
    else:
        a, b = xy, xy + nrm * ln * sgn
    return [Paths(np.stack([a, b], axis=1), stroke=col, width=w)]


# --------------------------------------------------------------------------- pictograms
# Small symbols in unit coordinates (radius about 1, y up), scaled by the symbol's ``r``
# in paper millimetres. Each part: (kind, coordinates, fill role, stroke role, width).
# Roles: "fill" = symbol colour, "ink" = outline colour, "paper" = near white, None.

def _ring(cx: float, cy: float, r: float, n: int = 20) -> np.ndarray:
    t = np.linspace(0, 2 * math.pi, n, endpoint=False)
    return np.column_stack([cx + r * np.cos(t), cy + r * np.sin(t)])


def _star(n: int = 5, r1: float = 1.15, r2: float = 0.48) -> np.ndarray:
    t = math.pi / 2 + np.arange(2 * n) * math.pi / n
    rr = np.where(np.arange(2 * n) % 2 == 0, r1, r2)
    return np.column_stack([rr * np.cos(t), rr * np.sin(t)])


def _rect(x0, y0, x1, y1) -> np.ndarray:
    return np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], dtype=np.float64)


PICTOGRAMS: dict[str, list] = {
    "square": [("poly", _rect(-1, -1, 1, 1), "fill", "ink", 0.18)],
    "diamond": [("poly", np.array([[0, -1.25], [1.25, 0], [0, 1.25], [-1.25, 0]], dtype=float), "fill", "ink", 0.18)],
    "triangle": [("poly", np.array([[-1.1, -0.85], [1.1, -0.85], [0, 1.15]]), "fill", "ink", 0.18)],
    "bar": [("poly", _rect(-1.6, -0.5, 1.6, 0.5), "fill", "ink", 0.18)],
    "star": [("poly", _star(), "fill", "ink", 0.16)],
    "ring": [("poly", _ring(0, 0, 1.0), "fill", "ink", 0.3), ("poly", _ring(0, 0, 0.45), "paper", "ink", 0.18)],
    "bench": [("poly", _rect(-1.35, -0.55, 1.35, 0.15), "fill", "ink", 0.18),
              ("line", np.array([[-1.35, 0.55], [1.35, 0.55]]), None, "ink", 0.3)],
    "bin": [("poly", _ring(0, 0, 0.85), "fill", "ink", 0.2), ("poly", _ring(0, 0, 0.42), None, "ink", 0.16)],
    "lamp": [("poly", _ring(0, 0, 0.8), "fill", "ink", 0.28),
             ("line", np.array([[-0.57, -0.57], [0.57, 0.57]]), None, "ink", 0.16),
             ("line", np.array([[-0.57, 0.57], [0.57, -0.57]]), None, "ink", 0.16)],
    "rack": [("line", np.array([[-0.75, -0.8], [-0.75, 0.3], [-0.62, 0.66], [-0.33, 0.66], [-0.2, 0.3], [-0.2, -0.8]]),
              None, "ink", 0.26),
             ("line", np.array([[0.2, -0.8], [0.2, 0.3], [0.33, 0.66], [0.62, 0.66], [0.75, 0.3], [0.75, -0.8]]),
              None, "ink", 0.26)],
    "sign": [("poly", _rect(-1.25, -0.05, 1.25, 0.6), "fill", "ink", 0.2),
             ("line", np.array([[-0.85, -0.05], [-0.85, -0.85]]), None, "ink", 0.26),
             ("line", np.array([[0.85, -0.05], [0.85, -0.85]]), None, "ink", 0.26)],
    "log": [("poly", _rect(-1.35, -0.42, 1.0, 0.42), "fill", "ink", 0.18),
            ("poly", _ring(1.0, 0, 0.42, 16), "paper", "ink", 0.18),
            ("poly", _ring(1.0, 0, 0.18, 12), None, "ink", 0.14)],
    "pile": [("poly", _ring(-0.55, -0.35, 0.45, 12), "fill", "ink", 0.16),
             ("poly", _ring(0.4, -0.4, 0.52, 12), "fill", "ink", 0.16),
             ("poly", _ring(-0.05, 0.38, 0.48, 12), "fill", "ink", 0.16),
             ("poly", _ring(0.82, 0.38, 0.3, 10), "fill", "ink", 0.16)],
    "box": [("poly", np.array([[-0.72, -0.85], [0.72, -0.85], [0.72, 0.28], [0, 0.98], [-0.72, 0.28]]), "fill", "ink", 0.2),
            ("poly", _ring(0, -0.1, 0.22, 12), "ink", None, 0.0)],
    "fountain": [("poly", _ring(0, 0, 1.0), "fill", "ink", 0.22), ("poly", _ring(0, 0, 0.55), None, "ink", 0.16),
                 ("poly", _ring(0, 0, 0.16, 10), "ink", None, 0.0)],
    "spring": [("poly", _ring(0, 0, 0.72), "fill", "ink", 0.24),
               ("curve", np.array([[0.72, 0.0], [1.05, -0.22], [1.4, 0.05], [1.8, -0.2]]), None, "ink", 0.22)],
    "cross": [("line", np.array([[-1, 0], [1, 0]]), None, "fill", 0.3), ("line", np.array([[0, -1], [0, 1]]), None, "fill", 0.3)],
    "planter": [("poly", _rect(-0.95, -0.95, 0.95, 0.95), "fill", "ink", 0.2),
                ("poly", _ring(0, 0, 0.58, 14), "accent", "ink", 0.14)],
}


def _pictogram(kind: str, xy: np.ndarray, spec: dict, el: Element, ctx: Ctx, opts: Options) -> list:
    r = spec.get("r", 0.6) * opts.symbol_scale
    col = spec.get("color") or el.fill or "#505B61"
    roles = {"fill": col, "ink": spec.get("ink") or C.darken(col, 0.2), "paper": "#FDFDFB",
             "accent": spec.get("accent") or col, None: None}
    items: list = []
    for part, coords, fill, stroke, width in PICTOGRAMS[kind]:
        pts = xy[:, None, :] + (coords * r * ctx.u)[None, :, :]
        closed = part == "poly"
        items.append(Paths(pts, fill=roles[fill] if closed else None, stroke=roles[stroke],
                           width=width * max(1.0, opts.symbol_scale ** 0.5), closed=closed,
                           kind=SMOOTH if part == "curve" else LINE, fill_rule="nonzero"))
    return items


def draw_points(xy: np.ndarray, sizes: np.ndarray | None, el: Element, ctx: Ctx, opts: Options,
                stems: np.ndarray | None = None) -> Group:
    spec = el.symbol or {"kind": "dot", "r": 0.6, "color": el.fill or "#505B61"}
    kind = spec.get("kind", "dot")
    seed = R.stable_seed(opts.seed, el.id)
    u = ctx.u
    if kind == "crown":
        p = params_for("canopy", spec, ctx.lod)
        dia = np.full(len(xy), float(spec.get("crown_m", 6.0))) if sizes is None else np.where(
            np.isfinite(sizes) & (sizes > 0), sizes, spec.get("crown_m", 6.0))
        mm = np.clip(dia / u, spec.get("size_min", 1.6), spec.get("size_max", 60.0))
        s = _pos_stream(xy, seed)
        if ctx.lod == 0:
            return Group([Dots(xy, mm * 0.5, p["tones"][0] if p.get("tones") else el.fill)], element=el.id)
        p["star"] = p.get("star", True) and ctx.lod >= 2
        return Group(crown_items(xy[:, 0], xy[:, 1], 0.5 * mm * u, s, p, ctx, stems=stems), element=el.id)
    r = spec.get("r", 0.6) * opts.symbol_scale
    col = spec.get("color") or el.fill or "#505B61"
    if kind == "dot":
        items = [Dots(xy, r, col)]
        if spec.get("halo"):
            items.insert(0, Dots(xy, r + spec.get("halo_width", 0.25) * opts.symbol_scale, spec["halo"]))
        return Group(items, element=el.id)
    if kind in PICTOGRAMS:
        return Group(_pictogram(kind, xy, spec, el, ctx, opts), element=el.id)
    return Group([Dots(xy, r, col)], element=el.id)


_NUMBER = re.compile(r"^\s*(-?\d+(?:[.,]\d+)?)")


def _number(props: dict, fields: tuple) -> float:
    """First usable number among ``fields``; tolerates text such as ``"6 m"`` or ``"6,5"``."""
    for k in fields:
        v = props.get(k)
        if v is None or v == "":
            continue
        try:
            f = float(v)
        except (TypeError, ValueError):
            m = _NUMBER.match(str(v))
            if not m:
                continue
            f = float(m.group(1).replace(",", "."))
        if f == f:
            return f
    return float("nan")


def centreline_area(geom: BaseGeometry, props: dict, el: Element, catalog: Catalog) -> BaseGeometry:
    """The area of a road, path or surface that arrives as a centre line (OSM highways), at its width.

    Width: the feature's own ``width`` (``width_m``, ``breite``, ``est_width``), else ``lanes`` x
    lane width, else the defaults in ``settings.json -> centreline_widths_m`` by OSM ``highway``
    class, by element id, and finally a general default.
    """
    cfg = catalog.settings.get("centreline_widths_m", {})
    lower = {str(k).lower(): v for k, v in (props or {}).items()}
    w = _number(lower, WIDTH_FIELDS)
    if not (w == w and w > 0):
        lanes = _number(lower, ("lanes",))
        w = lanes * cfg.get("lane_m", 3.0) if lanes == lanes and lanes > 0 else float("nan")
    if not (w == w and w > 0):
        w = (cfg.get("highway", {}).get(str(lower.get("highway") or ""))
             or cfg.get("element", {}).get(el.id) or cfg.get("default", 2.0))
    return geom.buffer(w / 2.0, quad_segs=8)


def area_only(el: Element) -> bool:
    """True for elements that are drawn as areas only (a line feature becomes a strip of its width)."""
    return "polygon" in el.geometry and "line" not in el.geometry


def draw_order(geom: BaseGeometry, el: Element) -> tuple[int, float]:
    """(z, area) of a feature: lines and centre-line strips go to ``STRIP_Z`` at least; areas of
    equal z are painted largest first (a pond mapped on top of a park stays visible)."""
    t = geom.geom_type
    if t in ("LineString", "MultiLineString", "LinearRing"):
        return max(el.z, STRIP_Z), 0.0
    if t in ("Polygon", "MultiPolygon"):
        return el.z, geom.area
    return el.z, 0.0


def build(features: list[Feature], catalog: Catalog, ctx: Ctx, opts: Options | None = None,
          extent: tuple | None = None) -> list[Group]:
    """Display list for all features, painted in catalog z-order."""
    opts = opts or Options()
    clip = box(*extent).buffer(6 * ctx.u) if extent else None
    ctx = Ctx(ctx.u, ctx.lod, opts.seed, opts.handdrawn, ctx.period)
    todo: list[tuple[int, float, int, BaseGeometry, dict, Element]] = []

    def add(geom: BaseGeometry, props: dict, el: Element, n: int) -> None:
        if geom is None or geom.is_empty:
            return
        if geom.geom_type == "GeometryCollection":
            for part in geom.geoms:
                add(part, props, el, n)
            return
        if geom.geom_type in ("LineString", "MultiLineString", "LinearRing") and area_only(el):
            geom = centreline_area(geom, props, el, catalog)  # a road or path given as centre line
            todo.append((max(el.z, STRIP_Z), -geom.area, n, geom, props, el))
            return
        z, area = draw_order(geom, el)
        todo.append((z, -area, n, geom, props, el))

    for n, f in enumerate(features):
        el = catalog.get(f.element) if f.element is not None else None
        if el is None and opts.fallback:
            el = catalog.get(opts.fallback)
        if el is not None:
            add(f.geometry, f.props, el, n)
    todo.sort(key=lambda t: (t[0], t[1], t[2]))

    out: list[tuple[int, int, Group]] = []
    points: dict[str, tuple[Element, list, list, list]] = {}
    for k, (z, _, n, geom, props, el) in enumerate(todo):
        t = geom.geom_type
        if t in ("Point", "MultiPoint"):
            xy = G.points_of(geom)
            lower = {str(k).lower(): v for k, v in props.items()}
            size = _number(lower, SIZE_FIELDS)
            stem = _number(lower, STEM_FIELDS)
            if stem != stem:
                girth = _number(lower, GIRTH_FIELDS)
                stem = girth / 100.0 / math.pi if girth == girth else float("nan")
            slot = points.setdefault(el.id, (el, [], [], []))
            slot[1].append(xy)
            slot[2].extend([size] * len(xy))
            slot[3].extend([stem] * len(xy))
            continue
        if clip is not None:
            if not geom.intersects(clip):
                continue
            if not clip.contains(geom):
                geom = geom.intersection(clip)
                if geom.is_empty:
                    continue
        t = geom.geom_type
        if t in ("Polygon", "MultiPolygon"):
            out.append((z, k, draw_polygon(geom, el, ctx, opts)))
        elif t in ("LineString", "MultiLineString", "LinearRing"):
            out.append((z, k, draw_line(geom, el, ctx, opts)))
    for el, xys, sizes, stems in points.values():
        xy, sz, st = np.concatenate(xys), np.asarray(sizes, dtype=float), np.asarray(stems, dtype=float)
        if extent:
            pad = 30 * ctx.u
            m = ((xy[:, 0] >= extent[0] - pad) & (xy[:, 0] <= extent[2] + pad)
                 & (xy[:, 1] >= extent[1] - pad) & (xy[:, 1] <= extent[3] + pad))
            xy, sz, st = xy[m], sz[m], st[m]
        if len(xy):
            out.append((el.z, 1 << 60, draw_points(xy, sz, el, ctx, opts, stems=st)))
    out.sort(key=lambda t: (t[0], t[1]))
    return [g for _, _, g in out]

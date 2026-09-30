"""Texture motifs: the small hand-drawn marks that tell one surface from another.

Every motif is a function ``(region, params, ctx) -> list of display items``.
``region`` is a shapely polygon in map coordinates, ``params`` are the merged
settings for the current level of detail (sizes in paper mm unless the name
says ``_m``), and ``ctx`` carries scale and seed.

Level of detail (``ctx.lod``):
    0  overview  - no texture, flat fills only
    1  mass      - small simple marks, the character of the surface
    2  structure - tufts, stones, leaves become readable
    3  elements  - individual blades, flowers, boards
"""

from __future__ import annotations

import math

import numpy as np

from . import geom as G
from . import rand as R
from .geom import Ctx
from .ir import LINE, QUAD, SMOOTH, Dots, Group, Paths

TAU = 2 * math.pi


# --------------------------------------------------------------------------- defaults

DEFAULTS: dict[str, dict] = {
    "grass_ticks": {
        "all": dict(width=0.17, blades=2, gap=0.30, lean=14, clump=0.25, keep=0.9),
        1: dict(spacing=1.9, length=0.50, blades=1, width=0.15),
        2: dict(spacing=2.3, length=0.75),
        3: dict(spacing=2.9, length=1.10, blades=3, width=0.19),
    },
    "grass_tufts": {
        "all": dict(width=0.18, spread=26, clump=0.35, keep=0.92, ticks=True),
        1: dict(spacing=2.3, height=0.85, blades=3, blades_min=2, base=0.10, width=0.15, ticks=False),
        2: dict(spacing=3.0, height=1.50, blades=4, blades_min=2, base=0.16),
        3: dict(spacing=3.9, height=2.40, blades=5, blades_min=3, base=0.24, width=0.21),
    },
    "flowers": {
        "all": dict(width=0.17, keep=0.8, clump=0.5, kinds=("disc", "spike", "cluster", "umbel")),
        1: dict(spacing=2.7, height=0.0, head=0.27),
        2: dict(spacing=3.6, height=1.6, head=0.42),
        3: dict(spacing=4.7, height=2.8, head=0.62, width=0.2),
    },
    "reeds": {
        "all": dict(width=0.19, spread=9, clump=0.4, keep=0.9, heads=0.14),
        1: dict(spacing=2.0, height=1.3, blades=2, blades_min=1, base=0.12, width=0.16, heads=0.0),
        2: dict(spacing=2.7, height=2.5, blades=3, blades_min=2, base=0.2),
        3: dict(spacing=3.4, height=3.9, blades=4, blades_min=2, base=0.3, width=0.22),
    },
    "stipple": {
        "all": dict(keep=0.85, skew=2.0, clump=0.0, ink2_share=0.0),
        1: dict(spacing=1.2, r_min=0.06, r_max=0.13),
        2: dict(spacing=1.5, r_min=0.08, r_max=0.22),
        3: dict(spacing=1.9, r_min=0.10, r_max=0.32),
    },
    "pebbles": {
        "all": dict(width=0.15, keep=0.92),
        1: dict(spacing=1.15, size=0.55, width=0.13),
        2: dict(spacing=1.6, size=0.95),
        3: dict(spacing=2.2, size=1.45, width=0.17),
    },
    "waves": {
        "all": dict(width=0.19, keep=0.5, aspect=0.6),
        1: dict(spacing=2.6, length=1.6, amp=0.0, width=0.16),
        2: dict(spacing=3.6, length=2.8, amp=0.10),
        3: dict(spacing=4.6, length=4.0, amp=0.15, width=0.21),
    },
    "hatch": {
        "all": dict(width=0.16, angle=45, amp=0.10, cross=False),
        1: dict(spacing=1.3), 2: dict(spacing=1.8), 3: dict(spacing=2.4),
    },
    "herringbone": {
        "all": dict(width=0.14, angle=45, unit_m=0.10, amp=0.06, trim=0.08),
        1: dict(unit_min=0.62, unit_max=0.9),
        2: dict(unit_min=0.85, unit_max=1.6),
        3: dict(unit_min=1.1, unit_max=3.0),
    },
    "bond": {
        "all": dict(width=0.14, angle=0, course_m=0.10, unit_m=0.20, offset=0.5, jitter=0.06,
                    merge=0.0, amp=0.06, trim=0.06),
        1: dict(course_min=0.7, course_max=1.0),
        2: dict(course_min=1.0, course_max=1.8),
        3: dict(course_min=1.3, course_max=3.2),
    },
    "stripes": {
        "all": dict(band_m=5.0, angle="auto", opacity=0.75),
        1: dict(band_min=1.1, band_max=2.0),
        2: dict(band_min=1.6, band_max=4.0),
        3: dict(band_min=2.2, band_max=8.0),
    },
    "cells": {
        "all": dict(cell_m=0.12, fill_ratio=0.5, angle=0),
        1: dict(cell_min=0.9, cell_max=1.2),
        2: dict(cell_min=1.3, cell_max=2.0),
        3: dict(cell_min=1.7, cell_max=3.0),
    },
    "chips": {
        "all": dict(width=0.2, keep=0.9),
        1: dict(spacing=1.2, length=0.45, width=0.17),
        2: dict(spacing=1.6, length=0.75),
        3: dict(spacing=2.1, length=1.05, width=0.23),
    },
    "rosettes": {
        "all": dict(width=0.17, keep=0.9, clump=0.3),
        1: dict(spacing=1.9, size=0.35, arms=0),
        2: dict(spacing=2.6, size=0.6, arms=3),
        3: dict(spacing=3.4, size=0.9, arms=4, width=0.19),
    },
    "canopy": {
        "all": dict(crown_m=7.0, pack=1.45, depth=0.10, lobes=10, width=0.2, star=True, star_min=3.0,
                    opacity=0.95, vary=0.35, dots=0, inset=0.2),
        1: dict(crown_min=1.7, crown_max=3.2, star=False, width=0.0, lobes=7, pack=1.6, opacity=0.8),
        2: dict(crown_min=2.8, crown_max=8.0, width=0.15),
        3: dict(crown_min=4.0, crown_max=26.0, dots=4),
    },
    "rows": {
        "all": dict(width=0.17, angle=0, amp=0.08, dots=True, row_m=2.0),
        1: dict(row_min=1.1, row_max=1.6, dots=False),
        2: dict(row_min=1.6, row_max=3.0),
        3: dict(row_min=2.2, row_max=6.0),
    },
    "wash": {
        "all": dict(spacing=13.0, size=9.0, opacity=0.16, keep=0.6),
        1: dict(), 2: dict(), 3: dict(),
    },
}


def params_for(motif: str, spec: dict, lod: int) -> dict:
    """Merge built-in defaults, the element's texture spec and its per-LOD overrides."""
    base = DEFAULTS.get(motif, {})
    p = dict(base.get("all", {}))
    p.update(base.get(lod, {}))
    p.update({k: v for k, v in spec.items() if k not in ("lod", "motif")})
    p.update(spec.get("lod", {}).get(str(lod), {}))
    return p


def _ground(p: dict, ctx: Ctx, key: str) -> float:
    """A real-world size (``<key>_m``) clamped to a readable paper size, in map units."""
    mm = p.get(f"{key}_m", 1.0) / ctx.u
    mm = min(max(mm, p.get(f"{key}_min", 0.0)), p.get(f"{key}_max", 1e9))
    return mm * ctx.u * p.get("scale", 1.0)


def _stack(*cols) -> np.ndarray:
    """(n,) arrays x0,y0,x1,y1,... -> (n, k, 2)"""
    k = len(cols) // 2
    return np.stack([np.column_stack([cols[2 * i], cols[2 * i + 1]]) for i in range(k)], axis=1)


def _cat(batches: list[np.ndarray], k: int) -> np.ndarray:
    batches = [b for b in batches if len(b)]
    return np.concatenate(batches) if batches else np.empty((0, k, 2))


# --------------------------------------------------------------------------- grasses

def grass_ticks(region, p, ctx: Ctx):
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 11), jitter=0.46,
                        keep=p["keep"], inset_mm=p["length"] * 0.7, clump=p["clump"])
    if not len(x):
        return []
    u, nb = ctx.u, int(p["blades"])
    n = 1 + s.choice(nb)
    out = []
    for b in range(nb):
        m = n > b
        if not m.any():
            continue
        off = (b - (n - 1) / 2) * p["gap"] * u + 0.08 * u * s.pm()
        lean = math.radians(p["lean"]) * s.pm()
        ln = p["length"] * u * (0.65 + 0.6 * s.next())
        x0, y0 = x + off, y + 0.12 * u * s.pm()
        out.append(_stack(x0, y0, x0 + ln * np.sin(lean), y0 + ln * np.cos(lean))[m])
    return [Paths(_cat(out, 2), stroke=p["ink"], width=p["width"], opacity=p.get("opacity", 1.0))]


def _fan(x, y, s, p, ctx: Ctx, curved: bool):
    """Blades fanning out from a common base. Returns (n_total, k, 2) array."""
    u, nb, bmin = ctx.u, int(p["blades"]), int(p.get("blades_min", 1))
    n = bmin + s.choice(nb - bmin + 1)
    h = p["height"] * u * (0.62 + 0.55 * s.next())
    spread = math.radians(p["spread"])
    out = []
    for b in range(nb):
        m = n > b
        if not m.any():
            continue
        frac = np.where(n > 1, 2.0 * b / np.maximum(n - 1, 1) - 1.0, 0.0)
        ang = frac * spread + math.radians(6) * s.pm()
        ln = h * (1.0 - 0.32 * np.abs(frac)) * (0.8 + 0.4 * s.next())
        x0 = x + frac * p["base"] * u
        x2, y2 = x0 + ln * np.sin(ang), y + ln * np.cos(ang)
        if curved:
            # control point straight above the base: the blade leaves the ground upright and bows outward
            xm = 0.25 * x0 + 0.5 * x0 + 0.25 * x2
            ym = 0.25 * y + 0.5 * (y + 0.6 * ln) + 0.25 * y2
            out.append(_stack(x0, y, xm, ym, x2, y2)[m])
        else:
            out.append(_stack(x0, y, x2, y2)[m])
    return _cat(out, 3 if curved else 2)


def grass_tufts(region, p, ctx: Ctx):
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 12), jitter=0.47,
                        keep=p["keep"], inset_mm=p["height"] * 0.6, clump=p["clump"])
    items = []
    if p.get("ticks"):
        sub = params_for("grass_ticks", {"ink": p.get("ink2", p["ink"]), "salt": 13, "keep": 0.6}, ctx.lod)
        sub["spacing"] = p["spacing"] * 0.62
        items += grass_ticks(region, sub, ctx)
    if len(x):
        curved = ctx.lod >= 2
        items.append(Paths(_fan(x, y, s, p, ctx, curved), stroke=p["ink"], width=p["width"],
                           kind=SMOOTH if curved else LINE))
    return items


def reeds(region, p, ctx: Ctx):
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 14), jitter=0.47,
                        keep=p["keep"], inset_mm=p["height"] * 0.55, clump=p["clump"])
    if not len(x):
        return []
    curved = ctx.lod >= 2
    blades = _fan(x, y, s, p, ctx, curved)
    items = [Paths(blades, stroke=p["ink"], width=p["width"], kind=SMOOTH if curved else LINE)]
    if p.get("heads", 0) > 0 and len(blades):
        # seed heads: a short thick dash just below the tip of some blades
        tip, prev = blades[:, -1, :], blades[:, -2, :]
        pick = ctx.rand_at(tip[:, 0], tip[:, 1], 141) < p["heads"]
        if pick.any():
            d = tip[pick] - prev[pick]
            d /= np.maximum(np.hypot(d[:, 0], d[:, 1]), 1e-9)[:, None]
            a = tip[pick] - d * 0.25 * ctx.u
            b = tip[pick] - d * (0.25 + 0.2 * p["height"]) * ctx.u
            items.append(Paths(np.stack([a, b], axis=1), stroke=p.get("ink2", p["ink"]),
                               width=p["width"] * 1.9))
    return items


# --------------------------------------------------------------------------- flowers

def flowers(region, p, ctx: Ctx):
    accents = list(p.get("accents") or ["#E8CF6A"])
    kinds = list(p.get("kinds") or ["disc"])
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 15), jitter=0.48,
                        keep=p["keep"], inset_mm=p["height"] + p["head"] * 1.5, clump=p["clump"])
    if not len(x):
        return []
    u, head = ctx.u, p["head"]
    sp = s.choice(len(accents))
    h = p["height"] * u * (0.7 + 0.5 * s.next())
    lean = math.radians(11) * s.pm()
    tx, ty = x + h * np.sin(lean), y + h * np.cos(lean)
    items = []
    if p["height"] > 0:
        items.append(Paths(_stack(x, y, tx, ty), stroke=p.get("stem", p["ink"]), width=p["width"]))
        if ctx.lod >= 3:
            side = np.where(s.next() < 0.5, -1.0, 1.0)
            for k, f in enumerate((0.32, 0.52)):
                bx, by = x + (tx - x) * f, y + (ty - y) * f
                ln = 0.26 * h * (0.7 + 0.6 * s.next())
                a = lean + side * (1 if k == 0 else -1) * math.radians(48)
                items.append(Paths(_stack(bx, by, bx + ln * np.sin(a), by + ln * np.cos(a)),
                                   stroke=p.get("stem", p["ink"]), width=p["width"]))
    jig = [s.pm() for _ in range(4)]
    for k, col in enumerate(accents):
        m = sp == k
        if not m.any():
            continue
        kind = kinds[k % len(kinds)] if p["height"] > 0 else "disc"
        cx, cy = tx[m], ty[m]
        if kind == "spike":
            d = head * 0.95 * u
            for q in range(4 if ctx.lod >= 3 else 3):
                ox = (0.32 if q % 2 else -0.32) * head * u
                items.append(Dots(np.column_stack([cx + ox - np.sin(lean[m]) * q * d,
                                                   cy - np.cos(lean[m]) * q * d]),
                                  head * (0.62 - 0.06 * q), col))
        elif kind == "cluster":
            for q in range(3):
                a = TAU * q / 3 + jig[0][m] * 0.6
                items.append(Dots(np.column_stack([cx + np.cos(a) * head * 0.62 * u,
                                                   cy + np.sin(a) * head * 0.62 * u]), head * 0.6, col))
        elif kind == "umbel":
            for q in range(5):
                a = math.pi * (0.12 + 0.19 * q) + jig[1][m] * 0.15
                items.append(Dots(np.column_stack([cx + np.cos(a) * head * 1.0 * u,
                                                   cy + np.sin(a) * head * 0.75 * u]), head * 0.4, col))
        else:
            items.append(Dots(np.column_stack([cx, cy]), head * (0.85 + 0.25 * jig[2][m]), col))
            if ctx.lod >= 2 and p.get("center"):
                items.append(Dots(np.column_stack([cx, cy]), head * 0.38, p["center"]))
    return items


def rosettes(region, p, ctx: Ctx):
    """Perennial planting: small leaf rosettes with a few flower dots."""
    accents = list(p.get("accents") or [])
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 16), jitter=0.45,
                        keep=p["keep"], inset_mm=p["size"], clump=p["clump"])
    if not len(x):
        return []
    u, arms = ctx.u, int(p["arms"])
    r = p["size"] * u * (0.7 + 0.6 * s.next())
    rot = math.pi * s.next()
    items = []
    if arms:
        out = []
        for k in range(arms):
            a = rot + math.pi * k / arms
            out.append(_stack(x - r * np.cos(a), y - r * np.sin(a), x + r * np.cos(a), y + r * np.sin(a)))
        items.append(Paths(_cat(out, 2), stroke=p["ink"], width=p["width"]))
    else:
        items.append(Dots(np.column_stack([x, y]), p["size"] * 0.55, p["ink"]))
    if accents:
        pick, sp = s.next() < p.get("bloom", 0.45), s.choice(len(accents))
        for k, col in enumerate(accents):
            m = pick & (sp == k)
            if m.any():
                items.append(Dots(np.column_stack([x[m], y[m]]), p["size"] * 0.42, col))
    return items


# --------------------------------------------------------------------------- mineral textures

def stipple(region, p, ctx: Ctx):
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 21), jitter=0.5,
                        keep=p["keep"], inset_mm=p["r_max"] * 1.3, clump=p["clump"])
    if not len(x):
        return []
    r = p["r_min"] + (p["r_max"] - p["r_min"]) * s.next() ** p["skew"]
    xy = np.column_stack([x, y])
    op = p.get("opacity", 1.0)
    if p.get("ink2") and p["ink2_share"] > 0:
        m = s.next() < p["ink2_share"]
        return [Dots(xy[~m], r[~m], p["ink"], op), Dots(xy[m], r[m], p["ink2"], op)]
    return [Dots(xy, r, p["ink"], op)]


def pebbles(region, p, ctx: Ctx):
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 22), jitter=0.36,
                        keep=p["keep"], inset_mm=p["size"] * 0.7)
    if not len(x):
        return []
    k = 6
    a = 0.5 * p["size"] * ctx.u * (0.55 + 0.75 * s.next())
    b = a * (0.62 + 0.38 * s.next())
    rot = TAU * s.next()
    c, sn = np.cos(rot), np.sin(rot)
    cols = []
    for q in range(k):
        t = TAU * q / k
        rr = 1.0 + 0.2 * s.pm()
        px, py = a * math.cos(t) * rr, b * math.sin(t) * rr
        cols += [x + px * c - py * sn, y + px * sn + py * c]
    return [Paths(_stack(*cols), fill=p.get("fill"), stroke=p["ink"], width=p["width"], closed=True,
                  kind=SMOOTH, fill_rule="nonzero")]


def chips(region, p, ctx: Ctx):
    """Short dashes in all directions: bark mulch, wood chips, leaf litter."""
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 23), jitter=0.48,
                        keep=p["keep"], inset_mm=p["length"] * 0.6)
    if not len(x):
        return []
    a = math.pi * s.next()
    h = 0.5 * p["length"] * ctx.u * (0.6 + 0.8 * s.next())
    dx, dy = h * np.cos(a), h * np.sin(a)
    items = [Paths(_stack(x - dx, y - dy, x + dx, y + dy), stroke=p["ink"], width=p["width"])]
    if p.get("ink2"):
        m = s.next() < 0.35
        items = [Paths(items[0].paths[~m], stroke=p["ink"], width=p["width"]),
                 Paths(items[0].paths[m], stroke=p["ink2"], width=p["width"])]
    return items


# --------------------------------------------------------------------------- water

def waves(region, p, ctx: Ctx):
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 31), jitter=0.4,
                        keep=p["keep"], aspect=p["aspect"], inset_mm=0.5)
    if not len(x):
        return []
    u = ctx.u
    h = 0.5 * p["length"] * u * (0.45 + 1.0 * s.next())
    if p["amp"] > 0:
        a = p["amp"] * u * (0.5 + s.next()) * np.where(s.next() < 0.5, -1.0, 1.0)
        paths = _stack(x - h, y, x - 0.33 * h, y + a, x + 0.33 * h, y - a, x + h, y)
        kind = SMOOTH
    else:
        paths, kind = _stack(x - h, y, x + h, y), LINE
    paths = G.clip_lines(paths, region, whole_only=True)
    return [Paths(paths, stroke=p["ink"], width=p["width"], kind=kind)]


# --------------------------------------------------------------------------- line patterns

def _frame(region, angle: float):
    """Bounding box of the region in a frame rotated by ``angle``."""
    minx, miny, maxx, maxy = region.bounds
    c = G.rotate(np.array([[minx, miny], [maxx, miny], [maxx, maxy], [minx, maxy]]), -angle)
    return c[:, 0].min(), c[:, 1].min(), c[:, 0].max(), c[:, 1].max()


def _wobble_batch(segs: np.ndarray, ctx: Ctx, amp: float, wave: float = 6.0, step: float = 1.6) -> np.ndarray:
    """Hand-drawn displacement for many equally long segments at once: (n,2,2) -> (n,k,2)."""
    if len(segs) == 0 or amp * ctx.wobble <= 0:
        return segs
    d = segs[:, 1] - segs[:, 0]
    longest = float(np.hypot(d[:, 0], d[:, 1]).max())
    k = int(min(40, max(2, math.ceil(longest / (step * ctx.u)) + 1)))
    t = np.linspace(0.0, 1.0, k)[None, :, None]
    pts = segs[:, :1, :] + d[:, None, :] * t
    x, y = pts[..., 0].ravel(), pts[..., 1].ravel()
    a = amp * ctx.wobble * ctx.u
    dx = ctx.noise(x, y, wave, 7101) + 0.4 * ctx.noise(x, y, wave * 0.3, 7103)
    dy = ctx.noise(x, y, wave, 7102) + 0.4 * ctx.noise(x, y, wave * 0.3, 7104)
    return pts + (a / 1.4) * np.stack([dx, dy], axis=1).reshape(len(segs), k, 2)


def _trim(segs: np.ndarray, ctx: Ctx, amount_mm: float, salt: int) -> np.ndarray:
    """Pull each end back (or let it overshoot) a little, like a pen lifted by hand."""
    if len(segs) == 0 or amount_mm <= 0 or ctx.wobble <= 0:
        return segs
    d = segs[:, 1] - segs[:, 0]
    ln = np.maximum(np.hypot(d[:, 0], d[:, 1]), 1e-9)
    e = d / ln[:, None]
    mid = segs.mean(axis=1)
    a = amount_mm * ctx.u * ctx.wobble
    t0 = a * (1.6 * ctx.rand_at(mid[:, 0], mid[:, 1], salt) - 0.5)
    t1 = a * (1.6 * ctx.rand_at(mid[:, 0], mid[:, 1], salt + 1) - 0.5)
    out = segs.copy()
    out[:, 0] += e * t0[:, None]
    out[:, 1] -= e * t1[:, None]
    return out


def _angle(region, p: dict) -> float:
    """Pattern direction: a fixed angle, or ``"auto"`` = along the polygon's long side (+ ``angle_offset``)."""
    if p.get("angle") == "auto":
        return (G.main_angle(region) + p.get("angle_offset", 0.0)) % 180.0
    return float(p.get("angle", 0.0))


def _span_lines(region, ctx: Ctx, spacing: float, angle: float, offset: float = 0.0):
    """Parallel lines across the region; returns (n, 2, 2) in map coordinates."""
    fx0, fy0, fx1, fy1 = _frame(region, angle)
    j0, j1 = math.floor(fy0 / spacing - offset) - 1, math.ceil(fy1 / spacing - offset) + 1
    if j1 - j0 > 20000:
        return np.empty((0, 2, 2))
    yy = (np.arange(j0, j1 + 1) + offset) * spacing
    a = G.rotate(np.column_stack([np.full_like(yy, fx0 - spacing), yy]), angle)
    b = G.rotate(np.column_stack([np.full_like(yy, fx1 + spacing), yy]), angle)
    return np.stack([a, b], axis=1)


def _long_wobble(segs: np.ndarray, ctx: Ctx, amp: float, salt: int = 0) -> list[np.ndarray]:
    return [G.wobble(sg, ctx, amp=amp, wave=8.0, step=1.4, salt=salt) for sg in segs]


def hatch(region, p, ctx: Ctx):
    sp = p["spacing"] * ctx.u
    ang = _angle(region, p) if ctx.period is None else (45.0 if p.get("angle") == "auto" else float(p["angle"]))
    if ctx.period is not None:
        ang = 0 if abs(ang) < 22 or abs(ang - 180) < 22 else (90 if abs(ang - 90) < 22 else 45)
        sp = ctx.fit(sp * (math.sqrt(2) if ang == 45 else 1), 1)[0] / (math.sqrt(2) if ang == 45 else 1)
    lines = _long_wobble(_span_lines(region, ctx, sp, ang), ctx, p["amp"])
    if p.get("cross"):
        lines += _long_wobble(_span_lines(region, ctx, sp, ang + 90), ctx, p["amp"], salt=5)
    return [Paths(G.clip_lines(lines, region), stroke=p["ink"], width=p["width"],
                  opacity=p.get("opacity", 1.0), dash=p.get("dash"))]


def rows(region, p, ctx: Ctx):
    """Planting rows (vines, crops, nursery): parallel lines with plants dotted along them."""
    sp = _ground(p, ctx, "row")
    ang = _angle(region, p)
    if ctx.period is not None:
        ang, sp = 0, ctx.fit(sp, 1)[0]
    lines = G.clip_lines(_long_wobble(_span_lines(region, ctx, sp, ang), ctx, p["amp"]), region)
    items = [Paths(lines, stroke=p["ink"], width=p["width"])]
    if p.get("dots"):
        # plants sit on a ground-anchored lattice along the rows, so they survive tiling and clipping
        step = ctx.fit(sp * 0.55, 0)[0]
        fx0, fy0, fx1, fy1 = _frame(region, ang)
        ii = np.arange(math.floor(fx0 / step) - 1, math.ceil(fx1 / step) + 2)
        jj = np.arange(math.floor(fy0 / sp) - 1, math.ceil(fy1 / sp) + 2)
        if len(ii) * len(jj) <= G.MAX_CELLS:
            I, J = np.meshgrid(ii, jj)
            xy = G.rotate(np.column_stack([(I.ravel() + 0.5) * step, J.ravel() * sp]), ang)
            a = p["amp"] * ctx.wobble * ctx.u / 1.35
            xy = xy + a * np.column_stack([
                ctx.noise(xy[:, 0], xy[:, 1], 8.0, 7001) + 0.35 * ctx.noise(xy[:, 0], xy[:, 1], 8.0 * 0.45, 7003),
                ctx.noise(xy[:, 0], xy[:, 1], 8.0, 7002) + 0.35 * ctx.noise(xy[:, 0], xy[:, 1], 8.0 * 0.45, 7004)])
            import shapely
            xy = xy[shapely.contains_xy(G.inset(region, p.get("dot", 0.3) * ctx.u), xy[:, 0], xy[:, 1])]
            if len(xy):
                items.append(Dots(xy, p.get("dot", 0.3), p.get("ink2", p["ink"])))
    return items


def herringbone(region, p, ctx: Ctx):
    """Fischgrätverband. Bricks 2:1; each joint is drawn once as a run of three unit edges."""
    w = _ground(p, ctx, "unit")
    ang = _angle(region, p) if ctx.period is None else (45.0 if p.get("angle") == "auto" else float(p["angle"]))
    if ctx.period is not None:
        ang = 45 if 22 <= abs(ang) % 90 <= 68 else 0
        f = 4 * (math.sqrt(2) if ang == 45 else 1)
        w = ctx.fit(w * f, 0)[0] / f
    fx0, fy0, fx1, fy1 = _frame(region, ang)
    c0, c1 = math.floor(fx0 / w) - 4, math.ceil(fx1 / w) + 4
    r0, r1 = math.floor(fy0 / w) - 4, math.ceil(fy1 / w) + 4
    if (c1 - c0) * (r1 - r0) > 4 * G.MAX_CELLS:
        return []
    # vertical joints: on line x = c, from y = c + 4k to c + 4k + 3
    C, K = np.meshgrid(np.arange(c0, c1 + 1), np.arange(math.floor((r0 - c1) / 4) - 1, math.ceil((r1 - c0) / 4) + 1))
    C, K = C.ravel(), K.ravel()
    ya = C + 4 * K
    m = (ya + 3 >= r0) & (ya <= r1)
    v = _stack(C[m], ya[m], C[m], ya[m] + 3).astype(np.float64)
    # horizontal joints: on line y = r, from x = r - 1 + 4k to r + 2 + 4k
    Rr, K = np.meshgrid(np.arange(r0, r1 + 1), np.arange(math.floor((c0 - r1) / 4) - 1, math.ceil((c1 - r0) / 4) + 2))
    Rr, K = Rr.ravel(), K.ravel()
    xa = Rr - 1 + 4 * K
    m = (xa + 3 >= c0) & (xa <= c1)
    h = _stack(xa[m], Rr[m], xa[m] + 3, Rr[m]).astype(np.float64)
    segs = np.concatenate([v, h]) * w
    segs = G.rotate(segs.reshape(-1, 2), ang).reshape(-1, 2, 2)
    segs = _trim(segs, ctx, p["trim"], 301)
    lines = G.clip_lines(_wobble_batch(segs, ctx, p["amp"]), region)
    return [Paths(lines, stroke=p["ink"], width=p["width"], opacity=p.get("opacity", 1.0))]


def bond(region, p, ctx: Ctx):
    """Courses of stones or boards: running bond, stack bond, slabs, cobbles, planks.

    ``offset`` is the shift of every second course as a fraction of the unit
    (0.5 = Läuferverband, 0 = Kreuzfuge) or ``"random"`` for boards and wild bonds.
    ``merge`` drops a share of the joints so some stones come out longer.
    """
    h = _ground(p, ctx, "course")
    ratio = p["unit_m"] / p["course_m"]
    ln = h * ratio
    ang = _angle(region, p)
    nx = ny = None
    if ctx.period is not None:
        ang = 0
        h, ny = ctx.fit(h, 1, even=True)
        ln, nx = ctx.fit(ln, 0)
    fx0, fy0, fx1, fy1 = _frame(region, ang)
    j0, j1 = math.floor(fy0 / h) - 1, math.ceil(fy1 / h) + 1
    i0, i1 = math.floor(fx0 / ln) - 2, math.ceil(fx1 / ln) + 2
    if (i1 - i0) * (j1 - j0) > 4 * G.MAX_CELLS:
        return []
    courses = _span_lines(region, ctx, h, ang)
    I, J = np.meshgrid(np.arange(i0, i1 + 1, dtype=np.int64), np.arange(j0, j1 + 1, dtype=np.int64))
    I, J = I.ravel(), J.ravel()
    hi, hj = (I % nx, J % ny) if nx is not None else (I, J)
    if p["offset"] == "random":
        off = R.rand(np.zeros_like(hj), hj, ctx.seed, 411)
    else:
        off = float(p["offset"]) * (J & 1)
    x = (I + off + p["jitter"] * R.rand_pm(hi, hj, ctx.seed, 412)) * ln
    keep = R.rand(hi, hj, ctx.seed, 413) >= p["merge"]
    x, J = x[keep], J[keep]
    joints = _stack(x, J * h, x, (J + 1) * h).astype(np.float64)
    joints = G.rotate(joints.reshape(-1, 2), ang).reshape(-1, 2, 2)
    joints = _trim(joints, ctx, p["trim"], 414)
    lines = _long_wobble(courses, ctx, p["amp"]) + list(_wobble_batch(joints, ctx, p["amp"]))
    items = [Paths(G.clip_lines(lines, region), stroke=p["ink"], width=p["width"],
                   opacity=p.get("opacity", 1.0))]
    if p.get("grain") and ctx.lod >= 3:
        sub = dict(spacing=h / ctx.u * 1.7, length=h / ctx.u * 1.6, keep=0.35, width=p["width"] * 0.8,
                   ink=p["ink"], angle=ang, salt=415)
        items += _dashes(region, sub, ctx)
    return items


def _dashes(region, p, ctx: Ctx):
    """Sparse short strokes along one direction (wood grain)."""
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p["salt"], jitter=0.5, keep=p["keep"],
                        inset_mm=p["length"] * 0.5)
    if not len(x):
        return []
    a = math.radians(p["angle"])
    hl = 0.5 * p["length"] * ctx.u * (0.5 + s.next())
    dx, dy = hl * math.cos(a), hl * math.sin(a)
    return [Paths(_stack(x - dx, y - dy, x + dx, y + dy), stroke=p["ink"], width=p["width"], opacity=0.7)]


def stripes(region, p, ctx: Ctx):
    """Alternating bands, cut exactly to the polygon: mowing stripes on sports turf, zebra crossings."""
    import shapely

    w = _ground(p, ctx, "band")
    if ctx.period is None:
        ang = _angle(region, p)
    else:
        a = float(p.get("angle", 0)) if p.get("angle") != "auto" else 0.0
        ang = 90.0 if 45 < a % 180 < 135 else 0.0
        w = ctx.fit(2 * w, 0 if ang == 90.0 else 1)[0] / 2
    fx0, fy0, fx1, fy1 = _frame(region, ang)
    j0, j1 = math.floor(fy0 / (2 * w)) - 1, math.ceil(fy1 / (2 * w)) + 1
    if j1 - j0 > 5000:
        return []
    x0, x1 = fx0 - w, fx1 + w
    bands = [shapely.Polygon(G.rotate(np.array([[x0, y], [x1, y], [x1, y + w], [x0, y + w]]), ang))
             for y in np.arange(j0, j1 + 1) * 2 * w]
    parts = shapely.intersection(np.array(bands, dtype=object), region)
    rings = [ring for g in parts if not g.is_empty for ring in G.rings_of(g)]
    if not rings:
        return []
    return [Paths(rings, fill=p["ink"], closed=True, opacity=p.get("opacity", 1.0), width=0)]


def cells(region, p, ctx: Ctx):
    """Regular grid of small filled squares: grass pavers, tactile paving, grilles."""
    c = _ground(p, ctx, "cell")
    x, y, s = G.scatter(region, ctx, c / ctx.u, salt=p.get("salt", 51), jitter=0.0, stagger=False,
                        inset_mm=0.5 * c / ctx.u)
    if not len(x):
        return []
    hw = 0.5 * c * p["fill_ratio"] * (1 + 0.12 * s.pm()[:, None] * ctx.wobble)
    hh = 0.5 * c * p["fill_ratio"] * (1 + 0.12 * s.pm()[:, None] * ctx.wobble)
    sx = np.array([-1, 1, 1, -1])[None, :] * hw
    sy = np.array([-1, -1, 1, 1])[None, :] * hh
    paths = np.stack([x[:, None] + sx, y[:, None] + sy], axis=2)
    return [Paths(paths, fill=p["ink"], closed=True, fill_rule="nonzero", width=0,
                  opacity=p.get("opacity", 1.0))]


# --------------------------------------------------------------------------- canopies

def canopy_shapes(x, y, r, s, lobes: int, depth: float, ctx: Ctx, star: bool = False) -> list[np.ndarray]:
    """Scalloped crown outlines as closed quadratic chains (on, off, on, off ...).

    ``depth`` is how far the notches between lobes cut in (0.05 = nearly a
    circle, 0.18 = shrub). With ``star`` the lobes are pointed instead of
    rounded, the conventional plan symbol for conifers.
    """
    n = len(x)
    if n == 0:
        return []
    k = s.choice(3) - 1 + lobes
    irr = [(0.05 * s.pm(), TAU * s.next()) for _ in range(2)]
    phase = TAU * s.next()
    out: list = [None] * n
    for nl in np.unique(k):
        m = np.flatnonzero(k == nl)
        t = phase[m, None] + TAU * (np.arange(nl)[None, :] + 0.22 * np.stack([s.pm()[m] for _ in range(nl)], axis=1)) / nl
        t_next = np.roll(t, -1, axis=1)
        t_next[:, -1] += TAU
        tm = 0.5 * (t + t_next)
        half = 0.5 * (t_next - t)

        def wob(a):
            return 1 + irr[0][0][m, None] * np.cos(a + irr[0][1][m, None]) \
                     + irr[1][0][m, None] * np.cos(2 * a + irr[1][1][m, None])

        rm = r[m, None]
        r_in = rm * (1 - depth) * wob(t)
        if star:
            r_out = rm * wob(tm)
            on = np.stack([x[m, None] + r_in * np.cos(t), y[m, None] + r_in * np.sin(t)], axis=2)
            off = np.stack([x[m, None] + r_out * np.cos(tm), y[m, None] + r_out * np.sin(tm)], axis=2)
        else:
            # control radius chosen so the top of each lobe reaches the crown radius
            r_c = 2 * rm * wob(tm) - r_in * np.cos(half)
            on = np.stack([x[m, None] + r_in * np.cos(t), y[m, None] + r_in * np.sin(t)], axis=2)
            off = np.stack([x[m, None] + r_c * np.cos(tm), y[m, None] + r_c * np.sin(tm)], axis=2)
        chain = np.stack([on, off], axis=2).reshape(len(m), 2 * nl, 2)
        for q, idx in enumerate(m):
            out[idx] = chain[q]
    return out


def crown_stars(x, y, r, s, ctx: Ctx, arms: int = 6, length: float = 0.26) -> np.ndarray:
    """The little branch star at the centre of a crown: (n*arms, 2, 2) segments."""
    if len(x) == 0:
        return np.empty((0, 2, 2))
    rot = TAU * s.next()
    out = []
    for k in range(arms):
        a = rot + TAU * k / arms + 0.25 * s.pm()
        ln = r * length * (0.7 + 0.6 * s.next())
        inner = r * 0.03
        out.append(_stack(x + inner * np.cos(a), y + inner * np.sin(a), x + ln * np.cos(a), y + ln * np.sin(a)))
    return np.concatenate(out)


def _circles(x, y, r, n: int = 20) -> np.ndarray:
    t = np.linspace(0, TAU, n, endpoint=False)
    r = np.broadcast_to(np.asarray(r, dtype=np.float64), x.shape)[:, None]
    return np.stack([x[:, None] + r * np.cos(t), y[:, None] + r * np.sin(t)], axis=2)


def crown_items(x, y, r, s, p: dict, ctx: Ctx, clip=None, stems=None) -> list:
    """Display items for a set of crowns (used for woodland textures and single trees).

    Symbol vocabulary (ISO 11091 and PlanZV 13.2 combined):

    ``centre``  what sits in the middle of the crown: ``"star"`` (branch star, the
                house style for existing trees), ``"ring"`` (open circle: to be
                planted, PlanZV), ``"dot"`` (filled dot: to be preserved, PlanZV),
                ``"cross"`` (thin cross: proposed, ISO 11091), ``"ring_cross"``
                (both), or ``"none"``.
    ``frame``   ``"square"`` draws a chain-line square around the crown: tree to be
                protected (ISO 11091, 3.6). Colour ``frame_color``.
    ``cross_out`` colour of an × across the crown: tree to be removed (ISO 7518).
    ``pit_m``   tree pit square under the crown (street trees).
    ``dash``    dashed crown outline.
    ``stems``   (argument) stem diameters in map units; drawn to scale as a small
                circle when known (ISO 11091, 3.22).
    """
    n = len(x)
    if n == 0:
        return []
    tones = list(p.get("tones") or [p.get("fill", "#A0A986")])
    order = np.argsort(-y, kind="stable")  # paint from north to south so southern crowns sit on top
    x, y, r, s = x[order], y[order], r[order], s.take(order)
    if stems is not None:
        stems = np.asarray(stems, dtype=np.float64)[order]
    u = ctx.u
    items: list = []
    if p.get("pit_m"):
        h = 0.5 * max(p["pit_m"], 1.1 * u)
        sq = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]) * h
        items.append(Paths(np.stack([x, y], axis=1)[:, None, :] + sq[None, :, :], fill=p.get("pit", "#D3C1A9"),
                           stroke=p.get("pit_ink", "#9A876D"), width=0.13, closed=True, fill_rule="nonzero"))
    shapes = canopy_shapes(x, y, r, s, int(p["lobes"]), p["depth"], ctx, star=p.get("spiky", False))
    fills = [tones[i] for i in s.choice(len(tones))]
    items.append(Paths(shapes, fill=fills, stroke=p["ink"], width=p["width"], closed=True,
                       kind=LINE if p.get("spiky") else QUAD, compound=False, opacity=p.get("opacity", 1.0),
                       fill_rule="nonzero", dash=p.get("dash"), cap="butt" if p.get("dash") else "round"))
    if p.get("dots") and ctx.lod >= 3:
        pts = []
        for _ in range(int(p["dots"])):
            a, d = TAU * s.next(), r * 0.78 * np.sqrt(s.next())
            pts.append(np.column_stack([x + d * np.cos(a), y + d * np.sin(a)]))
        items.append(Dots(np.concatenate(pts), 0.11, p.get("ink2", p["ink"]), 0.55))
    centre = p.get("centre", "star" if p.get("star", True) else "none")
    col = p.get("branch", p["ink"])
    mm = 2 * r / u
    visible = mm >= p.get("centre_min", 1.4)
    has_stem = np.zeros(n, dtype=bool) if stems is None else (np.isfinite(stems) & (stems > 0) & (ctx.lod >= 2))
    if centre == "star" and p.get("star", True):
        big = (mm >= p.get("star_min", 3.0)) & ~has_stem
        if big.any():
            sb = s.take(big)
            items.append(Paths(crown_stars(x[big], y[big], r[big], sb, ctx), stroke=col, width=p["width"] * 0.95))
            items.append(Dots(np.column_stack([x[big], y[big]]), p["width"] * 1.25, col))
    if has_stem.any():
        rs = np.maximum(0.5 * stems[has_stem], 0.22 * u)
        items.append(Paths(_circles(x[has_stem], y[has_stem], rs), fill=p.get("stem_fill", "#FDFDFB"), stroke=col,
                           width=max(p["width"], 0.18) * 1.4, closed=True, kind=SMOOTH, fill_rule="nonzero",
                           compound=False))
    if centre in ("ring", "ring_cross") and visible.any():
        rr = np.clip(0.16 * r[visible], 0.32 * u, 0.9 * u)
        items.append(Paths(_circles(x[visible], y[visible], rr), fill=p.get("centre_fill", "#FDFDFB"), stroke=col,
                           width=0.2, closed=True, kind=SMOOTH, fill_rule="nonzero", compound=False))
    if centre in ("cross", "ring_cross") and visible.any():
        d = np.clip(0.26 * r[visible], 0.55 * u, 1.6 * u)
        xv, yv = x[visible], y[visible]
        a = np.stack([np.column_stack([xv - d, yv]), np.column_stack([xv + d, yv])], axis=1)
        b = np.stack([np.column_stack([xv, yv - d]), np.column_stack([xv, yv + d])], axis=1)
        items.append(Paths(np.concatenate([a, b]), stroke=col, width=0.16))
    if centre == "dot" and visible.any():
        items.append(Dots(np.column_stack([x[visible], y[visible]]), np.clip(0.15 * mm[visible], 0.32, 0.9), col))
    if p.get("frame") == "square":
        h = (r * 1.12 + 0.45 * u)[:, None]
        sq = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]], dtype=np.float64)[None, :, :]
        frames = np.stack([x, y], axis=1)[:, None, :] + sq * h[:, :, None]
        items.append(Paths(frames, stroke=p.get("frame_color", col), width=max(p["width"], 0.25), closed=True,
                           dash=p.get("frame_dash", (2.2, 0.6, 0.35, 0.6)), cap="butt", join="miter"))
    if p.get("ring"):  # kept for older element files
        items.append(Paths(_circles(x, y, r * 1.13 + 0.35 * u), stroke=p["ring"], width=max(p["width"], 0.22) * 1.2,
                           closed=True, kind=SMOOTH))
    if p.get("cross_out"):
        d = r * 0.82
        a = np.stack([np.column_stack([x - d, y - d]), np.column_stack([x + d, y + d])], axis=1)
        b = np.stack([np.column_stack([x - d, y + d]), np.column_stack([x + d, y - d])], axis=1)
        items.append(Paths(np.concatenate([a, b]), stroke=p["cross_out"], width=max(p["width"], 0.22) * 1.6))
    return [Group(items, clip=clip)] if clip is not None else items


def canopy(region, p, ctx: Ctx):
    """Closed tree or shrub cover: overlapping crowns packed into the polygon."""
    rad = 0.5 * _ground(p, ctx, "crown")
    # a small polygon still has to read as tree cover: make sure a handful of crowns fit
    rad = max(min(rad, 0.5 * math.sqrt(region.area / p.get("min_count", 5))), 0.5 * p.get("crown_min", 1.5) * ctx.u)
    x, y, s = G.scatter(region, ctx, rad / ctx.u * p["pack"], salt=p.get("salt", 61), jitter=p.get("jitter", 0.36),
                        stagger=p.get("stagger", True), keep=p.get("keep", 0.97), inset_mm=rad / ctx.u * p["inset"])
    if not len(x):
        c = region.representative_point()
        x, y = np.array([c.x]), np.array([c.y])
        s = R.Stream(np.round(x / ctx.u).astype(np.int64), np.round(y / ctx.u).astype(np.int64), ctx.seed, 61)
    r = rad * (1 - p["vary"] + 2 * p["vary"] * s.next())
    return crown_items(x, y, r, s, p, ctx, clip=G.rings_of(region))


# --------------------------------------------------------------------------- wash

def wash(region, p, ctx: Ctx):
    """Soft uneven tone, like pigment pooling in a watercolour wash, as a few flat blobs."""
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 71), jitter=0.5, keep=p["keep"])
    if not len(x):
        return []
    k = 7
    rad = 0.5 * p["size"] * ctx.u * (0.6 + 0.8 * s.next())
    cols = []
    for q in range(k):
        t = TAU * q / k
        rr = rad * (1.0 + 0.35 * s.pm())
        cols += [x + rr * math.cos(t), y + rr * math.sin(t) * 0.8]
    blobs = _stack(*cols)
    m = s.next() < 0.5
    items = []
    for sel, col in ((m, p["ink"]), (~m, p.get("ink2", p["ink"]))):
        if sel.any():
            items.append(Paths(blobs[sel], fill=col, closed=True, kind=SMOOTH, opacity=p["opacity"],
                               fill_rule="nonzero", width=0))
    return [Group(items, clip=G.rings_of(region))]


MOTIFS = {
    "grass_ticks": grass_ticks,
    "grass_tufts": grass_tufts,
    "flowers": flowers,
    "reeds": reeds,
    "rosettes": rosettes,
    "stipple": stipple,
    "pebbles": pebbles,
    "chips": chips,
    "waves": waves,
    "hatch": hatch,
    "rows": rows,
    "herringbone": herringbone,
    "bond": bond,
    "cells": cells,
    "stripes": stripes,
    "canopy": canopy,
    "wash": wash,
}

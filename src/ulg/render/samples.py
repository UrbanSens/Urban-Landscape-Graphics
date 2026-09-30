"""Seamless pattern tiles and legend swatches for single elements."""

from __future__ import annotations

import math

import numpy as np
from shapely.geometry import LineString, Point, Polygon, box

from ..catalog import Catalog, Element, load
from . import rand as R
from .geom import Ctx
from .ir import Group
from .motifs import MOTIFS, params_for
from .scene import Feature, Options, build
from .svg import Svg


def _flatten(items: list) -> list:
    """Drop clip groups: a tile is clipped by its own edge, and QtSvg (QGIS) ignores clipPath."""
    out = []
    for it in items:
        if isinstance(it, Group):
            out.extend(_flatten(it.items))
        else:
            out.append(it)
    return out


def tile_items(el: Element, size: float = 32.0, lod: int = 2, seed: int = 0, scale: float = 1000.0,
               margin: float = 14.0) -> list:
    """Texture of a polygon element for one seamless square tile of ``size`` mm (no fill, no outline).

    The texture is generated ``margin`` mm beyond the tile on every side, so
    marks that reach in from outside are complete; the caller crops to the tile.
    """
    u = scale / 1000.0
    side = size * u
    margin = margin * u
    region = box(-margin, -margin, side + margin, side + margin)
    items: list = []
    for k, tex in enumerate(el.textures):
        ctx = Ctx(u=u, lod=lod, seed=R.stable_seed(seed, el.id, k), wobble=1.0, period=(side, side))
        p = params_for(tex["motif"], tex, lod)
        if tex["motif"] == "canopy":
            p["crown_max"] = min(p.get("crown_max", 1e9), size / 3.0)
        items += MOTIFS[tex["motif"]](region, p, ctx)
    return _flatten(items)


def tile_svg(el: Element, size: float = 32.0, lod: int = 2, seed: int = 0, scale: float = 1000.0,
             background: bool = False, dots: str = "stroke") -> Svg:
    """A seamless pattern tile as an SVG page of ``size`` x ``size`` mm."""
    u = scale / 1000.0
    svg = Svg(size, size, background=el.fill if background else None, title=f"{el.id} (LOD {lod})", dots=dots)
    svg.frame(tile_items(el, size, lod, seed, scale), (0, 0, size * u, size * u), u, clip=False)
    return svg


# --------------------------------------------------------------------------- swatches

def _blob(w: float, h: float, seed: int) -> Polygon:
    rng = np.random.default_rng(seed)
    n = 9
    ang = np.linspace(0, 2 * math.pi, n, endpoint=False) + rng.uniform(-0.22, 0.22, n)
    r = rng.uniform(0.84, 1.0, n)
    return Polygon(np.column_stack([0.5 * w * r * np.cos(ang), 0.5 * h * r * np.sin(ang)]))


def swatch_features(el: Element, w: float, h: float, u: float, shape: str = "auto", seed: int = 1,
                    origin: tuple = (0.0, 0.0)) -> list[Feature]:
    """A small sample geometry for an element, ``w`` x ``h`` mm on paper, centred on ``origin``."""
    ox, oy = origin
    W, H = w * u, h * u
    if "polygon" in el.geometry and (el.fill or el.textures or el.outline or el.border) and (
            "line" not in el.geometry or el.fill or el.textures):
        if shape == "auto":
            shape = "rect" if el.group.startswith(("surface", "built", "context", "sport")) else "blob"
        if shape == "blob":
            poly = _blob(W, H, seed)
        else:
            poly = box(-W / 2, -H / 2, W / 2, H / 2)
        from shapely import affinity
        return [Feature(affinity.translate(poly, ox, oy), el.id)]
    if "line" in el.geometry:
        t = np.linspace(-0.5, 0.5, 24)
        pts = np.column_stack([ox + t * W * 0.92, oy + np.sin(t * 2 * math.pi) * H * 0.22])
        return [Feature(LineString(pts), el.id)]
    if shape == "grove":
        # a loose group of crowns of different sizes, as in a tree survey
        rng = np.random.default_rng(seed)
        spots = [(-0.36, 0.22), (-0.06, 0.30), (0.26, 0.20), (-0.30, -0.18), (0.02, -0.04), (0.34, -0.20), (-0.02, -0.34)]
        return [Feature(Point(ox + (fx + rng.uniform(-0.03, 0.03)) * W, oy + (fy + rng.uniform(-0.03, 0.03)) * H),
                        el.id, {"crown_diameter": H * rng.uniform(0.24, 0.36)}) for fx, fy in spots]
    dia = min(W, H) * 0.8
    return [Feature(Point(ox, oy), el.id, {"crown_diameter": dia})]


def swatch_svg(el: Element, w: float = 20.0, h: float = 12.0, lod: int = 2, scale: float | None = None,
               shape: str = "auto", catalog: Catalog | None = None, seed: int = 0, pad: float = 0.6) -> Svg:
    """Legend swatch for one element as its own small SVG."""
    catalog = catalog or load()
    u = (scale or {0: 20000, 1: 5000, 2: 1500, 3: 400}[lod]) / 1000.0
    feats = swatch_features(el, w - 2 * pad, h - 2 * pad, u, shape, seed=R.stable_seed(el.id) % 1000)
    items = build(feats, catalog, Ctx(u=u, lod=lod), Options(seed=seed, min_texture_area=0.0))
    svg = Svg(w, h, title=el.name())
    svg.frame(items, (-w * u / 2, -h * u / 2, w * u / 2, h * u / 2), u, clip=False)
    return svg


def symbol_items(el: Element, size: float = 8.0, lod: int = 2, catalog: Catalog | None = None) -> list:
    """Display items of a point element's symbol centred on (0, 0), about ``size`` mm across."""
    catalog = catalog or load()
    spec = el.symbol or {}
    if spec.get("kind") == "crown":
        props = {"crown_diameter": size * (0.72 if spec.get("frame") else 0.92)}
        opts = Options(min_texture_area=0.0)
    else:
        from ..render.scene import PICTOGRAMS

        parts = PICTOGRAMS.get(spec.get("kind", "dot"))
        extent = max((abs(c).max() for _, c, *_ in parts), default=1.0) if parts else 1.0
        r = spec.get("r", 0.6)
        props = {}
        opts = Options(min_texture_area=0.0, symbol_scale=0.44 * size / (r * max(extent, 1.0)))
    return build([Feature(Point(0.0, 0.0), el.id, props)], catalog, Ctx(u=1.0, lod=max(lod, 2)), opts)


def symbol_svg(el: Element, size: float = 8.0, lod: int = 2, catalog: Catalog | None = None) -> str:
    """A point element's symbol alone, centred in a ``size`` x ``size`` mm SVG (for QGIS markers, SLD, icons)."""
    h = 0.5 * size
    items = symbol_items(el, size, lod, catalog)
    svg = Svg(size, size, title=el.name())
    svg.frame(items, (-h, -h, h, h), 1.0, clip=False)
    return svg.tostring()

"""High-level entry points: render data to SVG or onto Matplotlib axes."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..catalog import Catalog, load
from .geom import Ctx
from .scene import Options, as_features, bounds_of, build, lod_for_scale
from .svg import Svg


def _prepare(data: Any, by: str, mapping: dict | None, extent, catalog: Catalog | None, theme: str | None = None):
    catalog = catalog or load(theme or "mellow")
    if hasattr(data, "crs") and data.crs is not None and getattr(data.crs, "is_geographic", False):
        data = data.to_crs(data.estimate_utm_crs())  # textures need metres, not degrees
    feats = as_features(data, by, mapping)
    if not feats:
        raise ValueError("nothing to draw: no features with a geometry")
    return catalog, feats, tuple(extent) if extent else bounds_of(feats)


def _handdrawn(value: float | None, catalog: Catalog) -> float:
    return float(catalog.theme.get("handdrawn", 1.0)) if value is None else float(value)


def _background(value: str | None, catalog: Catalog) -> str | None:
    if value == "auto":
        value = catalog.theme.get("background", "paper.base")
    return catalog.palette.resolve(value) if value else None


def render_svg(data: Any, by: str = "element", *, scale: float | None = None, width: float | None = None,
               extent: tuple | None = None, margin: float = 0.0, background: str | None = "auto",
               path: str | Path | None = None, catalog: Catalog | None = None, theme: str | None = None,
               mapping: dict | None = None, lod: int | None = None, seed: int = 0, handdrawn: float | None = None,
               options: Options | None = None, title: str | None = None) -> Svg:
    """Draw features in the house style and return the SVG page.

    ``data``     GeoDataFrame, GeoJSON FeatureCollection, or ``(geometry, element_id)`` pairs,
                 in a projected CRS with metres as unit.
    ``by``       column / property holding the element id; ``mapping`` translates other values.
    ``scale``    map scale denominator (500 for 1:500). The page size follows from the extent.
    ``width``    alternatively the page width in mm; the scale follows. Default 180 mm.
    ``lod``      level of detail 0-3; by default chosen from the scale.
    ``theme``    ``"mellow"`` (default) or an official theme: ``"planzv"``, ``"alkis"``, ``"basemap"``,
                 ``"bfn"``, ``"osm"``, ``"mono"`` (see ``ulg.themes()``).
    """
    catalog, feats, extent = _prepare(data, by, mapping, extent, catalog, theme)
    minx, miny, maxx, maxy = extent
    if scale:
        u = scale / 1000.0
    else:
        u = (maxx - minx) / ((width or 180.0) - 2 * margin)
    opts = options or Options(seed=seed, handdrawn=_handdrawn(handdrawn, catalog))
    ctx = Ctx(u=u, lod=lod if lod is not None else (opts.lod if opts.lod is not None else lod_for_scale(u * 1000)))
    items = build(feats, catalog, ctx, opts, extent)
    bg = _background(background, catalog)
    svg = Svg((maxx - minx) / u + 2 * margin, (maxy - miny) / u + 2 * margin, background=bg, title=title)
    svg.frame(items, extent, u, x=margin, y=margin, name="map")
    svg.scale = u * 1000.0
    svg.lod = ctx.lod
    if path:
        svg.save(path)
    return svg


def plot(data: Any, by: str = "element", *, ax=None, scale: float | None = None, width: float | None = None,
         extent: tuple | None = None, background: str | None = "auto", catalog: Catalog | None = None,
         theme: str | None = None, mapping: dict | None = None, lod: int | None = None, seed: int = 0,
         handdrawn: float | None = None, options: Options | None = None, zorder: float = 1.0, dpi: int = 150):
    """Draw features in the house style with Matplotlib and return the Axes.

    Without ``ax`` a figure is created whose size follows from ``scale`` (or
    ``width`` in mm), so that one paper millimetre is one millimetre. With an
    existing ``ax`` the current layout of that axes decides the scale; draw
    other layers on top afterwards as usual.
    """
    import matplotlib.pyplot as plt

    from .mpl import MplPainter, paper_scale

    catalog, feats, extent = _prepare(data, by, mapping, extent, catalog, theme)
    minx, miny, maxx, maxy = extent
    bg = _background(background, catalog)
    if ax is None:
        u = scale / 1000.0 if scale else (maxx - minx) / (width or 180.0)
        fig = plt.figure(figsize=((maxx - minx) / u / 25.4, (maxy - miny) / u / 25.4), dpi=dpi)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()
        if bg:
            fig.patch.set_facecolor(bg)
    ax.set_aspect("equal")
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
    if bg:
        ax.set_facecolor(bg)
    u = paper_scale(ax)
    opts = options or Options(seed=seed, handdrawn=_handdrawn(handdrawn, catalog))
    ctx = Ctx(u=u, lod=lod if lod is not None else (opts.lod if opts.lod is not None else lod_for_scale(u * 1000)))
    MplPainter(ax, zorder).draw(build(feats, catalog, ctx, opts, extent))
    return ax

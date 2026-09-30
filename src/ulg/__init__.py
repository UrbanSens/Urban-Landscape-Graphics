"""Urban Landscape Graphics - the UrbanSens Ecological Vector Style as a library.

A catalog of map elements (habitats, vegetation, water, surfaces, built context,
symbols) with mellow colours and lightly hand-drawn vector textures, tied to
German and European classification standards, plus renderers and exporters.

    import ulg

    ulg.element("lawn").fill                 # '#CDD2A9'
    ulg.find("Schotterrasen")                # search in English and German
    ulg.resolve("osm", landuse="grass")      # 'lawn'
    ulg.render_svg(gdf, by="element", scale=500, path="plan.svg")
    ulg.plot(gdf, by="element")              # Matplotlib
"""

from __future__ import annotations

from .analysis import flatten, indicators, root_protection_zone
from .brand import credit_line
from .catalog import Catalog, CatalogError, Element, Palette, load, themes
from .crosswalk import classify, codes_for, explain, official_colors, resolve, scheme, schemes
from .legend import legend_handles, legend_svg
from .render.api import plot, render_svg
from .render.scene import Feature, Options, lod_for_scale, lod_for_zoom

__version__ = "0.1.0"

__all__ = [
    "Catalog", "CatalogError", "Element", "Palette", "Feature", "Options", "load", "themes", "element", "find",
    "color", "fills", "ramp", "categories", "category_of", "style_function", "classify", "codes_for", "explain", "official_colors",
    "resolve", "scheme", "schemes", "flatten", "indicators", "root_protection_zone",
    "legend_handles", "legend_svg", "plot", "render_svg", "lod_for_scale", "lod_for_zoom", "style_sheet",
    "catalog_sheet", "credit_line", "__version__",
]


def element(element_id: str) -> Element:
    """The catalog entry for an element id (raises with suggestions if it does not exist)."""
    return load()[element_id]


def find(text: str, n: int = 5) -> list[Element]:
    """Search elements by id, English or German name, or alias; best match first."""
    return load().find(text, n)


def color(ref: str) -> str:
    """Hex colour of a palette token (``"grass.300"``) or of an element's fill (``"lawn"``)."""
    cat = load()
    if ref in cat:
        fill = cat[ref].fill
        if fill is None:
            raise CatalogError(f"element {ref!r} has no fill colour")
        return fill
    return cat.palette.resolve(ref)


def fills(geometry: str | None = None) -> dict[str, str]:
    """``element id -> fill colour`` for flat styling in any tool (``gdf.element.map(ulg.fills())``)."""
    return {el.id: el.fill for el in load() if el.fill and (geometry is None or geometry in el.geometry)}


def ramp(name: str, n: int | None = None) -> list[str]:
    """A mellow sequential or diverging colour ramp for analysis layers (``heat``, ``cool``, ``vitality`` ...)."""
    from . import colormath as C

    ramps = load().settings.get("ramps", {})
    if name not in ramps:
        raise CatalogError(f"unknown ramp {name!r}; available: {', '.join(sorted(ramps))}")
    stops = ramps[name]["colors"]
    return list(stops) if n is None else C.ramp(stops, n)


def categories(name: str) -> list[dict]:
    """Class list of a categorical palette (``klimatop``, ``utci``, ``pet``) with labels, limits and colours."""
    cats = load().settings.get("categories", {})
    if name not in cats:
        raise CatalogError(f"unknown category set {name!r}; available: {', '.join(sorted(cats))}")
    return [dict(c) for c in cats[name]["classes"]]


def category_of(name: str, value: float) -> dict:
    """The class of a numeric value in a banded category set, e.g. ``category_of("utci", 34.2)``."""
    for c in categories(name):
        lo, hi = c.get("min", float("-inf")), c.get("max", float("inf"))
        if lo <= value < hi:
            return c
    raise ValueError(f"{value} is outside the classes of {name!r}")


def style_function(field: str = "element", weight: float = 0.8, fill_opacity: float = 1.0):
    """A style callback for Leaflet-style APIs (``folium.GeoJson(data, style_function=ulg.style_function())``)."""
    cat = load()
    fallback = cat.get("unknown")

    def style(feature: dict) -> dict:
        el = cat.get((feature.get("properties") or {}).get(field)) or fallback
        if el is None:
            return {}
        line = el.line or {}
        return {
            "fillColor": el.fill or "#000000",
            "fillOpacity": fill_opacity * el.fill_opacity if el.fill else 0.0,
            "color": line.get("color") or el.outline or el.fill or "#505B61",
            "weight": weight if "polygon" in el.geometry else max(weight, line.get("width", 0.3) * 3.78),
            "opacity": 1.0,
        }

    return style


def style_sheet(path=None, **kw):
    """The one-page overview of the style as SVG (see :mod:`ulg.sheet`)."""
    from .sheet import style_sheet as _fn

    return _fn(path, **kw)


def catalog_sheet(path=None, **kw):
    """All elements with swatch, id and names as SVG (see :mod:`ulg.sheet`)."""
    from .sheet import catalog_sheet as _fn

    return _fn(path, **kw)

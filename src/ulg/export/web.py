"""Web exports: SVG pattern tiles, an SVG ``<defs>`` sheet, and a MapLibre GL sprite with style layers."""

from __future__ import annotations

import json
import math
from pathlib import Path

from .. import colormath as C
from ..catalog import Catalog, Element, load
from ..render.samples import tile_items, tile_svg
from ..render.scene import SIZE_FIELDS, area_only
from ..render.svg import Svg

PX_PER_MM = 96.0 / 25.4


def _textured(catalog: Catalog, elements=None) -> list[Element]:
    picked = [catalog[e] for e in elements] if elements else list(catalog)
    return [el for el in picked if "polygon" in el.geometry and el.textures]


def pattern_files(directory, *, lod: int = 2, size: float = 32.0, background: bool = True, elements=None,
                  catalog: Catalog | None = None) -> list[Path]:
    """One seamless SVG tile per textured polygon element (``<id>.svg``)."""
    catalog = catalog or load()
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    out = []
    for el in _textured(catalog, elements):
        out.append(tile_svg(el, size, lod, background=background).save(d / f"{el.id}.svg"))
    return out


def patterns_svg(path=None, *, lod: int = 2, size: float = 32.0, elements=None, prefix: str = "ulg-",
                 catalog: Catalog | None = None) -> str:
    """An SVG holding ``<pattern id="ulg-lawn">`` for every textured element.

    Inline it once in a page; then any SVG shape (Leaflet's SVG renderer, D3,
    hand-written SVG) can use ``fill="url(#ulg-lawn)"``. Pattern units are CSS
    pixels, so the marks have the same physical size as in print.
    """
    catalog = catalog or load()
    px = size * PX_PER_MM
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute" '
             'aria-hidden="true"><defs>']
    for el in _textured(catalog, elements):
        page = Svg(size, size)
        page.frame(tile_items(el, size, lod), (0, 0, size, size), 1.0, clip=False)
        parts.append(f'<pattern id="{prefix}{el.id}" patternUnits="userSpaceOnUse" width="{px:.2f}" height="{px:.2f}">'
                     f'<rect width="{px:.2f}" height="{px:.2f}" fill="{el.fill or "none"}"/>'
                     f'<g transform="scale({PX_PER_MM:.4f})">{"".join(page._body)}</g></pattern>')
    parts.append("</defs></svg>")
    text = "\n".join(parts) + "\n"
    if path:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return text


# --------------------------------------------------------------------------- MapLibre

def _tile_rgba(el: Element, px: int, ratio: int, lod: int, background: bool = False):
    """Rasterise one seamless pattern tile with Matplotlib (no SVG rasteriser needed).

    With ``background`` the element's fill is painted under the marks, so the tile
    replaces the flat fill and features stack correctly within a single layer.
    """
    import numpy as np
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    from matplotlib.patches import Rectangle

    from ..render.mpl import MplPainter

    size = px / PX_PER_MM
    fig = Figure(figsize=(px / 96.0, px / 96.0), dpi=96 * ratio)
    canvas = FigureCanvasAgg(fig)
    fig.patch.set_alpha(0.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    if background and el.fill:
        ax.add_patch(Rectangle((-1, -1), size + 2, size + 2, facecolor=el.fill, alpha=el.fill_opacity,
                               linewidth=0, zorder=0))
    MplPainter(ax).draw(tile_items(el, size, lod) if el.textures else [])
    canvas.draw()
    return np.asarray(canvas.buffer_rgba()).copy()


def _overlay(el: Element) -> bool:
    return el.attributes.get("layer") == "overlay"


def _sprite_tiles(catalog: Catalog, elements=None) -> list[Element]:
    """Polygon elements that get a sprite tile: every textured or filled area."""
    picked = [catalog[e] for e in elements] if elements else list(catalog)
    return [el for el in picked if "polygon" in el.geometry and (el.textures or el.fill)]


def _icon_rgba(el: Element, px: int, ratio: int):
    """Rasterise a point symbol (pictogram) into a transparent square icon."""
    import numpy as np
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure

    from ..render.mpl import MplPainter
    from ..render.samples import symbol_items

    size = px / PX_PER_MM
    fig = Figure(figsize=(px / 96.0, px / 96.0), dpi=96 * ratio)
    canvas = FigureCanvasAgg(fig)
    fig.patch.set_alpha(0.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.set_xlim(-size / 2, size / 2)
    ax.set_ylim(-size / 2, size / 2)
    MplPainter(ax).draw(symbol_items(el, size * 0.94))
    canvas.draw()
    return np.asarray(canvas.buffer_rgba()).copy()


def _pictograms(catalog: Catalog) -> list[Element]:
    return [el for el in catalog if "point" in el.geometry and el.symbol
            and el.symbol.get("kind") not in ("crown", "dot")]


def _crowns(catalog: Catalog) -> list[Element]:
    return [el for el in catalog if "point" in el.geometry and (el.symbol or {}).get("kind") == "crown"]


#: share of the icon box that the crown itself fills (see ``samples.symbol_items``)
CROWN_FILL = {True: 0.72, False: 0.92}


def maplibre_sprite(directory, *, name: str = "ulg-sprite", px: int = 128, icon_px: int = 24, crown_px: int = 64,
                    lod: int = 2, elements=None, prefix: str = "ulg-", catalog: Catalog | None = None) -> list[Path]:
    """Write ``<name>.png/.json`` and ``<name>@2x.png/.json``: one pattern tile per area element
    (``ulg-<id>``; opaque with the fill painted in, transparent for overlays), one icon per
    pictogram (``ulg-icon-<id>``, ``icon_px`` wide) and one
    crown per tree or shrub element (``ulg-crown-<id>``, ``crown_px`` wide, scaled to the real
    crown diameter by the layers of :func:`maplibre_layers`)."""
    import numpy as np
    from matplotlib import image as mimage

    catalog = catalog or load()
    els = _sprite_tiles(catalog, elements)
    groups = [(_pictograms(catalog), icon_px, "icon"), (_crowns(catalog), crown_px, "crown")]
    cols = max(1, math.ceil(math.sqrt(len(els))))
    rows = max(1, math.ceil(len(els) / cols))
    width = cols * px

    def rows_for(n: int, size: int) -> int:
        return math.ceil(n / max(1, width // size)) if n else 0

    extra = sum(rows_for(len(g), size) * size for g, size, _ in groups)
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    out = []
    for ratio in (1, 2):
        cell = px * ratio
        sheet = np.zeros((rows * cell + extra * ratio, cols * cell, 4), dtype=np.uint8)
        index = {}
        for k, el in enumerate(els):
            r, c = divmod(k, cols)
            sheet[r * cell:(r + 1) * cell, c * cell:(c + 1) * cell] = _tile_rgba(el, px, ratio, lod,
                                                                               background=not _overlay(el))
            index[f"{prefix}{el.id}"] = {"x": c * cell, "y": r * cell, "width": cell, "height": cell,
                                         "pixelRatio": ratio}
        y_base = rows * cell
        for group, size, kind in groups:
            icell = size * ratio
            per_row = max(1, (cols * cell) // icell)
            for k, el in enumerate(group):
                r, c = divmod(k, per_row)
                y0, x0 = y_base + r * icell, c * icell
                sheet[y0:y0 + icell, x0:x0 + icell] = _icon_rgba(el, size, ratio)
                index[f"{prefix}{kind}-{el.id}"] = {"x": x0, "y": y0, "width": icell, "height": icell,
                                                    "pixelRatio": ratio}
            y_base += rows_for(len(group), size) * icell
        suffix = "" if ratio == 1 else "@2x"
        png, js = d / f"{name}{suffix}.png", d / f"{name}{suffix}.json"
        mimage.imsave(png, sheet)
        js.write_text(json.dumps(index, indent=1), encoding="utf-8")
        out += [png, js]
    return out


def _match(field: str, pairs: list[tuple[str, object]], default) -> list:
    expr: list = ["match", ["get", field]]
    for key, value in pairs:
        expr += [key, value]
    expr.append(default)
    return expr


def _strip_width(el_ids: list[str], field: str, catalog: Catalog) -> list:
    """Width in metres of a centre line drawn as an area, as a MapLibre expression (see ``centreline_area``)."""
    cfg = catalog.settings.get("centreline_widths_m", {})
    by_element = _match(field, [(i, cfg.get("element", {})[i]) for i in el_ids if i in cfg.get("element", {})],
                        cfg.get("default", 2.0))
    by_class = ["match", ["to-string", ["get", "highway"]]]
    for k, v in cfg.get("highway", {}).items():
        by_class += [k, v]
    by_class.append(by_element)
    lanes = ["*", ["to-number", ["get", "lanes"], 0], cfg.get("lane_m", 3.0)]
    fallback = ["case", ["all", ["has", "lanes"], [">", lanes, 0]], lanes, by_class]
    return ["case", ["has", "width"], ["to-number", ["get", "width"], fallback], fallback]


def maplibre_layers(source: str = "ulg", *, source_layer: str | None = None, field: str = "element",
                    latitude: float = 50.0, pattern_minzoom: float = 15.5, prefix: str = "ulg-",
                    size_field: str = "crown_diameter", crown_px: int = 64, area_field: str = "area_m2",
                    catalog: Catalog | None = None) -> list[dict]:
    """Style layers for a MapLibre GL / Mapbox GL style: fills, patterns, outlines, strips, lines, tree crowns.

    Append them to the ``layers`` of your style and point ``sprite`` at the files
    from :func:`maplibre_sprite`. Features need the element id in ``field``; an
    ``area_field`` (added by :func:`to_geojson`) lets smaller areas draw on top of
    larger ones of the same z, as in the Python renderer. Roads and paths given as
    centre lines are drawn as strips of their real width (``width``, ``lanes``,
    ``highway`` or the element default).
    """
    catalog = catalog or load()
    base: dict = {"source": source}
    if source_layer:
        base["source-layer"] = source_layer
    polys = [el for el in catalog if "polygon" in el.geometry]
    lines = [el for el in catalog if "line" in el.geometry]
    crowns = [el for el in catalog if "point" in el.geometry and (el.symbol or {}).get("kind") == "crown"]
    markers = [el for el in catalog if "point" in el.geometry and el not in crowns]
    is_poly = ["match", ["geometry-type"], ["Polygon", "MultiPolygon"], True, False]
    is_line = ["match", ["geometry-type"], ["LineString", "MultiLineString"], True, False]
    is_point = ["match", ["geometry-type"], ["Point", "MultiPoint"], True, False]
    fills = [(el.id, el.fill) for el in polys if el.fill]
    inks = [(el.id, el.outline) for el in polys if el.outline]
    pats = [(el.id, f"{prefix}{el.id}") for el in _sprite_tiles(catalog)]
    order = [(el.id, el.z) for el in catalog]
    # z first, then larger areas below smaller ones (MapLibre draws higher keys on top)
    sort_key = ["-", ["*", _match(field, order, 50), 1e7], ["to-number", ["get", area_field], 0]]
    tiled = ["in", ["get", field], ["literal", [k for k, _ in pats]]]
    # below pattern_minzoom flat colours; above it one layer of tiles that carry their own fill,
    # so textures stack per feature exactly like the flat fills (a park never shows through its lawn)
    layers: list[dict] = [
        {"id": f"{prefix}fill", "type": "fill", **base, "maxzoom": pattern_minzoom, "filter": is_poly,
         "layout": {"fill-sort-key": sort_key},
         "paint": {"fill-color": _match(field, fills, "rgba(0,0,0,0)"), "fill-antialias": True}},
        {"id": f"{prefix}pattern", "type": "fill", **base, "minzoom": pattern_minzoom,
         "filter": ["all", is_poly, tiled],
         "layout": {"fill-sort-key": sort_key},
         "paint": {"fill-pattern": _match(field, pats, pats[0][1] if pats else "")}},
        {"id": f"{prefix}outline", "type": "line", **base, "filter": is_poly,
         "layout": {"line-join": "round", "line-sort-key": sort_key},
         "paint": {"line-color": _match(field, inks, "rgba(0,0,0,0)"),
                   "line-width": ["interpolate", ["linear"], ["zoom"], 12, 0.3, 17, 0.8]}},
    ]
    k = 512.0 / (40075016.686 * math.cos(math.radians(latitude)))  # pixels per metre at zoom 0 (512-px tiles)
    strips = [el for el in polys if area_only(el) and el.fill]
    if strips:
        ids = [el.id for el in strips]
        width = _strip_width(ids, field, catalog)
        px = ["interpolate", ["exponential", 2], ["zoom"], 10, ["*", width, k * 2**10], 24, ["*", width, k * 2**24]]
        is_strip = ["all", is_line, ["in", ["get", field], ["literal", ids]]]
        layers += [
            {"id": f"{prefix}strips-casing", "type": "line", **base, "filter": is_strip,
             "layout": {"line-join": "round", "line-cap": "round"},
             "paint": {"line-color": _match(field, [(el.id, el.outline or C.darken(el.fill, 0.1)) for el in strips],
                                            "#C6CACA"),
                       "line-width": ["interpolate", ["exponential", 2], ["zoom"],
                                      10, ["+", ["*", width, k * 2**10], 0.4], 24, ["+", ["*", width, k * 2**24], 0.8]]}},
            {"id": f"{prefix}strips", "type": "line", **base, "filter": is_strip,
             "layout": {"line-join": "round", "line-cap": "round",
                        "line-sort-key": ["-", 0, width]},
             "paint": {"line-color": _match(field, [(el.id, el.fill) for el in strips], "#FFFFFF"), "line-width": px}},
        ]
    if lines:
        cols = [(el.id, (el.line or {}).get("color") or el.outline or "rgba(0,0,0,0)") for el in lines]
        widths = [(el.id, round((el.line or {}).get("width", 0.3) * PX_PER_MM, 2)) for el in lines]
        layers.append({"id": f"{prefix}lines", "type": "line", **base,
                       "filter": ["all", is_line, ["in", ["get", field], ["literal", [el.id for el in lines]]]],
                       "layout": {"line-join": "round", "line-cap": "round"},
                       "paint": {"line-color": _match(field, cols, "#505B61"),
                                 "line-width": _match(field, widths, 1.0)}})
    if crowns:
        # crown diameter in metres from the first size attribute present (crown_diameter, OSM diameter_crown,
        # kronendurchmesser ...), else the element default; to-number(null) would give 0, hence "has"
        default = _match(field, [(el.id, el.symbol.get("crown_m", 6.0)) for el in crowns], 6.0)
        diameter: list = ["case"]
        for name in dict.fromkeys((size_field, *SIZE_FIELDS)):
            diameter += [["has", name], ["to-number", ["get", name], default]]
        diameter.append(default)
        in_crowns = ["in", ["get", field], ["literal", [el.id for el in crowns]]]
        # low zoom: plain circles in metres; from z15: the drawn crown icon, scaled to its real diameter
        layers.append({"id": f"{prefix}trees", "type": "circle", **base, "maxzoom": 15,
                       "filter": ["all", is_point, in_crowns],
                       "paint": {
                           "circle-radius": ["interpolate", ["exponential", 2], ["zoom"],
                                             0, ["*", diameter, k / 2], 24, ["*", diameter, k / 2 * 2**24]],
                           "circle-color": _match(field, [(el.id, el.symbol["tones"][0]) for el in crowns], "#98A585"),
                           "circle-opacity": 0.92, "circle-pitch-alignment": "map"}})
        fill = [(el.id, round(1.0 / (crown_px * CROWN_FILL[bool(el.symbol.get("frame"))]), 6)) for el in crowns]
        per_px = _match(field, fill, round(1.0 / (crown_px * 0.92), 6))
        layers.append({"id": f"{prefix}crowns", "type": "symbol", **base, "minzoom": 15,
                       "filter": ["all", is_point, in_crowns],
                       "layout": {"icon-image": ["concat", f"{prefix}crown-", ["get", field]],
                                  "icon-size": ["interpolate", ["exponential", 2], ["zoom"],
                                                15, ["*", ["*", diameter, per_px], k * 2**15],
                                                24, ["*", ["*", diameter, per_px], k * 2**24]],
                                  "icon-allow-overlap": True, "icon-ignore-placement": True,
                                  "icon-rotation-alignment": "map", "icon-pitch-alignment": "map",
                                  "symbol-sort-key": ["-", 0, diameter]}})
    dots = [el for el in markers if (el.symbol or {}).get("kind", "dot") == "dot"]
    icons = [el for el in markers if el not in dots]
    if dots:
        layers.append({"id": f"{prefix}points", "type": "circle", **base,
                       "filter": ["all", is_point, ["in", ["get", field], ["literal", [el.id for el in dots]]]],
                       "paint": {"circle-radius": _match(field, [(el.id, round((el.symbol or {}).get("r", 0.6) * PX_PER_MM, 2)) for el in dots], 2.5),
                                 "circle-color": _match(field, [(el.id, (el.symbol or {}).get("color") or el.fill or "#505B61") for el in dots], "#505B61"),
                                 "circle-stroke-color": "#FDFDFB", "circle-stroke-width": 0.8}})
    if icons:
        layers.append({"id": f"{prefix}icons", "type": "symbol", **base, "minzoom": 17,
                       "filter": ["all", is_point, ["in", ["get", field], ["literal", [el.id for el in icons]]]],
                       "layout": {"icon-image": ["concat", f"{prefix}icon-", ["get", field]],
                                  "icon-size": ["interpolate", ["linear"], ["zoom"], 17, 0.5, 20, 1.1],
                                  "icon-allow-overlap": True, "icon-ignore-placement": True}})
    return layers


def to_geojson(data, path=None, *, columns: list[str] | None = None, area_field: str = "area_m2") -> dict:
    """GeoJSON for web maps (RFC 7946, WGS 84) from a GeoDataFrame in any CRS.

    Adds ``area_field`` (m², computed in a metric CRS) to every area, which the
    MapLibre layers use to draw smaller areas above larger ones. ``columns`` limits
    the properties that are written (the element column and sizes, for example).
    """
    if getattr(data, "crs", None) is None:
        raise ValueError("to_geojson needs a GeoDataFrame with a CRS")
    metric = data.to_crs(data.estimate_utm_crs()) if data.crs.is_geographic else data
    out = data.copy()
    polygonal = metric.geom_type.isin(["Polygon", "MultiPolygon"])
    out[area_field] = metric.geometry.area.round(1).where(polygonal)
    keep = [c for c in (columns or [c for c in out.columns if c != out.geometry.name])] + (
        [area_field] if columns and area_field not in columns else [])
    doc = json.loads(out[keep + [out.geometry.name]].to_crs(4326).to_json(drop_id=True, na="drop"))
    if path is not None:
        Path(path).write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return doc


def export_web(directory, *, lod: int = 2, latitude: float = 50.0, sprite: bool = True,
               catalog: Catalog | None = None) -> list[Path]:
    """Everything a web app needs: tokens, catalog, SVG patterns and MapLibre assets."""
    from . import tokens

    catalog = catalog or load()
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    out = [d / "ulg.css", d / "ulg.tokens.json", d / "ulg-colors.json", d / "catalog.json", d / "patterns.svg",
           d / "maplibre-layers.json"]
    tokens.css(out[0], catalog=catalog)
    tokens.dtcg(out[1], catalog=catalog)
    tokens.tokens_json(out[2], catalog=catalog)
    tokens.catalog_json(out[3], catalog=catalog)
    patterns_svg(out[4], lod=lod, catalog=catalog)
    out[5].write_text(json.dumps(maplibre_layers(latitude=latitude, catalog=catalog), indent=1), encoding="utf-8")
    out += pattern_files(d / "patterns", lod=lod, catalog=catalog)
    if sprite:
        try:
            out += maplibre_sprite(d, lod=lod, catalog=catalog)
        except ImportError:  # Matplotlib not installed: everything else is still usable
            pass
    return out

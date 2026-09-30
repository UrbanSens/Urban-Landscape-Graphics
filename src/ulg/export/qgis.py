"""QGIS export: layer styles (.qml), a symbol library for the Style Manager (.xml) and a colour palette (.gpl).

Textures are embedded as seamless SVG pattern tiles (``base64:`` in an SVG fill
layer), so the files are self-contained: no SVG search path, no plugin. The XML
mirrors what QGIS 3.36 itself writes and loads in QGIS 3.28 and later.
"""

from __future__ import annotations

import base64
import uuid
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import numpy as np

from .. import colormath as C
from ..catalog import Catalog, Element, load
from ..render import rand as R
from ..render.geom import Ctx
from ..render.motifs import crown_items, params_for
from ..render.samples import tile_svg
from ..render.scene import LOD_BREAKS, area_only
from ..render.svg import Svg

MUS = "3x:0,0,0,0,0,0"  # default map-unit-scale
QGIS_VERSION = "3.28.0"


# --------------------------------------------------------------------------- XML helpers

def _rgba(hexc: str, alpha: float = 1.0) -> str:
    r, g, b = C.to_rgb255(hexc)
    return f"{r},{g},{b},{round(alpha * 255)}"


def _opt(name: str, value, typ: str = "QString") -> str:
    if isinstance(value, bool):
        value, typ = ("true" if value else "false"), "bool"
    return f"<Option name={quoteattr(name)} value={quoteattr(str(value))} type=\"{typ}\"/>"


def _ddp(props: dict[str, str] | None = None) -> str:
    """Data-defined properties block; ``props`` maps a property name to an expression."""
    if not props:
        inner = '<Option name="properties"/>'
    else:
        inner = '<Option name="properties" type="Map">' + "".join(
            f'<Option name={quoteattr(k)} type="Map">{_opt("active", True)}{_opt("expression", v)}'
            f'{_opt("type", 3, "int")}</Option>' for k, v in props.items()) + "</Option>"
    return ('<data_defined_properties><Option type="Map">' + _opt("name", "") + inner
            + _opt("type", "collection") + "</Option></data_defined_properties>")


def _layer(cls: str, options: dict, ddp: dict | None = None, sub: str = "") -> str:
    body = "".join(_opt(k, v) if not isinstance(v, str) or not v.startswith("<") else v for k, v in options.items())
    return (f'<layer class="{cls}" enabled="1" locked="0" pass="0" id="{{{uuid.uuid4()}}}">'
            f'<Option type="Map">{body}</Option>{_ddp(ddp)}{sub}</layer>')


def _symbol(name: str, typ: str, layers: list[str], alpha: float = 1.0) -> str:
    return (f'<symbol name={quoteattr(name)} type="{typ}" alpha="{alpha:g}" clip_to_extent="1" force_rhr="0" '
            f'is_animated="0" frame_rate="10">{_ddp()}{"".join(layers)}</symbol>')


def _b64(svg_text: str) -> str:
    return "base64:" + base64.b64encode(svg_text.encode("utf-8")).decode("ascii")


# --------------------------------------------------------------------------- symbol layers

def _geometry_generator(expression: str, sub_symbol: str, symbol_type: str = "Line", units: str = "MM") -> str:
    return _layer("GeometryGenerator", {"SymbolType": symbol_type, "geometryModifier": expression, "units": units},
                  sub=sub_symbol)


#: hand-drawn outline for QGIS >= 3.24: a seeded, randomised wave along the boundary, in paper millimetres.
#: The amplitude stays below half the line width, so the ink still covers the true edge.
WOBBLE_EXPR = "wave_randomized($geometry, 4, 12, 0.03, 0.09, $id + 1)"


def _simple_fill(hexc: str, alpha: float = 1.0) -> str:
    return _layer("SimpleFill", {
        "border_width_map_unit_scale": MUS, "color": _rgba(hexc, alpha), "joinstyle": "round", "offset": "0,0",
        "offset_map_unit_scale": MUS, "offset_unit": "MM", "outline_color": _rgba(hexc), "outline_style": "no",
        "outline_width": "0", "outline_width_unit": "MM", "style": "solid"})


def _svg_fill(svg_text: str, width: float, unit: str = "MM") -> str:
    return _layer("SVGFill", {
        "angle": "0", "color": "255,255,255,255", "outline_color": "35,35,35,255", "outline_width": "0.2",
        "outline_width_map_unit_scale": MUS, "outline_width_unit": "MM", "parameters": '<Option name="parameters"/>',
        "pattern_width_map_unit_scale": MUS, "pattern_width_unit": unit, "svgFile": _b64(svg_text),
        "svg_outline_width_map_unit_scale": MUS, "svg_outline_width_unit": "MM", "width": f"{width:g}"})


def _simple_line(hexc: str, width: float, dash: tuple | None = None, cap: str = "round", inside: bool = False) -> str:
    return _layer("SimpleLine", {
        "align_dash_pattern": "0", "capstyle": cap, "customdash": ";".join(f"{v:g}" for v in (dash or (5, 2))),
        "customdash_map_unit_scale": MUS, "customdash_unit": "MM", "dash_pattern_offset": "0",
        "dash_pattern_offset_map_unit_scale": MUS, "dash_pattern_offset_unit": "MM",
        "draw_inside_polygon": "1" if inside else "0", "joinstyle": "round", "line_color": _rgba(hexc),
        "line_style": "solid", "line_width": f"{width:g}", "line_width_unit": "MM", "offset": "0",
        "offset_map_unit_scale": MUS, "offset_unit": "MM", "ring_filter": "0", "trim_distance_end": "0",
        "trim_distance_end_map_unit_scale": MUS, "trim_distance_end_unit": "MM", "trim_distance_start": "0",
        "trim_distance_start_map_unit_scale": MUS, "trim_distance_start_unit": "MM",
        "tweak_dash_pattern_on_corners": "0", "use_custom_dash": "1" if dash else "0", "width_map_unit_scale": MUS})


def _simple_marker(shape: str, size: float, fill: str | None, stroke: str | None, stroke_width: float = 0.2,
                   angle: float = 0.0) -> str:
    return _layer("SimpleMarker", {
        "angle": f"{angle:g}", "cap_style": "round", "color": _rgba(fill) if fill else "0,0,0,0",
        "horizontal_anchor_point": "1", "joinstyle": "round", "name": shape, "offset": "0,0",
        "offset_map_unit_scale": MUS, "offset_unit": "MM", "outline_color": _rgba(stroke) if stroke else "0,0,0,0",
        "outline_style": "solid" if stroke else "no", "outline_width": f"{stroke_width:g}",
        "outline_width_map_unit_scale": MUS, "outline_width_unit": "MM", "scale_method": "diameter",
        "size": f"{size:g}", "size_map_unit_scale": MUS, "size_unit": "MM", "vertical_anchor_point": "1"})


def _svg_marker(svg_text: str, size: float, unit: str = "MM", ddp: dict | None = None) -> str:
    return _layer("SvgMarker", {
        "angle": "0", "color": "35,35,35,255", "fixedAspectRatio": "0", "horizontal_anchor_point": "1",
        "name": _b64(svg_text), "offset": "0,0", "offset_map_unit_scale": MUS, "offset_unit": "MM",
        "outline_color": "35,35,35,255", "outline_width": "0", "outline_width_map_unit_scale": MUS,
        "outline_width_unit": "MM", "parameters": '<Option name="parameters"/>', "scale_method": "diameter",
        "size": f"{size:g}", "size_map_unit_scale": MUS, "size_unit": unit, "vertical_anchor_point": "1"}, ddp)


def _marker_line(marker_symbol: str, interval: float, unit: str = "MM") -> str:
    return _layer("MarkerLine", {
        "average_angle_length": "4", "average_angle_map_unit_scale": MUS, "average_angle_unit": "MM",
        "interval": f"{interval:g}", "interval_map_unit_scale": MUS, "interval_unit": unit, "offset": "0",
        "offset_along_line": "0", "offset_along_line_map_unit_scale": MUS, "offset_along_line_unit": "MM",
        "offset_map_unit_scale": MUS, "offset_unit": "MM", "place_on_every_part": True, "placements": "Interval",
        "ring_filter": "0", "rotate": "1"}, sub=marker_symbol)


# --------------------------------------------------------------------------- symbols per element

def crown_svg(spec: dict, lod: int = 2, seed: int = 0, size: float = 12.0) -> str:
    """A single crown symbol as SVG text, drawn ``size`` mm wide (used as a scalable marker)."""
    p = params_for("canopy", spec, lod)
    p["star"] = p.get("star", True) and lod >= 2
    p["star_min"] = 0.0
    margin = 1.04
    half = 0.5 * size / margin
    s = R.Stream(np.array([seed + 3]), np.array([seed + 11]), R.stable_seed("crown", seed))
    items = crown_items(np.array([0.0]), np.array([0.0]), np.array([half]), s, p, Ctx(u=1.0, lod=lod))
    svg = Svg(size, size)
    h = 0.5 * size
    svg.frame(items, (-h, -h, h, h), 1.0, clip=False)
    return svg.tostring()


def symbol_for(el: Element, name: str | None = None, *, lod: int = 2, tile: float = 32.0,
               kind: str | None = None, size_field: str = "crown_diameter", handdrawn: bool = False) -> str | None:
    """``<symbol>`` XML for an element; ``kind`` picks fill, line or marker if the element allows several."""
    name = name or el.id
    kind = kind or {"polygon": "fill", "line": "line", "point": "marker"}[el.geometry[0]]
    if kind == "fill":
        layers = []
        if el.fill:
            layers.append(_simple_fill(el.fill, el.fill_opacity))
        if el.textures and lod >= 1:
            layers.append(_svg_fill(tile_svg(el, tile, lod).tostring(), tile))
        if el.outline:
            line = _simple_line(el.outline, el.outline_width or 0.18, el.outline_dash,
                                cap="flat" if el.outline_dash else "round")
            if handdrawn and lod >= 1 and not el.outline_dash:
                line = _geometry_generator(WOBBLE_EXPR, _symbol(f"@{name}@{len(layers)}", "line", [line]))
            layers.append(line)
        if el.border:
            b = el.border
            col = b.get("color") or el.outline or "#505B61"
            if b.get("kind") in ("dots", "rings"):
                marker = _simple_marker("circle", 2 * b.get("r", 0.35), col if b["kind"] == "dots" else "#FFFFFF",
                                        None if b["kind"] == "dots" else col, b.get("width", 0.2))
            else:
                marker = _simple_marker("line", b.get("length", 0.9), None, col, b.get("width", 0.2))
            layers.append(_marker_line(_symbol(f"@{name}@{len(layers)}", "marker", [marker]), b.get("step", 2.4)))
        return _symbol(name, "fill", layers) if layers else None
    if kind == "line":
        spec = el.line or {"color": el.outline or el.fill or "#505B61", "width": 0.3}
        w = spec.get("width", min(max(spec.get("width_m", 1.0), spec.get("width_min", 0.25)), 1.4))
        layers = []
        if spec.get("casing"):
            layers.append(_simple_line(spec["casing"], w + 2 * spec.get("casing_width", 0.18)))
        if spec.get("color"):
            layers.append(_simple_line(spec["color"], w, spec.get("dash"), cap="flat" if spec.get("dash") else "round"))
        marks = spec.get("marks")
        if marks:
            if marks.get("kind") == "crowns":
                dia = marks.get("crown_m", 1.5)
                sub = _symbol("@0@1", "marker", [_svg_marker(crown_svg(marks, lod), dia * 1.04, "MapUnit",
                                                             {"angle": "($id * 47 + @geometry_part_num * 83) % 360"})])
                layers.append(_marker_line(sub, dia * marks.get("pack", 0.8), "MapUnit"))
            elif marks.get("kind") == "dots":
                sub = _symbol("@0@1", "marker", [_simple_marker("circle", 2 * marks.get("r", 0.3),
                                                                marks.get("color") or el.outline, None)])
                layers.append(_marker_line(sub, marks.get("step", 2.4)))
            else:
                shape = "cross2" if marks.get("kind") == "cross" else "line"
                sub = _symbol("@0@1", "marker", [_simple_marker(shape, marks.get("length", 0.9), None,
                                                                marks.get("color") or el.outline,
                                                                marks.get("width", 0.2))])
                layers.append(_marker_line(sub, marks.get("step", 2.4)))
        return _symbol(name, "line", layers) if layers else None
    spec = el.symbol or {"kind": "dot", "r": 0.6, "color": el.fill or "#505B61"}
    if spec.get("kind") == "crown":
        default = spec.get("crown_m", 6.0)
        ddp = {"size": f'coalesce("{size_field}", {default:g}) * 1.04', "angle": "($id * 47) % 360"}
        return _symbol(name, "marker", [_svg_marker(crown_svg(spec, lod), default * 1.04, "MapUnit", ddp)])
    if spec.get("kind", "dot") == "dot":
        col = spec.get("color") or el.fill or "#505B61"
        layers = []
        if spec.get("halo"):
            layers.append(_simple_marker("circle", 2 * (spec.get("r", 0.6) + spec.get("halo_width", 0.25)), spec["halo"], None))
        layers.append(_simple_marker("circle", 2 * spec.get("r", 0.6), col, None))
        return _symbol(name, "marker", layers)
    from ..render.samples import symbol_svg

    size = 3.2 * spec.get("r", 0.6) + 0.6
    return _symbol(name, "marker", [_svg_marker(symbol_svg(el, 10.0), size)])


# --------------------------------------------------------------------------- documents

def _elements(catalog: Catalog, geometry: str, elements) -> list[Element]:
    picked = [catalog[e] for e in elements] if elements else list(catalog)
    if geometry == "line":  # roads and paths mapped as centre lines are drawn as strips of their width
        return [el for el in picked if "line" in el.geometry or area_only(el)]
    return [el for el in picked if geometry in el.geometry]


def _order_by(els: list[Element], field: str) -> str:
    """Feature drawing order = catalog z-order, then larger areas first (as the Python renderer)."""
    by_z: dict[int, list[str]] = {}
    for el in els:
        by_z.setdefault(el.z, []).append(el.id)
    whens = " ".join('WHEN "{}" IN ({}) THEN {}'.format(field, ", ".join(f"'{i}'" for i in ids), z)
                     for z, ids in sorted(by_z.items()))
    return (f'<orderby><orderByClause asc="1" nullsFirst="0">{escape(f"CASE {whens} ELSE 50 END")}</orderByClause>'
            '<orderByClause asc="0" nullsFirst="0">$area</orderByClause></orderby>')


def width_expression(el: Element, catalog: Catalog) -> str:
    """QGIS expression for the width in metres of a centre line drawn as an area (see ``centreline_area``)."""
    cfg = catalog.settings.get("centreline_widths_m", {})
    by_class = " ".join(f"WHEN attribute(@feature, 'highway') = '{k}' THEN {v:g}" for k, v in cfg.get("highway", {}).items())
    default = cfg.get("element", {}).get(el.id) or cfg.get("default", 2.0)
    return ("coalesce(to_real(replace(regexp_substr(to_string(attribute(@feature, 'width')), "
            "'[0-9]+(?:[.,][0-9]+)?'), ',', '.')), "
            f"to_real(attribute(@feature, 'lanes')) * {cfg.get('lane_m', 3.0):g}, "
            f"CASE {by_class} END, {default:g})")


def strip_symbol(el: Element, name: str, catalog: Catalog, *, lod: int = 2, tile: float = 32.0) -> str | None:
    """Line symbol that draws a centre line as the element's area, buffered to its width in map units."""
    fill = symbol_for(el, f"@{name}@0", lod=lod, tile=tile, kind="fill")
    if fill is None:
        return None
    expr = f"buffer($geometry, ({width_expression(el, catalog)}) / 2)"
    return _symbol(name, "line", [_geometry_generator(expr, fill, symbol_type="Fill", units="MapUnit")])


def layer_style(path, geometry: str = "polygon", *, field: str = "element", elements=None,
                lod: int | str = 2, lang: str = "en", tile: float = 32.0, handdrawn: bool = False,
                catalog: Catalog | None = None) -> Path:
    """Write a QGIS layer style (.qml) that draws every catalog element of one geometry type.

    Load it in QGIS via *Layer Properties > Style > Load Style*. The layer needs an
    attribute ``field`` holding element ids. With ``lod="auto"`` a rule-based
    renderer switches the level of detail with the map scale.
    """
    catalog = catalog or load()
    kind = {"polygon": "fill", "line": "line", "point": "marker"}[geometry]
    els = _elements(catalog, geometry, elements)
    symbols: list[str] = []
    order = _order_by(els, field)

    def make(el: Element, name: str, level: int) -> str | None:
        if kind == "line" and area_only(el):
            return strip_symbol(el, name, catalog, lod=level, tile=tile)
        return symbol_for(el, name, lod=level, tile=tile, kind=kind, handdrawn=handdrawn)

    if lod == "auto":
        a, b, c = LOD_BREAKS
        ranges = [(3, 0, a), (2, a, b), (1, b, c), (0, c, 0)]
        rules = []
        for el in els:
            children = []
            for level, smin, smax in ranges:
                sym = make(el, str(len(symbols)), level)
                if sym is None:
                    continue
                attrs = f' scalemindenom="{smin}"' if smin else ""
                attrs += f' scalemaxdenom="{smax}"' if smax else ""
                children.append(f'<rule key="{{{uuid.uuid4()}}}" symbol="{len(symbols)}" label="LOD {level}"{attrs}/>')
                symbols.append(sym)
            flt = f'"{field}" = \'{el.id}\''
            rules.append(f'<rule key="{{{uuid.uuid4()}}}" filter={quoteattr(flt)} label={quoteattr(el.name(lang))}>'
                         + "".join(children) + "</rule>")
        renderer = (f'<renderer-v2 type="RuleRenderer" forceraster="0" referencescale="-1" symbollevels="0" '
                    f'enableorderby="1"><rules key="{{{uuid.uuid4()}}}">{"".join(rules)}</rules>'
                    f'<symbols>{"".join(symbols)}</symbols>{order}</renderer-v2>')
    else:
        cats = []
        for el in els:
            sym = make(el, str(len(symbols)), int(lod))
            if sym is None:
                continue
            cats.append(f'<category type="string" value={quoteattr(el.id)} label={quoteattr(el.name(lang))} '
                        f'render="true" symbol="{len(symbols)}" uuid="{{{uuid.uuid4()}}}"/>')
            symbols.append(sym)
        renderer = (f'<renderer-v2 type="categorizedSymbol" attr={quoteattr(field)} forceraster="0" '
                    f'referencescale="-1" symbollevels="0" enableorderby="1"><categories>{"".join(cats)}</categories>'
                    f'<symbols>{"".join(symbols)}</symbols><rotation/><sizescale/>{order}</renderer-v2>')
    gtype = {"point": 0, "line": 1, "polygon": 2}[geometry]
    doc = ("<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>\n"
           f'<qgis version="{QGIS_VERSION}" styleCategories="Symbology">{renderer}'
           "<blendMode>0</blendMode><featureBlendMode>0</featureBlendMode>"
           f"<layerGeometryType>{gtype}</layerGeometryType></qgis>\n")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")
    return path


def style_library(path, *, lod: int = 2, tile: float = 32.0, lang: str = "en", catalog: Catalog | None = None) -> Path:
    """Write a symbol library (.xml) for *Settings > Style Manager > Import*.

    Every element becomes a named symbol tagged with its group; the palette
    families become colour ramps.
    """
    catalog = catalog or load()
    syms = []
    for el in catalog:
        for geometry in el.geometry:
            kind = {"polygon": "fill", "line": "line", "point": "marker"}[geometry]
            suffix = "" if len(el.geometry) == 1 else f" ({geometry})"
            xml = symbol_for(el, f"ULG {el.name(lang)}{suffix}", lod=lod, tile=tile, kind=kind)
            if xml:
                syms.append(xml.replace("<symbol ", f'<symbol tags={quoteattr("ULG," + el.group)} ', 1))
    ramps = []
    for fam, steps in catalog.palette.families.items():
        numeric = [(int(k), v) for k, v in steps.items() if k.isdigit()]
        if len(numeric) < 3:
            continue
        numeric.sort()
        lo, hi = numeric[0][0], numeric[-1][0]
        stops = ":".join(f"{(k - lo) / (hi - lo):.3f};{_rgba(v)};rgb;ccw" for k, v in numeric[1:-1])
        ramps.append(f'<colorramp name={quoteattr("ULG " + fam)} type="gradient" tags="ULG"><Option type="Map">'
                     + _opt("color1", _rgba(numeric[0][1])) + _opt("color2", _rgba(numeric[-1][1]))
                     + _opt("direction", "ccw") + _opt("discrete", "0") + _opt("rampType", "gradient")
                     + _opt("spec", "rgb") + _opt("stops", stops) + "</Option></colorramp>")
    doc = ('<!DOCTYPE qgis_style>\n<qgis_style version="2">'
           f'<symbols>{"".join(syms)}</symbols><colorramps>{"".join(ramps)}</colorramps>'
           "<textformats/><labelsettings/><legendpatchshapes/><symbols3d/></qgis_style>\n")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")
    return path


def palette_gpl(path, *, catalog: Catalog | None = None, elements: bool = True) -> Path:
    """Write a GIMP palette (.gpl): importable as a colour scheme in QGIS, Inkscape, GIMP and Krita."""
    catalog = catalog or load()
    lines = ["GIMP Palette", f"Name: {catalog.palette.name}", "Columns: 9", "#"]
    for token, hexc in catalog.palette.flat().items():
        r, g, b = C.to_rgb255(hexc)
        lines.append(f"{r:3d} {g:3d} {b:3d}\t{token}")
    if elements:
        lines.append("# element fills")
        for el in catalog:
            if el.fill:
                r, g, b = C.to_rgb255(el.fill)
                lines.append(f"{r:3d} {g:3d} {b:3d}\t{el.id}")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def export_qgis(directory, *, lod: int | str = 2, lang: str = "en", handdrawn: bool | None = None,
                theme: str = "mellow", catalog: Catalog | None = None) -> list[Path]:
    """Everything QGIS needs, in one folder. ``theme`` picks the colour theme (see ``ulg.themes()``)."""
    catalog = catalog or load(theme)
    if handdrawn is None:
        handdrawn = float(catalog.theme.get("handdrawn", 1.0)) > 0
    d = Path(directory)
    out = [
        layer_style(d / "ulg_polygons.qml", "polygon", lod=lod, lang=lang, handdrawn=handdrawn, catalog=catalog),
        layer_style(d / "ulg_lines.qml", "line", lod=lod if lod != "auto" else 2, lang=lang, catalog=catalog),
        layer_style(d / "ulg_points.qml", "point", lod=lod if lod != "auto" else 2, lang=lang, catalog=catalog),
        style_library(d / "ulg_style_library.xml", lod=lod if lod != "auto" else 2, lang=lang, catalog=catalog),
        palette_gpl(d / "ulg_palette.gpl", catalog=catalog),
    ]
    return out

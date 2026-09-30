"""OGC Styled Layer Descriptor export (SLD 1.0.0) for GeoServer, QGIS Server, MapServer and INSPIRE view services.

SLD is the interoperable, standardised style encoding. It cannot express the
procedural hand-drawn outline, so the style degrades gracefully: flat fill,
a seamless pattern tile as ``GraphicFill`` and a plain outline.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from ..catalog import Catalog, Element, load
from .web import PX_PER_MM, pattern_files

HEADER = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" '
          'xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" '
          'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
          'xsi:schemaLocation="http://www.opengis.net/sld '
          'http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd">\n')


def _css(name: str, value) -> str:
    return f'<CssParameter name="{name}">{escape(str(value))}</CssParameter>'


def _filter(field: str, value: str) -> str:
    return (f"<ogc:Filter><ogc:PropertyIsEqualTo><ogc:PropertyName>{escape(field)}</ogc:PropertyName>"
            f"<ogc:Literal>{escape(value)}</ogc:Literal></ogc:PropertyIsEqualTo></ogc:Filter>")


def _stroke(color: str, width_mm: float, dash: tuple | None = None) -> str:
    parts = [_css("stroke", color), _css("stroke-width", f"{width_mm * PX_PER_MM:.2f}"),
             _css("stroke-linejoin", "round"), _css("stroke-linecap", "round")]
    if dash:
        parts.append(_css("stroke-dasharray", " ".join(f"{v * PX_PER_MM:.1f}" for v in dash)))
    return "<Stroke>" + "".join(parts) + "</Stroke>"


def _rule(el: Element, geometry: str, field: str, lang: str, pattern_dir: str | None, tile_px: float) -> str:
    sym = []
    if geometry == "polygon":
        if el.fill:
            sym.append(f'<PolygonSymbolizer><Fill>{_css("fill", el.fill)}</Fill></PolygonSymbolizer>')
        if el.textures and pattern_dir:
            sym.append('<PolygonSymbolizer><Fill><GraphicFill><Graphic><ExternalGraphic>'
                       f'<OnlineResource xlink:type="simple" xlink:href="{pattern_dir}/{el.id}.svg"/>'
                       f"<Format>image/svg+xml</Format></ExternalGraphic><Size>{tile_px:.0f}</Size>"
                       "</Graphic></GraphicFill></Fill></PolygonSymbolizer>")
        if el.outline:
            sym.append(f"<PolygonSymbolizer>{_stroke(el.outline, 0.2)}</PolygonSymbolizer>")
    elif geometry == "line":
        spec = el.line or {"color": el.outline or el.fill or "#505B61", "width": 0.3}
        if spec.get("casing"):
            sym.append(f'<LineSymbolizer>{_stroke(spec["casing"], spec.get("width", 0.3) + 0.36)}</LineSymbolizer>')
        color = spec.get("color") or (spec.get("marks") or {}).get("ink") or el.fill or "#505B61"
        sym.append(f'<LineSymbolizer>{_stroke(color, spec.get("width", 0.5), spec.get("dash"))}</LineSymbolizer>')
    else:
        spec = el.symbol or {}
        if spec.get("kind", "dot") != "dot" and pattern_dir:
            size = 14 if spec.get("kind") == "crown" else (3.2 * spec.get("r", 0.6) + 0.6) * PX_PER_MM
            sym.append("<PointSymbolizer><Graphic><ExternalGraphic>"
                       f'<OnlineResource xlink:type="simple" xlink:href="symbols/{el.id}.svg"/>'
                       f"<Format>image/svg+xml</Format></ExternalGraphic><Size>{size:.1f}</Size>"
                       "</Graphic></PointSymbolizer>")
        else:
            color = (spec.get("tones") or [spec.get("color") or el.fill or "#505B61"])[0]
            ink = spec.get("ink") or "#505B61"
            size = 14 if spec.get("kind") == "crown" else 2 * spec.get("r", 0.6) * PX_PER_MM
            sym.append("<PointSymbolizer><Graphic><Mark><WellKnownName>circle</WellKnownName>"
                       f'<Fill>{_css("fill", color)}</Fill>{_stroke(ink, 0.2)}</Mark>'
                       f"<Size>{size:.1f}</Size></Graphic></PointSymbolizer>")
    return (f"<Rule><Name>{escape(el.id)}</Name><Title>{escape(el.name(lang))}</Title>"
            f"{_filter(field, el.id)}{''.join(sym)}</Rule>")


def sld(path, geometry: str = "polygon", *, field: str = "element", lang: str = "en", elements=None,
        patterns: bool = True, lod: int = 2, layer_name: str = "ulg", catalog: Catalog | None = None) -> Path:
    """Write one SLD per geometry type. Pattern tiles go to ``patterns/`` next to the file."""
    catalog = catalog or load()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tile_mm = 32.0
    pattern_dir = None
    if patterns and geometry == "polygon":
        pattern_files(path.parent / "patterns", lod=lod, size=tile_mm, background=False, elements=elements,
                      catalog=catalog)
        pattern_dir = "patterns"
    if patterns and geometry == "point":
        from ..render.samples import symbol_svg

        sd = path.parent / "symbols"
        sd.mkdir(parents=True, exist_ok=True)
        for el in catalog:
            if "point" in el.geometry and (el.symbol or {}).get("kind", "dot") != "dot":
                (sd / f"{el.id}.svg").write_text(symbol_svg(el, 10.0, catalog=catalog), encoding="utf-8")
        pattern_dir = "symbols"
    picked = [catalog[e] for e in elements] if elements else list(catalog)
    els = sorted((el for el in picked if geometry in el.geometry), key=lambda e: e.z)
    rules = "\n".join(_rule(el, geometry, field, lang, pattern_dir, tile_mm * PX_PER_MM) for el in els)
    doc = (f"{HEADER}<NamedLayer><Name>{escape(layer_name)}</Name><UserStyle>"
           f"<Title>{escape(catalog.palette.name)} ({geometry})</Title><FeatureTypeStyle>\n{rules}\n"
           "</FeatureTypeStyle></UserStyle></NamedLayer></StyledLayerDescriptor>\n")
    path.write_text(doc, encoding="utf-8")
    return path


def export_sld(directory, **kw) -> list[Path]:
    d = Path(directory)
    return [sld(d / f"ulg_{g}s.sld", g, **kw) for g in ("polygon", "line", "point")]

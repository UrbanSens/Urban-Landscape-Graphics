"""Style sheets generated from the catalog.

``style_sheet()``   the one-page overview of the house style (A3 landscape).
``catalog_sheet()`` every element of the catalog with id and names, grouped.

Both are drawn with the library itself, so they are documentation and a visual
regression test at the same time. They carry a small UrbanSens mark (see :mod:`ulg.brand`);
``credit=False`` leaves it out.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from shapely.geometry import Point

from . import __version__
from .brand import draw_credit
from .catalog import Catalog, Element, load
from .datasets import demo_park, demo_park_places
from .legend import draw_legend, draw_swatch, used_elements
from .render.geom import Ctx
from .render.scene import Feature, Options, as_features, bounds_of, build, lod_for_scale
from .render.svg import Svg

HABITATS = ["lawn", "meadow", "wildflower_meadow", "shrubs", "woodland",
            "tree", "reed", "water", "bare_soil", "sand"]
SURFACES = ["paving_light", "paving_dark", "asphalt", "concrete", "gravel", "wood_deck"]
#: what the example map of the style sheet shows, in the order of its legend
EXAMPLE_LEGEND = ["lawn", "meadow", "wildflower_meadow", "orchard_meadow", "woodland_mixed", "reed", "water", "waterbound",
                  "plaza", "gravel", "wood_deck", "safety_surface", "vegetable_garden", "green_roof_extensive",
                  "building", "cycleway", "green_track", "tree", "tree_street"]

TEXT = {
    "en": {
        "title": "UrbanSens Ecological Vector Style",
        "subtitle": "Habitat types and surface materials, designed for GIS.",
        "intro": "A clean, consistent and scalable visual language to represent nature, surfaces and "
                 "biodiversity in a professional, architectural style, using simple vector patterns and symbols.",
        "principles": "Design principles",
        "p": ["Vector-based (polygonizable, GIS compatible)", "Subtle, natural colour palette",
              "Consistent iconography and line weights", "Minimal, non-photorealistic, architectural style",
              "Scalable detail (works at all zoom levels)"],
        "palette": "Colour palette",
        "pal": ["Vegetation & nature", "Surfaces & materials", "Water & special", "Analysis / highlight"],
        "habitats": "Habitat types", "surfaces": "Surfaces",
        "lod": "Detail levels", "lod_sub": "(same habitat type, different scales)",
        "lods": [("1.  Zoomed out (mass)", "Clear, recognisable shape and texture. Focus on overall character."),
                 ("2.  Medium detail (structure)", "More visible grass and flower elements. Still abstract, not botanical."),
                 ("3.  Zoomed in (elements)", "Individual grass blades and flowers become visible. Still stylised.")],
        "symbols": "Symbol library", "symbols_sub": "(excerpt)",
        "example": "Example: parcel with multiple habitats & surfaces", "legend": "Legend",
        "context": "Different habitats in context", "context_sub": "(example: urban park)",
        "ctx": ["Urban park: overview", "Meadow & tree detail", "Water body with reed"],
        "sizes": ["large", "medium", "small"],
        "catalog": "Element catalog", "generated": "generated from the catalog", "n_elements": "{n} elements",
    },
    "de": {
        "title": "UrbanSens Ökologischer Vektorstil",
        "subtitle": "Biotoptypen und Oberflächenmaterialien, entworfen für GIS.",
        "intro": "Eine klare, einheitliche und skalierbare Bildsprache für Natur, Oberflächen und Biodiversität "
                 "in einem professionellen, architektonischen Stil, mit einfachen Vektormustern und Symbolen.",
        "principles": "Gestaltungsprinzipien",
        "p": ["Vektorbasiert (flächenscharf, GIS-kompatibel)", "Zurückhaltende, natürliche Farbpalette",
              "Einheitliche Symbolik und Strichstärken", "Reduziert, nicht fotorealistisch, architektonisch",
              "Skalierbarer Detailgrad (für alle Maßstäbe)"],
        "palette": "Farbpalette",
        "pal": ["Vegetation & Natur", "Oberflächen & Materialien", "Wasser & Sonstiges", "Analyse / Hervorhebung"],
        "habitats": "Biotoptypen", "surfaces": "Oberflächen",
        "lod": "Detailstufen", "lod_sub": "(gleicher Biotoptyp, verschiedene Maßstäbe)",
        "lods": [("1.  Übersicht (Masse)", "Klare, erkennbare Form und Textur. Gesamtcharakter im Vordergrund."),
                 ("2.  Mittlerer Detailgrad (Struktur)", "Gräser und Blüten werden sichtbar. Abstrakt, nicht botanisch."),
                 ("3.  Nahansicht (Elemente)", "Einzelne Halme und Blüten erkennbar. Weiterhin stilisiert.")],
        "symbols": "Symbolbibliothek", "symbols_sub": "(Auszug)",
        "example": "Beispiel: Grundstück mit mehreren Biotoptypen & Oberflächen", "legend": "Legende",
        "context": "Biotoptypen im Zusammenhang", "context_sub": "(Beispiel: Stadtpark)",
        "ctx": ["Stadtpark: Übersicht", "Wiese & Bäume im Detail", "Gewässer mit Röhricht"],
        "sizes": ["groß", "mittel", "klein"],
        "catalog": "Elementkatalog", "generated": "aus dem Katalog erzeugt", "n_elements": "{n} Elemente",
    },
}


#: German headings of the catalog groups on the catalog sheet (English: the group id, for example "surface · paved")
GROUPS_DE = {
    "vegetation.grass": "Vegetation · Rasen und Wiesen", "vegetation.planting": "Vegetation · Pflanzungen",
    "vegetation.greenspace": "Vegetation · Grünflächen und Gärten", "vegetation.woody": "Vegetation · Gehölze",
    "vegetation.agri": "Vegetation · Landwirtschaft", "vegetation.wetland": "Vegetation · Feuchtgebiete",
    "vegetation.roof": "Vegetation · Dach- und Fassadenbegrünung", "blue_green": "Blau-grüne Infrastruktur",
    "trees": "Bäume", "water": "Gewässer", "ground": "Offener Boden",
    "surface.sealed": "Oberflächen · versiegelt", "surface.paved": "Oberflächen · gepflastert",
    "surface.permeable": "Oberflächen · durchlässig", "surface.loose": "Oberflächen · lose",
    "surface.sport": "Oberflächen · Sport", "surface.rail": "Oberflächen · Gleise",
    "surface.function": "Oberflächen · Verkehrsflächen", "landuse": "Flächennutzung", "built": "Gebäude und Bauwerke",
    "furniture": "Ausstattung", "ecology": "Ökologische Strukturen", "analysis": "Analyse",
    "boundary": "Grenzen", "relief": "Relief", "planning": "Planung", "other": "Sonstiges", "context": "Umgebung",
}


def group_title(group: str, lang: str = "en") -> str:
    """Heading of a catalog group on the catalog sheet."""
    if lang == "de" and group in GROUPS_DE:
        return GROUPS_DE[group]
    return group.replace(".", " · ").replace("_", " ")


class _Page:
    """Small typographic helpers on top of :class:`Svg`."""

    def __init__(self, svg: Svg, catalog: Catalog):
        self.svg, self.cat = svg, catalog
        p = catalog.palette
        self.ink9, self.ink7, self.ink5, self.ink4 = (p.resolve(f"ink.{k}") for k in (900, 700, 500, 400))
        self.rule = p.resolve("ink.200")

    def heading(self, x, y, text, sub: str | None = None):
        self.svg.text(x, y, text.upper(), size=3.0, fill=self.ink9, weight="600", spacing=0.32)
        if sub:
            self.svg.text(x + len(text) * 2.28 + 3, y, sub, size=2.5, fill=self.ink5)

    def label(self, x, y, text, size=2.9):
        self.svg.text(x, y, text, size=size, fill=self.ink7, weight="600")

    def para(self, x, y, text, width_chars=34, size=2.35, leading=3.6, max_lines=3, fill=None):
        for k, line in enumerate(_fit(text, width_chars, max_lines)):
            self.svg.text(x, y + k * leading, line, size=size, fill=fill or self.ink4)

    def hrule(self, x0, x1, y):
        self.svg.line(x0, y, x1, y, stroke=self.rule, width=0.2)


def _fit(text: str, width: int, max_lines: int) -> list[str]:
    """Wrap ``text``; when it is too long, keep whole clauses and close with an ellipsis."""
    lines = textwrap.wrap(text, width)
    if len(lines) <= max_lines:
        return lines
    cut = text
    while True:
        k, sep = max((cut.rfind(s, 0, len(cut) - 1), s) for s in (". ", "; ", ": ", ", ", " ("))
        if k <= 0:
            break
        head = cut[:k + 1] if sep == ". " else cut[:k].rstrip() + " …"
        if len(textwrap.wrap(head, width)) <= max_lines:
            return textwrap.wrap(head, width)
        cut = cut[:k]
    return textwrap.wrap(text, width, max_lines=max_lines, placeholder=" …")


def _park_features(catalog: Catalog) -> list[Feature]:
    return [Feature(f["geometry"], f["element"], f) for f in demo_park() if f["element"] in catalog]


def _map(svg: Svg, feats, catalog, x, y, w, h, *, center=None, scale=None, lod=None, frame=True):
    """Draw features into a w x h mm window; returns the scale denominator used."""
    minx, miny, maxx, maxy = bounds_of(feats)
    if scale is None:
        scale = max((maxx - minx) / w, (maxy - miny) / h) * 1000.0
    u = scale / 1000.0
    cx, cy = center or ((minx + maxx) / 2, (miny + maxy) / 2)
    extent = (cx - w * u / 2, cy - h * u / 2, cx + w * u / 2, cy + h * u / 2)
    ctx = Ctx(u=u, lod=lod if lod is not None else lod_for_scale(scale))
    svg.rect(x, y, w, h, fill=catalog.palette.resolve("paper.base"))
    svg.frame(build(feats, catalog, ctx, Options(), extent), extent, u, x=x, y=y, clip=True)
    if frame:
        svg.rect(x, y, w, h, fill="none", stroke=catalog.palette.resolve("ink.200"), width=0.2)
    return scale


def style_sheet(path=None, *, lang: str = "en", catalog: Catalog | None = None, credit: bool = True) -> Svg:
    """The one-page overview of the style (A3 landscape, 420 x 297 mm).

    ``credit`` adds the small UrbanSens mark in the lower right corner (``credit=False`` leaves it out).
    """
    catalog = catalog or load()
    T = TEXT.get(lang, TEXT["en"])
    pal = catalog.palette
    W, H, M = 420.0, 297.0, 12.0
    svg = Svg(W, H, background=pal.resolve("paper.base"), title=T["title"])
    pg = _Page(svg, catalog)

    # -- header ------------------------------------------------------------
    svg.text(M, 24, T["title"], size=10.2, fill=pg.ink9, weight="500")
    svg.text(M, 33, T["subtitle"], size=4.7, fill=pg.ink7)
    pg.para(M, 42.5, T["intro"], width_chars=92, size=3.35, leading=5.0, fill=pg.ink5)
    svg.line(196, 14, 196, 50, stroke=pg.rule)
    pg.heading(203, 17.5, T["principles"])
    for k, line in enumerate(T["p"]):
        svg.text(203, 25.2 + k * 5.6, str(k + 1), size=2.9, fill=pg.ink7)
        svg.text(210, 25.2 + k * 5.6, line, size=2.9, fill=pg.ink7)
    svg.line(292, 14, 292, 50, stroke=pg.rule)
    pg.heading(299, 17.5, T["palette"])
    rows = [
        (["leaf.700", "grass.500", "grass.300", "grass.200", "earth.500", "sand.400"], T["pal"][0]),
        (["lichen.300", "lichen.700", "lichen.500", "stone.300", "earth.300", "sand.300"], T["pal"][1]),
        (["water.500", "water.600", "water.700", "water.100", None, "signal.highlight"], T["pal"][2]),
    ]
    for r, (tokens, text) in enumerate(rows):
        for c, tok in enumerate(tokens):
            if tok:
                svg.circle(303.5 + c * 9.2, 27.5 + r * 10.2, 3.7, fill=pal.resolve(tok))
        svg.text(362, 28.4 + r * 10.2 - (2.4 if r == 2 else 0), text, size=2.8, fill=pg.ink7)
    svg.text(362, 28.4 + 2 * 10.2 + 3.2, T["pal"][3], size=2.8, fill=pg.ink7)
    pg.hrule(M, W - M, 54)

    # -- habitat types -----------------------------------------------------
    pg.heading(M, 62, T["habitats"])
    cell = 45.2
    for k, eid in enumerate(e for e in HABITATS if e in catalog):
        el = catalog[eid]
        r, c = divmod(k, 5)
        x, y = M + c * cell, 66 + r * 45.5
        draw_swatch(svg, el, x, y, 37, 25, lod=3 if "point" in el.geometry else 2, catalog=catalog,
                    shape="grove" if "point" in el.geometry else "blob")
        pg.label(x, y + 30, el.name(lang))
        pg.para(x, y + 34.4, el.description.get(lang, ""), width_chars=33)

    # -- surfaces ----------------------------------------------------------
    pg.heading(M, 162, T["surfaces"])
    cell = 37.7
    for k, eid in enumerate(e for e in SURFACES if e in catalog):
        el = catalog[eid]
        x, y = M + k * cell, 166
        draw_swatch(svg, el, x, y, 30, 19, lod=2, catalog=catalog, shape="blob" if eid == "gravel" else "rect")
        pg.label(x, y + 24, el.name(lang))
        pg.para(x, y + 28.4, el.description.get(lang, ""), width_chars=27)
    pg.hrule(M, 238, 207)

    # -- detail levels -----------------------------------------------------
    pg.heading(M, 215, T["lod"], T["lod_sub"])
    demo = catalog.get("wildflower_meadow") or next(iter(catalog))
    for k, (name, text) in enumerate(T["lods"]):
        x = M + k * 49.5
        draw_swatch(svg, demo, x, 219, 42, 27, lod=k + 1, catalog=catalog, shape="blob")
        pg.label(x, 252, name, size=2.75)
        pg.para(x, 256.4, text, width_chars=38)
    svg.line(163, 211, 163, H - M, stroke=pg.rule)

    # -- symbol library ----------------------------------------------------
    pg.heading(169, 215, T["symbols"], T["symbols_sub"])
    rows_sym = [("tree", [11.0, 8.0, 5.5]), ("shrub", [8.0, 6.0, 4.2])]
    for r, (eid, sizes) in enumerate(rows_sym):
        el = catalog.get(eid)
        if el is None:
            continue
        for c, dia in enumerate(sizes):
            x, y = 169 + c * 23.5, 219 + r * 19
            u = 0.4
            items = build([Feature(Point(0, 0), el.id, {"crown_diameter": dia * u})], catalog,
                          Ctx(u=u, lod=3), Options())
            svg.frame(items, (-11 * u, -6.5 * u, 11 * u, 6.5 * u), u, x=x, y=y, clip=False)
            svg.text(x + 11, y + 16.5, f"{el.name(lang).split(' (')[0]} ({T['sizes'][c]})", size=2.15,
                     fill=pg.ink5, anchor="middle")
    for c, eid in enumerate(e for e in ("lawn", "meadow", "wildflower_meadow", "reed") if e in catalog):
        x, y = 169 + c * 17.6, 259
        draw_swatch(svg, catalog[eid], x, y, 15, 15, lod=3, catalog=catalog, shape="rect")
        svg.text(x + 7.5, y + 19.4, catalog[eid].name(lang).split(" / ")[0], size=2.15, fill=pg.ink5, anchor="middle")

    # -- example map -------------------------------------------------------
    svg.line(244, 58, 244, H - M, stroke=pg.rule)
    pg.heading(250, 62, T["example"])
    feats = _park_features(catalog)
    places = demo_park_places()
    _map(svg, feats, catalog, 250, 66, 110, 134, center=places["park"], scale=2350)
    present = {e.id for e in used_elements(feats, catalog)}
    pg.heading(366, 70, T["legend"])
    draw_legend(svg, [e for e in EXAMPLE_LEGEND if e in present], 366, 74.5, lang=lang, row=6.6, size=2.35,
                swatch=(8.0, 4.8), catalog=catalog)

    # -- context -----------------------------------------------------------
    pg.hrule(250, W - M, 205)
    pg.heading(250, 213, T["context"], T["context_sub"])
    views = [(places["park"], 4400, 1), (places["meadow"], 480, 3), (places["reed"], 480, 3)]
    for k, (center, scale, lod) in enumerate(views):
        x = 250 + k * 53.5
        _map(svg, feats, catalog, x, 217, 50, 50, center=center, scale=scale, lod=lod)
        svg.text(x, 272.5, T["ctx"][k], size=2.5, fill=pg.ink7)

    note = f"ulg {__version__} · {T['generated']}"
    if credit:
        draw_credit(svg, W - M, H - 5.0, height=9.5, lang=lang, note=note, ink=pg.ink4)
    else:
        svg.text(W - M, H - 6.5, note, size=2.0, fill=pg.ink4, anchor="end")
    if path:
        svg.save(path)
    return svg


def catalog_sheet(path=None, *, lang: str = "en", catalog: Catalog | None = None, columns: int = 8,
                  lod: int = 2, groups: list[str] | None = None, title: str | None = None, credit: bool = True) -> Svg:
    """All elements with swatch, id and name, grouped: the visual index of the catalog.

    ``groups`` limits the sheet to groups starting with one of the given prefixes; ``credit`` adds the small
    UrbanSens mark below the last group (``credit=False`` leaves it out).
    """
    catalog = catalog or load()
    T = TEXT.get(lang, TEXT["en"])
    pal = catalog.palette
    M, cw, ch = 12.0, 36.0, 31.0
    groups = {g: els for g, els in catalog.groups().items()
              if not groups or any(g == p or g.startswith(p + ".") for p in groups)}
    n_rows = sum(-(-len(v) // columns) for v in groups.values())
    W = 2 * M + columns * cw
    H = 34 + n_rows * ch + len(groups) * 11 + M + (6.5 if credit else 0.0)
    svg = Svg(W, H, background=pal.resolve("paper.base"), title=T["catalog"])
    pg = _Page(svg, catalog)
    n = sum(len(v) for v in groups.values())
    svg.text(M, 21, title or f"{T['title']} · {T['catalog']}", size=7.0, fill=pg.ink9, weight="500")
    svg.text(W - M, 21, f"{T['n_elements'].format(n=n)} · ulg {__version__}", size=2.8, fill=pg.ink5, anchor="end")
    y = 32.0
    for group, els in groups.items():
        pg.hrule(M, W - M, y - 3)
        pg.heading(M, y + 3, group_title(group, lang))
        y += 8
        for k, el in enumerate(els):
            r, c = divmod(k, columns)
            x, yy = M + c * cw, y + r * ch
            draw_swatch(svg, el, x, yy, 30, 17, lod=lod, catalog=catalog)
            pg.label(x, yy + 21.2, el.name(lang)[:30], size=2.35)
            svg.text(x, yy + 24.6, el.id, size=2.0, fill=pg.ink4, font="'SF Mono', Menlo, Consolas, monospace")
            other = el.name("de" if lang == "en" else "en")
            if other != el.name(lang):
                svg.text(x, yy + 27.6, other[:30], size=2.0, fill=pg.ink4, italic=True)
        y += -(-len(els) // columns) * ch + 3
    if credit:
        pg.hrule(M, W - M, y - 3)
        draw_credit(svg, W - M, y + 12.5, height=9.5, lang=lang, note=f"ulg {__version__} · {T['generated']}", ink=pg.ink4)
    if path:
        svg.save(path)
    return svg

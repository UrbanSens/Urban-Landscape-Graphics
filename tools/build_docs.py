"""Regenerate every image of the documentation from the library itself.

    python tools/build_docs.py            # all images, in both languages
    python tools/build_docs.py hero lod    # selected images

Figures that contain text are drawn twice: ``name.png`` in English and ``name-de.png`` in German (the German
pages of the documentation use the latter). Figures without text exist once.

Needs Matplotlib and an SVG rasteriser (rsvg-convert, CairoSVG or Inkscape).
The QGIS screenshot additionally needs a local QGIS installation and is skipped
when none is found.
"""

from __future__ import annotations

import argparse
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np  # noqa: E402

import ulg  # noqa: E402
from ulg import colormath as C  # noqa: E402
from ulg.brand import STYLE_NAME, WEBSITE_SHORT, draw_credit, logo_png  # noqa: E402
from ulg.datasets import ORIGIN, WINDOW, demo_park, demo_park_places  # noqa: E402
from ulg.legend import draw_swatch  # noqa: E402
from ulg.render import Ctx, Options, Svg, build, rasterize  # noqa: E402
from ulg.render.samples import tile_items  # noqa: E402
from ulg.render.scene import Feature, bounds_of  # noqa: E402

IMG = ROOT / "docs" / "img"
INK, INK5, RULE = "#112D36", "#505B61", "#C6CACA"
PAPER = "#F5F5F1"
LANGS = ("en", "de")
FONT_FILE = ROOT / "tools" / "html" / "fonts" / "RethinkSans-VariableFont_wght.ttf"


def sfx(lang: str) -> str:
    """File name suffix of a figure with text: ``hero.png`` in English, ``hero-de.png`` in German."""
    return "" if lang == "en" else f"-{lang}"


def pick(lang: str, en, de):
    """The English or the German version of a text."""
    return en if lang == "en" else de


def ui_font(size: int, weight: int = 400):
    """Rethink Sans (the font of the documentation) at a pixel size, for figures drawn with PIL."""
    from PIL import ImageFont

    f = ImageFont.truetype(str(FONT_FILE), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:                                    # FreeType without variation support: regular weight
        pass
    return f


def out(name: str) -> Path:
    IMG.mkdir(parents=True, exist_ok=True)
    return IMG / name


def add_credit(page: Svg, mode: str = "plate") -> None:
    """The small UrbanSens mark in the lower right corner of an image of the documentation.

    ``plate``: for maps, the logo on a small paper plate inside the picture. ``band``: for diagrams, a strip of its own
    below the picture with the logo and the credit text. Sheets and legends made by the library carry theirs already.
    """
    if mode == "band":
        h = max(4.2, min(8.5, 0.032 * page.width, 0.10 * page.height))
        page.line(0, page.height, page.width, page.height, stroke=RULE, width=0.2)
        page.height += h + 3.6
        draw_credit(page, page.width - 3.0, page.height - 1.8, height=h, text=h >= 6.0, ink=INK5)
    else:
        h = max(5.0, min(12.0, 0.04 * page.width, 0.08 * page.height))
        draw_credit(page, page.width - 2.4, page.height - 2.4, height=h, text=False, plate=PAPER)


def raster_credit(path: Path, mode: str = "plate", paper: str = PAPER) -> None:
    """The same mark on a finished PNG: images made with PIL, Matplotlib or QGIS."""
    from io import BytesIO

    from PIL import Image, ImageDraw

    im = Image.open(path).convert("RGB")
    w, h = im.size
    logo = Image.open(BytesIO(logo_png())).convert("RGBA")
    lh = round(max(34, min(0.032 * w, 0.10 * h) if mode == "band" else min(0.036 * w, 0.08 * h)))
    logo = logo.resize((round(logo.width * lh / logo.height), lh), Image.LANCZOS)
    pad = round(lh * 0.22)
    colour = tuple(int(paper[i:i + 2], 16) for i in (1, 3, 5))
    if mode == "band":
        strip = lh + 2 * pad
        canvas = Image.new("RGB", (w, h + strip), colour)
        canvas.paste(im, (0, 0))
        d = ImageDraw.Draw(canvas)
        d.line([(0, h), (w, h)], fill=(198, 202, 202), width=max(1, round(lh / 40)))
        canvas.paste(logo, (w - logo.width - 2 * pad, h + pad), logo)
        size = max(12, round(lh * 0.27))
        x = w - logo.width - 2 * pad - round(lh * 0.3)
        y0 = h + pad + lh // 2 - size
        for k, (text, weight) in enumerate(((f"{STYLE_NAME} · ulg {ulg.__version__}", 400), (WEBSITE_SHORT, 650))):
            f = ui_font(size, weight)
            d.text((x - d.textlength(text, font=f), y0 + k * round(size * 1.42)), text, font=f, fill=(80, 91, 97))
        canvas.save(path, optimize=True)
        return
    plate = Image.new("RGBA", (logo.width + 2 * pad, lh + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle((0, 0, plate.width - 1, plate.height - 1), radius=round(lh * 0.2),
                                            fill=colour + (237,), outline=(198, 202, 202, 255), width=max(1, round(lh / 40)))
    plate.alpha_composite(logo, (pad, pad))
    base = im.convert("RGBA")
    base.alpha_composite(plate, (w - plate.width - round(lh * 0.25), h - plate.height - round(lh * 0.25)))
    base.convert("RGB").save(path, optimize=True)


def png(svg: Svg, name: str, dpi: int = 150, keep_svg: bool = False, credit: str | None = None) -> Path:
    if credit:
        add_credit(svg, credit)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "page.svg"
        svg.save(src)
        target = out(name)
        rasterize(src, target, dpi=dpi)
        if keep_svg:
            shutil.copy(src, target.with_suffix(".svg"))
    print("  ", target.relative_to(ROOT))
    return target


def park() -> list[Feature]:
    return [Feature(f["geometry"], f["element"], f) for f in demo_park()]


PLACES = demo_park_places()
CENTRE = (ORIGIN[0] + WINDOW[0] / 2, ORIGIN[1] + WINDOW[1] / 2)      # middle of the demo quarter's window


def at(place: str, dx: float = 0.0, dy: float = 0.0) -> tuple[float, float]:
    """A named spot of the demo quarter, moved by (dx, dy) metres."""
    x, y = PLACES[place]
    return x + dx, y + dy


def draw_map(svg: Svg, feats, x, y, w, h, *, scale, center=None, lod=None, catalog=None, frame=True,
             handdrawn=None):
    catalog = catalog or ulg.load()
    u = scale / 1000.0
    minx, miny, maxx, maxy = bounds_of(feats)
    cx, cy = center or ((minx + maxx) / 2, (miny + maxy) / 2)
    extent = (cx - w * u / 2, cy - h * u / 2, cx + w * u / 2, cy + h * u / 2)
    opts = Options(handdrawn=catalog.theme.get("handdrawn", 1.0) if handdrawn is None else handdrawn)
    ctx = Ctx(u=u, lod=lod if lod is not None else ulg.lod_for_scale(scale))
    bg = catalog.palette.resolve(catalog.theme.get("background", "paper.base"))
    svg.rect(x, y, w, h, fill=bg)
    svg.frame(build(feats, catalog, ctx, opts, extent), extent, u, x=x, y=y, clip=True)
    if frame:
        svg.rect(x, y, w, h, fill="none", stroke=RULE, width=0.2)


# --------------------------------------------------------------------------- images

def _paper() -> str:
    return ulg.load().palette.resolve("paper.warm")


def scale_bar(page: Svg, x: float, y: float, scale: float, metres: float, parts: int = 4, unit_label: str = "m",
              size: float = 2.6, halo: bool = True) -> float:
    """A scale bar of ``metres`` (in ``parts`` alternating segments) with its lower left corner at (x, y) mm."""
    u = scale / 1000.0
    total = metres / u
    seg = total / parts
    h = size * 0.55
    for k in range(parts):
        page.rect(x + k * seg, y - h, seg, h, fill=INK if k % 2 == 0 else "#FDFDFB", stroke=INK, width=0.18)
    for k in range(parts + 1):
        v = metres * k / parts
        page.text(x + k * seg, y - h - size * 0.4, f"{v:g}" + (f" {unit_label}" if k == parts else ""), size=size,
                  fill=INK, anchor="middle" if k < parts else "start", halo=None)
    return total


def north_arrow(page: Svg, x: float, y: float, size: float = 11.0) -> None:
    """A slim north arrow (the demo quarter is drawn with north up) with its foot at (x, y) mm."""
    w = size * 0.2
    page.polygon([(x, y - size), (x + w, y), (x, y - size * 0.22), (x - w, y)], fill=INK, stroke=INK, width=0.15)
    page.polygon([(x, y - size), (x + w, y), (x, y - size * 0.22)], fill="#FDFDFB", stroke=INK, width=0.15)
    page.text(x, y - size - 1.6, "N", size=size * 0.34, fill=INK, anchor="middle", weight="600")


def plate(page: Svg, x, y, w, h) -> None:
    page.rect(x, y, w, h, fill=_paper(), stroke=RULE, width=0.2, rx=1.6, opacity=0.93)


#: (place, English, German, dx, dy in metres, rotation in degrees): the labels of the hero map
HERO_LABELS = [
    ("pond", "Pond", "Teich", 3, 0, 0),
    ("pavilion", "Pavilion", "Pavillon", -6, -13, 0),
    ("meadow", "Wildflower meadow", "Blumenwiese", 0, 0, 0),
    ("orchard", "Orchard", "Streuobstwiese", 0, -19, 0),
    ("garden", "Community garden", "Gemeinschaftsgarten", 2, -20, 0),
    ("playground", "Playground", "Spielplatz", 1, -14, 0),
    ("court", "Clay court", "Tennenplatz", 0, -14, 0),
    ("plaza", "Plaza", "Platz", 0, -25, 0),
    ("woodland", "Woodland belt", "Gehölzstreifen", -30, -12, 13),
    ("allee", "Avenue of trees", "Allee", -6, 8, 13),
    ("avenue", "Avenue with green tram track", "Straße mit Gleisrasen", 0, 0, 13),
    ("canal", "Canal", "Kanal", 0, 0, 13),
    ("field", "Sports field", "Sportplatz", 0, 0, 13),
]


def hero_labels(page: Svg, extent, u: float, x0: float = 0.0, y0: float = 0.0, size: float = 4.3,
                lang: str = "en") -> None:
    minx, miny, maxx, maxy = extent
    paper = ulg.load().palette.resolve("paper.base")
    for place, en, de, dx, dy, rot in HERO_LABELS:
        first, second = (en, de) if lang == "en" else (de, en)
        X, Y = at(place, dx, dy)
        px, py = x0 + (X - minx) / u, y0 + (maxy - Y) / u
        page.text(px, py, first, size=size, fill=INK, anchor="middle", weight="600", halo=paper, rotate=rot, spacing=0.05)
        # the other language sits underneath, along the same baseline direction
        ox, oy = size * 0.95 * math.sin(math.radians(rot)), size * 0.95 * math.cos(math.radians(rot))
        page.text(px + ox, py + oy, second, size=size * 0.72, fill=INK5, anchor="middle", italic=True, halo=paper,
                  rotate=rot)


def img_hero(lang: str = "en"):
    feats = park()
    scale = 1500
    W, H = WINDOW[0] / (scale / 1000), WINDOW[1] / (scale / 1000)
    page = Svg(W, H, background="#F5F5F1",
               title=pick(lang, "Angerpark, the demo quarter of ulg, 1:1500", "Angerpark, das Demoquartier von ulg, 1:1500"))
    draw_map(page, feats, 0, 0, W, H, scale=scale, center=CENTRE, frame=False)
    u = scale / 1000.0
    extent = (CENTRE[0] - W * u / 2, CENTRE[1] - H * u / 2, CENTRE[0] + W * u / 2, CENTRE[1] + H * u / 2)
    hero_labels(page, extent, u, lang=lang)
    plate(page, 5, H - 28, 62, 23)
    north_arrow(page, 13, H - 9.5, size=12.0)
    scale_bar(page, 24, H - 10, scale, 50, parts=2)
    page.text(24, H - 20.6, "1 : 1500", size=3.0, fill=INK, weight="600")
    png(page, f"hero{sfx(lang)}.png", dpi=130, credit="plate")
    if lang != "en":                                     # the close-up has no text: drawn once
        return
    # the same quarter close up: pavilion, boardwalk and reed belt at 1:500
    page = Svg(160, 100, background="#F5F5F1", title="Pavilion, boardwalk and reed belt at 1:500")
    draw_map(page, feats, 0, 0, 160, 100, scale=500, center=at("pavilion", 27, 2), frame=False)
    scale_bar(page, 6, 95, 500, 20, parts=4, size=2.5)
    png(page, "hero-detail.png", dpi=170, credit="plate")


#: titles of the themes in the German figures (the theme files carry the English ones)
THEME_TITLES_DE = {"mellow": "UrbanSens Mellow (Hausstil)", "bfn": "BfN Landschaftsplanung", "mono": "Mono (Zeichnung)"}


def img_conventions(lang: str = "en"):
    feats = park()
    scale = 2200
    u = scale / 1000
    w, h = 176.0 / u, 160.0 / u                     # 176 x 160 m: pond, plaza, street, avenue with tram, blocks
    center = (ORIGIN[0] + 338.0, ORIGIN[1] + 188.0)
    cols, gap = 4, 7.0
    names = [("mellow", pick(lang, "2026 · UrbanSens house style", "2026 · UrbanSens Hausstil")),
             ("planzv", "1965 / 1990 · PlanZV, Bauleitplan"), ("alkis", "ALKIS · Liegenschaftskarte"),
             ("basemap", pick(lang, "basemap.de · web basemap", "basemap.de · Web-Basiskarte")),
             ("bfn", pick(lang, "2017 · BfN landscape planning", "2017 · BfN Landschaftsplanung")),
             ("osm", pick(lang, "since 2004 · OpenStreetMap Carto", "seit 2004 · OpenStreetMap Carto")),
             ("mono", pick(lang, "ISO 11091 · black-and-white drawing", "ISO 11091 · Schwarz-Weiß-Zeichnung"))]
    W = cols * (w + gap) + gap
    H = 2 * (h + 13) + gap
    page = Svg(W, H, background="#FFFFFF")
    for k, (name, caption) in enumerate(names):
        cat = ulg.load(name)
        x0 = gap + (k % cols) * (w + gap)
        y0 = gap + (k // cols) * (h + 13)
        draw_map(page, feats, x0, y0, w, h, scale=scale, center=center, catalog=cat)
        title = THEME_TITLES_DE.get(name) if lang == "de" else None
        page.text(x0, y0 + h + 5.0, title or cat.theme.get("title", name), size=3.1, fill=INK, weight="600")
        page.text(x0, y0 + h + 9.2, caption, size=2.5, fill=INK5)
    x0, y0 = gap + 3 * (w + gap), gap + (h + 13)
    lines = pick(lang, ["One quarter, seven conventions.", "", "The same data drawn with", "ulg.render_svg(gdf, theme=...):",
                        "the house style and six official", "or familiar conventions, each", "with the colour values of its",
                        "published source."],
                 ["Ein Quartier, sieben Konventionen.", "", "Dieselben Daten, gezeichnet mit", "ulg.render_svg(gdf, theme=...):",
                  "dem Hausstil und sechs amtlichen", "oder vertrauten Konventionen, jede", "mit den Farbwerten ihrer",
                  "veröffentlichten Quelle."])
    for i, t in enumerate(lines):
        page.text(x0 + 2, y0 + 10 + i * 5.2, t, size=3.0 if i == 0 else 2.7, fill=INK if i == 0 else INK5,
                  weight="600" if i == 0 else "normal")
    png(page, f"conventions{sfx(lang)}.png", dpi=120, credit="plate")


def img_sheets(lang: str = "en"):
    s = sfx(lang)
    ulg.style_sheet(out(f"style-sheet{s}.svg"), lang=lang)
    rasterize(out(f"style-sheet{s}.svg"), out(f"style-sheet{s}.png"), dpi=110)
    print(f"   docs/img/style-sheet{s}.png")
    if lang != "en":                                     # the vector file of the style sheet is kept in English only
        out(f"style-sheet{s}.svg").unlink()
    parts = {
        "vegetation": (["vegetation", "blue_green"], ("Vegetation and blue-green infrastructure",
                                                      "Vegetation und blau-grüne Infrastruktur")),
        "trees-water-ground": (["trees", "water", "ground"], ("Trees, water and open ground",
                                                              "Bäume, Gewässer und offener Boden")),
        "surfaces": (["surface"], ("Surfaces and pavings", "Oberflächen und Beläge")),
        "built-landuse": (["landuse", "built", "furniture", "ecology"],
                          ("Land use, buildings, furniture, ecological structures",
                           "Flächennutzung, Gebäude, Ausstattung, ökologische Strukturen")),
        "lines-overlays": (["boundary", "relief", "planning", "analysis", "context", "other"],
                           ("Lines, planning and analysis overlays, context",
                            "Linien, Planungs- und Analyse-Overlays, Kontext")),
    }
    for key, (groups, titles) in parts.items():
        svg = ulg.catalog_sheet(groups=groups, title=pick(lang, *titles), lang=lang)
        png(svg, f"catalog-{key}{s}.png", dpi=110)
    ulg.catalog_sheet(out(f"catalog-sheet{s}.svg"), lang=lang)       # the whole catalog: linked from the pages as SVG
    if lang == "en":
        rasterize(out("catalog-sheet.svg"), out("catalog-sheet.png"), dpi=110)


def img_palette(lang: str = "en"):
    cat = ulg.load()
    fams = cat.palette.families
    rows = [f for f in fams]
    W, rh = 264.0, 11.5                                    # the longest rows (stone, signal) have ten steps
    page = Svg(W, 16 + len(rows) * rh, background="#F5F5F1")
    page.text(10, 10, pick(lang, "Palette · primitive colour tokens (family.step)",
                            "Palette · Basisfarben als Tokens (family.step)"), size=4, fill=INK, weight="600")
    for r, fam in enumerate(rows):
        y = 16 + r * rh
        page.text(10, y + 6.2, fam, size=2.8, fill=INK, weight="600")
        for c, (step, hexc) in enumerate(fams[fam].items()):
            x = 38 + c * 21.5
            page.rect(x, y, 20, 6.5, fill=hexc, stroke=C.darken(hexc, 0.08), width=0.15, rx=0.6)
            page.text(x, y + 9.3, f"{step}  {hexc}", size=1.9, fill=INK5)
    png(page, f"palette{sfx(lang)}.png", dpi=140, credit="band")


def img_lod(lang: str = "en"):
    feats = park()
    center = at("reed", -4, 2)
    page = Svg(3 * 64 + 4 * 5, 70, background="#FFFFFF")
    for k, (scale, text) in enumerate([(5000, pick(lang, "1 : 5000 · LOD 1: mass", "1 : 5000 · LOD 1: Masse")),
                                       (1500, pick(lang, "1 : 1500 · LOD 2: structure", "1 : 1500 · LOD 2: Struktur")),
                                       (400, pick(lang, "1 : 400 · LOD 3: elements", "1 : 400 · LOD 3: Elemente"))]):
        x = 5 + k * 69
        draw_map(page, feats, x, 5, 64, 52, scale=scale, center=center)
        page.text(x, 63, text, size=2.8, fill=INK, weight="600")
    png(page, f"lod{sfx(lang)}.png", dpi=170, credit="plate")


def img_tree_symbols(lang: str = "en"):
    from shapely.geometry import Point

    cat = ulg.load()
    specs = [("tree", {"crown_diameter": 9, "stammumfang": 190}, pick(lang, "existing, stem to scale", "Bestand, Stamm maßstäblich")),
             ("tree_conifer", {"crown_diameter": 7}, pick(lang, "conifer", "gezackter Kronenumriss")),
             ("tree_fruit", {"crown_diameter": 7}, pick(lang, "fruit tree", "Blütenpunkte in der Krone")),
             ("tree_street", {"crown_diameter": 8}, pick(lang, "street tree with pit", "mit Baumscheibe")),
             ("tree_veteran", {"crown_diameter": 12}, pick(lang, "veteran / habitat tree", "Höhlen, Totholz")),
             ("tree_planned", {"crown_diameter": 7}, pick(lang, "to plant (ISO 11091, PlanZV)", "ISO 11091, PlanZV")),
             ("tree_protected", {"crown_diameter": 8}, pick(lang, "to keep (chain-line frame)", "strichpunktiertes Quadrat")),
             ("tree_remove", {"crown_diameter": 8}, pick(lang, "to fell (ISO 7518, yellow)", "ISO 7518, gelb, durchkreuzt"))]
    scale, cell = 400, 34.0
    u = scale / 1000
    page = Svg(len(specs) * cell + 8, 52, background="#F5F5F1")
    for k, (eid, props, text) in enumerate(specs):
        x0 = 4 + k * cell
        cx = cy = 0.0
        feats = [Feature(Point(cx, cy), eid, props)]
        if eid == "tree_protected":
            zone = ulg.root_protection_zone([(Point(cx, cy), eid, props)])[0]
            feats.insert(0, Feature(zone, "root_protection_zone"))
        items = build(feats, cat, Ctx(u=u, lod=3), Options())
        h = 0.5 * cell * u
        page.frame(items, (-h, -h, h, h), u, x=x0, y=4, clip=False)
        page.text(x0 + cell / 2, cell + 9, cat[eid].name(lang), size=2.5, fill=INK, weight="600", anchor="middle")
        page.text(x0 + cell / 2, cell + 13, text, size=2.1, fill=INK5, anchor="middle")
    png(page, f"tree-symbols{sfx(lang)}.png", dpi=170, credit="band")


def img_textures(lang: str = "en"):
    cat = ulg.load()
    ids = ["lawn", "meadow", "wildflower_meadow", "dry_grassland", "meadow_wet", "ruderal", "perennials", "shrubs",
           "woodland", "woodland_coniferous", "reed", "water", "bare_soil", "sand", "gravel", "waterbound",
           "paving_light", "concrete_pavers", "natural_stone_paving", "clinker", "grass_pavers", "gravel_turf",
           "wood_deck", "green_roof_extensive"]
    size, cols = 24.0, 8
    page = Svg(cols * (size + 4) + 4, math.ceil(len(ids) / cols) * (size + 10) + 4, background="#F5F5F1")
    for k, eid in enumerate(ids):
        el = cat[eid]
        x0 = 4 + (k % cols) * (size + 4)
        y0 = 4 + (k // cols) * (size + 10)
        page.rect(x0, y0, size, size, fill=el.fill)
        items = tile_items(el, size / 2, 2)
        for i in range(2):
            for j in range(2):
                page.frame(items, (0, 0, size / 2, size / 2), 1.0, x=x0 + i * size / 2, y=y0 + j * size / 2)
        name = el.name(lang)
        page.text(x0, y0 + size + 4.2, name, size=2.3 * min(1.0, 22.0 / max(len(name), 1)), fill=INK)
    png(page, f"textures{sfx(lang)}.png", dpi=150, credit="band")


def img_legend(lang: str = "en"):
    ids = ["lawn", "meadow", "wildflower_meadow", "shrubs", "woodland", "tree", "tree_planned", "reed", "water",
           "gravel", "paving_light", "wood_deck", "building", "site_boundary"]
    svg = ulg.legend_svg(ids, lang=lang, title=pick(lang, "Legend", "Legende"), columns=2, background="#F5F5F1", credit=True)
    png(svg, f"legend{sfx(lang)}.png", dpi=200)


def img_analysis(lang: str = "en"):
    import geopandas as gpd
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    gdf = ulg.datasets.demo_park_gdf()
    site = gdf[gdf.layer.isin(["landcover", "trees"])]
    res = ulg.indicators(site)
    cat = ulg.load()
    polys = site[site.geom_type.isin(["Polygon", "MultiPolygon"])].copy()
    polys["runoff_cm"] = [cat[e].attributes.get("runoff_cm") for e in polys.element]
    minx, miny, maxx, maxy = site.total_bounds
    pad = 16.0
    extent = (minx - pad, miny - pad, maxx + pad, maxy + pad)
    fig = plt.figure(figsize=(9.4, 5.6), dpi=150)
    fig.patch.set_facecolor(cat.palette.resolve("paper.base"))
    aspect = (extent[3] - extent[1]) / (extent[2] - extent[0])
    aw = 0.58
    ah = min(0.92, aw * 9.4 * aspect / 5.6)                      # keep the map's proportions inside its column
    ax = fig.add_axes([0.025, (1 - ah) / 2, aw, ah])
    ulg.plot(gdf, ax=ax, theme="mono", lod=1, extent=extent)
    for artist in ax.get_children():                             # nothing may spill over the frame
        artist.set_clip_path(ax.patch)
    cmap = ListedColormap(ulg.ramp("cool", 6))
    polys.plot(column="runoff_cm", ax=ax, cmap=cmap, alpha=0.78, vmin=0, vmax=1, zorder=50,
               missing_kwds={"color": "none"})
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor(RULE)
        spine.set_linewidth(0.8)
    tx = fig.add_axes([0.64, 0.05, 0.34, 0.9])
    tx.set_axis_off()
    tx.text(0, 0.97, pick(lang, "Coefficients travel with the style", "Kennwerte sind Teil des Stils"), fontsize=12,
            color=INK, weight="bold", va="top")
    tx.text(0, 0.9, pick(lang, "Mean runoff coefficient Cm per surface\n(DIN 1986-100:2016-12), drawn over the\nblack-and-white theme; blank = no coefficient.",
                         "Mittlerer Abflussbeiwert Cm je Fläche\n(DIN 1986-100:2016-12), über das\nSchwarz-Weiß-Theme gezeichnet; leer = kein Beiwert."),
            fontsize=8.5, color=INK5, va="top")
    num = (lambda v, nd=2: f"{v:.{nd}f}") if lang == "en" else (lambda v, nd=2: f"{v:.{nd}f}".replace(".", ","))
    area = f"{res['plot_area_m2']:,.0f}" if lang == "en" else f"{res['plot_area_m2']:,.0f}".replace(",", ".")
    rows = [(pick(lang, "Plot area", "Grundstücksfläche"), f"{area} m²"),
            (pick(lang, "Sealed", "Versiegelt"), f"{res['sealed_share']:.0%}"),
            (pick(lang, "Partly sealed", "Teilversiegelt"), f"{res['partly_share']:.0%}"),
            (pick(lang, "Built", "Bebaut"), f"{res['built_share']:.0%}"),
            (pick(lang, "Biotope area factor (Berlin)", "Biotopflächenfaktor (Berlin)"), num(res["bff"])),
            (pick(lang, "Runoff coefficient Cm", "Abflussbeiwert Cm"), num(res["runoff_cm"]) if res["runoff_cm"] is not None else "–"),
            (pick(lang, "Mean albedo", "Mittlere Albedo"), num(res["albedo"]) if res["albedo"] is not None else "–"),
            (pick(lang, "Urban green (NRR)", "Urbanes Grün (NRR)"), f"{res['nrr_green_share']:.0%}"),
            (pick(lang, "Tree canopy", "Baumkronenanteil"), f"{res['canopy_share']:.0%}")]
    for i, (k, v) in enumerate(rows):
        y = 0.72 - i * 0.058
        tx.text(0, y, k, fontsize=9.5, color=INK)
        tx.text(0.98, y, v, fontsize=9.5, color=INK, ha="right", weight="bold")
    for i, col in enumerate(ulg.ramp("cool", 6)):
        tx.add_patch(plt.Rectangle((i * 0.16, 0.12), 0.15, 0.04, color=col, transform=tx.transAxes))
    tx.text(0, 0.07, "Cm 0", fontsize=8, color=INK5)
    tx.text(0.96, 0.07, "1", fontsize=8, color=INK5, ha="right")
    tx.text(0, 0.0, "ulg.indicators(gdf)", fontsize=9, color=INK, family="monospace")
    name = f"analysis{sfx(lang)}.png"
    fig.savefig(out(name), dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    raster_credit(out(name), "band", paper=cat.palette.resolve("paper.base"))
    print(f"   docs/img/{name}")


def img_cvd(lang: str = "en"):
    from PIL import Image

    ids = ["lawn", "meadow", "wildflower_meadow", "shrubs", "woodland", "reed", "water", "bare_soil", "sand",
           "gravel", "paving_light", "asphalt", "clinker", "wood_deck"]
    cat = ulg.load()
    sw, gap = 22.0, 3.0
    page = Svg(len(ids) * (sw + gap) + gap, 20, background="#FFFFFF")
    for k, eid in enumerate(ids):
        draw_swatch(page, cat[eid], gap + k * (sw + gap), 2, sw, 14, lod=2, shape="rect", catalog=cat)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "strip.svg"
        page.save(src)
        rasterize(src, Path(tmp) / "strip.png", dpi=150)
        base = np.asarray(Image.open(Path(tmp) / "strip.png").convert("RGB")).astype(np.float64) / 255.0

    def lin(v):
        return np.where(v <= 0.04045, v / 12.92, ((v + 0.055) / 1.055) ** 2.4)

    def gam(v):
        v = np.clip(v, 0, 1)
        return np.where(v <= 0.0031308, 12.92 * v, 1.055 * v ** (1 / 2.4) - 0.055)

    names = pick(lang, {"normal": "normal vision", "protanopia": "protanopia (red-blind)",
                        "deuteranopia": "deuteranopia (green-blind)", "tritanopia": "tritanopia (blue-blind)"},
                 {"normal": "normales Sehen", "protanopia": "Protanopie (Rotblindheit)",
                  "deuteranopia": "Deuteranopie (Grünblindheit)", "tritanopia": "Tritanopie (Blaublindheit)"})
    rows = [(names["normal"], base)]
    for kind in C.CVD_KINDS:
        m = np.array(C._CVD[kind])
        rows.append((names[kind], gam(lin(base) @ m.T)))
    h, w, _ = base.shape
    label_h = 38
    canvas = np.ones((len(rows) * (h + label_h), w, 3))
    for i, (_, img) in enumerate(rows):
        canvas[i * (h + label_h) + label_h: (i + 1) * (h + label_h)] = img
    im = Image.fromarray((canvas * 255).astype(np.uint8))
    from PIL import ImageDraw

    d = ImageDraw.Draw(im)
    label_font = ui_font(24, 560)
    for i, (name, _) in enumerate(rows):
        d.text((12, i * (h + label_h) + 6), name, font=label_font, fill=(17, 45, 54))
    target = out(f"cvd{sfx(lang)}.png")
    im.save(target)
    raster_credit(target, "band", paper="#FFFFFF")
    print(f"   docs/img/{target.name}")


def img_timeline(lang: str = "en"):
    import textwrap

    events = pick(lang, [
        (1789, "Englischer Garten", "Sckell's landscape park in Munich, plans drawn and washed by hand"),
        (1808, "Bavarian cadastral survey", "1:5000 (1:1250 in parts of Franconia), printed from Solnhofen limestone"),
        (1965, "Planzeichenverordnung", "first federal plan symbols for land-use plans; restated 1990"),
        (1969, "Design with Nature", "Ian McHarg's map overlays anticipate the layers of GIS"),
        (1994, "ISO 11091", "landscape drawing conventions: existing thin, proposed thick"),
        (2004, "OpenStreetMap", "open, tag-based data about every surface"),
        (2017, "BfN plan symbols", "federal catalogue for landscape plans with a pastel series"),
        (2024, "Nature Restoration Regulation", "urban green space and tree canopy become EU targets"),
        (2026, "ulg", "one catalog: hand-drawn look, standard codes, every platform"),
    ], [
        (1789, "Englischer Garten", "Sckells Landschaftspark in München, Pläne von Hand gezeichnet und laviert"),
        (1808, "Bayerische Katastervermessung", "1:5000 (in Teilen Frankens 1:1250), gedruckt vom Solnhofener Kalkstein"),
        (1965, "Planzeichenverordnung", "erste bundeseinheitliche Planzeichen für Flächennutzungspläne; 1990 neu gefasst"),
        (1969, "Design with Nature", "Ian McHargs Kartenüberlagerungen nehmen die Ebenen des GIS vorweg"),
        (1994, "ISO 11091", "Zeichenregeln für Landschaftspläne: Bestand dünn, Planung dick"),
        (2004, "OpenStreetMap", "offene, tagbasierte Daten über jede Oberfläche"),
        (2017, "BfN-Planzeichen", "Bundeskatalog für Landschaftspläne mit einer Pastellserie"),
        (2024, "Wiederherstellungsverordnung", "urbane Grünflächen und Baumkronenanteil werden EU-Ziele"),
        (2026, "ulg", "ein Katalog: handgezeichnete Anmutung, Normcodes, jede Plattform"),
    ])
    n = len(events)
    tall = max(len(textwrap.wrap(text, 30)) for k, (_, _, text) in enumerate(events) if k % 2 == 0)
    extra = 3.4 * max(0, tall - 3)                       # room for a fourth line above the axis
    W, H = 270.0, 70.0 + extra
    page = Svg(W, H, background="#F5F5F1")
    x0, x1, y = 16.0, W - 16.0, 34.0 + extra
    page.line(x0 - 6, y, x1 + 6, y, stroke=INK5, width=0.35)
    step = (x1 - x0) / (n - 1)
    for k, (year, title, text) in enumerate(events):
        x = x0 + k * step
        up = k % 2 == 0
        last = k == n - 1
        page.circle(x, y, 1.4, fill=ulg.color("signal.highlight") if last else ulg.color("grass.500"),
                    stroke=INK, width=0.2)
        page.line(x, y - 1.4 if up else y + 1.4, x, y - 7 if up else y + 7, stroke=RULE, width=0.25)
        lines = textwrap.wrap(text, 30)
        if up:
            top = y - 9 - 3.4 * len(lines) - 7.5
        else:
            top = y + 13
        page.text(x, top, str(year), size=3.2, fill=INK, weight="600", anchor="middle")
        page.text(x, top + 4.0, title, size=2.5, fill=INK, anchor="middle", weight="600" if last else "normal")
        for i, line in enumerate(lines):
            page.text(x, top + 7.6 + i * 3.1, line, size=2.05, fill=INK5, anchor="middle")
    page.text(W - 4, H - 3, pick(lang, "not to scale", "nicht maßstäblich"), size=1.8, fill=INK5, anchor="end")
    png(page, f"timeline{sfx(lang)}.png", dpi=170, credit="band")


def img_qgis():
    candidates = ["/Applications/QGIS.app/Contents/MacOS/bin/python3", shutil.which("qgis_process") and "python3"]
    qpy = next((c for c in candidates if c and os.path.exists(c)), None)
    if not qpy:
        print("   QGIS not found, skipping qgis.png")
        return
    import geopandas as gpd

    from ulg.export.qgis import export_qgis

    osm = gpd.read_file(ROOT / "examples" / "data" / "osm_sample.geojson").to_crs(25832)
    osm["element"] = ulg.classify(osm, "osm")
    osm = osm[[c for c in ("element", "highway", "width", "lanes", "diameter_crown", "geometry") if c in osm.columns]]
    window = (ORIGIN[0], ORIGIN[1], ORIGIN[0] + WINDOW[0], ORIGIN[1] + WINDOW[1])
    for gdf, name, args in ((ulg.datasets.demo_park_gdf(), "qgis.png", ["1600", *map(str, window)]),
                            (osm, "qgis-osm.png", ["700"])):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            export_qgis(tmp, lod="auto")
            for gt, layer in (("Polygon", "polygons"), ("LineString", "lines"), ("Point", "points")):
                gdf[gdf.geom_type.isin([gt, "Multi" + gt])].to_file(tmp / f"park_{layer}.gpkg", driver="GPKG")
            script = ROOT / "tools" / "qgis_render.py"
            env = dict(os.environ, QT_QPA_PLATFORM="offscreen", QGIS_PREFIX_PATH="/Applications/QGIS.app/Contents/MacOS",
                       PYTHONPATH="/Applications/QGIS.app/Contents/Resources/python")
            env.pop("PYTHONHOME", None)
            r = subprocess.run([qpy, str(script), str(tmp), str(out(name)), *args], env=env,
                               capture_output=True, text=True)
            print("  ", r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-400:])
            if out(name).exists():
                raster_credit(out(name), "plate")


def img_osm():
    import geopandas as gpd

    osm = gpd.read_file(ROOT / "examples" / "data" / "osm_sample.geojson").to_crs(25832)
    osm["element"] = ulg.classify(osm, "osm")
    minx, miny, maxx, maxy = osm.total_bounds
    pad = 26.0
    svg = ulg.render_svg(osm, scale=900, extent=(minx + pad, miny + pad, maxx - pad, maxy - pad))
    png(svg, "osm-block.png", dpi=150, credit="plate")



#: The documentation's banners are black-and-white drawings with three accents taken from the UrbanSens logo
#: (src/ulg/data/brand/urbansens-logo.png): water in its blue, paths and decks in its peach, sport and cycling
#: surfaces in its salmon. The drawing is the ``mono`` theme in soft grey on the paper colour of the pages, so
#: the pictures fade into the page instead of sitting on it like photographs.
UB_BLUE, UB_BLUE_INK, UB_PEACH, UB_SALMON = "#A9C5D5", "#6E9BB8", "#E7C0B1", "#E89484"
BW_INK, BW_PAPER = "#707070", "#F5F5F1"
ACCENTS = {
    UB_BLUE: ["water", "watercourse"],
    UB_PEACH: ["waterbound", "wood_deck", "sand", "gravel", "plaza", "path", "path_unpaved"],
    UB_SALMON: ["clay_court", "cycleway", "safety_surface", "synthetic_track"],
}


def accent_catalog():
    """The ``mono`` theme as a soft grey drawing on paper, with the three accent colours of the UrbanSens logo."""
    import json
    from importlib import resources

    from ulg import catalog as C

    th = json.loads(resources.files("ulg").joinpath("data", "themes", "mono.json").read_text(encoding="utf-8"))
    th.update(ink=BW_INK, paper=BW_PAPER, background=BW_PAPER)
    th["default"] = {"fill": BW_PAPER, "outline": BW_INK}
    th["groups"] = {"built": {"fill": "#E6E6E2", "outline": BW_INK}, "context": {"fill": BW_PAPER, "outline": "#AEAEAE"}}
    th["elements"] = {"asphalt": {"fill": "#E0E0DC"}, "building_context": {"fill": "#EEEEEA", "outline": "#AEAEAE"}}
    for colour, ids in ACCENTS.items():
        for eid in ids:
            th["elements"][eid] = {**th["elements"].get(eid, {}), "fill": colour}
    raw = {eid: r for _, data in C._read_dir("elements") for eid, r in data.get("elements", {}).items()}
    elements = C.apply_theme(raw, th)
    for eid in ("water", "watercourse"):                 # the waves in a deeper blue of the same family
        for t in elements[eid].get("textures", []):
            t["ink"] = UB_BLUE_INK
    meta = {k: v for k, v in th.items() if k not in ("default", "groups", "elements")}
    meta["name"] = "docs-banner"
    return C.Catalog(C.Palette(C._read_json("palette.json")), elements, dict(C._read_dir("crosswalks")),
                     C._read_json("settings.json"), meta)


#: banners of the HTML documentation: key -> crop of the demo quarter (size 320 x 90 mm, saved as a 2400 px JPEG)
BANNER_W, BANNER_H = 320.0, 90.0
BANNERS = {
    "home": dict(place=("pond", 4, -2), scale=640),
    "origins": dict(place=("orchard", 46, -4), scale=520),
    "style": dict(place=("meadow", -8, 4), scale=380),
    "python": dict(place=("avenue", -60, 12), scale=820),
    "gis": dict(place=("canal", 10, 14), scale=720),
    "agents": dict(place=("blocks", -40, 0), scale=820),
    "extending": dict(place=("playground", 26, 2), scale=520),
    "research": dict(place=("blocks", 70, -6), scale=900),
    "project": dict(place=("plaza", -20, 4), scale=560),
    "standards": dict(place=("blocks", -80, -40), scale=700),
}


def img_banners(only: list[str] | None = None):
    from PIL import Image

    feats = park()
    cat = accent_catalog()
    folder = IMG / "banners"
    folder.mkdir(parents=True, exist_ok=True)
    dpi = 2400 / (BANNER_W / 25.4)

    def save(page: Svg, key: str) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "b.svg"
            page.save(src)
            rasterize(src, Path(tmp) / "b.png", dpi=dpi)
            Image.open(Path(tmp) / "b.png").convert("RGB").save(folder / f"{key}.jpg", quality=82, optimize=True,
                                                                 progressive=True)
        print("  ", (folder / f"{key}.jpg").relative_to(ROOT))

    for key, spec in BANNERS.items():
        if only and key not in only:
            continue
        page = Svg(BANNER_W, BANNER_H, background=BW_PAPER)
        draw_map(page, feats, 0, 0, BANNER_W, BANNER_H, scale=spec["scale"], center=at(*spec["place"]), catalog=cat,
                 frame=False)
        save(page, key)

    if not only or "catalog" in only:                     # a wall of textures
        ids = ["lawn", "meadow", "wildflower_meadow", "shrubs", "woodland", "reed", "water", "sand",
               "gravel", "paving_light", "wood_deck", "green_roof_extensive", "orchard_meadow", "vegetable_garden",
               "dry_grassland", "waterbound"]
        page = Svg(BANNER_W, BANNER_H, background=BW_PAPER)
        cw, ch = BANNER_W / 8, BANNER_H / 2
        for k, eid in enumerate(ids):
            draw_swatch(page, cat[eid], (k % 8) * cw, (k // 8) * ch, cw, ch, lod=2, shape="rect", catalog=cat)
        save(page, "catalog")


def img_social(lang: str = "en"):
    """The 1280 x 640 preview of the GitHub repository (Settings > Social preview): logo, tagline, a drawing of the park.

    ``social-preview.png`` is the German one (the default language of the repository), ``social-preview-en.png`` the English one.
    """
    from PIL import Image, ImageDraw

    W, H, PX = 1280, 640, 1280
    feats = park()
    cat = accent_catalog()
    page = Svg(320, 160, background=BW_PAPER)
    draw_map(page, feats, 0, 0, 320, 160, scale=520, center=at("pond", -36, -4), catalog=cat, frame=False)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "s.svg"
        page.save(src)
        rasterize(src, Path(tmp) / "s.png", dpi=PX / (320 / 25.4))
        drawing = Image.open(Path(tmp) / "s.png").convert("RGB").resize((W, H), Image.LANCZOS)
    paper = tuple(int(BW_PAPER[i:i + 2], 16) for i in (1, 3, 5))
    canvas = Image.new("RGB", (W, H), paper)
    column = [int(255 * (t * t * (3 - 2 * t))) for t in (min(1.0, max(0.0, (x / W - 0.40) / 0.38)) for x in range(W))]
    ramp = Image.new("L", (W, 1))                        # paper covers the left 40 %, the drawing shows fully from 78 %
    ramp.putdata(column)
    canvas.paste(drawing, (0, 0), ramp.resize((W, H)))
    d = ImageDraw.Draw(canvas)
    font = ui_font

    lockup = Image.open(IMG / "logo" / "ulg-logo.png").convert("RGBA")
    lw = 600
    lockup = lockup.resize((lw, round(lockup.height * lw / lockup.width)), Image.LANCZOS)
    canvas.paste(lockup, (70, 92), lockup)
    x, y = 76, 92 + lockup.height + 34
    for i, colour in enumerate(("#6E9BB8", "#A9C5D5", "#E7C0B1", "#E48878", "#C65F60", "#A35459", "#6F8C9D")):   # logo stripes
        d.rectangle((x + i * 18, y, x + i * 18 + 17, y + 6), fill=colour)
    three = lang == "de"                                 # the German tagline needs a third line: tighter spacing, smaller logo below
    y += 26 if three else 34
    head = pick(lang, ["The UrbanSens Ecological Vector Style", "as a library."],
                ["Der UrbanSens Ecological Vector Style", "als Bibliothek."])
    body = pick(lang, ["Colours, textures and symbols for urban landscape maps,", "tied to German and European standards."],
                ["Farben, Texturen und Symbole für Karten der", "Stadtlandschaft, nach deutschen und europäischen", "Standards."])
    d.text((x, y), head[0], font=font(33, 700), fill="#1F2426")
    d.text((x, y + 42), head[1], font=font(33, 700), fill="#1F2426")
    for i, line in enumerate(body):
        d.text((x, y + (90 if three else 100) + i * (32 if three else 34)), line, font=font(23, 500), fill="#596164")
    ub = Image.open(ROOT / "src" / "ulg" / "data" / "brand" / "urbansens-logo.png").convert("RGBA")
    ub_h = 78 if three else 96
    ub = ub.resize((round(ub.width * ub_h / ub.height), ub_h), Image.LANCZOS)
    canvas.paste(ub, (70, H - ub.height - 38), ub)
    d.text((70 + ub.width + 18, H - 38 - ub.height // 2 - 14), WEBSITE_SHORT, font=font(26, 650), fill="#596164")
    target = IMG / ("social-preview.png" if lang == "de" else "social-preview-en.png")
    canvas.save(target, optimize=True)
    print("  ", target.relative_to(ROOT))


#: name -> (function, has text): figures with text are drawn once per language, the others once
IMAGES = {"hero": (img_hero, True), "osm": (img_osm, False), "conventions": (img_conventions, True),
          "sheets": (img_sheets, True), "palette": (img_palette, True), "lod": (img_lod, True),
          "trees": (img_tree_symbols, True), "textures": (img_textures, True), "legend": (img_legend, True),
          "analysis": (img_analysis, True), "cvd": (img_cvd, True), "timeline": (img_timeline, True),
          "qgis": (img_qgis, False), "banners": (img_banners, False), "social": (img_social, True)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("names", nargs="*", help=f"any of: {', '.join(IMAGES)}")
    args = ap.parse_args()
    unknown = [n for n in args.names if n not in IMAGES]
    if unknown:
        ap.error(f"unknown image(s): {', '.join(unknown)}")
    for name in args.names or IMAGES:
        print(name)
        draw, has_text = IMAGES[name]
        if has_text:
            for lang in LANGS:
                draw(lang)
        else:
            draw()


if __name__ == "__main__":
    main()

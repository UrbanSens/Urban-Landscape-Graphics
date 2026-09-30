"""Draw the ulg logo with the library itself.

    python tools/build_logo.py            # writes docs/img/logo/*.svg and *.png, the favicon set

The mark spells "ulg" with three things of a landscape plan, each drawn with a real catalog element: a pond in the
shape of a *u* (``water``), a tree-lined path as the *l* (``waterbound`` and ``tree``), and a tree crown with a stream
as the tail of the *g* (``tree`` and ``watercourse``). The hand-drawn outline and the texture marks come from the
renderer, so the logo is also a specimen of the style: exact geometry underneath, an imperfect drawing on top.

The wordmark is set in Rethink Sans (SIL Open Font License) and converted to outlines, so the SVG files need no font.
The font is looked up in ``~/Library/Fonts`` and in ``tools/html/fonts``.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np  # noqa: E402
from shapely.geometry import LineString, Point, Polygon, box  # noqa: E402

import ulg  # noqa: E402
from ulg.render import Ctx, Options, Svg, build, rasterize  # noqa: E402
from ulg.render.scene import Feature  # noqa: E402

OUT = ROOT / "docs" / "img" / "logo"
FONT_DIRS = [ROOT / "tools" / "html" / "fonts", Path.home() / "Library" / "Fonts"]
FONT_FILE = "RethinkSans-VariableFont_wght.ttf"

SCALE = 300.0                  # the mark is drawn at 1:300: the marks and outlines then have the weight of a plan
LOD = 2
OPTIONS = Options(outline_width=0.4, outline_wobble=0.17, outline_contrast=2.0)

STROKE = 3.4                   # stroke of the u and the l (m)
UX0, UX1 = 1.9, 8.9            # centre lines of the u's stems
LX = 14.6                      # the allée
GX, GY, GD = 24.4, 5.2, 10.4   # the crown of the g: centre and diameter


# --------------------------------------------------------------------------- geometry of the mark

def _arc(cx, cy, r, a0, a1, n=32):
    t = np.radians(np.linspace(a0, a1, n))
    return [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in t]


def mark_geometry() -> dict:
    """The exact geometry of the mark in metres: polygons, tree points and their names."""
    half = STROKE / 2
    cx, r = (UX0 + UX1) / 2, (UX1 - UX0) / 2
    u_line = LineString([(UX0, 10.6), (UX0, 4.6)] + _arc(cx, 4.6, r, 180, 360) + [(UX1, 4.6), (UX1, 10.6)])
    u = u_line.buffer(half, cap_style="flat", join_style="round").buffer(-0.45).buffer(0.45)
    l_bar = box(LX - half, -0.9, LX + half, 16.2).buffer(-0.5).buffer(0.5)
    stem = GX + GD / 2 + 0.55                                    # the stem stands right of the bowl, like a single-storey g
    tail_line = LineString([(stem, 6.6), (stem, 0.6)] + _arc(stem - 3.0, 0.6, 3.0, 0, -95, 16) + [(GX + 0.4, -3.55)])
    tail = tail_line.buffer(1.35, cap_style="round", join_style="round")
    return {"u": u, "l": l_bar, "tail": tail,
            "allee": [(LX, 1.4, 4.6), (LX, 7.4, 4.8), (LX, 13.4, 4.6)], "crown": (GX, GY, GD)}


def mark_features(geo: dict | None = None) -> list[Feature]:
    geo = geo or mark_geometry()
    feats = [Feature(geo["u"], "water"), Feature(geo["l"], "waterbound"), Feature(geo["tail"], "watercourse")]
    for x, y, d in geo["allee"]:
        feats.append(Feature(Point(x, y), "tree", {"crown_diameter": d}))
    x, y, d = geo["crown"]
    feats.append(Feature(Point(x, y), "tree", {"crown_diameter": d}))
    return feats


def mark_bounds(geo: dict | None = None, pad: float = 0.6) -> tuple[float, float, float, float]:
    """Bounds of the drawn mark in metres, with room for the hand-drawn outline."""
    geo = geo or mark_geometry()
    shapes = [geo["u"], geo["l"], geo["tail"]] + [Point(x, y).buffer(d / 2) for x, y, d in geo["allee"] + [geo["crown"]]]
    minx = min(s.bounds[0] for s in shapes)
    miny = min(s.bounds[1] for s in shapes)
    maxx = max(s.bounds[2] for s in shapes)
    maxy = max(s.bounds[3] for s in shapes)
    return minx - pad, miny - pad, maxx + pad, maxy + pad


SIMPLE = Options(outline_width=0.55, outline_wobble=0.22, outline_contrast=2.0, textures=False)


def draw_mark(page: Svg, x: float, y: float, height: float, feats=None, bounds=None, simple: bool = False) -> float:
    """Draw the mark with its top left corner at (x, y) mm, ``height`` mm tall; returns its width in mm.

    ``simple`` leaves out the texture marks and thickens the outline: the version for sizes below about 40 px.
    """
    feats = feats or mark_features()
    bounds = bounds or mark_bounds()
    u = SCALE / 1000.0
    catalog = ulg.load()
    items = build(feats, catalog, Ctx(u=u, lod=1 if simple else LOD), SIMPLE if simple else OPTIONS, bounds)
    w_mm, h_mm = (bounds[2] - bounds[0]) / u, (bounds[3] - bounds[1]) / u
    k = height / h_mm
    page.open_group(attrs={"transform": f"translate({x:.3f} {y:.3f}) scale({k:.5f})"})
    page.frame(items, bounds, u, x=0, y=0, clip=False)
    page.close_group()
    return w_mm * k


# --------------------------------------------------------------------------- outlined text

def _font(weight: int):
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont

    path = next((d / FONT_FILE for d in FONT_DIRS if (d / FONT_FILE).exists()), None)
    if path is None:
        raise SystemExit(f"{FONT_FILE} not found in {', '.join(map(str, FONT_DIRS))}")
    return instantiateVariableFont(TTFont(path), {"wght": weight}, inplace=False)


_FONTS: dict[int, object] = {}


def text_path(text: str, x: float, y: float, size: float, weight: int = 600, tracking: float = 0.0,
              kerning: dict | None = None) -> tuple[str, float]:
    """The outlines of ``text`` as an SVG path (mm, baseline at y). Returns (d, advance width).

    ``size`` is the em size in mm, ``tracking`` in em; ``kerning`` maps letter pairs to em adjustments.
    """
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen

    if weight not in _FONTS:
        _FONTS[weight] = _font(weight)
    font = _FONTS[weight]
    glyphs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
    s = size / font["head"].unitsPerEm
    kerning = kerning or {}
    parts, cursor, prev = [], 0.0, None
    for ch in text:
        name = cmap[ord(ch)]
        if prev is not None:
            cursor += kerning.get(prev + ch, 0.0) * size
        pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.3f}".rstrip("0").rstrip("."))
        glyphs[name].draw(TransformPen(pen, (s, 0, 0, -s, x + cursor, y)))
        parts.append(pen.getCommands())
        cursor += hmtx[name][0] * s + tracking * size
        prev = ch
    return " ".join(p for p in parts if p), cursor - tracking * size


def text_width(text: str, size: float, weight: int = 600, tracking: float = 0.0, kerning: dict | None = None) -> float:
    return text_path(text, 0, 0, size, weight, tracking, kerning)[1]


def put_text(page: Svg, text: str, x: float, y: float, size: float, fill: str, weight: int = 600, tracking: float = 0.0,
             kerning: dict | None = None, anchor: str = "start") -> float:
    width = text_width(text, size, weight, tracking, kerning)
    x0 = x - width / 2 if anchor == "middle" else x - width if anchor == "end" else x
    d, _ = text_path(text, x0, y, size, weight, tracking, kerning)
    page.raw(f'<path d="{d}" fill="{fill}"/>')
    return width


# --------------------------------------------------------------------------- lockups

KERN = {"La": -0.02, "Gr": -0.01, "rb": 0.0, "Ur": -0.005, "ap": 0.0}


def colours(dark: bool = False) -> dict:
    p = ulg.load().palette
    return {"ink": p.resolve("paper.warm") if dark else p.resolve("ink.900"),
            "soft": p.resolve("ink.200") if dark else p.resolve("ink.500"),
            "bg": p.resolve("ink.900") if dark else None,
            "accent": p.resolve("signal.highlight")}


def horizontal(dark: bool = False, background: bool = False) -> Svg:
    """Mark on the left, the name in two lines and the tagline on the right."""
    c = colours(dark)
    H = 34.0
    pad = 4.0
    mark_h = H
    name_size = 9.6
    tag_size = 2.95
    probe = Svg(10, 10)
    mark_w = draw_mark(probe, 0, 0, mark_h)
    x_text = pad + mark_w + 8.5
    w1 = text_width("Urban Landscape", name_size, 620, -0.004, KERN)
    w2 = text_width("Graphics", name_size, 620, -0.004, KERN)
    tag = "UrbanSens · Ecological Vector Style"
    wt = text_width(tag.upper(), tag_size, 560, 0.16)
    W = x_text + max(w1, w2, wt) + pad
    Hh = mark_h + 2 * pad
    page = Svg(W, Hh, background=(c["bg"] if dark and background else None), title="Urban Landscape Graphics (ulg)")
    draw_mark(page, pad, pad, mark_h)
    base = pad + 12.6
    put_text(page, "Urban Landscape", x_text, base, name_size, c["ink"], 620, -0.004, KERN)
    put_text(page, "Graphics", x_text, base + name_size * 1.1, name_size, c["ink"], 620, -0.004, KERN)
    put_text(page, tag.upper(), x_text + 0.2, Hh - pad - 1.0, tag_size, c["soft"], 560, 0.16)
    return page


def stacked(dark: bool = False, background: bool = False) -> Svg:
    """Mark above the name, centred."""
    c = colours(dark)
    pad = 6.0
    mark_h = 36.0
    name_size = 8.6
    tag_size = 2.75
    probe = Svg(10, 10)
    mark_w = draw_mark(probe, 0, 0, mark_h)
    name = "Urban Landscape Graphics"
    tag = "UrbanSens · Ecological Vector Style"
    wn = text_width(name, name_size, 620, -0.004, KERN)
    wt = text_width(tag.upper(), tag_size, 560, 0.16)
    W = max(mark_w, wn, wt) + 2 * pad
    H = pad + mark_h + 9.5 + name_size * 0.72 + 5.0 + tag_size + pad
    page = Svg(W, H, background=(c["bg"] if dark and background else None), title="Urban Landscape Graphics (ulg)")
    draw_mark(page, (W - mark_w) / 2, pad, mark_h)
    y = pad + mark_h + 9.5 + name_size * 0.72
    put_text(page, name, W / 2, y, name_size, c["ink"], 620, -0.004, KERN, anchor="middle")
    put_text(page, tag.upper(), W / 2, y + 5.0 + tag_size * 0.72, tag_size, c["soft"], 560, 0.16, anchor="middle")
    return page


def mark_only(dark: bool = False, background: bool = False, pad: float = 3.0, height: float = 40.0,
              simple: bool = False) -> Svg:
    c = colours(dark)
    probe = Svg(10, 10)
    w = draw_mark(probe, 0, 0, height, simple=simple)
    page = Svg(w + 2 * pad, height + 2 * pad, background=(c["bg"] if dark and background else None),
               title="Urban Landscape Graphics (ulg)")
    draw_mark(page, pad, pad, height, simple=simple)
    return page


# --------------------------------------------------------------------------- favicon

def favicon(size: float = 64.0, radius: float = 13.0, tile: str | None = None, border: bool = True) -> Svg:
    """The g on a rounded tile: crown and stream, the part of the mark that stays readable at 16 px.

    ``radius=0, border=False`` gives the full-bleed square that iOS and Android round off themselves.
    """
    p = ulg.load().palette
    geo = mark_geometry()
    feats = [f for f in mark_features(geo) if f.element in ("watercourse",) or (f.element == "tree" and f.props.get("crown_diameter") == GD)]
    minx, miny, maxx, maxy = (GX - GD / 2 - 0.5, -5.2, GX + GD / 2 + 3.0, GY + GD / 2 + 0.5)
    page = Svg(size, size, title="ulg")
    page.rect(0, 0, size, size, fill=tile or p.resolve("paper.warm"), rx=radius,
              stroke=p.resolve("ink.200") if border else None, width=size * 0.012)
    u = SCALE / 1000.0
    items = build(feats, ulg.load(), Ctx(u=u, lod=1), OPTIONS, (minx, miny, maxx, maxy))
    w_mm, h_mm = (maxx - minx) / u, (maxy - miny) / u
    k = size * 0.74 / max(w_mm, h_mm)
    ox, oy = (size - w_mm * k) / 2, (size - h_mm * k) / 2
    page.open_group(attrs={"transform": f"translate({ox:.3f} {oy:.3f}) scale({k:.5f})"})
    page.frame(items, (minx, miny, maxx, maxy), u, x=0, y=0, clip=False)
    page.close_group()
    return page


# --------------------------------------------------------------------------- construction figure

def construction() -> Svg:
    """Left: the exact geometry with its vertices. Right: what the renderer makes of it."""
    p = ulg.load().palette
    ink, rule = p.resolve("ink.700"), p.resolve("ink.200")
    geo = mark_geometry()
    bounds = mark_bounds()
    u = SCALE / 1000.0
    w_mm, h_mm = (bounds[2] - bounds[0]) / u, (bounds[3] - bounds[1]) / u
    k = 1.0
    gap, pad, head = 14.0, 8.0, 12.0
    W = 2 * (w_mm * k) + gap + 2 * pad
    H = h_mm * k + 2 * pad + head + 8.0
    page = Svg(W, H, background=p.resolve("paper.base"), title="How the ulg mark is made")

    def to_page(x, y, ox):
        return ox + (x - bounds[0]) / u * k, pad + head + (bounds[3] - y) / u * k

    ox = pad
    page.text(ox, pad + 4.0, "1 · exact geometry", size=3.4, fill=ink, weight="600")
    page.text(ox, pad + 8.0, "polygons and points, in metres", size=2.7, fill=p.resolve("ink.500"))
    shapes = [("u", geo["u"]), ("l", geo["l"]), ("tail", geo["tail"])]
    for _, poly in shapes:
        simple = poly.simplify(0.3, preserve_topology=True)
        pts = [to_page(x, y, ox) for x, y in simple.exterior.coords]
        page.polygon(pts, fill="#FDFDFB", stroke=ink, width=0.22)
        for px, py in pts[:-1]:
            page.circle(px, py, 0.62, fill=p.resolve("paper.white"), stroke=ink, width=0.2)
    for x, y, d in geo["allee"] + [geo["crown"]]:
        cx, cy = to_page(x, y, ox)
        r = d / 2 / u * k
        page.circle(cx, cy, r, fill="#FDFDFB", stroke=ink, width=0.22)
        page.circle(cx, cy, 0.9, fill=ink)
        page.line(cx, cy, cx + r, cy, stroke=ink, width=0.16, dash=(0.8, 0.8))
    ox2 = pad + w_mm * k + gap
    page.text(ox2, pad + 4.0, "2 · drawn by the renderer", size=3.4, fill=ink, weight="600")
    page.text(ox2, pad + 8.0, "textures, outline and crowns from the catalog", size=2.7, fill=p.resolve("ink.500"))
    draw_mark(page, ox2, pad + head, h_mm * k)
    return page


# --------------------------------------------------------------------------- output

def png(svg: Svg, name: str, dpi: int | None = None, width: int | None = None) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / name
    svg.save(target.with_suffix(".svg"))
    if width:
        dpi = round(width / (svg.width / 25.4))
    rasterize(target.with_suffix(".svg"), target, dpi=dpi or 300)
    print("  ", target.relative_to(ROOT))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    png(mark_only(), "ulg-mark.png", width=1400)
    mark_only(pad=0.6, height=24.0, simple=True).save(OUT / "ulg-mark-small.svg")     # for headers and lists
    print("   docs/img/logo/ulg-mark-small.svg")
    png(mark_only(dark=True, background=True), "ulg-mark-dark.png", width=1400)
    png(horizontal(), "ulg-logo.png", width=2000)
    png(horizontal(dark=True, background=True), "ulg-logo-dark.png", width=2000)
    png(horizontal(dark=True, background=False), "ulg-logo-on-dark.png", width=2000)     # transparent, for dark pages
    png(stacked(), "ulg-logo-stacked.png", width=1400)
    png(construction(), "ulg-mark-construction.png", width=1800)
    fav = favicon()
    png(fav, "ulg-favicon.png", width=512)
    from PIL import Image

    base = Image.open(OUT / "ulg-favicon.png").convert("RGBA")
    for px, name in ((32, "favicon-32.png"), (16, "favicon-16.png")):
        base.resize((px, px), Image.LANCZOS).save(OUT / name)
    square = favicon(radius=0.0, border=False)                      # the home-screen icons are full-bleed squares
    square.save(OUT / "icon-square.svg")
    rasterize(OUT / "icon-square.svg", OUT / "icon-square.png", dpi=round(512 / (square.width / 25.4)))
    full = Image.open(OUT / "icon-square.png").convert("RGB")
    for px, name in ((180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")):
        full.resize((px, px), Image.LANCZOS).save(OUT / name)
    (OUT / "icon-square.png").unlink()
    base.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("   docs/img/logo/favicon.ico")


def brand_badge() -> None:
    """The UrbanSens logo on a rounded paper-white plate, for dark pages (the README on GitHub in dark mode).

    The logo itself (docs/img/brand/urbansens-logo.png) is supplied by UrbanSens and stays as it is; its dark wordmark
    needs a light ground, so on dark pages it is shown on this plate.
    """
    from PIL import Image, ImageDraw

    src = ROOT / "docs" / "img" / "brand" / "urbansens-logo.png"
    if not src.exists():
        print("   (docs/img/brand/urbansens-logo.png not found, no badge)")
        return
    logo = Image.open(src).convert("RGBA")
    pad, k = 26, 4                                             # drawn 4x larger, then reduced: smooth corners
    w, h = logo.width + 2 * pad, logo.height + 2 * pad
    plate = Image.new("RGBA", (w * k, h * k), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=22 * k, fill=(253, 253, 251, 255))
    plate = plate.resize((w, h), Image.LANCZOS)
    plate.alpha_composite(logo, (pad, pad))
    target = ROOT / "docs" / "img" / "brand" / "urbansens-logo-on-white.png"
    plate.save(target, optimize=True)
    print("  ", target.relative_to(ROOT))


if __name__ == "__main__":
    main()
    brand_badge()

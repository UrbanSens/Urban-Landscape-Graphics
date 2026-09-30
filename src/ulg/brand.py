"""The UrbanSens credit: the website, the logo and the small mark the library's own sheets carry.

``ulg`` is MIT-licensed. What UrbanSens asks for in return is a mention: say where the style comes from.

    import ulg

    ulg.credit_line()            # 'Style: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'
    ulg.credit_line("de")        # 'Kartenstil: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'
    ulg.style_sheet("s.svg")     # carries the small UrbanSens mark in a corner; credit=False leaves it out

Only the sheets and legends the library draws itself (``style_sheet``, ``catalog_sheet``, ``legend_svg(credit=True)``)
use the mark. Your maps are never stamped: ``render_svg``, ``plot`` and the exported styles add nothing.

The logo file is UrbanSens' artwork and ships with the package (``ulg/data/brand``). It is there to credit the
project; the MIT licence does not grant trademark rights. See docs/en/licence-and-credit.md (German: docs/licence-and-credit.md).
"""

from __future__ import annotations

import base64
import struct
from functools import lru_cache
from importlib import resources

WEBSITE = "https://urbansens.de/"
WEBSITE_SHORT = "urbansens.de"
REPOSITORY = "https://github.com/UrbanSens/Urban-Landscape-Graphics"
DOCUMENTATION = "https://urbansens.github.io/Urban-Landscape-Graphics/"
STYLE_NAME = "UrbanSens Ecological Vector Style"

_PREFIX = {"en": "Style", "de": "Kartenstil"}


def credit_line(lang: str = "en", *, version: bool = True) -> str:
    """The line to put into a map caption, a legend or a list of sources.

    ``'Style: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'``; ``lang="de"`` starts with *Kartenstil*.
    """
    from . import __version__

    name = f"ulg {__version__}" if version else "ulg"
    return f"{_PREFIX.get(lang, _PREFIX['en'])}: {STYLE_NAME} ({name}) · {WEBSITE_SHORT}"


@lru_cache(maxsize=1)
def logo_png() -> bytes:
    """The UrbanSens logo as a PNG with transparent background."""
    return resources.files("ulg").joinpath("data", "brand", "urbansens-logo.png").read_bytes()


def logo_size() -> tuple[int, int]:
    """Width and height of :func:`logo_png` in pixels (read from the PNG header, no imaging library needed)."""
    w, h = struct.unpack(">II", logo_png()[16:24])
    return int(w), int(h)


@lru_cache(maxsize=1)
def logo_data_uri() -> str:
    return "data:image/png;base64," + base64.b64encode(logo_png()).decode("ascii")


def draw_credit(svg, x: float, y: float, *, height: float = 9.0, align: str = "right", text: bool = True,
                lang: str = "en", note: str | None = None, plate: str | None = None, rule: str = "#C6CACA",
                opacity: float = 0.92, ink: str = "#6B7375") -> tuple[float, float, float, float]:
    """Draw the small UrbanSens logo, with its credit text, onto an SVG page.

    ``(x, y)`` is the bottom right corner of the block (``align="right"``) or its bottom left corner
    (``align="left"``), in the page's millimetres; ``height`` is the height of the logo. ``text`` adds two small
    lines beside it (the style's name with the version and the website; ``note`` replaces the first line), left of
    the logo for ``align="right"``. ``plate`` is a colour: the block then sits on a rounded plate of that colour, for
    use on maps. Returns the box ``(x0, y0, x1, y1)`` the block covers, so that callers can keep other marks clear.
    """
    from . import __version__

    wpx, hpx = logo_size()
    lw = height * wpx / hpx
    lines: list[str] = []
    size = min(2.3, height * 0.26)
    if text and height >= 6.5:
        lines = [note or f"{STYLE_NAME} · ulg {__version__}", WEBSITE_SHORT if not note else f"{STYLE_NAME} · {WEBSITE_SHORT}"]
    gap = height * 0.28
    text_w = max((len(s) for s in lines), default=0) * size * 0.54
    total = lw + (gap + text_w if lines else 0.0)
    x0 = x - total if align == "right" else x
    top = y - height
    logo_x = x0 + (total - lw if align == "right" else 0.0)
    if plate:
        pad = height * 0.17
        svg.rect(x0 - pad, top - pad, total + 2 * pad, height + 2 * pad, fill=plate, stroke=rule, width=0.2, rx=height * 0.2,
                 opacity=0.93)
    svg.image(logo_x, top, lw, height, logo_data_uri(), opacity=opacity)
    if lines:
        lead = size * 1.42
        first = top + height / 2 - lead / 2 + size * 0.35
        tx = logo_x - gap if align == "right" else logo_x + lw + gap
        anchor = "end" if align == "right" else "start"
        for k, line in enumerate(lines):
            svg.text(tx, first + k * lead, line, size=size, fill=ink, anchor=anchor, weight="600" if k == len(lines) - 1 else "normal")
    pad = height * 0.17 if plate else 0.0
    return x0 - pad, top - pad, x0 + total + pad, y + pad

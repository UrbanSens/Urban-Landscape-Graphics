"""SVG backend: turns a display list into compact, editable vector output.

The document is laid out in millimetres (1 user unit = 1 mm), so the file
prints at the requested map scale and opens true to size in Inkscape,
Illustrator or Affinity. Each feature group keeps its element id as
``data-element`` for styling and scripting on the web.
"""

from __future__ import annotations

import html
import shutil
import subprocess
from pathlib import Path

import numpy as np

from .ir import LINE, QUAD, SMOOTH, Dots, Group, Paths, Text

FONT = "'Avenir Next', 'Nunito Sans', 'Source Sans 3', 'Helvetica Neue', Helvetica, Arial, sans-serif"


def _n(v: float) -> str:
    s = f"{v:.2f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _pairs(a) -> str:
    return " ".join(f"{_n(x)} {_n(y)}" for x, y in a)


# --------------------------------------------------------------------------- path data

def _catmull(p: np.ndarray, closed: bool):
    """Control points of the Catmull-Rom spline through p: returns (c1, c2, ends)."""
    if closed:
        prev, nxt, nxt2 = np.roll(p, 1, axis=-2), np.roll(p, -1, axis=-2), np.roll(p, -2, axis=-2)
        return p + (nxt - prev) / 6.0, nxt - (nxt2 - p) / 6.0, nxt
    pad = np.concatenate([p[..., :1, :], p, p[..., -1:, :]], axis=-2)
    p0, p1, p2, p3 = pad[..., :-3, :], pad[..., 1:-2, :], pad[..., 2:-1, :], pad[..., 3:, :]
    return p1 + (p2 - p0) / 6.0, p2 - (p3 - p1) / 6.0, p2


def path_d(pts: np.ndarray, kind: str = LINE, closed: bool = False) -> str:
    """SVG path data for one polyline given in paper coordinates."""
    pts = np.round(np.asarray(pts, dtype=np.float64), 2)
    n = len(pts)
    if n < 2:
        return ""
    if kind == QUAD:
        rows = pts.tolist()
        on, off = rows[0::2], rows[1::2]
        d = [f"M{_n(on[0][0])} {_n(on[0][1])}"]
        for i in range(len(off)):
            e = on[(i + 1) % len(on)]
            d.append(f"Q{_n(off[i][0])} {_n(off[i][1])} {_n(e[0])} {_n(e[1])}")
        return "".join(d) + "Z"
    if kind == SMOOTH and n >= 3:
        if closed and np.allclose(pts[0], pts[-1]):
            pts = pts[:-1]
        c1, c2, e = _catmull(pts, closed)
        d = [f"M{_n(pts[0, 0])} {_n(pts[0, 1])}"]
        for a, b, c in zip(c1.tolist(), c2.tolist(), e.tolist()):
            d.append(f"C{_n(a[0])} {_n(a[1])} {_n(b[0])} {_n(b[1])} {_n(c[0])} {_n(c[1])}")
        return "".join(d) + ("Z" if closed else "")
    rows = pts.tolist()
    return f"M{_n(rows[0][0])} {_n(rows[0][1])}L" + _pairs(rows[1:]) + ("Z" if closed else "")


def batch_d(paths, kind: str, closed: bool, tf) -> str:
    """Path data for a whole batch; fast paths for the common (n, k, 2) arrays."""
    if isinstance(paths, np.ndarray) and paths.ndim == 3 and len(paths):
        n, k, _ = paths.shape
        p = np.round(tf(paths.reshape(-1, 2)).reshape(n, k, 2), 2)
        if kind == LINE and k == 2 and not closed:
            return "".join(f"M{_n(a)} {_n(b)}L{_n(c)} {_n(d)}" for a, b, c, d in p.reshape(n, 4).tolist())
        if kind == SMOOTH and k >= 3:
            c1, c2, e = _catmull(p, closed)
            start = p[:, 0, :].tolist()
            seg = np.concatenate([c1, c2, e], axis=2).tolist()
            out = []
            for s0, row in zip(start, seg):
                out.append(f"M{_n(s0[0])} {_n(s0[1])}")
                out.extend(f"C{_n(v[0])} {_n(v[1])} {_n(v[2])} {_n(v[3])} {_n(v[4])} {_n(v[5])}" for v in row)
                if closed:
                    out.append("Z")
            return "".join(out)
        return "".join(path_d(q, kind, closed) for q in p)
    return "".join(path_d(tf(np.asarray(q)), kind, closed) for q in paths if len(q) >= 2)


# --------------------------------------------------------------------------- document

class Svg:
    """A page in millimetres onto which map frames and page furniture are drawn."""

    def __init__(self, width: float, height: float, background: str | None = None,
                 title: str | None = None, dots: str = "stroke"):
        self.width, self.height = float(width), float(height)
        self.background, self.title = background, title
        self.dots = dots
        self._defs: list[str] = []
        self._body: list[str] = []
        self._clip = 0

    # -- low level ---------------------------------------------------------
    def raw(self, fragment: str) -> None:
        self._body.append(fragment)

    def _clip_id(self, d: str) -> str:
        self._clip += 1
        cid = f"c{self._clip}"
        self._defs.append(f'<clipPath id="{cid}"><path d="{d}" clip-rule="evenodd"/></clipPath>')
        return cid

    def open_group(self, *, clip_d: str | None = None, attrs: dict | None = None) -> None:
        a = "".join(f' {k}="{html.escape(str(v), quote=True)}"' for k, v in (attrs or {}).items() if v is not None)
        if clip_d:
            a += f' clip-path="url(#{self._clip_id(clip_d)})"'
        self._body.append(f"<g{a}>")

    def close_group(self) -> None:
        self._body.append("</g>")

    # -- page furniture (paper coordinates, y down) -------------------------
    def rect(self, x, y, w, h, fill="none", stroke=None, width=0.2, rx=0, opacity=1.0) -> None:
        s = f' stroke="{stroke}" stroke-width="{_n(width)}"' if stroke else ""
        o = f' opacity="{_n(opacity)}"' if opacity < 1 else ""
        r = f' rx="{_n(rx)}"' if rx else ""
        self._body.append(f'<rect x="{_n(x)}" y="{_n(y)}" width="{_n(w)}" height="{_n(h)}" fill="{fill}"{s}{r}{o}/>')

    def line(self, x0, y0, x1, y1, stroke="#293941", width=0.2, dash=None, opacity=1.0) -> None:
        d = f' stroke-dasharray="{" ".join(_n(v) for v in dash)}"' if dash else ""
        o = f' opacity="{_n(opacity)}"' if opacity < 1 else ""
        self._body.append(f'<path d="M{_n(x0)} {_n(y0)}L{_n(x1)} {_n(y1)}" fill="none" stroke="{stroke}" '
                          f'stroke-width="{_n(width)}" stroke-linecap="round"{d}{o}/>')

    def circle(self, x, y, r, fill="none", stroke=None, width=0.2) -> None:
        s = f' stroke="{stroke}" stroke-width="{_n(width)}"' if stroke else ""
        self._body.append(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(r)}" fill="{fill}"{s}/>')

    def text(self, x, y, text, size=3.0, fill="#293941", anchor="start", weight="normal",
             italic=False, halo=None, spacing=None, font=None, rotate=None) -> None:
        """Text at (x, y) mm; ``rotate`` turns it by that many degrees (counter-clockwise) about (x, y)."""
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        w = f' font-weight="{weight}"' if weight != "normal" else ""
        i = ' font-style="italic"' if italic else ""
        sp = f' letter-spacing="{_n(spacing)}"' if spacing else ""
        f = f' font-family="{font}"' if font else ""
        h = (f' stroke="{halo}" stroke-width="{_n(size * 0.28)}" stroke-linejoin="round" paint-order="stroke"'
             if halo else "")
        r = f' transform="rotate({_n(-rotate)} {_n(x)} {_n(y)})"' if rotate else ""
        self._body.append(f'<text x="{_n(x)}" y="{_n(y)}" font-size="{_n(size)}" fill="{fill}"{a}{w}{i}{sp}{f}{h}{r}>'
                          f"{html.escape(str(text))}</text>")

    def polygon(self, points, fill="#293941", stroke=None, width=0.2, opacity=1.0) -> None:
        """A closed polygon through ``points`` (mm)."""
        d = "M" + "L".join(f"{_n(px)} {_n(py)}" for px, py in points) + "Z"
        s = f' stroke="{stroke}" stroke-width="{_n(width)}" stroke-linejoin="round"' if stroke else ""
        o = f' opacity="{_n(opacity)}"' if opacity < 1 else ""
        self._body.append(f'<path d="{d}" fill="{fill}"{s}{o}/>')

    # -- map frames --------------------------------------------------------
    def frame(self, items: list, bounds, u: float, x: float = 0.0, y: float = 0.0,
              clip: bool = True, name: str | None = None) -> None:
        """Draw a display list. ``bounds`` (minx, miny, maxx, maxy) maps to a box at (x, y) mm."""
        minx, miny, maxx, maxy = bounds
        w, h = (maxx - minx) / u, (maxy - miny) / u

        def tf(xy: np.ndarray) -> np.ndarray:
            xy = np.asarray(xy, dtype=np.float64)
            return np.column_stack([x + (xy[:, 0] - minx) / u, y + (maxy - xy[:, 1]) / u])

        clip_d = f"M{_n(x)} {_n(y)}h{_n(w)}v{_n(h)}h{_n(-w)}Z" if clip else None
        self.open_group(clip_d=clip_d, attrs={"id": name})
        self._items(items, tf)
        self.close_group()

    def _items(self, items: list, tf) -> None:
        for it in items:
            if isinstance(it, Group):
                clip_d = batch_d(it.clip, LINE, True, tf) if it.clip else None
                attrs = {"data-element": it.element, "data-name": it.name,
                         "opacity": _n(it.opacity) if it.opacity < 1 else None}
                self.open_group(clip_d=clip_d, attrs=attrs)
                self._items(it.items, tf)
                self.close_group()
            elif isinstance(it, Paths):
                self._paths(it, tf)
            elif isinstance(it, Dots):
                self._dots(it, tf)
            elif isinstance(it, Text):
                p = tf(np.array([it.xy]))[0]
                self.text(p[0], p[1], it.text, it.size, it.fill, it.anchor, it.weight, it.italic, it.halo)

    def _style(self, it: Paths, fill, stroke) -> str:
        a = [f'fill="{fill}"' if fill else 'fill="none"']
        if fill and it.fill_rule == "evenodd":
            a.append('fill-rule="evenodd"')
        if stroke and it.width > 0:
            a.append(f'stroke="{stroke}" stroke-width="{_n(it.width)}"')
            if it.cap != "butt":
                a.append(f'stroke-linecap="{it.cap}"')
            if it.join != "miter":
                a.append(f'stroke-linejoin="{it.join}"')
            if it.dash:
                a.append(f'stroke-dasharray="{" ".join(_n(v) for v in it.dash)}"')
        if it.opacity < 1:
            a.append(f'opacity="{_n(it.opacity)}"')
        return " ".join(a)

    def _paths(self, it: Paths, tf) -> None:
        if len(it.paths) == 0:
            return
        if it.compound:
            d = batch_d(it.paths, it.kind, it.closed, tf)
            if d:
                self._body.append(f'<path d="{d}" {self._style(it, it.fill, it.stroke)}/>')
            return
        n = len(it.paths)
        fills = it.fill if isinstance(it.fill, (list, tuple)) else [it.fill] * n
        strokes = it.stroke if isinstance(it.stroke, (list, tuple)) else [it.stroke] * n
        shared = self._style(Paths([], width=it.width, cap=it.cap, join=it.join, dash=it.dash,
                                   opacity=it.opacity, fill_rule="nonzero"), None, strokes[0])
        shared = shared.replace('fill="none" ', "").replace('fill="none"', "")
        same_stroke = all(s == strokes[0] for s in strokes)
        self._body.append(f"<g {shared}>" if same_stroke else "<g>")
        for q, f, s in zip(it.paths, fills, strokes):
            d = path_d(tf(np.asarray(q)), it.kind, it.closed)
            if not d:
                continue
            extra = "" if same_stroke else f' stroke="{s}"'
            self._body.append(f'<path d="{d}" fill="{f or "none"}"{extra}/>')
        self._body.append("</g>")

    def _dots(self, it: Dots, tf) -> None:
        if len(it.xy) == 0:
            return
        p = np.round(tf(it.xy), 2)
        r = np.broadcast_to(np.round(np.asarray(it.r, dtype=np.float64) / 0.02) * 0.02, (len(p),))
        o = f' opacity="{_n(it.opacity)}"' if it.opacity < 1 else ""
        if self.dots == "arc":
            d = "".join(f"M{_n(x - rr)} {_n(y)}a{_n(rr)} {_n(rr)} 0 1 0 {_n(2 * rr)} 0a{_n(rr)} {_n(rr)} 0 1 0 {_n(-2 * rr)} 0"
                        for (x, y), rr in zip(p.tolist(), r.tolist()))
            self._body.append(f'<path d="{d}" fill="{it.fill}"{o}/>')
            return
        for rr in np.unique(r):
            if rr <= 0:
                continue
            sel = p[r == rr].tolist()
            d = "".join(f"M{_n(x)} {_n(y)}h.01" for x, y in sel)
            self._body.append(f'<path d="{d}" fill="none" stroke="{it.fill}" stroke-width="{_n(2 * rr)}" '
                              f'stroke-linecap="round"{o}/>')

    # -- output ------------------------------------------------------------
    def tostring(self) -> str:
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{_n(self.width)}mm" height="{_n(self.height)}mm" '
                f'viewBox="0 0 {_n(self.width)} {_n(self.height)}" font-family="{FONT}">')
        parts = [head]
        if self.title:
            parts.append(f"<title>{html.escape(self.title)}</title>")
        if self._defs:
            parts.append("<defs>" + "".join(self._defs) + "</defs>")
        if self.background:
            parts.append(f'<rect width="100%" height="100%" fill="{self.background}"/>')
        parts.extend(self._body)
        parts.append("</svg>")
        return "\n".join(parts)

    def save(self, path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.tostring(), encoding="utf-8")
        return path


def rasterize(svg_path, png_path=None, dpi: int = 200) -> Path:
    """Convert an SVG file to PNG with whatever rasteriser is installed."""
    svg_path = Path(svg_path)
    png_path = Path(png_path) if png_path else svg_path.with_suffix(".png")
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-d", str(dpi), "-p", str(dpi), "-o", str(png_path), str(svg_path)], check=True)
        return png_path
    try:
        import cairosvg  # type: ignore
    except ImportError:
        pass
    else:
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), dpi=dpi)
        return png_path
    if shutil.which("inkscape"):
        subprocess.run(["inkscape", str(svg_path), f"--export-dpi={dpi}", "--export-type=png",
                        f"--export-filename={png_path}"], check=True, capture_output=True)
        return png_path
    raise RuntimeError("No SVG rasteriser found (install librsvg, cairosvg or Inkscape), "
                       "or render with the Matplotlib backend instead.")

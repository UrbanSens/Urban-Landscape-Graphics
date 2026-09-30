"""Matplotlib backend: draws the same display list as the SVG backend onto an Axes.

The axes stay in map coordinates, so anything else (analysis layers, basemaps,
annotations from GeoPandas) can be plotted on top in the usual way. Line widths
and mark sizes are paper sizes, as in the SVG output.
"""

from __future__ import annotations

import numpy as np

from .ir import LINE, QUAD, SMOOTH, Dots, Group, Paths, Text
from .svg import _catmull

MM_TO_PT = 72.0 / 25.4


def _mpath():
    from matplotlib.path import Path  # imported lazily so the core works without Matplotlib

    return Path


def _one(pts: np.ndarray, kind: str, closed: bool):
    """Vertices and codes for a single polyline."""
    Path = _mpath()
    pts = np.asarray(pts, dtype=np.float64)
    n = len(pts)
    if n < 2:
        return None
    if kind == QUAD:
        on, off = pts[0::2], pts[1::2]
        k = len(off)
        v = np.empty((1 + 2 * k + 1, 2))
        v[0] = on[0]
        v[1:-1:2] = off
        v[2:-1:2] = np.roll(on, -1, axis=0)[:k]
        v[-1] = on[0]
        c = np.full(len(v), Path.CURVE3, dtype=np.uint8)
        c[0], c[-1] = Path.MOVETO, Path.CLOSEPOLY
        return v, c
    if kind == SMOOTH and n >= 3:
        if closed and np.allclose(pts[0], pts[-1]):
            pts = pts[:-1]
        c1, c2, e = _catmull(pts, closed)
        k = len(e)
        v = np.empty((1 + 3 * k + (1 if closed else 0), 2))
        v[0] = pts[0]
        v[1:1 + 3 * k:3], v[2:1 + 3 * k:3], v[3:1 + 3 * k:3] = c1, c2, e
        c = np.full(len(v), Path.CURVE4, dtype=np.uint8)
        c[0] = Path.MOVETO
        if closed:
            v[-1], c[-1] = pts[0], Path.CLOSEPOLY
        return v, c
    if closed:
        v = np.vstack([pts, pts[:1]])
        c = np.full(len(v), Path.LINETO, dtype=np.uint8)
        c[0], c[-1] = Path.MOVETO, Path.CLOSEPOLY
        return v, c
    c = np.full(n, Path.LINETO, dtype=np.uint8)
    c[0] = Path.MOVETO
    return pts, c


def _compound(paths, kind: str, closed: bool):
    Path = _mpath()
    if isinstance(paths, np.ndarray) and paths.ndim == 3 and kind == LINE and not closed and len(paths):
        n, k, _ = paths.shape
        c = np.full((n, k), Path.LINETO, dtype=np.uint8)
        c[:, 0] = Path.MOVETO
        return Path(paths.reshape(-1, 2), c.ravel())
    vs, cs = [], []
    for q in paths:
        r = _one(q, kind, closed)
        if r is not None:
            vs.append(r[0])
            cs.append(r[1])
    if not vs:
        return None
    return Path(np.concatenate(vs), np.concatenate(cs))


class MplPainter:
    def __init__(self, ax, zorder: float = 1.0):
        self.ax = ax
        self.z = zorder
        self.artists: list = []

    def _add(self, artist, clip):
        self.z += 1e-4
        artist.set_zorder(self.z)
        if clip is not None:
            artist.set_clip_path(clip, transform=self.ax.transData)
        self.artists.append(artist)

    def draw(self, items: list, clip=None) -> list:
        from matplotlib.collections import PathCollection
        from matplotlib.patches import PathPatch

        ax = self.ax
        for it in items:
            if isinstance(it, Group):
                sub = _compound(it.clip, LINE, True) if it.clip else clip
                self.draw(it.items, sub)
            elif isinstance(it, Paths):
                if len(it.paths) == 0:
                    continue
                lw = it.width * MM_TO_PT if it.stroke and it.width > 0 else 0.0
                common = dict(linewidth=lw, alpha=it.opacity if it.opacity < 1 else None)
                if it.compound:
                    path = _compound(it.paths, it.kind, it.closed)
                    if path is None:
                        continue
                    patch = PathPatch(path, facecolor=it.fill or "none", edgecolor=it.stroke if lw else "none",
                                      capstyle=it.cap, joinstyle=it.join, fill=bool(it.fill), **common)
                    if it.dash and lw:
                        patch.set_linestyle((0, tuple(v * MM_TO_PT for v in it.dash)))
                    ax.add_patch(patch)
                    self._add(patch, clip)
                else:
                    paths = [p for p in (_compound([q], it.kind, it.closed) for q in it.paths) if p is not None]
                    n = len(paths)
                    fills = it.fill if isinstance(it.fill, (list, tuple)) else [it.fill or "none"] * n
                    strokes = it.stroke if isinstance(it.stroke, (list, tuple)) else [it.stroke or "none"] * n
                    coll = PathCollection(paths, facecolors=list(fills), edgecolors=list(strokes) if lw else "none",
                                          linewidths=lw, capstyle=it.cap, joinstyle=it.join,
                                          alpha=it.opacity if it.opacity < 1 else None)
                    ax.add_collection(coll, autolim=False)
                    self._add(coll, clip)
            elif isinstance(it, Dots):
                if len(it.xy) == 0:
                    continue
                d = 2.0 * np.broadcast_to(np.asarray(it.r, dtype=np.float64), (len(it.xy),)) * MM_TO_PT
                coll = ax.scatter(it.xy[:, 0], it.xy[:, 1], s=d**2, c=it.fill, marker="o", linewidths=0,
                                  alpha=it.opacity if it.opacity < 1 else None)
                self._add(coll, clip)
            elif isinstance(it, Text):
                import matplotlib.patheffects as pe

                t = ax.text(it.xy[0], it.xy[1], it.text, fontsize=it.size * MM_TO_PT, color=it.fill,
                            ha={"start": "left", "middle": "center", "end": "right"}[it.anchor],
                            fontweight=it.weight, fontstyle="italic" if it.italic else "normal")
                if it.halo:
                    t.set_path_effects([pe.withStroke(linewidth=it.size * MM_TO_PT * 0.28, foreground=it.halo)])
                self._add(t, None)
        return self.artists


def paper_scale(ax) -> float:
    """Map units per paper millimetre for the axes as they are laid out right now."""
    ax.apply_aspect()
    fig = ax.figure
    box = ax.get_window_extent()
    width_mm = box.width / fig.dpi * 25.4
    x0, x1 = ax.get_xlim()
    return abs(x1 - x0) / width_mm

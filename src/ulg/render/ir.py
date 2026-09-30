"""Display list shared by all backends.

Generators emit these few primitives in *map coordinates* (the CRS units of the
data, y up). Sizes that belong to the drawing rather than to the ground — line
widths, dot radii, dash lengths — are in *millimetres on paper*. The SVG and
Matplotlib backends draw exactly the same list, so both outputs match.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

LINE = "line"      # straight segments through the points
SMOOTH = "smooth"  # Catmull-Rom spline through the points
QUAD = "quad"      # closed chain of quadratic Béziers: on, off, on, off, ...


@dataclass
class Paths:
    """A batch of polylines or polygons that share a style.

    ``fill`` and ``stroke`` are hex strings, or lists with one colour per path
    when ``compound`` is False. A compound batch is painted as one shape (rings
    of one polygon, or thousands of texture strokes in a single element);
    a non-compound batch paints path after path, so later ones cover earlier ones.
    """

    paths: list
    fill: str | list | None = None
    stroke: str | list | None = None
    width: float = 0.2
    opacity: float = 1.0
    closed: bool = False
    kind: str = LINE
    compound: bool = True
    cap: str = "round"
    join: str = "round"
    dash: tuple | None = None
    fill_rule: str = "evenodd"


@dataclass
class Dots:
    """Filled discs; ``r`` is a radius in paper millimetres (scalar or one per dot)."""

    xy: np.ndarray
    r: float | np.ndarray
    fill: str
    opacity: float = 1.0


@dataclass
class Text:
    xy: tuple
    text: str
    size: float = 2.6            # cap height-ish, paper mm
    fill: str = "#293941"
    anchor: str = "start"        # start | middle | end
    weight: str = "normal"
    italic: bool = False
    halo: str | None = None


@dataclass
class Group:
    """Children painted in order, optionally clipped to polygon rings (even-odd)."""

    items: list = field(default_factory=list)
    clip: list | None = None
    name: str | None = None
    element: str | None = None
    opacity: float = 1.0

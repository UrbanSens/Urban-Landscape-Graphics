"""Small synthetic datasets for documentation, tests and the style sheet.

``demo_park()`` builds *Angerpark*, a fictitious city quarter of about 20 ha in a metric CRS
(ETRS89 / UTM 32N, EPSG:25832): a 5 ha park (allée, great lawn, meadows, orchard, community garden,
playground, pond with reed belt, pavilion and plaza) between an avenue with a green tram track, perimeter
blocks with courtyards, a school, a canal with promenades and street trees. The ground is a clean planar
partition; the street grid is turned against north, as real ones are. Everything is generated in code, so
the package ships no binary data.

Layers: ``landcover``, ``trees`` and ``lines`` belong to the park (the *site*); ``context`` is the
surrounding quarter. ``demo_park_places()`` names the interesting spots for crops and labels.
"""

from __future__ import annotations

import functools
import math

import numpy as np
import shapely
from shapely import affinity, make_valid, set_precision
from shapely.geometry import LineString, MultiPolygon, Point, Polygon, box
from shapely.ops import linemerge, unary_union

ORIGIN = (583600.0, 5509300.0)
CRS = "EPSG:25832"

#: design space (m): x east, y north; the visible window is cut out after turning by ANGLE
FRAME = box(-60.0, -120.0, 880.0, 640.0)
CENTRE = (392.0, 268.0)
ANGLE = 13.0
WINDOW = (560.0, 360.0)

#: park corner in design space (the park fills the block between avenue, north street, west and middle street)
PARK_X0, PARK_Y0 = 202.5, 196.2


# --------------------------------------------------------------------------- geometry helpers

def _chaikin(pts: np.ndarray, closed: bool, rounds: int = 3) -> np.ndarray:
    p = np.asarray(pts, dtype=float)
    for _ in range(rounds):
        if closed:
            q = np.roll(p, -1, axis=0)
            p = np.column_stack([0.75 * p + 0.25 * q, 0.25 * p + 0.75 * q]).reshape(-1, 2)
        else:
            a, b = p[:-1], p[1:]
            mid = np.column_stack([0.75 * a + 0.25 * b, 0.25 * a + 0.75 * b]).reshape(-1, 2)
            p = np.vstack([p[:1], mid, p[-1:]])
    return p


def _blob(cx, cy, rx, ry, rng, n=9, rough=0.18, rot=0.0) -> Polygon:
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False) + rng.uniform(-0.2, 0.2, n)
    r = 1 + rng.uniform(-rough, rough, n)
    pts = np.column_stack([rx * r * np.cos(ang), ry * r * np.sin(ang)])
    poly = Polygon(_chaikin(pts, True))
    return affinity.translate(affinity.rotate(poly, rot, origin=(0, 0)), cx, cy)


def _curve(pts, closed=False, rounds=3) -> LineString:
    c = _chaikin(np.asarray(pts, dtype=float), closed, rounds)
    if closed:
        c = np.vstack([c, c[:1]])
    return LineString(c)


def _rect(cx, cy, w, h, rot=0.0) -> Polygon:
    return affinity.rotate(box(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), rot, origin=(cx, cy))


def _wedge(cx, cy, r, a0, a1) -> Polygon:
    """Pie slice from angle a0 to a1 (degrees, counter-clockwise from east)."""
    t = np.radians(np.linspace(a0, a1, 24))
    return Polygon([(cx, cy), *zip(cx + r * np.cos(t), cy + r * np.sin(t))])


def _polys(geom) -> list[Polygon]:
    """Every polygon inside a geometry, however deeply nested in collections."""
    if geom is None or geom.is_empty:
        return []
    if isinstance(geom, Polygon):
        return [geom]
    return [p for g in getattr(geom, "geoms", []) for p in _polys(g)]


def _lines(geom) -> list[LineString]:
    """Every line inside a geometry, however deeply nested in collections."""
    if geom is None or geom.is_empty:
        return []
    if isinstance(geom, LineString):
        return [geom]
    return [ln for g in getattr(geom, "geoms", []) for ln in _lines(g)]


def _long_axis(geom) -> tuple[float, tuple[float, float]]:
    """Direction (degrees) of the long side of the minimum rotated rectangle of ``geom`` and that rectangle's centre."""
    with np.errstate(divide="ignore", invalid="ignore"):         # GEOS 3.13 reports harmless float events here
        rect = geom.minimum_rotated_rectangle
    xs, ys = rect.exterior.coords.xy
    sides = [(math.hypot(xs[i + 1] - xs[i], ys[i + 1] - ys[i]), math.degrees(math.atan2(ys[i + 1] - ys[i], xs[i + 1] - xs[i])))
             for i in range(2)]
    c = rect.centroid
    return max(sides)[1], (c.x, c.y)


def _valid(geom):
    """Repair a geometry without losing holes that touch the shell (``make_valid`` would fill them)."""
    return make_valid(geom, method="structure")


def _union(items) -> Polygon | MultiPolygon:
    items = [g for g in items if g is not None and not g.is_empty]
    return _valid(unary_union(items)) if items else Polygon()


def _stripe(line: LineString, width: float):
    return line.buffer(width / 2.0, cap_style="flat", join_style="round")


def _offset(line: LineString, dist: float) -> LineString:
    """Parallel line at ``dist`` metres to the left (negative: right)."""
    out = shapely.offset_curve(line, dist)
    parts = _lines(out)
    return max(parts, key=lambda g: g.length) if parts else LineString()


def _along(line: LineString, step: float, start: float = 0.0, end: float | None = None):
    """Points every ``step`` metres along a line: [(x, y, bearing in degrees)]."""
    total = line.length
    end = total if end is None else min(end, total)
    out, t = [], start
    while t <= end + 1e-9:
        p, a, b = line.interpolate(t), line.interpolate(min(t + 0.5, total)), line.interpolate(max(t - 0.5, 0.0))
        out.append((p.x, p.y, math.degrees(math.atan2(a.y - b.y, a.x - b.x))))
        t += step
    return out


def _scatter(rng, region, n, dmin, dmax, existing, gap=0.42, tries=70):
    """Random crowns inside ``region`` that overlap their neighbours by at most ``1 - gap``: [(x, y, d)]."""
    if region is None or region.is_empty:
        return []
    minx, miny, maxx, maxy = region.bounds
    prep = shapely.prepared.prep(region)
    got: list[tuple[float, float, float]] = []
    for _ in range(int(n * tries)):
        if len(got) >= n:
            break
        x, y, d = rng.uniform(minx, maxx), rng.uniform(miny, maxy), rng.uniform(dmin, dmax)
        if not prep.contains(Point(x, y)):
            continue
        if any(math.hypot(x - a, y - b) < gap * (d + c) for a, b, c in existing + got):
            continue
        got.append((x, y, d))
    return got


def _wavy_edge(x0, x1, y, amp, rng, step=16.0, sign=1.0):
    n = max(3, int((x1 - x0) / step))
    xs = np.linspace(x0, x1, n)
    return [(float(x), float(y + sign * rng.uniform(-amp, amp))) for x in xs]


class _Ground:
    """A planar partition: features are added highest priority first and never overlap."""

    def __init__(self, clip):
        self.clip, self.taken, self.feats = clip, Polygon(), []

    def add(self, element, geom, layer, **props):
        g = _valid(_valid(geom).intersection(self.clip).difference(self.taken))
        keep = [part for poly in _polys(g) for part in _polys(_valid(poly.buffer(0))) if part.area > 0.8]
        if not keep:
            return
        self.taken = _valid(unary_union([self.taken, *keep]))    # slivers stay free for what comes later
        for part in keep:
            self.feats.append({"geometry": part, "element": element, "layer": layer, **props})


# --------------------------------------------------------------------------- the quarter

#: cross-sections (m from the centre line outwards): tram track, lane, cycle lane, parking/tree bay, footway
STREETS = {
    "avenue": dict(pts=[(-100, 182), (900, 182)], tram=6.5, lane=3.3, cyc=2.0, bay=2.4, walk=3.2),
    "north": dict(pts=[(-100, 378), (900, 378)], tram=0.0, lane=3.4, cyc=0.0, bay=2.2, walk=3.0),
    "north2": dict(pts=[(-100, 476), (900, 476)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=3.0),
    "west": dict(pts=[(196, -140), (196, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=3.0),
    "west2": dict(pts=[(74, -140), (74, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=2.6),
    "middle": dict(pts=[(520, 182), (520, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=3.0),
    "east1": dict(pts=[(614, 182), (614, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=2.6),
    "east": dict(pts=[(706, -140), (706, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=3.0),
    "north_a": dict(pts=[(348, 378), (348, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=2.6),
    "north_b": dict(pts=[(470, 378), (470, 700)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=2.6),
    "south_a": dict(pts=[(352, -140), (352, 122)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=2.6),
    "south_b": dict(pts=[(566, -140), (566, 122)], tram=0.0, lane=3.0, cyc=0.0, bay=0.0, walk=2.6),
}


def _half(s):
    return s["tram"] / 2 + s["lane"] + s["cyc"] + s["bay"] + s["walk"]


def _perimeter(block, rng, depth=13.0, setback=1.0, spacing=(46, 74), gap=(2.6, 5.0)):
    """Buildings along the edge of a block with gaps for entries: (buildings, courtyard, hedges across the gaps)."""
    inner = block.buffer(-setback)
    if inner.is_empty:
        return [], Polygon(), []
    court = inner.buffer(-depth)
    ring = inner.difference(court)
    axes = [p.buffer(-depth / 2).exterior for p in _polys(inner) if not p.buffer(-depth / 2).is_empty]
    cuts = []
    for ax in axes:
        length = ax.length
        n = max(2, int(length / rng.uniform(*spacing)))
        for t in np.linspace(0, length, n, endpoint=False) + rng.uniform(0, length / n):
            p, q = ax.interpolate(t), ax.interpolate((t + 1.0) % length)
            ang = math.degrees(math.atan2(q.y - p.y, q.x - p.x))
            cuts.append(_rect(p.x, p.y, rng.uniform(*gap), depth + 6, ang))
    gaps = _union(cuts)
    parts = ring.difference(gaps)
    hedges = [ln for p in _polys(inner) for ln in _lines(p.exterior.intersection(gaps.buffer(-0.2))) if ln.length > 1.5]
    return [b for b in _polys(parts) if b.area > 140], court, hedges


def _slabs(block, rng, depth=12.0, length=(46, 70), spacing=26.0):
    """Parallel rows of slab buildings along the long axis of a block (Zeilenbau)."""
    ang, c = _long_axis(block)
    turned = affinity.rotate(block.buffer(-4), -ang, origin=c)
    minx, miny, maxx, maxy = turned.bounds
    out = []
    y = miny + depth
    while y < maxy - depth / 2:
        x = minx + 6
        while x < maxx - 20:
            ln = rng.uniform(*length)
            b = box(x, y - depth / 2, min(x + ln, maxx - 6), y + depth / 2)
            if turned.contains(b) and b.area > 200:
                out.append(affinity.rotate(b, ang, origin=c))
            x += ln + rng.uniform(8, 16)
        y += spacing
    return out


def _street_furniture(net, canal_line, ctx_trees, ctx_points, rng, blocked):
    """Street trees, lamps and benches along the streets, the promenade and the canal."""
    def keep(x, y, r=2.5):
        return not blocked.buffer(r).contains(Point(x, y))

    for key, s in net.items():
        half_lane = s["tram"] / 2 + s["lane"] + s["cyc"]
        if s["bay"]:
            off = half_lane + s["bay"] / 2                          # trees stand in the parking strip
        else:
            off = half_lane + s["walk"] * 0.62
        for side in (1, -1):
            line = _offset(s["line"], side * off)
            if line.is_empty:
                continue
            step = 11.0 if key == "avenue" else 12.0
            for i, (x, y, _) in enumerate(_along(line, step, start=rng.uniform(0, 6))):
                if keep(x, y, 3.0):
                    ctx_trees.append((x + rng.normal(0, 0.3), y + rng.normal(0, 0.3), rng.uniform(6.6, 8.6), "tree_street"))
            for x, y, _ in _along(_offset(s["line"], side * (half_lane + 0.6)), 28.0, start=8.0):
                if keep(x, y, 3.0) and key in ("avenue", "north"):
                    ctx_points.append((x, y, "lamp"))
    # riverside: a row of trees on the lawn strip, benches and lamps on the promenade
    for x, y, _ in _along(_offset(canal_line, 21.0), 13.0, start=4.0):
        if keep(x, y, 4.0) and rng.random() < 0.92:
            ctx_trees.append((x, y, rng.uniform(8.5, 11.0), "tree"))
    for x, y, _ in _along(_offset(canal_line, 11.0), 44.0, start=12.0):
        if keep(x, y, 4.0):
            ctx_points.append((x, y, "bench"))
    for x, y, _ in _along(_offset(canal_line, 11.0), 22.0, start=0.0):
        if keep(x, y, 4.0) and rng.random() < 0.5:
            ctx_points.append((x + 1.2, y + 1.0, "lamp"))


def _park(rng, parcel):
    """The park as ground polygons (highest priority first), trees, points, lines and named places."""
    X0, Y0 = PARK_X0, PARK_Y0
    L = lambda pts: [(X0 + x, Y0 + y) for x, y in pts]
    pt = lambda x, y: (X0 + x, Y0 + y)
    ground: list[tuple[str, object]] = []
    trees: list[tuple[float, float, float, str]] = []
    points: list[tuple[float, float, str]] = []
    lines: list[tuple[LineString, str]] = []
    places: dict[str, tuple[float, float]] = {}

    # water ------------------------------------------------------------------------------------
    pond = _blob(*pt(238, 124), 34, 19.5, rng, n=10, rough=0.13, rot=-8)
    pc = pond.centroid
    inflow = _curve(L([(224, 180), (219, 162), (226, 148), (231, 139)])).buffer(1.7)
    outflow = _curve(L([(224, 108), (228, 94), (236, 80), (233, 64), (237, 46), (246, 30), (254, 16)])).buffer(1.5)
    streams = _union([inflow, outflow])
    places.update(pond=(pc.x, pc.y), reed=(pc.x + 30.0, pc.y + 5.0), stream=pt(234, 64))

    # paths ------------------------------------------------------------------------------------
    axis = LineString(L([(-8, 64), (266, 64)]))
    secondary = [
        _curve(L([(118, 180), (116, 152), (124, 124), (113, 94), (118, 64)])),             # north gate -> axis
        _curve(L([(60, 64), (66, 46), (80, 32), (92, 26)])),                                # to playground
        _curve(L([(112, 34), (128, 30), (150, 24), (174, 26)])),                            # to the court
        _curve(L([(30, 64), (34, 84), (50, 98), (70, 104), (92, 112), (108, 122)])),       # orchard walk
        _curve(L([(170, 64), (178, 84), (190, 100), (198, 110)])),                          # to the pavilion
        _curve(L([(282, 83), (290, 108), (294, 140), (298, 182)])),                         # plaza -> north east gate
        _curve(L([(282, 45), (288, 26), (300, 0)])),                                        # plaza -> south gate
        _curve(L([(-6, 132), (26, 138), (60, 146), (96, 150)])),                            # west gate through the orchard
    ]
    loop = _curve([pt(238 + 46 * math.cos(a) * 1.0, 124 + 31 * math.sin(a)) for a in np.radians(np.arange(0, 360, 45))],
                  closed=True)
    paths = _union([_stripe(axis, 5.0)] + [_stripe(c, 2.8) for c in secondary] + [_stripe(loop, 2.4)])
    mown = _union([
        _stripe(_curve(L([(70, 100), (90, 110), (108, 104), (126, 114), (148, 108), (170, 120)])), 2.4),
        _stripe(_curve(L([(160, 22), (176, 30), (192, 26), (214, 34)])), 2.2),
    ])
    bridge = _stripe(axis, 5.6).intersection(outflow.buffer(1.4))

    # plaza and its furniture ---------------------------------------------------------------------
    plaza = Point(*pt(283, 64)).buffer(19.0)
    fx, fy = pt(283, 64)
    places["plaza"] = (fx, fy)
    points.append((fx, fy, "fountain"))
    for a in range(0, 360, 45):
        if a != 180:
            points.append((fx + 12.4 * math.cos(math.radians(a)), fy + 12.4 * math.sin(math.radians(a)), "bench"))
    for a in range(30, 360, 60):
        trees.append((fx + 15.6 * math.cos(math.radians(a)), fy + 15.6 * math.sin(math.radians(a)), rng.uniform(7.6, 8.8), "tree_street"))
    for i in range(3):
        points.append((*pt(266.5, 46 + 3.2 * i), "bike_rack"))
    points += [(*pt(268, 84), "litter_bin"), (*pt(300, 84), "litter_bin"), (*pt(268, 44), "lamp"), (*pt(298, 44), "lamp")]

    # play, sport, garden, pavilion -------------------------------------------------------------------
    play_box = _rect(*pt(102, 38), 30, 22).buffer(-3.5).buffer(3.5)
    sand_pit = _blob(*pt(95, 36), 6.5, 5.0, rng, n=8, rough=0.12)
    for x, y in [(110, 44), (112, 33), (104, 30), (96, 45), (108, 38), (100, 40)]:
        points.append((*pt(x, y), "play_equipment"))
    points += [(*pt(86, 26), "bench"), (*pt(118, 52), "bench")]
    places["playground"] = pt(102, 38)
    court = _rect(*pt(194, 22), 34, 17)
    points += [(*pt(176, 36), "bench"), (*pt(212, 36), "bench")]
    places["court"] = pt(194, 22)
    gates = paths.buffer(1.0)                                             # fences open where a path enters
    lines.append((court.buffer(2.2).exterior.difference(gates), "fence"))
    lines.append((play_box.buffer(3.0).exterior.difference(gates), "fence"))

    plots, beds = [], []
    for i in range(3):
        for j in range(2):
            plot = box(*pt(10.5 + i * 15.4, 17 + j * 20), *pt(10.5 + i * 15.4 + 13.6, 17 + j * 20 + 17.5))
            (beds if (i, j) in ((2, 1),) else plots).append(plot)
    huts = [_rect(*pt(52, 61), 4.0, 3.2), _rect(*pt(52, 22), 3.6, 3.0)]
    garden_yard = box(*pt(7, 14), *pt(57, 67))
    lines.append((garden_yard.buffer(1.4).exterior.difference(gates), "fence"))
    places["garden"] = pt(32, 42)

    pav_c = pt(197.0, 124.5)
    pavilion = _rect(*pav_c, 16.0, 9.6, -8)
    terrace = _rect(pav_c[0] + 12.6, pav_c[1] - 1.7, 11.5, 13.5, -8)
    jetty = _rect(pav_c[0] + 25.4, pav_c[1] - 3.9, 15, 2.6, -8)
    places["pavilion"] = pav_c
    points += [(pav_c[0] + 12.5, pav_c[1] + 2.4, "bench"), (pav_c[0] + 14.6, pav_c[1] - 4.4, "bench")]

    # vegetation areas ---------------------------------------------------------------------------------
    edge = _wavy_edge(-12, 326, 149, 6.5, rng, step=15.0)
    woodland = Polygon(_chaikin(np.array(L([(-12, 200)] + edge + [(326, 200)])), True, rounds=2))
    woodland = woodland.difference(_blob(*pt(150, 158), 15, 7, rng, rough=0.1))
    orchard = _blob(*pt(34, 122), 31, 24, rng, n=9, rough=0.1, rot=6)
    wild1 = _blob(*pt(138, 112), 40, 22, rng, n=9, rough=0.12, rot=-6)
    meadow1 = _blob(*pt(132, 112), 58, 35, rng, n=10, rough=0.1, rot=-6)
    wild2 = _blob(*pt(206, 27), 32, 15, rng, n=9, rough=0.12)
    meadow2 = _blob(*pt(202, 28), 46, 24, rng, n=9, rough=0.1)
    swale_line = _curve(L([(34, 6.5), (90, 5), (150, 7), (226, 5.5)]))
    swale = _stripe(swale_line, 3.4)
    rain = [_blob(*pt(258, 9), 9.0, 5.0, rng, n=8, rough=0.12), _blob(*pt(272, 33), 6.5, 3.6, rng, n=8, rough=0.12)]
    soft = lambda g: g.buffer(-0.9).buffer(0.9)
    reed = _union([soft(pond.buffer(4.6).difference(pond).intersection(_blob(pc.x + 27, pc.y + 6, 34, 27, rng, n=8, rough=0.1))),
                   inflow.buffer(3.4).intersection(box(*pt(200, 130), *pt(250, 176)))])
    riparian = soft(pond.buffer(8.0).difference(pond).intersection(_blob(pc.x + 2, pc.y - 21, 30, 10, rng, n=8, rough=0.1, rot=-6)))
    places.update(orchard=pt(34, 122), meadow=pt(138, 112), woodland=pt(150, 166), allee=pt(60, 64),
                  oak=pt(150, 42), park=pt(150, 90))

    ground += [
        ("building", pavilion), ("wood_deck", _union([terrace, jetty, bridge])),
        ("water", pond), ("watercourse", streams), ("plaza", plaza), ("waterbound", paths),
        ("sand", sand_pit), ("safety_surface", play_box), ("clay_court", court),
        ("building_minor", _union(huts)), ("vegetable_garden", _union(plots)), ("perennials", _union(beds)),
        ("waterbound", garden_yard),
        ("reed", reed), ("riparian_strip", riparian), ("swale", swale), ("rain_garden", _union(rain)),
        ("lawn", mown), ("woodland_mixed", woodland), ("orchard_meadow", orchard),
        ("wildflower_meadow", _union([wild1, wild2])), ("meadow", _union([meadow1, meadow2])),
    ]

    # trees ------------------------------------------------------------------------------------------------
    blocked = _union([streams.buffer(4.0), paths.difference(_stripe(axis, 5.0)).buffer(3.4), plaza.buffer(2.0), pond.buffer(3.0),
                      play_box.buffer(3), court.buffer(3), garden_yard.buffer(3), pavilion.buffer(3), terrace.buffer(2), woodland,
                      orchard, swale.buffer(2)])
    for side in (1, -1):
        for x, y, _ in _along(_offset(axis, side * 7.4), 10.6, start=8.0, end=252.0):
            if not streams.buffer(3.8).contains(Point(x, y)) and not paths.difference(_stripe(axis, 5.0)).buffer(2.4).contains(Point(x, y)):
                trees.append((x, y, rng.uniform(8.8, 9.8), "tree"))
    oak = pt(150, 42)
    trees.append((*oak, 19.5, "tree_veteran"))
    existing = [(x, y, d) for x, y, d, _ in trees]
    open_lawn = parcel.difference(blocked).difference(meadow1.buffer(-4)).difference(meadow2.buffer(-4)).buffer(-6.5)
    for x, y, d in _scatter(rng, open_lawn.difference(Point(*oak).buffer(14)), 14, 9.5, 13.5, existing, gap=0.55):
        trees.append((x, y, d, "tree"))
    existing = [(x, y, d) for x, y, d, _ in trees]
    for x, y, d in _scatter(rng, meadow1.buffer(-6).difference(mown.buffer(2)).difference(paths.buffer(3)), 7, 7.5, 10.5,
                            existing, gap=0.5):
        trees.append((x, y, d, "tree"))
    existing = [(x, y, d) for x, y, d, _ in trees]
    for x, y, d in _scatter(rng, _blob(*pt(203, 46), 12, 6, rng).difference(court.buffer(4)).difference(paths.buffer(3)), 5, 7.5, 10.5,
                            existing, gap=0.45):
        trees.append((x, y, d, "tree"))
    existing = [(x, y, d) for x, y, d, _ in trees]
    for x, y, d in _scatter(rng, _blob(*pt(294, 152), 14, 12, rng).difference(paths.buffer(3)).intersection(parcel), 5, 6.0, 8.0,
                            existing, gap=0.5):
        trees.append((x, y, d, "tree_conifer"))
    for x, y, _ in _along(LineString(L([(8, 143), (60, 146), (120, 143), (180, 146), (250, 142), (304, 146)])), 15.0, start=4.0):
        trees.append((x + rng.normal(0, 2.0), y + rng.normal(0, 1.5), rng.uniform(10.5, 13.5), "tree"))
    for x, y, d in [(214, 96, 12.0), (250, 100, 11.0), (208, 148, 11.5)]:
        trees.append((*pt(x, y), d, "tree"))
    for line in [garden_yard.buffer(3.2).exterior, LineString(L([(118, 150), (116, 124), (124, 100)])), swale_line]:
        for x, y, _ in _along(line, rng.uniform(9, 14)):
            if parcel.buffer(-2).contains(Point(x, y)) and not paths.buffer(1.5).contains(Point(x, y)) \
                    and not garden_yard.buffer(1).contains(Point(x, y)):
                trees.append((x + rng.normal(0, 0.6), y + rng.normal(0, 0.6), rng.uniform(2.0, 3.2), "shrub"))

    # remaining furniture ---------------------------------------------------------------------------------
    for x in (36, 66, 96, 140, 182, 214):
        points.append((*pt(x, 55.4 if x % 2 == 0 else 72.6), "bench"))
    for x in (2, 44, 110, 160):
        points.append((*pt(x, 61.2), "lamp"))
    points += [(*pt(150, 47.5), "bench"), (*pt(212, 108), "bench"), (*pt(270, 118), "bench"), (*pt(264, 134), "bench")]
    points += [(*pt(128, 140), "deadwood"), (*pt(140, 140), "stone_pile"), (*pt(86, 146), "nesting_aid"), (*pt(232, 158), "deadwood")]

    # lines ----------------------------------------------------------------------------------------------------
    lines.append((LineString(parcel.exterior.coords), "site_boundary"))
    inner = parcel.buffer(-1.7).exterior
    lines.append((inner.intersection(box(X0 - 5, Y0 + 96, X0 + 5, Y0 + 176)), "hedge"))
    lines.append((inner.intersection(box(X0 + 305, Y0 + 96, X0 + 316, Y0 + 176)), "hedge"))
    lines.append((_offset(swale_line, -3.0), "kerb"))
    return dict(ground=ground, trees=trees, points=points, lines=lines, places=places, roofs=[pavilion.buffer(-0.8)])


def _zones(poly, rng):
    """Cut a courtyard across its long axis into one to three zones; yields (zone, turn) with turn = (angle, origin)."""
    ang, c = _long_axis(poly)
    local = affinity.rotate(poly, -ang, origin=c)
    minx, miny, maxx, maxy = local.bounds
    n = 1 if poly.area < 1900 else (2 if poly.area < 4300 else 3)
    cuts = np.linspace(minx, maxx, n + 1)
    cuts[1:-1] += rng.uniform(-0.07, 0.07, n - 1) * (maxx - minx)
    for i in range(n):
        zone = local.intersection(box(cuts[i], miny - 1, cuts[i + 1], maxy + 1))
        for part in _polys(zone):
            if part.area > 60:
                yield part


def _court(court, rng):
    """Courtyards: [(element, polygon)], trees [(x, y, crown, element)], points [(x, y, element)], lines [(line, element)].

    Every courtyard is cut across its long axis into zones with their own use: garden with a path, playground,
    paved grid of trees, parking with a tree row, gravel with old trees, wildflower meadow.
    """
    fills, trees, points, lines = [], [], [], []
    weights = {"garden": 3.0, "play": 1.0, "paved": 1.4, "parking": 1.0, "gravel": 0.9, "wild": 1.2}
    kinds, probs = list(weights), np.array(list(weights.values())) / sum(weights.values())
    for poly in _polys(court):
        if poly.area < 120:
            continue
        ang, c = _long_axis(poly)
        back = lambda g: affinity.rotate(g, ang, origin=c)
        put = lambda x, y: tuple(back(Point(x, y)).coords[0])
        used, previous = [], None
        for zone in _zones(poly, rng):
            x0, y0, x1, y1 = zone.bounds
            mid = (y0 + y1) / 2
            kind = str(rng.choice(kinds, p=probs))
            if zone.area < 420 or (y1 - y0) < 13:
                kind = "garden"
            if kind == previous:                                   # neighbouring zones differ
                kind = "garden" if kind != "garden" else "gravel"
            previous = kind
            inner = zone.buffer(-2.6)
            spine = _stripe(LineString([(x0 - 2, mid), (x1 + 2, mid)]), 2.2).intersection(zone)
            zf, zt = [], []                                        # zone fills/trees in the local frame
            if kind == "garden":
                zf += [("waterbound", spine), ("garden", zone)]
                zt += [(x, y, d, "tree") for x, y, d in _scatter(rng, inner.difference(spine.buffer(2.2)),
                                                                   max(2, int(zone.area / 1500)), 8.0, 11.5, [], gap=0.7)]
                for k in (0.3, 0.7):
                    points.append(put(x0 + (x1 - x0) * k, mid + 2.5) + ("bench",))
            elif kind == "play":
                pad = box(x0 + (x1 - x0) / 2 - 12, mid - 8, x0 + (x1 - x0) / 2 + 12, mid + 8).intersection(inner).buffer(-2.0).buffer(2.0)
                zf += [("safety_surface", pad), ("lawn", zone)]
                px0, py0, px1, py1 = pad.bounds
                for k, (fx, fy) in enumerate([(0.2, 0.3), (0.5, 0.7), (0.8, 0.35), (0.35, 0.75), (0.7, 0.5)]):
                    points.append(put(px0 + (px1 - px0) * fx, py0 + (py1 - py0) * fy) + ("play_equipment",))
                points.append(put(px0 - 2.0, mid) + ("bench",))
                lines.append((back(pad.buffer(1.8).exterior), "fence"))
                zt += [(x, y, d, "tree") for x, y, d in _scatter(rng, inner.difference(pad.buffer(5)), 3, 8.0, 10.5, [], gap=0.7)]
            elif kind == "paved":
                zf += [("concrete_pavers", zone)]
                for gx in np.arange(x0 + 6.0, x1 - 3.0, 10.0):
                    for gy in np.arange(y0 + 6.0, y1 - 3.0, 10.0):
                        if inner.contains(Point(gx, gy)):
                            zt.append((gx, gy, float(rng.uniform(5.6, 7.0)), "tree_street"))
                points += [put(x0 + (x1 - x0) * k, mid) + ("bench",) for k in (0.25, 0.75)]
                points += [put(x0 + 2.4, y0 + 2.2) + ("bike_rack",), put(x0 + 4.6, y0 + 2.2) + ("bike_rack",)]
            elif kind == "parking":
                band = zone.intersection(box(x0 - 1, y0 - 1, x1 + 1, y0 + 5.4))
                zf += [("parking", band.buffer(-0.4)), ("garden", zone)]
                for gx in np.arange(x0 + 5.0, x1 - 3.0, 10.5):
                    if zone.buffer(-2.0).contains(Point(gx, y0 + 7.4)):
                        zt.append((gx, y0 + 7.4, float(rng.uniform(5.8, 7.0)), "tree_street"))
                zt += [(x, y, d, "tree") for x, y, d in _scatter(rng, inner.difference(band.buffer(5)), max(1, int(zone.area / 2200)),
                                                                   8.0, 10.5, [], gap=0.7)]
            elif kind == "gravel":
                zf += [("gravel", zone.buffer(-1.2)), ("garden", zone)]
                for gx in np.arange(x0 + 6.0, x1 - 3.0, 10.5):
                    for gy in np.arange(y0 + 6.0, y1 - 3.0, 10.5):
                        if inner.contains(Point(gx, gy)) and rng.random() < 0.8:
                            zt.append((gx + rng.normal(0, 0.6), gy + rng.normal(0, 0.6), float(rng.uniform(7.6, 9.4)), "tree"))
                points += [put(x0 + (x1 - x0) * k, mid) + ("bench",) for k in (0.3, 0.7)]
            else:                                                  # wild
                zf += [("wildflower_meadow", inner.buffer(-1.0).buffer(1.0)), ("meadow", zone.buffer(-1.4))]
                zf += [("lawn", zone)]
                zt += [(x, y, d, "tree") for x, y, d in _scatter(rng, inner, max(1, int(zone.area / 2600)), 8.5, 11.0, [], gap=0.7)]
            fills += [(el, back(g)) for el, g in zf]
            trees += [put(x, y) + (d, el) for x, y, d, el in zt]
            used.append(zone)
        for za, zb in zip(used, used[1:]):                         # a clipped hedge where two uses meet
            for ln in _lines(za.boundary.intersection(zb.boundary)):
                if ln.length > 4:
                    lines.append((back(ln), "hedge_clipped"))
    return fills, trees, points, lines


def _annexes(court, rng, n=(2, 5)):
    """Small sheds, garages and bicycle stores along the edge of a courtyard."""
    out = []
    for poly in _polys(court):
        inner = _polys(poly.buffer(-3.0))
        if poly.area < 500 or not inner:
            continue
        ring = max(inner, key=lambda g: g.area).exterior
        for _ in range(int(rng.integers(*n))):
            t = rng.uniform(0, ring.length)
            a, b = ring.interpolate(t), ring.interpolate((t + 1.0) % ring.length)
            ang = math.degrees(math.atan2(b.y - a.y, b.x - a.x))
            out.append(_rect(a.x, a.y, rng.uniform(5.5, 9.0), rng.uniform(3.0, 4.6), ang))
    return out


def _school(b, rng):
    """A school block: L-shaped building, gym, schoolyard, sports field with running track."""
    main = _union([box(100, 338, 176, 354), box(160, 288, 176, 354)])
    gym = box(112, 298, 148, 322)
    field = box(92, 214, 164, 268)
    track = field.buffer(6.5, join_style="round").difference(field)
    yard = box(92, 274, 158, 336)
    fills = [("building", _union([main, gym])), ("sports_turf", field), ("synthetic_track", track),
             ("paving_light", yard.difference(gym)), ("parking", box(140, 356, 186, 366))]
    trees = [(86, y, rng.uniform(7.5, 9.0), "tree") for y in np.arange(214, 350, 15)]
    trees += [(x, 331, 7.0, "tree_street") for x in (100, 116, 132, 148)]
    return fills, trees


@functools.lru_cache(maxsize=4)
def _build(seed: int):
    rng = np.random.default_rng([seed, 1])              # blocks and courtyards
    rng_street, rng_park = np.random.default_rng([seed, 2]), np.random.default_rng([seed, 3])
    net = {k: dict(s, line=LineString(s["pts"])) for k, s in STREETS.items()}
    canal_line = _curve([(-100, 140), (140, 132), (330, 143), (540, 131), (700, 143), (920, 133)])
    canal = canal_line.buffer(8.0, cap_style="flat")
    promenade = canal_line.buffer(14.0, cap_style="flat").difference(canal)
    water_zone = canal_line.buffer(14.0, cap_style="flat")
    row_all = _union([s["line"].buffer(_half(s), cap_style="flat") for s in net.values()])
    blocks = [g for b in _polys(FRAME.difference(row_all).difference(water_zone)) if b.area > 600
              for g in _polys(b.buffer(-3.5).buffer(3.5))]
    urban = FRAME.difference(_union(blocks)).difference(water_zone)

    def stripe(inner, outer):
        parts = []
        for s in net.values():
            a, b = inner(s), outer(s)
            if b > a:
                parts.append(s["line"].buffer(b, cap_style="flat").difference(s["line"].buffer(a, cap_style="flat")))
        return _union(parts)

    lanes = stripe(lambda s: s["tram"] / 2, lambda s: s["tram"] / 2 + s["lane"])
    tram = _union([s["line"].buffer(s["tram"] / 2, cap_style="flat") for s in net.values() if s["tram"]])
    cycle = stripe(lambda s: s["tram"] / 2 + s["lane"], lambda s: s["tram"] / 2 + s["lane"] + s["cyc"])
    bays = stripe(lambda s: s["tram"] / 2 + s["lane"] + s["cyc"], lambda s: s["tram"] / 2 + s["lane"] + s["cyc"] + s["bay"])
    bridges = _union([s["line"].buffer(_half(s), cap_style="flat") for s in net.values() if s["line"].intersects(canal_line)]
                     ).intersection(canal.buffer(2.0))
    parcel = next(b for b in blocks if b.contains(Point(350, 285)))

    # -- city blocks ------------------------------------------------------------------------------------------
    buildings, annexes, roofs, ctx_trees, ctx_points, ctx_lines = [], [], [], [], [], []
    court_fills: list[tuple[str, object]] = []

    def dress(bs):
        for b in bs:
            r = rng.random()
            if r < 0.30 and b.area > 260:
                roofs.append(("green_roof_extensive", b.buffer(-0.7)))
            elif r < 0.34 and b.area > 260:
                roofs.append(("roof_pv", b.buffer(-0.9)))

    for b in blocks:
        if b is parcel:
            continue
        c = b.centroid
        if 146 < c.y < 176:                                                # riverside lawn strips
            court_fills.append(("lawn", b))
        elif 630 < c.x < 700 and b.area > 3000:                            # slab housing between the trees
            bs = _slabs(b, rng)
            buildings += bs
            dress(bs)
            court_fills.append(("lawn", b))
            for x, y, d in _scatter(rng, b.buffer(-4).difference(_union(bs).buffer(3)), int(b.area / 420), 8.0, 11.0, [], gap=0.6):
                ctx_trees.append((x, y, d, "tree"))
        elif b.contains(Point(132, 290)):                                  # the school
            fills, ts = _school(b, rng)
            for element, geom in fills:
                if element == "building":
                    buildings.append(geom)
                else:
                    court_fills.append((element, geom.intersection(b)))
            ctx_trees += ts
            court_fills.append(("lawn", b))
        else:
            bs, court, hedges = _perimeter(b, rng, depth=float(rng.choice([14.0, 15.0, 16.0])), spacing=(42, 66))
            annexes += _annexes(court, rng)
            buildings += bs
            dress(bs)
            fills, ts, ps, ls = _court(court, rng)
            court_fills += fills
            ctx_trees += ts
            ctx_points += ps
            ctx_lines += ls + [(h, "hedge_clipped") for h in hedges]
            court_fills.append(("lawn", b))

    _street_furniture(net, canal_line, ctx_trees, ctx_points, rng_street, _union([canal.buffer(0.5), lanes]))

    # -- the park ------------------------------------------------------------------------------------------------
    park = _park(rng_park, parcel)
    site = _Ground(parcel)
    for element, geom in park["ground"]:
        site.add(element, geom, "landcover")
    site.add("lawn", parcel, "landcover")

    world = _Ground(FRAME.difference(parcel))
    for element, geom in [("bridge", bridges), ("watercourse", canal), ("building", _union(buildings)),
                          ("building_minor", _union(annexes)),
                          ("green_track", tram), ("road", lanes), ("cycleway", cycle), ("parking", bays),
                          ("paving_light", promenade), ("footway", urban)] + court_fills + [("lawn", FRAME)]:
        world.add(element, geom, "context")

    feats = list(site.feats) + list(world.feats)
    for element, geom in roofs:
        feats.append({"geometry": geom, "element": element, "layer": "context"})
    for geom in park["roofs"]:
        feats.append({"geometry": geom, "element": "green_roof_intensive", "layer": "landcover"})
    for x, y, d, kind in park["trees"]:
        feats.append({"geometry": Point(x, y), "element": kind, "layer": "trees", "crown_diameter": round(float(d), 1)})
    for x, y, kind in park["points"]:
        feats.append({"geometry": Point(x, y), "element": kind, "layer": "trees" if kind in ("deadwood", "stone_pile", "nesting_aid") else "lines"})
    for geom, kind in park["lines"]:
        for part in _lines(geom):
            if part.length > 2:
                feats.append({"geometry": LineString(part.coords), "element": kind, "layer": "lines"})
    solid = _union(buildings + annexes).buffer(1.2)
    prep = shapely.prepared.prep(solid)
    for x, y, d, kind in ctx_trees:
        if not prep.contains(Point(x, y)):
            feats.append({"geometry": Point(x, y), "element": kind, "layer": "context", "crown_diameter": round(float(d), 1)})
    for x, y, kind in ctx_points:
        if not prep.contains(Point(x, y)):
            feats.append({"geometry": Point(x, y), "element": kind, "layer": "context"})
    for geom, kind in ctx_lines:
        for part in _lines(geom):
            if part.length > 2:
                feats.append({"geometry": LineString(part.coords), "element": kind, "layer": "context"})
    places = dict(park["places"], avenue=(392.0, 182.0), canal=(392.0, 139.5), school=(132.0, 290.0),
                  field=(128.0, 241.0), blocks=(470.0, 420.0))
    return feats, places, parcel


def _finish(feats, places, origin):
    """Turn the design by ANGLE, cut the window and move it to ``origin``."""
    cx, cy = CENTRE
    w, h = WINDOW
    window = box(0, 0, w, h).buffer(28, join_style="mitre")
    dx, dy = origin[0] - (cx - w / 2), origin[1] - (cy - h / 2)

    def move(g):
        return affinity.translate(affinity.rotate(g, ANGLE, origin=CENTRE), dx, dy)

    out = []
    win = affinity.translate(window, origin[0], origin[1])
    for f in feats:
        g = move(f["geometry"])
        if g.geom_type in ("Polygon", "MultiPolygon"):
            g = _valid(_valid(g).intersection(win))
            try:   # snap to 1 mm so that shared edges stay shared, then repair
                g = _valid(set_precision(g, 0.001))
            except Exception:
                pass
            parts = [p for p in _polys(g) if p.area > 0.5]
            if not parts:
                continue
            g = parts[0] if len(parts) == 1 else MultiPolygon(parts)
        elif g.geom_type in ("LineString", "MultiLineString"):
            g = g.intersection(win)
            parts = [p for p in _lines(g) if p.length > 1.5]
            if not parts:
                continue
            g = parts[0] if len(parts) == 1 else shapely.MultiLineString(parts)
        elif not win.contains(g):
            continue
        out.append({**f, "geometry": g})
    return out, {k: tuple(np.array(move(Point(*v)).coords[0])) for k, v in places.items()}


def demo_park(seed: int = 6, origin: tuple[float, float] = ORIGIN) -> list[dict]:
    """Features of the demo quarter as dicts: ``{"geometry", "element", "layer", ...}``.

    ``layer`` is ``landcover``, ``trees`` or ``lines`` inside the park, ``context`` around it.
    """
    feats, places, _ = _build(seed)
    return _finish([dict(f) for f in feats], places, origin)[0]


def demo_park_places(seed: int = 6, origin: tuple[float, float] = ORIGIN) -> dict[str, tuple[float, float]]:
    """Named spots of the demo quarter in the coordinates of :func:`demo_park` (pond, plaza, playground ...)."""
    feats, places, _ = _build(seed)
    return _finish([], places, origin)[1]


def demo_park_gdf(seed: int = 6):
    """The demo quarter as a GeoDataFrame (requires geopandas)."""
    import geopandas as gpd

    return gpd.GeoDataFrame(demo_park(seed), geometry="geometry", crs=CRS)

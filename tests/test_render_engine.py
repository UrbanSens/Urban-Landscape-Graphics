"""Properties of the rendering engine that do not depend on the catalog's content."""

import xml.dom.minidom as minidom

import numpy as np
import pytest
from shapely.geometry import Polygon, box

import ulg
from ulg.render import Ctx, Options, build, Feature
from ulg.render import geom as G
from ulg.render import rand as R
from ulg.render.ir import Dots, Group, Paths
from ulg.render.samples import tile_items

CAT = ulg.load()
TEXTURED = [el.id for el in CAT if "polygon" in el.geometry and el.textures]


def test_hash_is_stable_and_uniform():
    a = R.rand(np.arange(1000), np.arange(1000)[::-1], seed=5, salt=2)
    b = R.rand(np.arange(1000), np.arange(1000)[::-1], seed=5, salt=2)
    assert np.array_equal(a, b)
    assert 0.0 <= a.min() and a.max() < 1.0 and 0.45 < a.mean() < 0.55
    assert not np.array_equal(a, R.rand(np.arange(1000), np.arange(1000)[::-1], seed=6, salt=2))
    assert R.stable_seed("lawn", 0) == R.stable_seed("lawn", 0) != R.stable_seed("meadow", 0)


def test_scatter_is_anchored_to_the_ground_not_to_the_polygon():
    ctx = Ctx(u=0.5, lod=2, seed=3)
    big = box(0, 0, 60, 40)
    small = box(10, 10, 30, 25)
    xb, yb, _ = G.scatter(big, ctx, 2.5)
    xs, ys, _ = G.scatter(small, ctx, 2.5)
    inside = (xb > 10) & (xb < 30) & (yb > 10) & (yb < 25)
    assert len(xs) > 20
    got = {(round(x, 6), round(y, 6)) for x, y in zip(xs, ys)}
    assert got == {(round(x, 6), round(y, 6)) for x, y in zip(xb[inside], yb[inside])}


def test_wobble_is_small_and_shared_between_neighbours():
    ctx = Ctx(u=0.5, lod=2, seed=1)
    edge = np.array([[0.0, 0.0], [40.0, 0.0]])
    a = G.wobble(edge, ctx, amp=0.11)
    b = G.wobble(edge[::-1], ctx, amp=0.11)[::-1]
    assert np.allclose(a, b)                      # same edge drawn from either side is identical
    part = G.wobble(np.array([[12.3, 0.0], [31.7, 0.0]]), ctx, amp=0.11)
    inner = part[1:-1]
    assert all(np.isclose(a, q).all(axis=1).any() for q in inner)   # a piece of the edge traces the same line
    dev = np.abs(a[:, 1]).max() / ctx.u            # deviation in paper mm
    assert 0.0 < dev <= 0.11 * 1.01                # never further off than the requested amplitude
    assert np.allclose(G.wobble(edge, Ctx(u=0.5, wobble=0.0), amp=0.11), edge)


def test_rings_are_oriented_for_both_fill_rules():
    poly = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)], [[(2, 2), (4, 2), (4, 4), (2, 4)]])
    shell, hole = G.rings_of(poly)
    assert G._signed_area(shell) > 0 > G._signed_area(hole)


def _vertices(items, out=None):
    """Every vertex and dot centre of a display list, as one (n, 2) array."""
    out = [] if out is None else out
    for it in items:
        if isinstance(it, Group):
            _vertices(it.items, out)
        elif isinstance(it, Dots):
            out.append(np.asarray(it.xy, dtype=float).reshape(-1, 2))
        elif isinstance(it, Paths) and len(it.paths):
            out.append(np.concatenate([np.asarray(q, dtype=float).reshape(-1, 2) for q in it.paths]))
    return out


def _keys(xy, offset):
    """Integer grid keys at 1 micrometre; two offsets make the match immune to rounding at cell borders."""
    q = np.floor(xy / 1e-3 + offset).astype(np.int64)
    return q[:, 0] * 4_000_000_007 + q[:, 1]


def _same_points(a, b):
    if len(a) != len(b):
        return False
    hit = np.isin(_keys(a, 0.0), _keys(b, 0.0)) | np.isin(_keys(a, 0.5), _keys(b, 0.5))
    back = np.isin(_keys(b, 0.0), _keys(a, 0.0)) | np.isin(_keys(b, 0.5), _keys(a, 0.5))
    return bool(hit.all() and back.all())


@pytest.mark.parametrize("eid", TEXTURED)
@pytest.mark.parametrize("lod", [1, 2, 3])
def test_pattern_tiles_are_seamless(eid, lod):
    """Textures are periodic: what is drawn in one tile equals what is drawn one tile further right and up.

    Generated over two tiles in each direction with a wide margin, so the
    comparison is free of edge effects.
    """
    size = 32.0
    parts = _vertices(tile_items(CAT[eid], size, lod, margin=size + 12.0))
    assert parts, "a textured element must produce marks"
    xy = np.concatenate(parts)

    ox, oy = 0.3713, 0.2917   # keep the window edges off the pattern lattices, where rounding decides membership

    def window(dx, dy):
        m = ((xy[:, 0] > dx + ox) & (xy[:, 0] < dx + ox + size)
             & (xy[:, 1] > dy + oy) & (xy[:, 1] < dy + oy + size))
        return xy[m] - [dx, dy]

    base = window(0.0, 0.0)
    assert len(base), "expected marks inside the tile"
    assert _same_points(base, window(size, 0.0)), (eid, lod, "x")
    assert _same_points(base, window(0.0, size)), (eid, lod, "y")


def test_rendering_is_deterministic_and_seeded():
    feats = [Feature(box(0, 0, 40, 30), TEXTURED[0])]
    a = ulg.render_svg(feats, scale=500).tostring()
    b = ulg.render_svg(feats, scale=500).tostring()
    c = ulg.render_svg(feats, scale=500, seed=1).tostring()
    assert a == b and a != c
    minidom.parseString(a)


def test_level_of_detail_follows_scale():
    from ulg.render import lod_for_scale, lod_for_zoom
    assert [lod_for_scale(s) for s in (200, 750, 1000, 2500, 5000, 10000, 25000)] == [3, 3, 2, 2, 1, 1, 0]
    assert lod_for_zoom(19) == 3 and lod_for_zoom(14) == 0
    flat = ulg.render_svg([Feature(box(0, 0, 400, 300), TEXTURED[0])], scale=25000).tostring()
    rich = ulg.render_svg([Feature(box(0, 0, 40, 30), TEXTURED[0])], scale=500).tostring()
    assert len(rich) > 3 * len(flat)


def test_unknown_classes_fall_back_instead_of_failing():
    items = build([Feature(box(0, 0, 10, 10), "no_such_element"), Feature(box(20, 0, 30, 10), None)],
                  CAT, Ctx(u=0.5, lod=2), Options())
    assert [g.element for g in items] == ["unknown", "unknown"]
    assert build([Feature(box(0, 0, 10, 10), "nope")], CAT, Ctx(u=0.5), Options(fallback=None)) == []


def test_matplotlib_backend_draws_same_display_list():
    import matplotlib.pyplot as plt
    feats = [Feature(box(0, 0, 40, 30), TEXTURED[0]), Feature(box(45, 0, 80, 30), "water")]
    ax = ulg.plot(feats, scale=500)
    assert len(ax.patches) + len(ax.collections) >= 4
    w_in, _ = ax.figure.get_size_inches()
    assert w_in * 25.4 == pytest.approx(80 / 0.5, rel=1e-3)   # 80 m at 1:500 is 160 mm
    plt.close(ax.figure)


def test_wobble_stays_within_half_the_outline_width():
    from ulg.render import geom as G

    ctx = G.Ctx(u=2.0, lod=2)
    line = np.array([[0.0, 0.0], [900.0, 340.0], [1200.0, -80.0]])
    dense = G.densify(line, 1.1 * ctx.u, ctx)
    moved = G.wobble(line, ctx, amp=0.09)
    assert moved.shape == dense.shape
    shift_mm = np.hypot(*(moved - dense).T) / ctx.u
    assert shift_mm.max() <= 0.09 + 1e-9          # the ink of a 0.18 mm line always covers the true edge
    assert shift_mm.mean() > 0.02                 # and the line does wobble

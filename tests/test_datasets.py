"""The demo quarter: valid, reproducible, a clean planar partition, drawable at every scale."""

import pytest
from shapely import STRtree
from shapely.geometry import Polygon, box
from shapely.ops import unary_union

import ulg
from ulg.datasets import ORIGIN, WINDOW, demo_park, demo_park_places

ROOFS = {"green_roof_intensive", "green_roof_extensive", "roof_pv"}     # laid over the buildings on purpose


@pytest.fixture(scope="module")
def feats():
    return demo_park()


def polygons(feats, layer):
    return [f for f in feats if f["layer"] == layer and f["geometry"].geom_type in ("Polygon", "MultiPolygon")
            and f["element"] not in ROOFS]


def test_geometries_are_valid_and_known(feats):
    catalog = ulg.load()
    assert len(feats) > 800
    for f in feats:
        assert f["element"] in catalog, f["element"]
        assert f["layer"] in {"landcover", "trees", "lines", "context"}
        assert f["geometry"].is_valid and not f["geometry"].is_empty
        assert f["geometry"].geom_type in {"Point", "LineString", "Polygon", "MultiPolygon"}   # no LinearRing


def test_is_reproducible():
    a, b = demo_park(6), demo_park(6)
    assert [(f["element"], f["geometry"].wkb) for f in a] == [(f["element"], f["geometry"].wkb) for f in b]
    assert [f["geometry"].wkb for f in a] != [f["geometry"].wkb for f in demo_park(7)]


def test_lies_in_the_window(feats):
    minx, miny, maxx, maxy = unary_union([f["geometry"] for f in feats]).bounds
    margin = 28.0 + 1e-6
    assert minx >= ORIGIN[0] - margin and miny >= ORIGIN[1] - margin
    assert maxx <= ORIGIN[0] + WINDOW[0] + margin and maxy <= ORIGIN[1] + WINDOW[1] + margin


@pytest.mark.parametrize("layer", ["landcover", "context"])
def test_ground_does_not_overlap(feats, layer):
    polys = polygons(feats, layer)
    geoms = [f["geometry"] for f in polys]
    tree = STRtree(geoms)
    for i, g in enumerate(geoms):
        for j in tree.query(g):
            if j > i:
                assert g.intersection(geoms[j]).area < 0.5, (polys[i]["element"], polys[j]["element"])


def test_park_has_no_gaps(feats):
    """Every square metre of the park carries a land cover: the union has no hole above the snapping tolerance."""
    union = unary_union([f["geometry"] for f in polygons(feats, "landcover")])
    assert union.geom_type == "Polygon"
    holes = [Polygon(r).area for r in union.interiors]
    assert max(holes, default=0.0) < 1.0
    assert 50_000 < union.area < 60_000


def test_park_sits_in_a_hole_of_the_context(feats):
    context = unary_union([f["geometry"] for f in polygons(feats, "context")])
    park = unary_union([f["geometry"] for f in polygons(feats, "landcover")])
    assert context.intersection(park).area < 5.0


def test_places_are_inside_the_window():
    places = demo_park_places()
    window = box(ORIGIN[0], ORIGIN[1], ORIGIN[0] + WINDOW[0], ORIGIN[1] + WINDOW[1])
    for name in ("pond", "plaza", "meadow", "orchard", "playground", "avenue", "canal", "park"):
        assert window.contains(ulg_point(places[name])), name


def ulg_point(xy):
    from shapely.geometry import Point
    return Point(*xy)


def test_indicators_of_the_park(feats):
    gdf = pytest.importorskip("geopandas").GeoDataFrame(feats, geometry="geometry", crs="EPSG:25832")
    res = ulg.indicators(gdf[gdf.layer.isin(["landcover", "trees"])])
    assert 50_000 < res["plot_area_m2"] < 60_000
    assert res["sealed_share"] < 0.1 and res["nrr_green_share"] > 0.7
    assert 0.5 < res["bff"] < 1.0 and 0.1 < res["canopy_share"] < 0.5


@pytest.mark.parametrize("scale", [6000, 1500, 400])
def test_draws_at_every_level_of_detail(feats, scale):
    x, y = demo_park_places()["pond"]
    svg = ulg.render_svg(feats, scale=scale, extent=(x - 40, y - 25, x + 40, y + 25))
    text = svg.tostring()
    assert text.startswith("<svg") and svg.lod == ulg.lod_for_scale(scale)
    assert len(text) > 20_000

"""Indicators computed from element coefficients."""

import math

import pytest
from shapely.geometry import Point, box

import ulg


def test_berlin_bff_brochure_scenario_a():
    """Brochure example A (SenUVK 2021, p. 19): plot 750 m², BFF 0.04."""
    feats = [
        (box(0, 0, 33, 10), "building"),          # 330 m² built, factor 0
        (box(33, 0, 59.2, 10), "asphalt"),        # 262 m² sealed, factor 0
        (box(59.2, 0, 73.4, 10), "paving_light"),  # 142 m² partly sealed, factor 0.1
        (box(73.4, 0, 75.0, 10), "lawn"),          # 16 m² vegetation, factor 1.0
    ]
    r = ulg.indicators(feats)
    assert r["plot_area_m2"] == pytest.approx(750, abs=0.01)
    assert r["bff"] == pytest.approx(30.2 / 750, abs=1e-3)
    assert round(r["bff"], 2) == 0.04
    assert r["sealed_share"] == pytest.approx(262 / 750, abs=1e-3)
    assert r["built_share"] == pytest.approx(330 / 750, abs=1e-3)


def test_green_roof_counts_on_top_of_building():
    feats = [(box(0, 0, 10, 10), "building"), (box(0, 0, 10, 10), "green_roof_extensive"), (box(10, 0, 20, 10), "lawn")]
    r = ulg.indicators(feats)
    assert r["plot_area_m2"] == pytest.approx(200)
    assert r["bff"] == pytest.approx((100 * 0.5 + 100 * 1.0) / 200)
    # runoff: the roof replaces the building surface
    assert r["runoff_cm"] == pytest.approx((100 * 0.3 + 100 * 0.1) / 200)


def test_canopy_from_points_and_green_share():
    feats = [(box(0, 0, 20, 20), "asphalt"), (Point(10, 10), "tree", {"crown_diameter": 10})]
    r = ulg.indicators(feats)
    assert r["canopy_share"] == pytest.approx(3.1416 * 25 / 400, rel=0.01)
    assert r["nrr_green_share"] == pytest.approx(r["canopy_share"])
    assert r["sealed_share"] == 1.0


def test_unknown_coefficients_are_reported_not_guessed():
    r = ulg.indicators([(box(0, 0, 10, 10), "road"), (box(10, 0, 20, 10), "lawn")])
    assert r["bff_coverage"] == pytest.approx(0.5)
    assert r["runoff_cm_coverage"] == pytest.approx(0.5)


def test_root_protection_zone_din18920():
    zones = ulg.root_protection_zone([(Point(0, 0), "tree", {"crown_diameter": 8})])
    assert zones[0].area == pytest.approx(3.14159 * (4 + 1.5) ** 2, rel=0.01)


def test_flatten_keeps_what_is_drawn_on_top():
    from shapely.geometry import LineString, Point, box

    park = box(0, 0, 100, 100)
    pond = Point(50, 50).buffer(10)
    path = LineString([(0, 20), (100, 20)])
    feats = [(park, "green_space"), (box(1, 1, 99, 99), "lawn"), (pond, "water"),
             (path, "footway", {"width": "3"})]
    flat = ulg.flatten(feats)
    area = {}
    for f in flat:
        area[f.element] = area.get(f.element, 0.0) + f.geometry.area
    caps = math.pi * 1.5 ** 2                              # round ends of the 3 m strip
    assert area["water"] == pytest.approx(pond.area)      # the pond is not hidden under the lawn
    assert area["footway"] == pytest.approx(300 + caps, rel=0.01)  # the centre line became a 3 m strip
    assert area["lawn"] < 98 * 98 - pond.area - 250        # the lawn lost the pond and the path
    assert sum(area.values()) == pytest.approx(100 * 100 + caps, rel=1e-3)  # no overlaps left


def test_centreline_width_sources():
    from shapely.geometry import LineString

    from ulg.render.scene import centreline_area

    cat = ulg.load()
    line = LineString([(0, 0), (100, 0)])

    def strip(w):  # 100 m long with round caps
        return 100 * w + math.pi * (w / 2) ** 2

    assert centreline_area(line, {"width": "6,5 m"}, cat["road"], cat).area == pytest.approx(strip(6.5), rel=0.01)
    assert centreline_area(line, {"lanes": "2"}, cat["road"], cat).area == pytest.approx(strip(6.0), rel=0.01)
    assert centreline_area(line, {"highway": "footway"}, cat["asphalt"], cat).area == pytest.approx(strip(2.0), rel=0.01)

"""Write osm_sample.geojson: a small, invented city block tagged the way OpenStreetMap maps it.

The geometry is made up (no OpenStreetMap data is used), so the file carries no
ODbL obligations. It stacks areas the way OSM does - a park polygon under grass,
a pond and paths - and keeps roads and footways as centre lines, which is what
real extracts look like.

    python examples/data/make_osm_sample.py
"""

from __future__ import annotations

import math
from pathlib import Path

import geopandas as gpd
from shapely import affinity
from shapely.geometry import LineString, Point, Polygon

HERE = Path(__file__).resolve().parent
E0, N0 = 692300.0, 5337100.0  # local origin in ETRS89 / UTM 32N (EPSG:25832), Munich


def blob(cx, cy, rx, ry, rot=0.0, wobble=0.08, n=28, seed=1):
    pts = []
    for k in range(n):
        a = 2 * math.pi * k / n
        f = 1 + wobble * math.sin(3 * a + seed) + 0.5 * wobble * math.cos(5 * a + 2 * seed)
        pts.append((cx + rx * f * math.cos(a), cy + ry * f * math.sin(a)))
    return affinity.rotate(Polygon(pts), rot, origin=(cx, cy))


def rect(x0, y0, x1, y1):
    return Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def curve(*pts, n=12):
    """Smooth polyline through the points (Catmull-Rom)."""
    p = [pts[0], *pts, pts[-1]]
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
    out.append(pts[-1])
    return LineString(out)


def features():
    f = []

    def add(geom, **tags):
        f.append({"geometry": geom, **tags})

    # streets and sidewalks as centre lines
    add(LineString([(-40, -12), (240, -12)]), highway="residential", surface="asphalt", name="Lindenstraße")
    add(LineString([(-12, -40), (-12, 200)]), highway="residential", surface="asphalt", name="Parkweg")
    add(LineString([(-40, 172), (240, 172)]), highway="tertiary", lanes="2", surface="asphalt", name="Am Anger")
    add(LineString([(202, -40), (202, 200)]), highway="residential", surface="asphalt", name="Uferstraße")
    for line in ([(-40, -3.5), (240, -3.5)], [(-3.5, -40), (-3.5, 200)], [(-40, 163.5), (240, 163.5)],
                 [(193.5, -40), (193.5, 200)]):
        add(LineString(line), highway="footway", footway="sidewalk", surface="paving_stones", width="2.5")

    # the park, mapped in layers as in OSM
    park = rect(0, 0, 110, 160)
    add(park, leisure="park", name="Anger-Park")
    add(rect(1, 1, 109, 159), landuse="grass")
    add(blob(22, 128, 18, 24, rot=10, seed=2), landuse="meadow", meadow="wildflower")
    add(blob(70, 47, 21, 12, rot=15, seed=3), natural="water", water="pond")
    add(blob(50, 52, 6, 9, rot=-10, wobble=0.12, seed=5), natural="wetland", wetland="reedbed")
    add(blob(95, 24, 11, 9, seed=4), natural="scrub")
    add(rect(10, 10, 36, 36), leisure="playground")
    add(blob(88, 122, 11, 6, rot=-8, wobble=0.05, seed=6), landuse="flowerbed")
    add(curve((0, 84), (38, 90), (76, 78), (110, 84)), highway="footway", surface="compacted", width="3")
    add(curve((32, 0), (38, 36), (42, 78), (52, 122), (62, 160)), highway="footway", surface="compacted", width="2.5")
    add(LineString([(110, 0), (110, 160)]), barrier="hedge")

    trees = [(8, 60, 12), (10, 150, 11), (30, 152, 9), (100, 150, 13), (104, 100, 10), (6, 104, 8),
             (60, 140, 12), (86, 64, 9), (20, 72, 10), (100, 60, 11), (70, 106, 14), (48, 18, 8)]
    for x, y, d in trees:
        add(Point(x, y), natural="tree", diameter_crown=str(d), leaf_type="broadleaved")
    for y in range(8, 160, 16):
        add(Point(197, y + 4), natural="tree", denotation="avenue", diameter_crown="7")
    for x, y in ((45, 86), (80, 82), (46, 104)):
        add(Point(x, y), amenity="bench")
    add(Point(62, 88), amenity="waste_basket")
    add(Point(40, 40), amenity="bicycle_parking")

    # the residential half
    add(rect(112, 0, 190, 160), landuse="residential")
    add(rect(120, 12, 150, 46), building="apartments", **{"building:levels": "4"})
    add(rect(158, 12, 186, 50), building="apartments", **{"building:levels": "4"})
    add(Polygon([(120, 108), (186, 108), (186, 150), (160, 150), (160, 128), (120, 128)]), building="apartments")
    add(rect(120, 56, 150, 98), leisure="garden", **{"garden:type": "residential"})
    add(rect(158, 60, 186, 98), amenity="parking")
    add(LineString([(172, 98), (172, 104), (202, 104)]), highway="service", width="4")
    return f


def main() -> Path:
    rows = features()
    gdf = gpd.GeoDataFrame(rows, geometry=[r.pop("geometry") for r in rows], crs=25832)
    gdf["geometry"] = gdf.geometry.translate(E0, N0)
    out = HERE / "osm_sample.geojson"
    gdf.to_crs(4326).to_file(out, driver="GeoJSON", COORDINATE_PRECISION=7)
    print(f"{len(gdf)} features -> {out}")
    return out


if __name__ == "__main__":
    main()

"""Prepare the MapLibre example: two datasets as GeoJSON (WGS 84) plus the exported web style.

    python examples/web/build.py
    python -m http.server 8765 --directory examples/web
    # http://localhost:8765            the demo park (a clean site plan)
    # http://localhost:8765/?data=osm  an OpenStreetMap-style block: stacked areas, streets as centre lines
"""

from pathlib import Path

import geopandas as gpd

import ulg
from ulg.datasets import demo_park_gdf
from ulg.export.web import export_web, to_geojson

HERE = Path(__file__).resolve().parent

park = demo_park_gdf()
to_geojson(park, HERE / "park.geojson", columns=["element", "layer", "crown_diameter"])

osm = gpd.read_file(HERE.parent / "data" / "osm_sample.geojson")
osm["element"] = ulg.classify(osm, "osm")
to_geojson(osm, HERE / "osm.geojson")

lat = park.to_crs(4326).geometry.union_all().centroid.y
files = export_web(HERE / "ulg", latitude=lat)
print(f"{len(park)} + {len(osm)} features, {len(files)} style files, centred at latitude {lat:.3f}")

"""From OpenStreetMap tags to a finished plan and its key figures.

The input, examples/data/osm_sample.geojson, is a small invented block tagged the
way OpenStreetMap maps cities: a park polygon under grass, a pond and paths,
streets and sidewalks as centre lines. For real data, fetch an extract with
osmnx and continue at step 2:

    import osmnx
    osm = osmnx.features_from_place("Schwabing, München", tags={"landuse": True, "leisure": True,
                                    "natural": True, "highway": True, "building": True, "amenity": True})

    python examples/osm_workflow.py        # writes into examples/output/
"""

from pathlib import Path

import geopandas as gpd

import ulg
from ulg.render import rasterize

HERE = Path(__file__).resolve().parent
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)

# 1. Read and project to metres (textures, widths and areas need a metric CRS)
osm = gpd.read_file(HERE / "data" / "osm_sample.geojson").to_crs(25832)

# 2. Classify: every row's tags are matched against the OSM crosswalk
osm["element"] = ulg.classify(osm, "osm")
print(osm.element.value_counts().to_string())

# 3. Look at what did not match, and why a row became what it became
missing = osm[osm.element == "unknown"]
print(f"{len(missing)} unclassified features")
tags = {k: v for k, v in osm.iloc[0].drop(["geometry", "element"]).items() if isinstance(v, str)}
print("first row", tags, "->", ulg.explain("osm", **tags)["name"])

# 4. Draw: stacked areas are layered like OSM Carto, streets become strips of their width
ulg.render_svg(osm, scale=1000, path=OUT / "osm_block.svg")
rasterize(OUT / "osm_block.svg", OUT / "osm_block.png", dpi=150)

# 5. Numbers: flatten the stacked areas into a clean partition first
flat = ulg.flatten(osm)
flat.to_file(OUT / "osm_block_flat.gpkg", driver="GPKG")
figures = ulg.indicators(flat)
for key in ("plot_area_m2", "sealed_share", "built_share", "bff", "runoff_cm", "nrr_green_share", "canopy_share"):
    print(f"{key:18s} {figures[key]}")
print("written to", OUT)

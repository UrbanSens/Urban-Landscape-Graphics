"""Site figures from a classified plan: sealing, biotope area factor, runoff, albedo, green space, canopy.

    python examples/indicators.py        # writes into examples/output/
"""

from pathlib import Path

import ulg
from ulg.datasets import demo_park_gdf

OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

gdf = demo_park_gdf()
site = gdf[gdf.layer.isin(["landcover", "trees"])]      # the park is the site; the streets and blocks around it are context

figures = ulg.indicators(site)
labels = {
    "plot_area_m2": "plot area (m²)",
    "sealed_share": "sealed", "partly_share": "partly sealed", "unsealed_share": "unsealed", "built_share": "built",
    "bff": "biotope area factor (Berlin 2021)", "bff_coverage": "  … share of area with a factor",
    "runoff_cm": "mean runoff coefficient Cm", "runoff_cs": "peak runoff coefficient Cs",
    "albedo": "mean albedo", "nrr_green_share": "urban green space (EU NRR)", "canopy_share": "tree canopy",
}
for key, label in labels.items():
    value = figures[key]
    shown = f"{value:,.0f}" if key.endswith("_m2") else (f"{value:.0%}" if key.endswith(("share", "coverage")) else f"{value:.2f}")
    print(f"{label:38s} {shown:>10s}")

print("\nlargest surfaces (m²):")
for eid, area in list(figures["by_element_m2"].items())[:6]:
    print(f"  {ulg.element(eid).name('en'):28s} {area:>10,.0f}")

# DIN 18920 root protection zones (crown drip line + 1.50 m) as polygons, e.g. for a construction plan
trees = gdf[gdf.element.str.startswith("tree") & (gdf.geom_type == "Point")]
zones = ulg.root_protection_zone(trees)
zones.to_file(OUT / "root_protection_zones.gpkg", driver="GPKG")
print(f"\n{len(zones)} root protection zones written to", OUT / "root_protection_zones.gpkg")

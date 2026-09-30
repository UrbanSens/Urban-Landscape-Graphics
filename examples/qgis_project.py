"""Everything QGIS needs: styles for polygons, lines and points plus demo data in one GeoPackage.

    python examples/qgis_project.py      # writes into examples/output/qgis/

Then in QGIS: add the three layers of park.gpkg, and for each layer choose
Layer Properties > Symbology > Style > Load Style… with ulg_polygons.qml,
ulg_lines.qml or ulg_points.qml. The styles switch their level of detail with
the map scale and draw the hand-drawn outline with a geometry generator.
"""

from pathlib import Path

import ulg
from ulg.datasets import demo_park_gdf
from ulg.export.qgis import export_qgis

OUT = Path(__file__).resolve().parent / "output" / "qgis"
OUT.mkdir(parents=True, exist_ok=True)

files = export_qgis(OUT, lod="auto")
for f in files:
    print("style", f.name)

gdf = demo_park_gdf()
package = OUT / "park.gpkg"
for kind, layer in (("Polygon", "polygons"), ("LineString", "lines"), ("Point", "points")):
    part = gdf[gdf.geom_type.isin([kind, "Multi" + kind])]
    part.to_file(package, layer=layer, driver="GPKG")
    print(f"data  {package.name}:{layer} ({len(part)} features)")

# the same styles in the official PlanZV colours, for a Bauleitplan
export_qgis(OUT / "planzv", lod="auto", theme="planzv")
print("themes available:", ", ".join(ulg.themes()))

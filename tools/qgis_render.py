"""Render the demo quarter with the exported QGIS styles (run with the Python that ships with QGIS).

    <qgis python> tools/qgis_render.py <folder with park_*.gpkg and ulg_*.qml> <out.png> [width_px [minx miny maxx maxy]]

Used by tools/build_docs.py; also a smoke test that the .qml files load and render.
"""

import sys

from qgis.core import (QgsApplication, QgsMapRendererCustomPainterJob, QgsMapSettings, QgsRectangle,
                       QgsVectorLayer)
from qgis.PyQt.QtCore import QSize
from qgis.PyQt.QtGui import QColor, QImage, QPainter

folder, target = sys.argv[1], sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS", True)
app = QgsApplication([], False)
app.initQgis()
layers = []
for name, qml in (("polygons", "ulg_polygons.qml"), ("lines", "ulg_lines.qml"), ("points", "ulg_points.qml")):
    vl = QgsVectorLayer(f"{folder}/park_{name}.gpkg", name, "ogr")
    if not vl.isValid():
        raise SystemExit(f"cannot open {name}")
    msg, ok = vl.loadNamedStyle(f"{folder}/{qml}")
    if not ok:
        raise SystemExit(f"style {qml} did not load: {msg}")
    layers.append(vl)
if len(sys.argv) >= 8:
    ext = QgsRectangle(*(float(v) for v in sys.argv[4:8]))
else:
    ext = QgsRectangle(layers[0].extent())
    ext.scale(1.01)
ms = QgsMapSettings()
ms.setLayers(list(reversed(layers)))
ms.setDestinationCrs(layers[0].crs())
height = int(width * ext.height() / ext.width())
ms.setOutputSize(QSize(width, height))
ms.setOutputDpi(96 * width / (ext.width() / 1.0 / 25.4 * 96 / 1.0) * 0 + 150)
ms.setExtent(ext)
ms.setBackgroundColor(QColor("#F5F5F1"))
img = QImage(ms.outputSize(), QImage.Format_ARGB32_Premultiplied)
img.fill(QColor("#F5F5F1"))
painter = QPainter(img)
job = QgsMapRendererCustomPainterJob(ms, painter)
job.start()
job.waitForFinished()
painter.end()
img.save(target)
errors = [e.message for e in job.errors()]
print(f"QGIS rendered {target} at 1:{round(ms.scale())}" + (f" with errors {errors}" if errors else ""))
app.exitQgis()

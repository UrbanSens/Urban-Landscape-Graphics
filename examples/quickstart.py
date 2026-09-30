"""Five minutes with ulg: look up the style, draw a site plan, add a legend, switch the theme.

    python examples/quickstart.py        # writes into examples/output/
"""

from pathlib import Path

import ulg
from ulg.datasets import demo_park_gdf
from ulg.legend import used_elements
from ulg.render import rasterize

OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

# 1. The style is data: look things up instead of choosing colours by eye
lawn = ulg.element("lawn")
print(lawn.name("en"), "/", lawn.name("de"), lawn.fill)            # Lawn / Rasen #CDD2A9
print([el.id for el in ulg.find("Schotterrasen")])                 # ['gravel_turf', ...]
print(ulg.color("water.300"), ulg.ramp("heat", 5))

# 2. A classified site plan: a GeoDataFrame in metres with an "element" column
gdf = demo_park_gdf()                                               # EPSG:25832
print(len(gdf), "features, e.g.", sorted(gdf.element.unique())[:6])

# 3. Draw it at 1:1500 (SVG in paper millimetres) and rasterise a PNG
ulg.render_svg(gdf, scale=1500, path=OUT / "park_1500.svg")
rasterize(OUT / "park_1500.svg", OUT / "park_1500.png", dpi=110)

# 4. A German legend with exactly the elements on the map
legend = used_elements(zip(gdf.geometry, gdf.element))
ulg.legend_svg(legend, lang="de", title="Legende", columns=4, background="#F5F5F1").save(OUT / "legend_de.svg")

# 5. The same plan in the colours of a Bauleitplan (PlanZV) and as a black-and-white drawing
ulg.render_svg(gdf, scale=1500, theme="planzv", path=OUT / "park_planzv.svg")
ulg.render_svg(gdf, scale=1500, theme="mono", path=OUT / "park_mono.svg")

# 6. Matplotlib, for notebooks and figures
try:
    ax = ulg.plot(gdf, scale=3000)
    ax.figure.savefig(OUT / "park_plot.png", dpi=150)
except ImportError:
    print("Matplotlib is not installed: skipped the plot")

print("written to", OUT)

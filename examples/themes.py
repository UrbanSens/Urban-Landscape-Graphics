"""One plan, seven conventions: the demo quarter in every theme.

    python examples/themes.py            # writes into examples/output/themes/
"""

from pathlib import Path

import ulg
from ulg.datasets import demo_park_gdf

OUT = Path(__file__).resolve().parent / "output" / "themes"
OUT.mkdir(parents=True, exist_ok=True)

gdf = demo_park_gdf()
for name, title in ulg.themes().items():
    ulg.render_svg(gdf, scale=2500, theme=name, title=title, path=OUT / f"park_{name}.svg")
    print(f"{name:8s} {title}")
print("written to", OUT)

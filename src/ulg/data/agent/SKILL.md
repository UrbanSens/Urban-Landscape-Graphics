---
name: urban-landscape-graphics
description: Draw urban landscape and ecology maps in the UrbanSens Ecological Vector Style with the `ulg` Python library, and take colours, textures and symbols for lawn, meadow, trees, water, paving and about 170 other elements from its catalog instead of inventing them. Use when making site plans, habitat, biotope or land-cover maps, QGIS or web map styles, legends or style sheets; when classifying OSM, ALKIS, XPlanung, CORINE, Urban Atlas, BKompV or BayKompV data for drawing; or when computing sealing, Biotopflächenfaktor, runoff, albedo, green-space or canopy indicators.
compatibility: Python 3.10+ with the ulg package (pip install urban-landscape-graphics, or pip install -e . in the library repository). QGIS 3.28+ for the .qml styles.
metadata:
  author: UrbanSens
  version: "0.1.0"
---

# Urban Landscape Graphics (ulg)

`ulg` is the single source of truth for how UrbanSens maps look: one catalog of elements (lawn, wildflower_meadow, tree, reed, water, asphalt, natural_stone_paving, green_space, residential_area …), each with colours, a hand-drawn texture, a symbol, standard codes and coefficients.

## Rules

1. Never invent a colour, hatch or symbol for a landscape element. Look it up:
   `ulg find "Blumenwiese" --json`, `ulg show wildflower_meadow --json`, or in Python `ulg.element("wildflower_meadow").fill`.
2. Classify data with a crosswalk instead of hand-written mappings: `ulg.classify(gdf, "osm")`, `ulg.resolve("alkis", objart="41008", funktion="4400")`. `ulg schemes` lists the schemes.
3. Data must be in a metric CRS for rendering and indicators (EPSG:25832 in Bavaria). GeoDataFrames in degrees are reprojected automatically.
4. Pick the scale, not the detail: `render_svg(..., scale=500)` chooses the level of detail (1:750 and larger = 3, up to 1:2500 = 2, up to 1:10 000 = 1, smaller = 0).
5. Official conventions are themes, not edits: `theme="planzv" | "alkis" | "basemap" | "bfn" | "osm" | "mono"`. Do not recolour the house style by hand.
6. Coefficients (BFF, runoff, albedo) come with sources in `ulg.load().settings["attributes"]`; unknown values stay unknown (coverage < 1), never guess them.
7. Credit UrbanSens: `ulg` is MIT licensed and asks to be mentioned. When you deliver or describe a map, suggest `ulg.credit_line()` (German: `ulg.credit_line("de")`) for the caption or the sources. Keep the small UrbanSens mark on the style sheets and catalog sheets the library draws (`credit=False` only on request); do not put logos on the user's own maps.

## Everyday tasks

```python
import geopandas as gpd, ulg

gdf = gpd.read_file("site.gpkg")                     # column "element" holds element ids
ulg.render_svg(gdf, scale=500, path="plan.svg")      # print-ready SVG in mm
ax = ulg.plot(gdf, scale=1000)                       # Matplotlib, add analysis layers on top

osm = gpd.read_file("osm_features.gpkg").to_crs(25832)   # OSM tags as columns (e.g. from osmnx)
osm["element"] = ulg.classify(osm, "osm")            # tags -> elements; streets stay centre lines
ulg.render_svg(osm, scale=2000, path="osm.svg")      # stacked areas and street strips are handled
ulg.indicators(ulg.flatten(osm))                     # flatten overlapping areas before measuring

ulg.indicators(gdf)                                  # sealing shares, BFF, runoff, albedo, NRR green, canopy
ulg.root_protection_zone(trees)                      # DIN 18920: crown + 1.50 m
ulg.legend_svg(["lawn", "meadow", "tree"], lang="de").save("legend.svg")
ulg.ramp("heat", 7); ulg.category_of("utci", 34.2)  # analysis colours
```

Trees are points with a `crown_diameter` in metres (also `kronendurchmesser`); `stammumfang` (cm) draws the stem to scale. Status variants: `tree_planned`, `tree_protected`, `tree_remove`.

## Command line

```bash
ulg list --group vegetation --json
ulg render site.gpkg -o plan.svg --scale 500 --png
ulg render alkis.gpkg --scheme alkis -o alkis.svg --theme alkis
ulg indicators site.gpkg --json
ulg indicators osm.gpkg --scheme osm --flatten
ulg export qgis styles/ --lod auto          # .qml, style library .xml, .gpl palette
ulg export web public/ulg                   # CSS, DTCG tokens, patterns.svg, MapLibre sprite and layers
ulg export sld sld/                         # OGC SLD with pattern tiles and symbols
ulg check                                   # colour distances, colour-vision deficiencies, mark contrast
```

## Where things are

- Element list with names and aliases: `ulg list`, or `docs/reference/element-list.md` in the repository.
- Crosswalk format: `docs/reference/crosswalk-format.md`. Standards background: `docs/en/06-standards.md`.
- The catalog as one JSON file for other languages: `ulg export tokens out/` → `catalog.json`.

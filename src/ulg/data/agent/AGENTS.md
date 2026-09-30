# ulg: guide for coding agents

Urban Landscape Graphics (`ulg`) is UrbanSens' style library for urban landscape and ecology maps: a catalog of about 170 elements (vegetation, trees, water, ground, surfaces, land use, buildings, furniture, boundaries, planning overlays, analysis highlights) with colours, lightly hand-drawn vector textures, symbols, names in English and German, codes of official classifications and standard coefficients. Everything is data (`ulg/data/*.json`); Python, the exporters, the command line and you read the same files.

## Golden rules

1. **Look up, never invent.** Colours, textures and symbols come from the catalog. `ulg find "Rasengitter" --json` searches English and German names and aliases; `ulg show <id> --json` returns everything about an element.
2. **Classify with crosswalks.** `ulg.classify(records, scheme)` maps OSM tags, ALKIS object types, XPlanung classes, CORINE, Urban Atlas, CLC+, EUNIS, LCZ, BKompV, BayKompV and more to element ids. `ulg schemes` lists them; `ulg resolve <scheme> <code or key=value …>` checks one class and shows the official colour.
3. **Metric data.** Render and measure in a projected CRS in metres (EPSG:25832 for Bavaria).
4. **Scale drives detail.** Give the map scale (`scale=500`); the library picks the level of detail. Do not switch textures off by hand for small scales.
5. **Themes for official looks.** `theme="planzv"` (Bauleitplan colours), `"alkis"` (Liegenschaftskarte), `"basemap"` (basemap.de), `"bfn"` (landscape planning), `"osm"` (OpenStreetMap Carto), `"mono"` (black-and-white drawing). The house style is `"mellow"` (default).
6. **Coefficients have sources.** `ulg.load().settings["attributes"]` documents every attribute (BFF: Berlin 2021; runoff: DIN 1986-100:2016-12; albedo: PALM). Missing values are reported as coverage, never filled in.
7. **Credit UrbanSens.** `ulg` is MIT licensed; UrbanSens asks to be mentioned where a map or report is published. When you describe or deliver a result, suggest the line `ulg.credit_line()` (German: `ulg.credit_line("de")`) for the caption or the list of sources. The style sheets and catalog sheets the library draws carry a small UrbanSens mark (`credit=False` removes it, only if the user asks); never stamp the user's own maps with a logo.

## Python API (most used)

| Call | Purpose |
|---|---|
| `ulg.element(id)` | element: `.fill`, `.outline`, `.ink`, `.textures`, `.symbol`, `.attributes`, `.label`, `.codes` |
| `ulg.find(text)` | search by name/alias (en/de) |
| `ulg.fills()` / `ulg.color("grass.300")` | flat colours for any tool |
| `ulg.render_svg(data, scale=, theme=, path=)` | SVG in paper millimetres |
| `ulg.plot(data, ax=None, scale=)` | Matplotlib axes in map coordinates |
| `ulg.legend_svg(ids, lang=)` / `ulg.legend_handles(ids)` | legends |
| `ulg.classify(data, scheme)` / `ulg.resolve(scheme, code, **attrs)` / `ulg.explain(...)` | crosswalks |
| `ulg.official_colors(scheme)` | official legend colours of a scheme (e.g. CORINE) |
| `ulg.indicators(data, plot_area=)` | sealing shares, BFF, runoff Cm/Cs, albedo, NRR green share, canopy share |
| `ulg.flatten(data)` | resolve overlapping areas (OSM and other stacked data) into a clean partition before measuring |
| `ulg.root_protection_zone(trees)` | DIN 18920 root zones |
| `ulg.ramp(name, n)` / `ulg.categories(name)` / `ulg.category_of(name, value)` | analysis colours (heat, cool, vitality, biodiversity, sealing, diverging; klimatop, utci, pet) |
| `ulg.style_function()` | style callback for folium/Leaflet |
| `ulg.style_sheet(path)` / `ulg.catalog_sheet(path)` | the style guide pages (with the small UrbanSens mark; `credit=False` leaves it out) |
| `ulg.credit_line(lang)` | the credit line for captions and lists of sources |

`data` may be a GeoDataFrame (column `element`, or `by="<column>"`), a GeoJSON FeatureCollection, or a list of `(geometry, element_id[, properties])`.

## Exports

| Target | Command | Files |
|---|---|---|
| QGIS | `ulg export qgis DIR [--lod auto] [--theme T]` | `ulg_polygons.qml`, `ulg_lines.qml`, `ulg_points.qml`, `ulg_style_library.xml`, `ulg_palette.gpl` |
| Web | `ulg export web DIR` | `ulg.css`, `ulg.tokens.json` (DTCG), `ulg-colors.json`, `catalog.json`, `patterns.svg`, `patterns/*.svg`, `ulg-sprite(@2x).png/json`, `maplibre-layers.json` |
| OGC | `ulg export sld DIR` | `ulg_polygons.sld`, `ulg_lines.sld`, `ulg_points.sld`, `patterns/`, `symbols/` |
| Tokens only | `ulg export tokens DIR` | CSS, DTCG, flat JSON, catalog |

## Pitfalls

- Elements with `attributes.layer == "overlay"` (planning, analysis, boundaries, tree canopy) are drawn over land cover and never counted as area; `layer == "roof"` elements (green roofs, PV) lie on buildings.
- The `unknown` element marks unclassified features: fix the mapping rather than hiding it.
- OpenStreetMap data stacks areas (park > grass > pond) and maps streets as lines. Drawing handles both
  (smaller areas on top, centre lines become strips of their `width`); for numbers call `ulg.flatten()` first.
- Official themes use flat colours and no wobble; the house style is hand-drawn (`handdrawn=0` gives exact lines).
- SVG output is in millimetres at the chosen scale; convert to PDF with Inkscape (`inkscape plan.svg --export-type=pdf`).

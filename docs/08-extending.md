# 8 · Extending the style

*How the style guide grows: adding elements, colours, textures, themes and crosswalks, checking them,
and releasing a new version that every map, app and agent picks up.*

## 8.1 Where things live

```text
src/ulg/
  data/
    palette.json            colour tokens (family.step)
    settings.json           line weights, LOD breaks, ramps, class palettes, attribute docs, centre-line widths
    elements/*.json         the catalog, one file per theme group, keyed by element id
    themes/*.json           official conventions (planzv, alkis, basemap, bfn, osm, mono)
    crosswalks/*.json       26 external classifications -> element ids
    agent/                  SKILL.md, AGENTS.md, AGENTS.snippet.md for coding agents
  catalog.py                loading, palette resolution, themes
  crosswalk.py              resolve / classify / explain
  render/                   renderer: geometry, texture motifs, scene, SVG and Matplotlib backends
  export/                   QGIS, SLD, web (MapLibre), design tokens
  analysis.py               indicators, flatten, root protection zones
  check.py                  legibility report
  legend.py, sheet.py       legends and style sheets
tools/                      build_docs.py, build_html.py, build_logo.py, build_reference.py, format_data.py, qgis_render.py
  html/                     style sheet, script and font of the HTML documentation
tests/                      pytest suite
docs/                       this documentation; docs/reference and docs/html are generated
examples/                   runnable examples and the MapLibre page
```

**Data first.** Almost every change is a change to a JSON file. Python code changes only when the
style needs a new kind of mark (a motif or a pictogram) or a new capability.

## 8.2 Add an element

1. **Check that it is missing.** `ulg find "<German and English names>"`. Many "new" things are aliases of
   an existing element – then add the alias instead.
2. **Pick the group and file.** Vegetation in `10_…`/`20_…`, trees in `30_trees.json`, water, ground,
   surfaces, land use, built, points, lines, overlays in their files.
3. **Write the entry** with palette tokens only:

```json
"wood_pasture": {
  "group": "vegetation.woody",
  "geometry": ["polygon"],
  "z": 20,
  "label":       {"en": "Wood pasture", "de": "Hutewald / Weide mit Bäumen"},
  "description": {"en": "Grazed grassland with scattered old trees. Very high biodiversity.",
                  "de": "Beweidetes Grünland mit locker stehenden alten Bäumen. Sehr hohe Biodiversität."},
  "fill": "fallow.200",
  "textures": [
    {"motif": "grass_tufts", "ink": "fallow.700", "ink2": "grass.700", "keep": 0.45},
    {"motif": "canopy", "ink": "leaf.800", "tones": ["leaf.400", "leaf.500", "leaf.300"],
     "crown_m": 12.0, "pack": 3.4, "keep": 0.7}
  ],
  "attributes": {"sealing": "unsealed", "bff": 1.0, "runoff_cm": 0.1, "nrr_urban_green": true, "layer": "ground"},
  "aliases": ["Hutewald", "Hutung", "Waldweide", "wood pasture", "wooded pasture"]
}
```

4. **Choose `z` by band** ([style guide 2.7](02-style.md#27-drawing-order)): 20 for anything that covers
   the ground (including complexes), 30–33 for water and what lies on it, 50–66 for hedges and built
   structures, 66–76 for trees and points, 84–98 for overlays.
5. **Attributes only with a source.** Use the keys documented in `settings.json → attributes`; leave a
   coefficient out rather than estimate it. A new attribute needs its own entry there
   (`meaning`, `source`, `evidence`).
6. **Aliases in both languages**, including the terms of the standards that name this thing
   (ALKIS, BKompV, OSM) – search and agents rely on them.
7. **Connect it**: point the crosswalk entries that describe it to the new id (8.6).
8. **Check and regenerate** (8.8).

## 8.3 Add or change a colour

Colours live only in `palette.json`. Stay in the tonal range of the family: light steps (100–400) for
fills, darker steps (500–900) for marks. `ulg check` shows whether a change brings two land covers
closer than ΔE₀₀ 10 without a texture difference, also for simulated colour-vision deficiencies.
Changing a token changes every element, theme export and sheet that uses it – that is the point, but
note it in the changelog.

## 8.4 Add a texture motif

A motif is a function in `src/ulg/render/motifs.py`:

```python
def my_motif(region, p, ctx: Ctx) -> list:
    """What it draws, in one line."""
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 31), keep=p["keep"])
    ...
    return [Paths(...), Dots(...)]
```

- `region` is the polygon, `p` the parameters merged from `DEFAULTS[motif]` (per LOD) and the
  element's texture entry, `ctx` carries the scale (`ctx.u` metres per paper mm), the LOD and the
  hand-drawn factor.
- Place marks with the ground-anchored helpers (`G.scatter`, `_span_lines`, the `R` streams), never
  with an unseeded random generator: that keeps patterns continuous across neighbouring polygons,
  reproducible, and seamless when drawn into tiles (`ctx.period`).
- Sizes are in paper millimetres; convert with `ctx.u`.
- Register it in `MOTIFS` and give it `DEFAULTS` for LOD 1–3. `tests/test_render_engine.py` checks
  that tiles repeat without seams.

## 8.5 Add a pictogram or a theme

**Pictograms** are small vector drawings in `PICTOGRAMS` (`src/ulg/render/scene.py`): a list of parts
`(kind, coordinates, fill role, stroke role, width)`, coordinates in units of the symbol radius, roles
`fill`, `ink`, `paper`, `accent` taken from the element's `symbol`.

**Themes** are JSON files in `src/ulg/data/themes/`:

| Key | Meaning |
|---|---|
| `title`, `description`, `source`, `evidence` | what the convention is and where the values come from |
| `handdrawn` | outline wobble for this theme (0 = exact lines) |
| `textures` | `"none"` (flat fills; overlays keep their hatches) or `"mono"` (every mark in ink) |
| `background`, `ink`, `paper` | page colours |
| `default`, `groups`, `elements` | fill/outline overrides, from general to specific; each with an `evidence` note |

A new theme appears in `ulg.themes()`, the CLI `--theme` options and all exporters automatically.

## 8.6 Add or extend a crosswalk

One file per scheme in `src/ulg/data/crosswalks/`; the format is in
[reference/crosswalk-format.md](reference/crosswalk-format.md). Essentials:

- metadata: `title`, `publisher`, `version`, `source`, `license_note`, `key`, `fields` (column aliases),
  optional `hierarchy`, `suffixes`, `fallback_pattern`;
- one entry per class with `code` or `match`, `name`, `element` (or `null`), `fit`, and `color` only
  if the scheme's own legend colour was verified;
- the most specific match wins, then file order.

`python -m pytest tests/test_crosswalks.py` validates every file. Add spot checks for the lookups your
project relies on.

## 8.7 Tools

| Command | Does |
|---|---|
| `python tools/format_data.py` | normalises the layout of all JSON data files (`--check` only reports) |
| `python tools/build_reference.py` | regenerates `docs/reference/*.md` from the data and docstrings |
| `python tools/build_docs.py [names]` | regenerates the images in `docs/img/` (sheets, textures, maps, QGIS renders, the banners of the HTML pages) |
| `python tools/build_logo.py` | redraws the logo, its variants and the favicons in `docs/img/logo/` from the catalog |
| `python tools/build_html.py` | builds `docs/html/`: the multi-page site and the single file `ulg-documentation.html` (banner, serif text, numbered figures, quotations with their source); checks every link |
| `python -m pytest` | the test suite (`-m "not slow"` skips sprite rasterisation) |
| `ulg check` | the legibility report |

## 8.8 Checklist for every change

```bash
python tools/format_data.py
```

```bash
ulg check
```

```bash
python -m pytest
```

```bash
python tools/build_reference.py
```

```bash
python tools/build_docs.py sheets
```

```bash
python tools/build_html.py
```

Then look at the regenerated sheets – the style is visual, and the sheets are its review copy.

## 8.9 Versions and the living style guide

The style is versioned with the package (`pyproject.toml`, `ulg.__version__` and `palette.json →
version` move together) and every release is described in [`CHANGELOG.md`](../CHANGELOG.md):

| Change | Version step |
|---|---|
| an element id removed or renamed, or its meaning changed | major |
| new elements, themes, crosswalks, motifs; visible colour or texture changes | minor |
| fixes that do not change how existing maps look | patch |

Proposals for the style work best as a picture: a crop of the sheet or a map with the problem, the
element ids involved, and – for anything official – the source. Apps pick up a release through
`ulg export tokens` / `ulg export web`; QGIS projects by reloading the exported QML files; agents
through the installed skill, which reads the installed package.

## 8.10 Publishing

Two GitHub workflows in `.github/workflows/` run on every push to `main`:

| Workflow | Does |
|---|---|
| `ci.yml` (Tests) | installs the package on Python 3.10, 3.12 and 3.13, checks the data layout, runs `ulg check` and the test suite |
| `pages.yml` (Documentation) | builds the site and the single file with `python tools/build_html.py --out _site` (it fails on a broken link), exports and copies the MapLibre demo, and publishes everything with GitHub Pages at <https://urbansens.github.io/Urban-Landscape-Graphics/> |

Generated files are not committed: `docs/html/`, `examples/output/` and the exported web style in
`examples/web/ulg/` are rebuilt by the workflows or by the commands in 8.7. What *is* committed are the
images in `docs/img/` (sheets, maps, banners, logos), because they are the review copy of the style –
regenerate them with `python tools/build_docs.py` and `python tools/build_logo.py` before committing a
change that alters how the style looks. The GitHub social preview (1280 × 640 px, set by hand under
Settings > General) is `docs/img/social-preview.png`, made by `python tools/build_docs.py social`.

---

Back to the [overview](index.md)

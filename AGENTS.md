# Working on Urban Landscape Graphics (`ulg`)

Guidance for coding agents and contributors changing this repository. (Agents that only *use* the
library in another project get `ulg agent install` – see `docs/07-agents.md`.)

## What this is

A style library: the UrbanSens Ecological Vector Style as data (`src/ulg/data/`) plus a renderer,
exporters, crosswalks to external classifications and indicators. The documentation starts at
`docs/index.md`; the rules of the style are in `docs/02-style.md`.

## Commands

```bash
pip install -e ".[dev]"                 # editable install with test dependencies
python -m pytest                          # all tests; -m "not slow" skips sprite rasterising and the HTML docs build
ulg check                                 # legibility report, must end with OK
python tools/format_data.py               # normalise JSON layout after editing data files
python tools/build_reference.py           # regenerate docs/reference/*.md
python tools/build_docs.py [names]        # regenerate docs/img/* (sheets, maps, QGIS renders)
python tools/build_html.py                # regenerate docs/html (site and single file); fails on broken links
python tools/build_logo.py                # redraw the logo and favicons (docs/img/logo) from the catalog
python tools/format_data.py --check       # what CI runs first; then `ulg check` and `python -m pytest`
```

Without an install, prefix commands with `PYTHONPATH=src`.

## Rules

1. **Data first.** Elements, colours, themes and crosswalks are JSON in `src/ulg/data/`. Change code
   only for new kinds of marks (motifs, pictograms) or new capabilities.
2. **Palette tokens only.** Element and texture colours are `family.step` tokens from `palette.json`;
   never hex values in element files. Themes may use hex values, each with an `evidence` note.
3. **Every value has a source.** Coefficients, official colours and codes carry their source and an
   evidence mark (V, V\*, S, R as in `docs/research/`). Never estimate a coefficient; leave it out.
4. **GIS-exact.** Geometry is never altered for looks: the outline wobble is bounded by half the line
   width, textures are clipped to their polygon, marks are anchored to ground coordinates (use the
   helpers in `render/geom.py` and `render/rand.py`, never an unseeded random generator).
5. **Drawing order is by band** (`docs/02-style.md` §2.7): ground 20 (largest first), water 30–33,
   lines and centre-line strips 35, built 50–66, trees and points 66–76, overlays 84–98.
6. **Bilingual.** Labels, descriptions and aliases in English and German.
7. **After changing data or docs:** format, `ulg check`, tests, regenerate reference pages, the sheets and the
   HTML (`tools/build_html.py`), and look at the sheets. Add a CHANGELOG entry.
8. **Do not bundle third-party symbol files** (BfN, UKHab, OSM Carto icons); draw own symbols after the
   same conventions. Hotlink, do not copy, historical images in the docs.

## Layout

| Path | Content |
|---|---|
| `src/ulg/data/elements/*.json` | the catalog, keyed by element id |
| `src/ulg/data/crosswalks/*.json` | 26 schemes, format in `docs/reference/crosswalk-format.md` |
| `src/ulg/data/themes/*.json` | official conventions |
| `src/ulg/render/` | geometry helpers, motifs, scene building, SVG and Matplotlib backends |
| `src/ulg/export/` | QGIS, SLD, MapLibre, tokens |
| `src/ulg/analysis.py` | `indicators`, `flatten`, `root_protection_zone` |
| `docs/research/` | the standards research and the synthesis report |
| `examples/` | runnable examples; `examples/output/` is generated and ignored |
| `tools/html/` | style sheet, script and the bundled Rethink Sans (SIL OFL) of the HTML documentation |
| `.github/workflows/` | `ci.yml` (tests) and `pages.yml` (documentation site and live demo on GitHub Pages) |

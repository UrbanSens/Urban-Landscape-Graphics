<!-- github-only:start -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/logo/ulg-logo-on-dark.png">
  <img src="docs/img/logo/ulg-logo.png" alt="ulg – Urban Landscape Graphics, the UrbanSens Ecological Vector Style" width="520">
</picture>

<br>

### [Documentation](https://urbansens.github.io/Urban-Landscape-Graphics/) · [Live demo map](https://urbansens.github.io/Urban-Landscape-Graphics/demo/) · [Changelog](CHANGELOG.md)

[History](https://urbansens.github.io/Urban-Landscape-Graphics/01-origins.html) ·
[Style guide](https://urbansens.github.io/Urban-Landscape-Graphics/02-style.html) ·
[Catalog](https://urbansens.github.io/Urban-Landscape-Graphics/03-catalog.html) ·
[Python](https://urbansens.github.io/Urban-Landscape-Graphics/04-python.html) ·
[GIS and web](https://urbansens.github.io/Urban-Landscape-Graphics/05-gis-and-web.html) ·
[Standards](https://urbansens.github.io/Urban-Landscape-Graphics/06-standards.html)

[![Tests](https://github.com/UrbanSens/Urban-Landscape-Graphics/actions/workflows/ci.yml/badge.svg)](https://github.com/UrbanSens/Urban-Landscape-Graphics/actions/workflows/ci.yml)
[![Documentation](https://github.com/UrbanSens/Urban-Landscape-Graphics/actions/workflows/pages.yml/badge.svg)](https://urbansens.github.io/Urban-Landscape-Graphics/)

</div>
<!-- github-only:end -->

**The UrbanSens Ecological Vector Style as a library.** One catalog of colours, lightly hand-drawn
textures and symbols for urban landscape maps – lawns and meadows, trees, water, pavings, land use,
planning status – tied to German and European standards, with renderers for Python and exporters for
QGIS, GeoServer, MapLibre and design tools.

![Angerpark, the demo quarter, drawn in the house style at 1:1500](docs/img/hero.png)

```python
import ulg

ulg.element("wildflower_meadow").fill        # '#DADDBC' – look colours up, never invent them
ulg.resolve("osm", landuse="meadow", meadow="wildflower")    # 'wildflower_meadow'
ulg.resolve("alkis", objart="41008", funktion="4420")         # 'green_space'

gdf["element"] = ulg.classify(gdf, "osm")     # OSM, ALKIS, XPlanung, CORINE … → elements
ulg.render_svg(gdf, scale=500, path="plan.svg")         # print-ready SVG, true to scale
ulg.render_svg(gdf, scale=1500, theme="planzv")         # the same data as a Bauleitplan
ulg.indicators(ulg.flatten(gdf))              # sealing, biotope area factor, runoff, canopy
```

## What it is

- **173 elements** in English and German – vegetation, trees, water, ground, 33 surfaces, land use,
  buildings, furniture, boundaries, planning and analysis overlays – each with a fill, a texture per
  level of detail, a line or point symbol, aliases and documented coefficients.
- **A style that stays GIS-exact.** Marks are placed on the ground, not on the feature, so patterns
  continue across polygons and tile seamlessly; the hand-drawn outline never moves more than half a
  line width off the true edge.
- **26 crosswalks** from OSM tags, ALKIS/NAK, XPlanung, PlanZV, basemap.de, LBM-DE, BKompV, BayKompV,
  FFH, the Berlin biotope map, DIN 276, CORINE, Urban Atlas, CLC+, EUNIS, HILUCS, LUCAS, ESA WorldCover,
  LCZ, and the Dutch, Swiss, Austrian and English national models – 3 926 classes, each with a fit grade.
- **Seven themes**: the mellow house style plus PlanZV, ALKIS, basemap.de, BfN landscape planning,
  OpenStreetMap Carto and a black-and-white drawing, with the published colour values.
- **Standards built in**: ISO 11091 and PlanZV status symbols for trees, DIN 18920 root protection
  zones, Berlin BFF, DIN 1986-100 runoff, the EU Nature Restoration Regulation's urban green space,
  WCAG-checked legibility including colour-vision deficiencies.
- **Everywhere**: SVG and Matplotlib; QGIS (QML with the hand-drawn outline and scale-dependent
  detail); OGC SLD; MapLibre sprites and layers with trees and streets in metres; CSS and DTCG design
  tokens; a command line; a skill for AI coding agents.

![One quarter, seven conventions](docs/img/conventions.png)

## Install

```bash
pip install "urban-landscape-graphics[all] @ git+https://github.com/UrbanSens/Urban-Landscape-Graphics"
```

Python 3.10+. Core dependencies are NumPy and Shapely; `[all]` adds GeoPandas and Matplotlib. PNG
output uses `rsvg-convert`, CairoSVG or Inkscape if one is installed. Check the installation:

```bash
ulg check
```

To try the examples or to work on the library, use a clone:

```bash
git clone https://github.com/UrbanSens/Urban-Landscape-Graphics.git
cd Urban-Landscape-Graphics
pip install -e ".[dev]"
python examples/quickstart.py
```

## Documentation

<!-- github-only:start -->
**Read it online: [urbansens.github.io/Urban-Landscape-Graphics](https://urbansens.github.io/Urban-Landscape-Graphics/)**
– with search, light and dark mode, and a
[live demo map](https://urbansens.github.io/Urban-Landscape-Graphics/demo/) drawn with the exported MapLibre style.

| | Chapter | What you find there |
|---|---|---|
| 1 | [Origins](https://urbansens.github.io/Urban-Landscape-Graphics/01-origins.html) | from the Englischer Garten and the 1808 Bavarian survey to GIS |
| 2 | [The style guide](https://urbansens.github.io/Urban-Landscape-Graphics/02-style.html) | principles, palette, textures, symbols, drawing order, legibility |
| 3 | [The catalog](https://urbansens.github.io/Urban-Landscape-Graphics/03-catalog.html) | all elements and their coefficients |
| 4 | [Python](https://urbansens.github.io/Urban-Landscape-Graphics/04-python.html) | drawing, classifying, measuring, the command line |
| 5 | [GIS and web](https://urbansens.github.io/Urban-Landscape-Graphics/05-gis-and-web.html) | QGIS, GeoServer, MapLibre, tokens |
| 6 | [Standards](https://urbansens.github.io/Urban-Landscape-Graphics/06-standards.html) | what the style conforms to, with the full [standards report](https://urbansens.github.io/Urban-Landscape-Graphics/research/standards-report.html) |
| 7 | [For AI agents](https://urbansens.github.io/Urban-Landscape-Graphics/07-agents.html) | `ulg agent install` |
| 8 | [Extending](https://urbansens.github.io/Urban-Landscape-Graphics/08-extending.html) | how the style guide grows |

The same pages are Markdown in [`docs/`](docs/index.md), so they can be read here on GitHub as well. The
whole documentation is also one self-contained file, [ulg-documentation.html](https://urbansens.github.io/Urban-Landscape-Graphics/ulg-documentation.html),
for e-mail and offline reading. GitHub builds the site on every push; locally:
`python tools/build_html.py`.
<!-- github-only:end -->
<!-- site-only
Start at **[docs/index.md](docs/index.md)**:

1. [Origins](docs/01-origins.md) – from the Englischer Garten and the 1808 Bavarian survey to GIS
2. [The style guide](docs/02-style.md) – principles, palette, textures, symbols, drawing order, legibility
3. [The catalog](docs/03-catalog.md) – all elements and their coefficients
4. [Python](docs/04-python.md) – drawing, classifying, measuring, the command line
5. [GIS and web](docs/05-gis-and-web.md) – QGIS, GeoServer, MapLibre, tokens
6. [Standards](docs/06-standards.md) – what the style conforms to, with the full [standards report](docs/research/standards-report.md)
7. [For AI agents](docs/07-agents.md) – `ulg agent install`
8. [Extending](docs/08-extending.md) – how the style guide grows
-->

![The style sheet, generated from the catalog](docs/img/style-sheet.png)

## Repository

```text
src/ulg/          the package; src/ulg/data holds the catalog, palette, themes and crosswalks as JSON
docs/             documentation, generated reference pages, research
examples/         runnable examples, sample data, a MapLibre page
tools/            builders for the documentation images, logo, reference pages and HTML; data formatter
tests/            pytest suite
.github/          tests and the documentation site (GitHub Pages) run on every push
```

Working on the library: the rules and commands are in [AGENTS.md](AGENTS.md) (for people and coding
agents alike) and in the chapter [Extending](docs/08-extending.md).

## Status

Version 0.1.0 (2026-09-30), UrbanSens. See [CHANGELOG.md](CHANGELOG.md). Standards were researched
on 2026-09-30; the [standards report](docs/research/standards-report.md) lists what was verified,
what is paywalled and what to re-check when standards change.

<!-- github-only:start -->
<br>

<div align="center">

<a href="https://github.com/UrbanSens">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/img/brand/urbansens-logo-on-white.png">
    <img src="docs/img/brand/urbansens-logo.png" alt="UrbanSens – Let's be part of the change." width="180">
  </picture>
</a>

<sub>A project by <a href="https://github.com/UrbanSens">UrbanSens</a>.</sub>

</div>
<!-- github-only:end -->

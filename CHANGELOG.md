# Changelog

All notable changes to the style and the library. Versions follow the rules in
[docs/en/08-extending.md](docs/en/08-extending.md#89-versions-and-the-living-style-guide): removing or
renaming an element is a major change, new elements or visible changes are minor, invisible fixes
are patches. The changelog is written in English.

## 0.1.0 (2026-09-30)

First release of the UrbanSens Ecological Vector Style as a library.

**Style and catalog**

- 173 elements in English and German: vegetation, blue-green infrastructure, trees, water, ground,
  33 surfaces, land use, built structures, furniture, ecological structures, boundaries, relief,
  planning and analysis overlays, context.
- Palette of 21 colour families; 17 texture motifs with four levels of detail; ISO 128 line weights.
- Tree and shrub status symbols after ISO 11091 and PlanZV 13.2; status overlays after the Bavarian
  Bauvorlagenverordnung (planned: red cross-hatch) and ISO 11091 (removal: dashed hatch); PlanZV
  borders for compensation, planting and preservation areas; DIN 18920 root protection zones.
- Coefficients per element with sources: Berlin BFF 2021 and 1990, DIN 1986-100 runoff, UBA sealing,
  bdla classes, Berlin paving classes, PALM albedo and emissivity, EU NRR urban green space.
- Drawing bands for stacked data: all ground cover at one z, drawn largest first; water, wetland,
  centre-line strips, built, trees and overlays above.
- Themes: `mellow` (house), `planzv`, `alkis`, `basemap`, `bfn`, `osm`, `mono`.

**Data interoperability**

- 26 crosswalks with 3 926 classes: OSM, ALKIS, ALKIS NAK, AdV LB/LN, XPlanung, PlanZV, basemap.de,
  LBM-DE, BKompV, BayKompV, FFH, Berlin biotopes, DIN 276, CORINE, Urban Atlas, CLC+, EUNIS, HILUCS,
  LUCAS, ESA WorldCover, LCZ, BGT, Swiss AV, Austrian DKM, England's biodiversity metric, UKHab.
- Hierarchy fallback with zero-padded groups, code suffixes (BKompV age classes) and a fallback
  pattern (BayKompV).

**Library**

- Renderer with SVG (true to scale, in millimetres) and Matplotlib backends; ground-anchored,
  reproducible, seamless textures; hand-drawn outline bounded by half the line width.
- Roads and paths given as centre lines are drawn as strips of their width (`width`, `lanes`, OSM
  `highway`); `ulg.flatten()` turns stacked data into a planar partition.
- `ulg.indicators()`, `ulg.root_protection_zone()`, legends, style and catalog sheets.
- Exporters: QGIS (QML with hand-drawn outline, scale-dependent detail, strips, area ordering), OGC
  SLD 1.0, MapLibre (sprite, layers with trees and streets in metres), CSS and DTCG tokens.
- Command line `ulg` with JSON output; `ulg agent install` for coding agents; `ulg check` legibility
  report including colour-vision deficiency.
- Demo data: `ulg.datasets.demo_park()` draws *Angerpark*, a fictitious quarter of about 20 ha (a designed
  park with allée, pond and reed belt, meadows, orchard, community garden, playground and plaza; an avenue
  with a green tram track; a canal; perimeter blocks with zoned courtyards; slab housing and a school) as a
  clean planar partition in EPSG:25832; `demo_park_places()` names the spots for crops and labels.

**Licence and credit**

- MIT licence (`LICENSE`, licence metadata after PEP 639 in `pyproject.toml`) and `CITATION.cff`, so that GitHub
  offers "Cite this repository". Naming UrbanSens and linking <https://urbansens.de/> is asked for politely, not
  required by the licence ([licence and credit](docs/en/licence-and-credit.md)); the request is repeated in the
  README, the footer of the documentation site and the agent skill.
- `ulg.brand`: the UrbanSens logo as package data, `ulg.credit_line()`, and a small mark (logo, version, website)
  on the sheets and legends the library draws itself (`style_sheet`, `catalog_sheet`, `legend_svg(credit=True)`;
  `credit=False` or `--no-credit` leaves it out). The figures of the documentation carry it too. Maps drawn by
  users never get a mark.

**Documentation**

- Two languages: German is the default (`README.md`, `docs/`, the root of the website, formal "Sie"), English is
  the second (`README.en.md`, `docs/en/`, `/en/`). The website has a language switch that pairs the pages,
  per-language search and single files (`ulg-dokumentation.html`, `en/ulg-documentation.html`); figures with text
  exist per language (`name.png`, `name-de.png`), and the MapLibre demo switches with `?lang=en`. The reference
  pages, research files, examples and this changelog stay English. `tests/test_docs_i18n.py` compares both trees.
- House rule for all text: no em dashes and no spaced en dashes in their place (`tests/test_style_rules.py`).
- Eight chapters from the history of the style to extending it, generated reference pages, the
  standards report and seven research streams.
- HTML version (`python tools/build_html.py`): a multi-page site in `docs/html/` on light paper with an editorial
  layout (a banner with the title over a faded black-and-white drawing of the demo map, with accents in the blue,
  peach and salmon of the UrbanSens logo; a narrow serif column; bold sans headings in Rethink Sans, SIL OFL,
  bundled; numbered figure captions; quotations with their source; "continue reading" cards; a sitemap
  footer that carries the UrbanSens logo), plus sidebar navigation, search that works from `file://`, optional
  dark mode, zoomable figures and copy buttons, and one self-contained file per language with the guide, the
  reference, the standards report and the examples. The builder checks every link and anchor;
  `tests/test_docs.py` runs the same check.
- GitHub: `.github/workflows/ci.yml` runs the tests on Python 3.10, 3.12 and 3.13; `pages.yml` publishes the
  site, the single files and a live MapLibre demo with GitHub Pages at
  <https://urbansens.github.io/Urban-Landscape-Graphics/>. The README is written for GitHub (logo, links to the
  site, dark-mode variants of the logos); `docs/img/social-preview.png` (German) and `social-preview-en.png` are
  the repository's social preview.
- Logo (`python tools/build_logo.py`): the mark spells *ulg* with a pond, a tree-lined path and a tree crown with
  a stream, drawn by the library from catalog elements; lockups, a dark version, a small version and favicons in
  `docs/img/logo/`, described in [style guide 2.12](docs/en/02-style.md#212-the-mark).

**Known gaps** (from the standards report)

- Elements not yet in the catalog: moss and lichen cover, biodiverse green roofs, pollard trees,
  neophyte stands, tree trenches (*Baumrigolen*), setback areas, PlanZV 11.1/11.2/15.8 areas.
- No ATKIS theme, no BfN saturated series, SLD 1.0 only (no SE 1.1, no scale rules).
- `protected_biotope` is green where Bavarian practice uses magenta; the site boundary and
  protected-area and flood-zone borders follow landscape-plan practice rather than every official line.
- Only one of the Berlin BFF brochure examples is a test.

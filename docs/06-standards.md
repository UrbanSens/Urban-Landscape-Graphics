# 6 · Standards and conformance

*Which German and European standards the style follows, how, and where it deliberately does not.
The full evidence is in the [standards report](research/standards-report.md).*

## 6.1 What "conform" means here

Colour is almost never law. The only statutory plan symbology in Germany, the PlanZV, names colours in
words, applies only to land-use and zoning plans and allows deviations as long as the plan stays
legible. What *is* fixed are codes, symbols with a meaning, and numbers.

> Eine Verletzung von Vorschriften der Absätze 1 bis 4 ist unbeachtlich, wenn die Darstellung, Festsetzung, Kennzeichnung, nachrichtliche Übernahme oder der Vermerk hinreichend deutlich erkennbar ist.
>
> — Planzeichenverordnung 1990, § 2 Abs. 5 (in English: a breach of the rules of paragraphs 1 to 4 is immaterial when the content is clearly recognisable)

The library therefore conforms in five ways:

| Layer | What is standardised | How ulg follows it |
|---|---|---|
| **Codes** | the classes of cadastral, planning, biotope, land-cover and OSM schemes | 26 crosswalks translate 3 926 classes into elements, each with a fit grade and an evidence mark (6.3) |
| **Official looks** | published colour values of ALKIS, basemap.de, BfN, OSM Carto, PlanZV practice | six themes redraw any map in those colours (6.2); crosswalk entries carry a scheme's own colour where it was verified |
| **Symbols with meaning** | existing / proposed / preserved / removed; plan borders; root protection | tree and shrub status symbols, PlanZV borders, DIN 18920 zones ([style guide 2.5](02-style.md#25-symbols)) |
| **Numbers** | weighting factors, runoff coefficients, sealing classes, EU green-space definitions | element attributes with their sources, `ulg.indicators()` (6.4) |
| **Legibility** | WCAG 2.2 criteria 1.4.1 and 1.4.11, colour-vision deficiency | `ulg check` in the test suite ([style guide 2.8](02-style.md#28-legibility)) |

The research behind this was done in seven streams on 2026-09-30, each value marked by how it was
verified: **V** read in the primary source, **V\*** read through an extraction or sampled from an
official swatch, **S** from a secondary source, **R** recalled and not verified.

## 6.2 Themes

| Theme | Convention | Edition used | Evidence |
|---|---|---|---|
| `mellow` | UrbanSens house style | this library | – |
| `planzv` | colours of German land-use and zoning plans | PlanZV 1990 (amended 2025), hex values of the XPlanung reference implementation xPlanBox | colour words V; hex V from xPlanBox |
| `alkis` | cadastral map (Liegenschaftskarte) | ALKIS-Signaturenkatalog 2.1.0 (01.10.2024) | V |
| `basemap` | the federal web basemap | basemap.de Web Vektor `bm_web_col` 5.0.3 | V |
| `bfn` | landscape plans | BfN-Skripten 461/2 (2017), pastel series | V |
| `osm` | OpenStreetMap | OSM Carto v6.1.0 | V |
| `mono` | black-and-white drawing | after ISO 11091 conventions | house interpretation |

Official themes switch the hand-drawn outline off and use flat fills, as the originals do. Elements
without an entry of their own take the colour of the category they belong to in that convention; the
evidence of every colour is written into the theme file (see [reference/themes.md](reference/themes.md)).

## 6.3 Crosswalks

| Family | Schemes (entries) |
|---|---|
| German planning and cadastre | `planzv` (72), `xplanung` (357), `alkis` (292), `alkis_nak` (138), `adv_lbln` (141), `basemap_de` (140), `lbm_de` (116) |
| Biotopes, compensation, costs | `bkompv` (369), `baykompv` (345), `ffh_lrt` (41), `berlin_biotope` (33), `din276` (70) |
| European and global | `clc` (64), `urban_atlas` (44), `clcplus` (14), `eunis` (381), `hilucs` (92), `lucas` (111), `esa_worldcover` (11), `lcz` (24) |
| OpenStreetMap and national models | `osm` (457), `bgt` (NL, 114), `swiss_av` (CH, 96), `at_dkm` (AT, 126), `uk_metric` (121), `ukhab` (157) |

Every entry states how faithful the translation is:

| Fit | Meaning | Example |
|---|---|---|
| `exact` | same concept | CLC 141 *Green urban areas* → `green_space` |
| `narrower` | the element is more specific than the class | ALKIS *Pflaster* → `concrete_pavers` |
| `broader` | the element is more general than the class | ALKIS *Salzweide* → `salt_marsh` |
| `nearest` | no real equivalent; the closest drawing | OSM `landuse=greenery` → `perennials` |
| `none` | not a drawable class | OSM `highway=proposed` |

Biotope schemes carry their valuation: BKompV entries hold the biotope value (0–24, or per age class),
BayKompV entries the value points (0–15) and the legal protection. Official legend colours are kept
per class (`ulg.official_colors("clc")`), so a map that must use CORINE's pink for green urban areas
can. Details, sources and licence notes per scheme: [reference/crosswalks.md](reference/crosswalks.md).

## 6.4 Coefficients

| Attribute | Standard | Evidence |
|---|---|---|
| `bff`, `bff_1990` | Berlin Biotopflächenfaktor, brochure 02/2021 (16 types) and the 1990 list | V |
| `runoff_cs`, `runoff_cm` | DIN 1986-100:2016-12, Table 9 | S (municipal reproduction; the standard is paywalled) |
| `sealing` | Umweltbundesamt definitions | V |
| `bdla_class` | bdla, qualified open-space plan (07/2022) | V |
| `belagsklasse` | Berlin Umweltatlas 01.02 (2017) | V |
| `albedo`, `emissivity` | PALM model system 6.0 lookup tables | V |
| `nrr_urban_green` | Regulation (EU) 2024/1991 Art. 3(20); CLC+ Backbone classes 2, 3, 4, 5, 6, 8, 10 | V |

Values are copied, never interpolated. Where two instruments disagree – a water-bound path has a low
BFF weight but a high runoff coefficient – both are kept, because they answer different questions.

## 6.5 Drawing conventions

| Convention | Source | In ulg |
|---|---|---|
| existing thin, proposed thick; protected with a chain-line frame; removal dashed and crossed | ISO 11091 | tree and shrub status symbols, `mono` theme |
| open centre = to plant, filled centre = to preserve | PlanZV 13.2 | `tree_planned`, `shrub_planned`, `tree_protected` |
| borders with inward T-ticks, open circles, filled dots; plan area boundary | PlanZV 13.1, 13.2.1, 13.2.2, 15.13 | `compensation_area`, `planting_area`, `preservation_area`, `planning_boundary` |
| grey existing, red new, yellow removal; new works cross-hatched | Bavarian Bauvorlagenverordnung, Anlage 1 | `signal.*` tokens, `status_planned` (red cross-hatch), `status_removal`, `tree_remove` |
| removal as a thin dashed hatch | ISO 11091 | `status_removal` (yellow, dashed hatch) |
| root zone = drip line + 1.50 m (columnar + 5.00 m); trenches ≥ 4 × girth, at least 2.50 m | DIN 18920 (2014 text), R SBB | `ulg.root_protection_zone()` |
| brown vertical dashes for fallow | BfN 461/2 | `grassland_fallow` |
| line widths | ISO 128 series | `settings.json → line_weights` |
| scales per work stage | HOAI Anlage 11 | level-of-detail breaks 1:750 / 1:2 500 / 1:10 000 |

## 6.6 Deliberate departures

The house style is free where no rule binds it, and says so:

- **Protected biotopes** are a green hatch; the Bavarian biotope viewer uses magenta. Use the `bfn`
  theme or recolour the overlay where the local convention matters.
- **Boundaries** follow landscape-plan practice rather than every official line: the site boundary is
  a neutral solid line (the Bauvorlagenverordnung uses a violet long dash), protected-area boundaries a
  green chain line (PlanZV 13.3 uses groups of strokes), flood zones a hatch (PlanZV 10.2 a wavy border).
- **Lawn, meadow and wildflower meadow** share one colour family, as in every scheme researched; the
  house style separates them by texture, not by hue.
- **Paving materials** are a house-level distinction: no European scheme and only a few German ones
  know them, so external codes resolve to generic elements (`sealed`, `concrete_pavers`) rather than
  to a guessed material.
- **Climate classes** (`klimatop`, `utci`, `pet`) use house colours in the customary hue order; no
  numeric colour standard exists yet (VDI 3787 Blatt 12 is in preparation).

## 6.7 Keeping current

Standards change: PlanZV was amended in 2025, CLC 2024 is due, DIN 18920 appeared in a new edition in
2026. The report lists what to watch and the state on 2026-09-30
([report 5.4](research/standards-report.md#54-what-to-re-check-when-standards-change)). When a source
changes, update the element, theme or crosswalk file, note the edition in its `version` or `evidence`
field, run the tests and regenerate the sheets ([Extending](08-extending.md)).

**Licences.** Codes and published colour values are facts and are cited, not copied as artwork. Symbol
files of the BfN (CC BY-ND / all rights reserved) and UKHab (licence-gated) are not bundled; the library
draws its own symbols after the same conventions. When you publish a map in the `basemap` theme,
credit "© basemap.de / BKG" ([report 5.3](research/standards-report.md#53-licences)).

---

Next: [7 · For AI agents](07-agents.md)

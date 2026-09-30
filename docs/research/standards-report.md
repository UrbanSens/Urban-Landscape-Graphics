# Standards report — what the Ecological Vector Style conforms to

**Date:** 2026-09-30 · **Library:** Urban Landscape Graphics (`ulg`) 0.1.0, house style "UrbanSens – Ecological Vector Style"

## How to read this

**Scope.** This report states which laws, technical rules, official catalogues and de-facto conventions the library follows, how far, and where it deliberately does not. "Conformance" has three meanings here:

1. **Semantics** – the library reads the codes of a scheme and draws each class as a catalog element (crosswalks).
2. **Convention** – colours, textures, line styles and symbols respect what official maps and plans already use (themes, motifs, status symbols).
3. **Rules and numbers** – where a regulation or technical rule fixes a number (a weighting factor, a buffer, a class limit), the library uses it and names the source.

**Method.** This is a synthesis. Every statement about a standard comes from the seven research streams of 2026-09-30 and their working notes; nothing was looked up again. Every statement about the library was checked against the code and data in `src/ulg/`. The library was still changing on the day of writing; library statements reflect the last check.

| Stream | Scope |
|---|---|
| [01](streams/01_de_planning_cadastre.md) | PlanZV, XPlanung/XPlanGML, ALKIS/ATKIS and their signature catalogues, basemap.de, LBM-DE |
| [02](streams/02_de_biotope_landscape_planning.md) | BfN biotope list, BKompV, BayKompV, § 30 BNatSchG / Art. 23 BayNatSchG, FFH habitat types, BfN plan symbols, Bavarian and Berlin biotope maps |
| [03](streams/03_eu_classifications.md) | CORINE, Urban Atlas, CLC+ Backbone, Nature Restoration Regulation, EUNIS, MAES / EU ecosystem typology, INSPIRE, LUCAS/EAGLE, LCZ, ESA WorldCover |
| [04](streams/04_osm_national_topo_prior_art.md) | OSM tags and OSM Carto, NL BGT/IMGeo, Swiss AV, Austrian DKM, England's biodiversity metric and UKHab, prior-art legends |
| [05](streams/05_de_freianlagen_typologies.md) | FLL OK FREI, DIN 276 KG 500, lawn and planting standards, green roofs and façades, surfaces and bonds, trees, HOAI scales |
| [06](streams/06_coefficients_drawing_standards.md) | Berlin BFF and similar factors, runoff coefficients, sealing, albedo; ISO 11091, building-drawing standards, status colours, DIN 18920; VDI 3787, UTCI/PET; minimum sizes |
| [07](streams/07_rendering_interop.md) | QGIS formats, SLD/SE, GeoServer, INSPIRE view services, web map libraries, hand-drawn rendering, design tokens, accessibility |
| [notes](streams/notes/) | page-image transcriptions behind streams 02 and 04 |

**Evidence marks.** Each stream defines its own marks; this report keeps them as given:

| Mark | Meaning |
|---|---|
| V | verified in a primary source during the research (streams 04 and 07 read web pages through a text-extraction tool) |
| V* | primary source read through a summarising extraction (02), or a colour sampled from an official legend swatch (03 §5.6) |
| V-img | verified on the page images of the primary source (04) |
| S | secondary source |
| R | recalled, **not verified** – a lead, not a fact |
| A / D | author's assessment (03) / own derivation or design proposal (04, 07) |
| T | tested locally by the research agent (07) |

References in brackets point to stream and section: [01 §4.1] is stream 01, section 4.1. "Not verified" is written wherever a stream says so.

**The library in brief.** `ulg` holds 173 elements in `src/ulg/data/elements/*.json`, grouped as `vegetation.*`, `blue_green`, `trees`, `water`, `ground`, `surface.*`, `landuse`, `built`, `furniture`, `ecology`, `boundary`, `relief`, `planning`, `analysis`, `context` and `other`. An element has a fill and outline (by default the fill darkened by 10 %), texture recipes per level of detail, a line or point symbol, German and English aliases, and attributes documented in `src/ulg/data/settings.json`. External codes are attached at load time from the crosswalk files in `src/ulg/data/crosswalks/` (format: [crosswalk-format](../reference/crosswalk-format.md)). The house palette is `src/ulg/data/palette.json` (theme "mellow"); six more themes live in `src/ulg/data/themes/`. Exporters are in `src/ulg/export/`, indicators in `src/ulg/analysis.py`, the legibility report in `src/ulg/check.py`.

**Binding levels.** *Law* (statute or ordinance) · *technical rule* (DIN, ISO, VDI, DWA, FLL; binding by contract or reference) · *official standard* (data model or signature catalogue of a public body) · *recommendation* · *convention* (de-facto practice).

## 1. Summary

1. **Colour is almost never law.** The *Planzeichenverordnung* (PlanZV; ordinance on plan symbols), the only statutory symbology found, names colours in words only, applies only to *Bauleitpläne* (statutory land-use plans), is a "soll" rule and tolerates deviations while the plan stays legible (§ 2 Abs. 1–5, V) [01 §1.2]. BKompV and the Bavarian value list prescribe no colours [02 §0]. — **ulg:** the house style is free; the `planzv` theme uses the de-facto hex values of the XPlanung reference implementation xPlanBox.
2. **Numeric official palettes exist for more than a dozen schemes:** ALKIS-Signaturenkatalog 2.1, basemap.de 5.0.3, BfN 461/2, OSM Carto v6.1.0, BGT, Swiss AV, CORINE, Urban Atlas, CLC+ Backbone, HILUCS, LCZ, ESA WorldCover, the Berlin biotope map (V; Swiss AV V-img) [01 §4, 02 §7–8, 03 §11, 04 §2–4]. — **ulg:** themes `alkis`, `basemap`, `bfn`, `osm`, `planzv`, `mono`; crosswalk entries carry a scheme's own colour only where it was verified.
3. **Pastel is the established look at parcel scale.** ALKIS tints, basemap.de, the BfN "Kulisse" series, the BGT pastel and background sets, the OS "Outdoor style" and OSM Carto (Lch lightness 80–99) are all light and low in chroma [01 §7.2, 02 §7.4, 04 §8.4]. — **ulg:** the mellow palette sits inside this convention; only `planzv` is saturated, like the plans it imitates.
4. **Only a small core of hue conventions is stable:** water blue, woodland green, bright yellow-green shrubs and tree rows, pale yellow-green grassland including lawns, pale yellow/beige arable land, pink/magenta heath, grey traffic areas, a blue shift for wetness; reeds, ruderal vegetation, raw soil, parks and built-up areas vary [02 §8.4–8.6]. European legends add: red means sealed (A) [03 §11]. — **ulg:** the house palette follows the core; the periphery is a documented house choice; `bfn` is a ready preset.
5. **One drawn element is not one code.** Elements map to code *families* that differ by age, naturalness, species richness or sealing; code spaces cannot be converted by pattern; identical digits mean different things across editions and lists [01 §7.6, 02 §11.1, 05 §2.2]. — **ulg:** one crosswalk file per scheme with version, fit grade (exact, narrower, broader, nearest, none) and evidence mark.
6. **XPlanung 6.1 is the machine form of the PlanZV.** Published 15.04.2025 (V); its landscape-plan model names BKompV, Länder and FFH keys for biotopes, but those code lists were empty on 2026-09-30 (V) [01 §2]. — **ulg:** `xplanung` and `planzv` crosswalks.
7. **ALKIS describes land use in depth, surface materials hardly at all.** AAA 7.1.2 has the full *Tatsächliche Nutzung* (actual land use) and the 8-digit *Nutzungsartkennung* (NAK, land-use key of the area statistics), but only four road-surface materials (V) [01 §3, §7.4]. — **ulg:** `alkis`, `alkis_nak`, `adv_lbln` crosswalks; the material *Pflaster* reaches `concrete_pavers` only as `narrower`, and most other paving types and decking have no ALKIS code.
8. **Biotope valuation runs in two code spaces:** BKompV Anlage 2 (0–24, BfN codes, federal projects) and the Bavarian *Biotopwertliste* (biotope value list; 0–15, list of 2014) (V*/V) [02 §2–3]; neither has green roofs. — **ulg:** `bkompv` and `baykompv` crosswalks carry the values; green roofs stay without a biotope code.
9. **Lawn, meadow and species-rich meadow share one hue in every scheme** and are separated by management and species criteria (V) [02 §9]; in Europe only EUNIS separates them [03 §13.1]. — **ulg:** eight lawn and meadow elements share the `grass` colour family and differ by texture (ticks, tufts, flower dots, mowing stripes); dry, wet and fallow grassland move to straw, marsh and fallow tones.
10. **Legal protection is an overlay.** § 30 BNatSchG and Art. 23 BayNatSchG protect biotopes of any type (V*); BfN labels them, the Bavarian viewer tints them magenta (V) [02 §5, §7.3, §8.1]. — **ulg:** `protected_biotope` is an overlay hatch (in green, which departs from the red/magenta practice).
11. **The Nature Restoration Regulation measures a land-cover mask.** Art. 8 targets urban green space and canopy; the Commission/EEA note uses CLC+ Backbone 2023 (classes 2, 3, 4, 5, 6, 8, 10) and HRL Tree Cover Density 2024; green roofs are invisible to both (V) [03 §4]. — **ulg:** `nrr_urban_green`, `canopy`, `tree_canopy`, `nrr_green_share`, `canopy_share`.
12. **European land-cover schemes do not know paving materials**; lawn and meadow also collapse into one class [03 §13.1]. — **ulg:** material stays a house-level distinction; European codes resolve to generic elements (CLC+ class 1 → `sealed`), never to a paving type.
13. **Coefficients disagree by design.** Berlin's *Biotopflächenfaktor* (BFF, biotope area factor) 2021 has 16 types and changed 1990 factors (V); DIN 1986-100 runoff values are known from reproductions only (S); a water-bound path scores BFF 0.1 but Cs 0.9 [06 §A]. — **ulg:** per-element coefficients with source and mark; never interpolated.
14. **Plan status follows three verified rules:** ISO 11091 (existing thin, proposed thick, protected chain line, removal dashed hatch), PlanZV 13.2 (open centre = to plant, filled = to preserve), Bavarian *Bauvorlagenverordnung* (BauVorlV; grey existing, red planned, yellow removed) (V) [06 §B5, §B7; 01 §1.4]. — **ulg:** tree and shrub symbols and `status_*` overlays (the hatch motifs differ from the BauVorlV, see 3.9).
15. **Tree protection has a fixed geometry.** DIN 18920: root zone = crown drip line + 1.50 m (columnar + 5.00 m); trenches ≥ 4 × stem girth, at least 2.50 m (V for 2014-07; 2026-06 wording not verified) [06 §B8]. — **ulg:** `root_protection_zone()`.
16. **Climate maps have no numeric colour standard yet**; VDI 3787 Blatt 12 may appear 2027-03 (V) [06 §C10]. — **ulg:** `klimatop`, `utci`, `pet` categories in house colours.
17. **Interoperable formats cannot carry the hand-drawn look.** SLD 1.0 / SE 1.1 are the only widely implemented OGC encodings; converters drop random fills, tiles and seeds; MapLibre has no randomness (V) [07 §2–3]. — **ulg:** native writers per target; seamless tiles; wobble only where supported.
18. **Pastel fills cannot carry class identity alone.** WCAG 2.2 SC 1.4.1 and 1.4.11 (V); pastel pairs reach about 1.01–1.11:1 (T); ΔE00 = 10 is recommended (V) [07 §6]. — **ulg:** `check.py` requires texture or outline differences below ΔE00 10, also under simulated colour-vision deficiency; `Options.accessible()` gives 3:1.

## 2. Conformance matrix

| Standard | Edition / version checked | Binding | Governs | How ulg implements it | Evidence |
|---|---|---|---|---|---|
| PlanZV, Anlage | 1990, last amended 12.08.2025 | law ("soll"), Bauleitpläne only | colour words, symbol geometry | `planzv` theme and crosswalk; motifs in `compensation_area`, `planting_area`, `preservation_area`, `tree_planned`, `tree_protected`, `planning_boundary` | V [01 §1] |
| XPlanung / XPlanGML | 6.1 (15.04.2025) | data standard (binding force not researched in 01) | plan classes and enumerations | `xplanung` crosswalk | V [01 §2] |
| xPlanBox default styles | tags 7.0 and 9.3 | convention (AGPL v3 code) | hex colours per XPlanung class | `planzv` theme; `color` in `planzv`, `xplanung` | V [01 §2.6] |
| ALKIS AAA schema and NAK | 7.1.2 (Stand 01.11.2022) | official standard | actual land use, overlays, statistics key | `alkis`, `alkis_nak` crosswalks | V [01 §3] |
| AdV Landbedeckung / Landnutzung | LB 1.0.1, LN 1.0.2 | official standard | separate cover and use schemas | `adv_lbln` crosswalk | V [01 §3.6] |
| ALKIS-Signaturenkatalog | AAA-SK 2.1, Farbausgabe 2.1.0 (01.10.2024) | official standard | area fills, 33 colours | `alkis` theme; `color` in `alkis`, `alkis_nak` | V [01 §4.1] |
| ATKIS-Signaturenkatalog | SK10 2.1.3 (30.11.2024) | official standard | CMYK colours | not implemented | V [01 §4.2] |
| basemap.de Web Vektor | `bm_web_col` 5.0.3 | convention | web colours per `klasse` | `basemap` theme; `basemap_de` crosswalk | V [01 §4.3] |
| LBM-DE | 2021 (doc. 30.04.2025) | official product | cover × use, MMU 1 ha | `lbm_de` crosswalk | V [01 §5] |
| BfN Rote Liste Biotoptypen | 3rd ed. 2017 (short list) | reference list | biotope code space | code space of `bkompv` | V [02 §1] |
| BKompV Anlage 2 | 14.05.2020, amended 22.12.2025 | law (federal projects) | biotope values 0–24 | `bkompv` crosswalk | V* [02 §2] |
| BayKompV Biotopwertliste | 28.02.2014; re-mapping 09/2021 | law (Bavaria; not Bauleitpläne) | BNT codes, 0–15 points | `baykompv` crosswalk | V [02 §3] |
| § 30 BNatSchG / Art. 23 BayNatSchG | as read 2026-09-30 | law | protected biotopes | `protected_biotope` overlay | V* [02 §5] |
| FFH Annex I | names of 13.05.2013 (BfN list) | law (EU) | habitat types | `ffh_lrt` crosswalk | V [02 §6] |
| Berlin Umweltatlas 05.08 | Biotoptypen 2024 | official map | 24 legend classes and colours | `berlin_biotope` crosswalk | V [02 §8.3] |
| BfN Planzeichen Landschaftsplanung | BfN-Skripten 461/2 (2017), 486 (2018) | recommendation | group colours, overlays, status | `bfn` theme; overlay textures | V [02 §7] |
| FLL OK FREI | 2025 (codes not public) | technical rule | open-space object types | aliases, element split; no crosswalk | V/S [05 §1] |
| DIN 276 KG 500 | 2018-12 | technical rule | cost groups | `din276` crosswalk (third level) | S [05 §2] |
| DIN 18917 / RSM Rasen | 2018-07 / 48th ed. 2026 | technical rule | lawn types, seed mixtures | `lawn`, `lawn_extensive`, `flower_lawn`, `sports_turf` | V, table S [05 §3] |
| FLL roof and façade greening rules | both 2018 | technical rule | greening types | `green_roof_extensive`, `green_roof_intensive`, `green_facade` | V [05 §4] |
| FLL permeable surfaces; ZTV-Wegebau | 2018; 2022 | technical rule | permeable, water-bound surfaces | `gravel_turf`, `grass_pavers`, `grass_joint_paving`, `waterbound` | V [05 §6] |
| HOAI Anlage 11 | HOAI 2013 as amended (date R) | law (fees) | scales per work stage | LOD breaks 1:750 / 1:2,500 / 1:10,000 | V [05 §8] |
| CORINE Land Cover | 1990–2018 nomenclature | official product | 44 classes, MMU 25 ha | `clc` crosswalk with colours | V [03 §1] |
| Urban Atlas + Street Tree Layer | 2021 (PUM 1.0.2) | official product | urban classes, access | `urban_atlas` crosswalk with colours | V [03 §2] |
| CLC+ Backbone | 2018, 2021, 2023 | official product | 11 land-cover classes | `clcplus` crosswalk, NRR flags | V [03 §3] |
| Nature Restoration Regulation | (EU) 2024/1991; note v2.0 (07/2026) | law (EU) | urban green space, canopy | `nrr_urban_green`, `canopy`, `tree_canopy`, `indicators()` | V [03 §4] |
| EUNIS | 2021/2022 + 2012 | reference classification | habitat types | `eunis` crosswalk | V, colours V* [03 §5] |
| MAES / EU ecosystem typology | 2013; Eurostat 07/2026 | reference; level 1 by Reg. 2024/3024 | ecosystem types | no crosswalk | V [03 §6] |
| INSPIRE LU (HILUCS), LC, HB | guidelines 2024 | law (EU spatial data) | values, default styles | `hilucs` crosswalk with colours | V [03 §7] |
| LUCAS / EAGLE | 2022 (C3 issue 3.0) | survey / concept | cover and use axes | `lucas` crosswalk | V [03 §8] |
| Local Climate Zones | global map v3.0.0 | convention | 17 classes, colours | `lcz` crosswalk (palette A) | V [03 §9.1] |
| ESA WorldCover | v200 (PUM v2.0) | official product | 11 classes, colours | `esa_worldcover` crosswalk | V [03 §9.2] |
| OSM tags / OSM Carto | taginfo 2026-09-29; Carto v6.1.0 | convention | tags, default colours | `osm` crosswalk; `osm` theme | V [04 §1–2] |
| BGT / IMGeo | visualisation rules 2.3 | official standard (NL) | materials, colour sets | `bgt` crosswalk | V [04 §3] |
| Swiss AV | DM.01-AV-CH; DMAV 1.0 (2024) | official standard (CH) | land cover, RGB | `swiss_av` crosswalk | V / V-img [04 §4] |
| Austrian DKM / BANU-V | BGBl. II 116/2010; SHP v2.9 | official standard (AT) | use classes, no fills | `at_dkm` crosswalk | V-img [04 §5] |
| England metric / UKHab | tool v1.0.4; UKHab 2.01/2.1 | statutory metric / licensed | scored habitat list | `uk_metric`, `ukhab` crosswalks | V / S [04 §6] |
| Berlin BFF | 02/2021; 1990 | Berlin planning instrument | weighting factors | `bff`, `bff_1990`, `indicators()` | V [06 §A1] |
| DIN 1986-100 / DWA-A 138-1 | 2016-12 (draft 2025-06) / 10.2024 | technical rule | runoff coefficients | `runoff_cs`, `runoff_cm` | S [06 §A2] |
| UBA, bdla, Berlin sealing classes | 26.03.2026; 07/2022; 2017 | definitions, guidance | sealing classes | `sealing`, `bdla_class`, `belagsklasse` | V [06 §A3] |
| PALM lookup tables | 6.0 | model default | albedo, emissivity | `albedo`, `emissivity` | V [06 §A4] |
| ISO 11091 | 1994; DIN EN ISO 11091:1999-10 | technical rule | landscape-drawing signs | tree symbols, `mono` theme | V [06 §B5] |
| ISO 128 / DIN 1356-1 | ISO 128-2:2022 (S); E DIN 1356-1:2026-09 (V) | technical rule | line widths | `settings.line_weights` | S/R [06 §B6] |
| BauVorlV Bayern, Anlage 1 | text valid from 01.01.2025 | law (Bavaria) | status colours and signs | `signal.*` tokens, `status_*`, `tree_remove` | V [06 §B7] |
| DIN 18920 / R SBB | 2014-07 text; 2026-06 current; R SBB 2023 | technical rule | root zone, trench distance | `root_protection_zone()` | V / S [06 §B8] |
| VDI 3787; UTCI; PET | Blatt 1:2026-10; Blatt 12 project | technical rule; convention | climate classes | `categories.*` | V, PET S [06 §C10] |
| QGIS style formats | 3.44 LTR / 4.2; style "2" | software convention | QML, style XML | `export/qgis.py` | V [07 §1] |
| OGC SLD / SE | 1.0.0 / 1.1.0 | OGC standard | portable styles | `export/sld.py` (SLD 1.0) | V [07 §2] |
| INSPIRE view services | TG 3.3.0 | law (EU services) | default and extra styles | SLD as additional style | V [07 §2.5] |
| MapLibre style spec | GL JS 6.11.2 | software convention | patterns, sprites | `export/web.py` | V [07 §3.1] |
| DTCG design tokens | 2025.10 | community specification | token and colour format | `export/tokens.py` | V [07 §5] |
| WCAG 2.2 / EN 301 549 | WCAG 2.2; EN 301 549 V4.1.1 not yet cited | presumption of conformity (EAA, WAD) via EN 301 549 V3.2.1 (WCAG 2.1 AA) | non-colour cues, 3:1 | `check.py`, `Options.accessible()` | V [07 §6.1] |
| ΔE00 threshold; CVD simulation | Brychtová & Çöltekin 2016; Machado 2009 | research recommendation | ΔE00 ≥ 10, CVD matrices | `check.py`, `colormath.simulate_cvd` | V [07 §6.3–6.4] |

**Crosswalk files.** All 26 planned files are present at the time of writing: `adv_lbln`, `alkis`, `alkis_nak`, `at_dkm`, `basemap_de`, `baykompv`, `berlin_biotope`, `bgt`, `bkompv`, `clc`, `clcplus`, `din276`, `esa_worldcover`, `eunis`, `ffh_lrt`, `hilucs`, `lbm_de`, `lcz`, `lucas`, `osm`, `planzv`, `swiss_av`, `uk_metric`, `ukhab`, `urban_atlas`, `xplanung`. `crosswalk.validate()` reports no problems. Every file names title, publisher, version and source; every entry has a fit grade and, where given, an evidence mark.

## 3. Standards by domain

### 3.1 German planning law and plan symbols

**What the standard says** [01 §1–2, 06 §B9]

- The PlanZV of 18.12.1990 was last amended by Art. 6 of the act of 12.08.2025 (BGBl. 2025 I Nr. 189), which added no. 1.5 *Beschleunigungsgebiete für die Windenergie an Land* and renumbered the old 1.5 as 1.6, in force 15.08.2025 (V).
- § 2 (V): the *Planzeichen* (plan symbols) "sollen" be used in Bauleitpläne; they may be supplemented "sinngemäß"; hue, weight and density are adapted to the base map; a legend is required; a breach is harmless if the content is "hinreichend deutlich erkennbar". Black-and-white and colour are equally admissible. Colours are words only ("Grün mittel", "Blaugrün" …); values sampled from the JPEG scans are non-normative.
- Open-space motifs (V): *Randsignaturen* (border symbols) – T-ticks inward for areas for nature measures (13.1), open circles for planting areas (13.2.1), filled dots for preservation areas (13.2.2), stroke groups for protected areas (13.3); point symbols – circle = tree, cloud = shrub, **open centre = to plant, filled centre = to preserve** (13.2); purpose pictograms; plan boundary = thick broken band (15.13).
- XPlanGML 6.1 was published 15.04.2025 (GML 3.2.2); no newer version on 2026-09-30; removals are announced for version 7 (V). Key enumerations: `XP_ZweckbestimmungGruen` (35 values), `nutzungsform` (private/public), `SO_KlassifizGewaesser`, `XP_SPEMassnahmenTypen` (16), `XP_ABEMassnahmenTypen` (1000 = 13.2.2, 2000 = 13.2.1). The landscape-plan model names BKompV, Land and FFH keys, whose code lists were empty (V).
- xPlanBox (tags 7.0 and 9.3, identical; AGPL v3): `BP_GruenFlaeche` #7FC643, `FP_Gruen` public #80E41B, `SO_Gewaesser` #99D9E8, agriculture #CCE968, forest #34AB8F, roads #FFD92F, nature-measure band #4DAE38, plan boundary #80847A (V).

**How ulg uses it**

- `planzv` theme: xPlanBox colours, flat, no wobble, evidence notes on most element entries; elements without a Planzeichen take their plan category's colour.
- `planzv` crosswalk keyed by Planzeichen number (1.1–1.4, 4.2, 5, 6, 9–13, 15.13); its licence note says the scan colours are deliberately not used. `xplanung` crosswalk: class plus enumeration code.
- PlanZV motifs in the house style: `compensation_area` (T-ticks), `planting_area` (open circles), `preservation_area` (filled dots), `tree_planned` (open ring with cross), `tree_protected` (filled centre), `planning_boundary` (0.7 mm broken line).

**Limits and open points**

- The hex values are a convention; no Länder guide with numeric PlanZV colours was found [01 §6].
- `protection_zone` uses a dash-dot line instead of the 13.3 stroke groups, `flood_zone` a hatch instead of the 10.2 wavy border; 11.1/11.2 and 15.8 have no element.
- The legal force of XPlanung was not researched in primary sources; BfN says it binds landscape planning since 02/2023 (V*) [02 §7.1]. Whether § 9 Abs. 1 Nr. 15a / § 5 Abs. 2 Nr. 5a BauGB are in force was not checked.
- The `planzv` theme gives wetland elements the water colour without an evidence mark.

### 3.2 Official cadastre and topography

**What the standard says** [01 §3–5, §7]

- AAA-Anwendungsschema 7.1.2 (Stand 01.11.2022) plus separate *Landbedeckung* 1.0.1 and *Landnutzung* 1.0.2 schemas (V). The AdV reference-version statement (7.1 since 01.01.2024) was read through a summary and should be re-read.
- *Tatsächliche Nutzung*: object types 41001–44007, gap-free except overlays, capture threshold about 1,000 m² (V). The NAK is unique across object type and value list (41008 FKT 4400 Grünanlage = 18040000). LN codes differ from AAA codes.
- Surface materials: only four values on road axes plus LB loose-material classes (V). Light/dark paving, decking and wildflower meadow have no official code [01 §7.4].
- ALKIS-Signaturenkatalog 2.1 (Farbausgabe 2.1.0, 01.10.2024; 1:500–1:1,000): 33 colours with RGB, CMYK and hex (V). Recreation and cemeteries #DCE6C2, grassland #F3F5CC, arable #FFF8DC, woodland #CFE8D9, heath/bog/fallow #F3E3CA, water #C0E8FA with #0068A1 outline, vegetation symbols #008230; traffic areas unfilled.
- ATKIS-SK10 2.1.3 (30.11.2024) defines colours in CMYK only (V). basemap.de `bm_web_col` 5.0.3: background #FFFDEE, recreation #E6F7D2, grassland and cemetery #DFF0B6, woodland to #9AB66D, water #D2E8FA (V).
- LBM-DE2021: 31 cover and 16 use classes, MMU 1 ha, made to derive CORINE (V); its cross table is S quality.
- All German sources keep green space, grassland and woodland as three distinct greens and water light blue with a darker outline; topographic sources leave traffic white or grey, planning sources colour it yellow-ochre [01 §7.2].

**How ulg uses it**

- Themes `alkis` and `basemap` (fills with evidence notes).
- Crosswalks `alkis` (Kennung plus one coded attribute, field aliases FKT, VEG …), `alkis_nak` (prefix fallback to group codes), `adv_lbln`, `basemap_de` (with colours), `lbm_de`.

**Limits and open points**

- No ATKIS/DTK theme (CMYK only; a documented conversion would be needed).
- `alkis` theme building fill #CCCCCC is marked R in the theme.
- The `basemap` theme uses #738D0B for tree outlines; the style gives rgb(115,141,0) = #738D00, as the theme's own `tree_row` entry has.
- Signature shapes not viewed; AAA 6.0.1 → 7.1.2 not compared; only the colour style of basemap.de read.

### 3.3 Biotopes, compensation and protected habitats

**What the standard says** [02 §1–6, §8–9]

- BfN *Rote Liste der gefährdeten Biotoptypen Deutschlands*, 3rd ed. 2017: short list read (V), full book not accessible. Codes `GG.NN.NN`; groups 51–54 cover settlements; parks, gardens and cemeteries are not separate types.
- BKompV (14.05.2020; last amended 22.12.2025, BGBl. 2025 I Nr. 351, content not determined) applies to federal projects only (V*). Anlage 2 reuses BfN codes, adds splits and age classes J/M/A, values 0–24, ± 3 for condition (V*). Anchors: park lawn 34.09 = 8; intensive grassland 34.08a.01 = 8; species-rich hay meadow 34.07a.01 = 20; ruderal 39.06.x = 12–16; sealed surfaces 0; dry-stone wall 53.02.03a = 17 (V*). No roof or façade greening (checked). Four odd codes need a gazette check.
- BayKompV (07.08.2013, amended 23.06.2021; not for Bauleitpläne, V*) uses the *Biotop- und Nutzungstypen* (BNT) of the Biotopwertliste of 28.02.2014 (V): *Grundwert* 0–15 = G + W + N; mapping sub-types appended (`G214-GU651E`); settlement types impact-side only except P1, P43, V23, V33, V5. LfU re-mapped sub-types in 09/2021 and announced an update (V).
- Lawn to species-rich meadow (V): G4 (3) → G11 (3) → G211 (6) → G212 (8) → G213 (8) → G214 (12), by nutrient-poverty indicators, meadow forbs per 25 m² and mowing. The 2022 mapping key tests protected "GU" meadows differently (≥ 12 or 9 species on 3 m × 10 m); a freshly sown flower meadow is not GU.
- § 30 Abs. 2 BNatSchG (V*): seven groups; Nr. 7 adds lean hay meadows (Annex I), orchard meadows, stone ridges and dry-stone walls (date R). Art. 23 BayNatSchG (V*; valid from 01.04.2026; effect of the act of 26.03.2026 not determined) adds, among others, land reeds, thermophilous fringes, lean grassland, tall-stem orchards from 2,500 m² and species-rich permanent grassland.
- FFH Annex I (V): BfN list, names of 13.05.2013; 93 of 231 types occur in Germany (V*).
- Berlin: about 7,480 types with 5–8-digit codes; map 05.08 (2024) with 24 legend colours matching the SLD (V). Other Länder keys remained R.

**How ulg uses it**

- `bkompv` (dotted fallback, values per age class), `baykompv` (points, "+1" flag, sub-types incl. 2021 re-mapping), `ffh_lrt` (41 types, priority flag), `berlin_biotope` (legend classes and colours).
- Elements follow code families: grass family (`lawn` … `grassland_intensive`), `grassland_fallow`, `dry_grassland`, `meadow_wet`, `ruderal`, `tall_forbs`, `reed`, `sedge_marsh`, `bog`, `salt_marsh`, `aquatic_vegetation`, `hedge`, `hedge_clipped`, `wood_pasture`, woodland variants, trees. The `biodiversity` attribute is declared "a rough house heuristic … not a valuation".
- `protected_biotope` and `compensation_area` are overlays.

**Limits and open points**

- `protected_biotope` is green; verified practice is red/magenta (Bavarian viewer #D97EB0 / #EECACF / #FCEBFD, outline #EE5AC7; Berlin red cross-hatch) [02 §8.1, §8.3, §11.5].
- No neophyte stand, pollard tree or native/non-native shrub split, although both lists split them.
- BKompV rows are V*; the 2014/2022 Bavarian thresholds are not aligned; the Art. 23 definition ordinance was not retrieved.

### 3.4 Landscape-planning symbols

**What the standard says** [02 §7, notes/02 §C]

- BfN-Skripten 461/2 *Planzeichenkatalog* (Hoheisel et al. 2017, DOI 10.19217/skr4612) and 486 on GIS use (2018, DOI 10.19217/skr486) were read (V); 461/1 was not. A recommendation, not a statutory symbology.
- Rules (V): a pastel "Kulisse" (backdrop) series without outline for low–moderate value and a saturated series with black 2 pt outline for high value; objects below 1 ha (grassland, water) become 16 pt point symbols; **overlays instead of new colours** – wet = offset dashed blue lines, fallow = vertical dashed brown lines, orchards = red dot grid; protection by label; target areas at 50 % transparency; proposals without contour; no measure symbols. 1 pt = 0.35 mm; minimum outline 0.5 pt.
- Pastel values (V): grassland #D2F098, dry grassland #FFFFA1, shrubs and hedges #BEF583, coniferous forest #87BA78, reeds #FFAF5E, fringes and ruderal #DDC0EC, heath #FFB5C2, arable #F2DFB0, settlement green #ABF6B4, settlement #EBC1B0, standing water #C5E9FF. The deciduous-forest row repeats the grassland value – a probable misprint; take it from the BfN QGIS file.
- Licences: 461/2 CC BY-ND 4.0 (V*), 486 all rights reserved (V); values are citable, symbol files should not be bundled.

**How ulg uses it**

- `bfn` theme: pastel series, flat, no area outlines except water, trees, buildings and the grey context layers.
- House textures take the overlay idea: `grassland_fallow` has a vertical dashed hatch, `meadow_wet` and `sedge_marsh` a blue wave texture.
- All symbols are drawn by the library; `src/ulg/data` holds only JSON and Markdown.

**Limits and open points**

- The theme uses the coniferous value for all forests (documented) instead of the value from the BfN style file.
- Saturated series, area-to-point substitution and the contour rule are not implemented.
- Orchards use crowns, not the red dot grid; reeds use the grey-teal house `reed` family, not BfN orange (a "periphery" class, 02 §8.6).

### 3.5 Open-space object catalogues and technical typologies

**What the standard says** [05]

- FLL *Objektartenkatalog Freianlagen* (OK FREI; open-space object catalogue): the 2025 edition follows DIN 276:2018-12 with three service levels (V), but every public code is from the 2016/2018 numbering (S); no 2025 code was verified. SK FREI (2016, 1:500–1:200) exists (V).
- DIN 276:2018-12 KG 500 (S): 530 *Oberbau, Deckschichten*, 540 structures, 550 technical systems, 560 fittings, 570 *Vegetationsflächen* (573 planting, 574 lawn and seeding), 580 water; building greening moved to KG 335/353/363. The same digits mean different things in the 2008 edition.
- DIN 18917:2018-07 (V) distinguishes four *Rasentypen* (lawn types): ornamental, utility, hard-wearing, landscape (table S). RSM Rasen 2026 (48th ed.) lists the standard mixtures (V). No standard separates lawn from meadow; practice uses mowing frequency (utility lawn 8–20 cuts, meadow 1–3, S). § 40 BNatSchG requires regional seed in the open landscape since 1 March 2020 (V).
- DIN 18916:2016-06 and DIN 18919:2016-12 (V) govern planting and aftercare. FLL green-roof rules 2018 (intensive, simple-intensive, extensive) and façade rules 2018 (ground-based, wall-bound) (V).
- Surfaces: ZTV-Wegebau 2022, FLL water-bound paths 2007, FLL permeable surfaces 2018 (V); product-standard editions not verified. Bond geometry is mostly R; "Passe" is unverified. Tree-pit figures (12 m³, 1.5 m, 6 m²) were not confirmed (R).
- HOAI Anlage 11: design 1:500–1:100, construction drawings 1:200–1:50 (V); landscape plans have no prescribed scale (V).

**How ulg uses it**

- `din276` crosswalk: third-level cost groups (S), with the 2008 renumbering noted; most non-area groups map to `none`.
- Names and aliases follow this vocabulary (`lawn` = Gebrauchs-/Zierrasen, `lawn_extensive` = Landschaftsrasen, `flower_lawn` = Kräuterrasen, `perennials`, `bedding`, `hedge_clipped`, `gravel_turf`, `grass_pavers`, `waterbound`, `swale`, `rain_garden`, `planter` …).
- Paving textures are lattices in metres: stretcher bond 10 × 20 cm (`concrete_pavers`), 40 × 40 cm grid (`slabs`), herringbone (`clinker`, `paving_light`), random courses (`natural_stone_paving`, `cobblestone`), planks (`wood_deck`).
- LOD breaks 1:750 / 1:2,500 / 1:10,000 bracket the HOAI and SK FREI scales.

**Limits and open points**

- No OK FREI crosswalk (2025 codes unknown).
- Missing: simple-intensive green roof, plastic grass grids, *Baumrigole* (tree trench); both façade types share `green_facade`; containers exist only as the point symbol `planter`.
- Bond textures are illustrations, not specifications.

### 3.6 European and international classifications

**What the standard says** [03]

- CORINE: 44 classes, MMU 25 ha, a context layer for cities (V); CLC 2024 announced for Q3 2026, not yet listed. Green urban areas are pink (#FFA6FF).
- Urban Atlas 2021 (790 FUAs, 3-year cycle, MMU 0.25 ha urban): urban fabric split only by sealing degree (five red steps); green urban areas split by access in 2021; Street Tree Layer = tree patches ≥ 500 m² (V).
- CLC+ Backbone: 10 m raster, 11 land-cover classes after EAGLE; class 1 includes vegetated roofs and railway tracks; grass pavers → 9; vines and hops → 5 (V).
- Regulation (EU) 2024/1991, Art. 8 (V, verbatim in the stream): no net loss of urban green space and canopy by 31.12.2030 against 2024; increasing trends from 2031, measured every six years; satisfactory levels by 2030; guiding framework by 31.12.2028. The non-binding note (v2.0, 07/2026): green space = CLC+ 2023 classes 2, 3, 4, 5, 6, 8, 10; canopy = HRL Tree Cover Density 2024, including street trees; green-roof inventories allowed as supplementary data.
- EUNIS: revised 2021/2022 except C, J and X (2012 codes current); 2012 codes have a dot (E2.64), revised codes none (V31); colours only for 2012 levels 1–2 (V*). Only EUNIS separates lawn, hay meadow and species-rich grassland.
- EU ecosystem typology (Eurostat 07/2026; level 1 by Reg. 2024/3024): *urban greenspace* excludes sealing above 30 %; no official colours (V).
- INSPIRE (V): Land Cover has no nomenclature and an informative 18-component colour map; Land Use prescribes six HILUCS level-1 colours; Habitats uses grey. Five relations for local vs reference types: congruent, includedIn, includes, overlaps, excludes.
- LUCAS 2022: separate cover and use axes, no colours (V). LCZ palette A declared official (V), palette B circulates (S). ESA WorldCover v200: urban green is not built-up (V).

**How ulg uses it**

- Crosswalks `clc`, `urban_atlas`, `clcplus`, `eunis` (both generations), `hilucs`, `lucas`, `lcz`, `esa_worldcover`; colours via `ulg.official_colors()`.
- `nrr_urban_green` follows the CLC+ logic (vegetation and water true; arable, sealed, bare ground, green roofs false); `tree_canopy` and point trees count as canopy over any surface; `indicators()` returns `nrr_green_share` and `canopy_share`.

**Limits and open points**

- No CORINE, Urban Atlas, CLC+, HILUCS, LCZ or WorldCover *theme*.
- NRR flags that conflict with CLC+: `vineyard` false (vines are class 5, counted); `green_track` true (tracks are class 1); `retention_basin` false (open water and vegetated basins count). The `settings.json` statement that pools do not count is not in stream 03.
- Missing: moss/lichen cover (CLC+ 8, counted; mapped to `dry_grassland` as nearest) and an urban-fabric sealing ramp. Ports, airports, salt marsh, mudflats, dunes, and snow and ice have elements.
- Stream 03 recommends a red "sealed" rendering for sealing maps; the `sealing` ramp runs green → grey.
- EUNIS 2012 → 2021 correspondences are name-based (A).

### 3.7 OpenStreetMap and national large-scale models

**What the standard says** [04]

- OSM (V): cover from `landuse`/`natural`/`leisure`, material from `surface` (45 documented values), detail from `leaf_type`, `diameter_crown`, `wetland`, `meadow`, `basin`, `green_roof`. Hooks: `meadow=wildflower`, `wetland=reedbed`, `surface=wood`. Counts: `natural=tree` 34.3 million, `landuse=grass` 7.7 million, `landuse=flowerbed` 159,370; `landcover=*` is marginal. Green roof = `green_roof=yes`, `roof:material` grass/plants/roof_greening or `garden:type=roof_garden`.
- OSM Carto v6.1.0 (V): @grass #CDEBB0, @forest #ADD19E, @park #C8FACC, water #AAD3DF; shrubbery, greenery and surfaces not rendered.
- BGT/IMGeo: the finest official material vocabulary; *standaard*, *achtergrond* and *pastel* colour sets (V); polygons stroked in their fill colour.
- Swiss AV: colour optional, black-and-white mandatory for the land-register plan; 2024 RGB (buildings #FFBFBF, water #B3E6FF, forest #9CFF9C at 50 %); soft covers dashed (V-img).
- Austrian DKM: 26 use classes as glyphs, no fills; the drawing key is "rechtlich nicht verbindlich" for DKM display (V-img).
- England: metric tool v1.0.4 scores 21 urban habitat types (V); the UKHab palette is licence-gated.
- Prior art: LBP-Musterlegendenkatalog (12/2021; 35 % transparency over aerials; hatch in the target colour for new planting) and OS "Outdoor style" (V-img/V). Lessons: few hues, many textures; paving rarely coloured; state modifiers; function as overlay [04 §8.4].

**How ulg uses it**

- `osm` crosswalk (tag combinations before single tags); `osm` theme (derived values marked D).
- `bgt`, `swiss_av`, `at_dkm`, `uk_metric`, `ukhab` crosswalks; colours only for BGT and Swiss AV.
- Elements close the gaps stream 04 lists: `hedge`, `tree_row`, `wall`, `fence`, furniture, `garden`, `permeable_paving`, `waterbound`, `clinker`, `artificial_turf`, `swale`, `rain_garden`, green roofs, `unknown`.
- Soft vegetation meets without dark lines (outline = fill darkened 10 %); paving differs by texture in a narrow grey-warm range.

**Limits and open points**

- The `osm` theme's outlines #B5CF9B, #A6D9AA, #90B983, #89B8C6, #D5CBC1 are not in stream 04, though the theme says "Hex values V".
- No UKHab colours (licence); UKHab codes partly S.
- No "over orthophoto" variant and no line-plus-glyph cadastral theme (04 §8.4).

### 3.8 Coefficients

**What the standard says** [06 §A]

- Berlin BFF = ecologically effective area ÷ plot area (V). 2021 list (16 types): sealed 0.0; partly sealed 0.1 (setts, clinker, water-bound); permeable 0.2 (drainage pavers, sand, crushed stone); vegetated paving 0.4; vegetation on soil 1.0 (down to 0.5 for plain ornamental lawn); over structures 0.5–0.9 by depth; infiltration 0.2; water 0.5; roofs 0.5/0.7/0.8; façades 0.5/0.7 (V). Worked examples: 0.04, 0.45, 0.45, 0.6. The 1990 list (9 types, partly sealed 0.3, roofs 0.7) still governs older plans (V).
- Comparable: London UGF (S), Seattle (V/R), Swedish GYF (S), Graz (V). In Bavaria municipalities may since 01.10.2025 only *prohibit* sealing and gravel gardens (Art. 81 BayBO; V/S), so a BFF is an indicator there, not a local rule.
- *Abflussbeiwerte* (runoff coefficients): DIN 1986-100:2016-12, Tabelle 9, Cs and Cm – values S; draft 2025-06 exists. DWA-A 138-1 (10/2024) adds rows (S); its sports rows differ.
- *Versiegelung* (sealing): no statutory classes (UBA, V); Berlin *Belagsklassen* 1–4 (V); bdla five classes (V). Albedo and emissivity: PALM 6.0 (V), with a 0.17 placeholder for most pavements.
- One texture is not one coefficient; BFF rewards vegetation, runoff permeability; never derive one from another.

**How ulg uses it**

- `settings.json` documents `sealing`, `bdla_class`, `bff`, `bff_1990`, `runoff_cs`, `runoff_cm` (S), `albedo`, `emissivity`, `belagsklasse`, `nrr_urban_green` with source and mark.
- Values match stream 06's table: asphalt BFF 0, Cs/Cm 1.0/0.9; paving in sand 0.1 (1990: 0.3), 0.9/0.7; grass pavers 0.4, 0.4/0.2; water-bound 0.1, 0.9/0.7 ("Do not derive one from the other"); lawn 1.0, 0.2/0.1; extensive roof 0.5, 0.5/0.3. Notes name exceptions (water, track ballast from DWA-A 138-1).
- `indicators()` returns sealing shares, BFF (ground plus roof credits over the plot), runoff, albedo and `*_coverage` where values are missing. Brochure example A is a unit test.

**Limits and open points**

- Runoff values are secondary; PALM pavement albedo is a placeholder.
- Only one of four brochure examples is tested; no UGF, GYF, Graz or DWA-A 102-2 attributes.
- `bdla_class` 3 for paving in sand is a documented house choice.

### 3.9 Drawing and graphic standards

**What the standard says** [06 §B, §C11; 01 §1.4]

- ISO 11091:1994 / DIN EN ISO 11091:1999-10 (V): black-and-white only; existing thin, proposed thick; protected area thick chain line (square frame around a crown); removal thin dashed diagonal hatch; existing tree = thin crown and thick trunk, to scale; proposed tree = thick circle with thin centre cross, **not** to scale; grass light stipple; hedges thin zigzag / thick wavy; paving patterns "representational only".
- DIN 1356-1:2024-04 was withdrawn for DIN EN ISO 7519:2025-01; E DIN 1356-1:2026-09 would restore it (V). Line groups II (0.5/0.35/0.25 mm, text 3.5) and III (1.0/0.5/0.35, text 5.0) (S).
- BauVorlV Bayern, Anlage 1 (V): plot boundary violet long dash; existing grey (single hatch); planned red (cross-hatch); removal yellow (× on outline); setback areas brown; words only; signs *or* colours.
- DIN 18920:2014-07 (V): *Wurzelbereich* (root zone) = ground under the *Kronentraufe* (crown drip line) + 1.50 m, columnar + 5.00 m; trenches ≥ 4 × *Stammumfang* (girth at 1.00 m), ≥ 2.50 m for stems under 20 cm. The 2026-06 edition is current; secondaries give the same rule (S). BS 5837: 12 × stem diameter (S).
- Minimum sizes for map graphics were not verified (R).

**How ulg uses it**

- `tree` (crown to scale, stem to scale when known); `tree_planned` (0.35 mm red outline, cross in an open ring) and `shrub_planned` (same motif); `tree_protected` (filled centre, chain-line square); `tree_remove` (pale yellow, dashed, crossed out).
- `status_planned` (single hatch, red) and `status_removal` (cross-hatch, yellow): colour always with a motif.
- `root_protection_zone()` buffers crowns by 1.5 m (5.0 m columnar) and adds `min_trench_distance_m = max(4 × girth, 2.5 m)`; tested.
- `settings.line_weights`: ISO 128 series 0.13–1.0 mm, outline default 0.18 mm; `mono` theme; `embankment` hachures; `lamp` after the ISO luminaire.

**Limits and open points**

- `tree_planned` has a nominal 6 m crown; ISO 11091 draws proposed trees not to scale.
- `tree_remove` cites ISO 7518 (content R); the × is verified through the BauVorlV.
- `analysis.py` cites DIN 18920:2014; the girth field is used whatever its measuring height (DIN 1.00 m, OSM 1.3 m).
- The status hatches do not follow the BauVorlV signs: `status_planned` has a single hatch (BauVorlV: cross-hatch; the single hatch marks existing parts), `status_removal` a cross-hatch (BauVorlV: × marks on the outline; ISO 11091: thin dashed hatch).
- `site_boundary` is neutral solid, not violet long dash; setback areas are missing; the root-protection line is dashed, not chain.
- Minimum sizes unverified; ulg only leaves polygons under 3 mm² on paper untextured.

### 3.10 Urban-climate map conventions

**What the standard says** [06 §C10]

- VDI 3787 Blatt 1:2026-10 replaces Blatt 1:2015-09 and Blatt 9:2004-12 (V; content not read); Blatt 2:2022-06 covers PET (V); Blatt 12 on visualisation is a project, possible publication 2027-03 (V).
- *Klimatope* (climatopes) are verified from the Klimaatlas Region Stuttgart, which says it largely follows VDI 3787 Blatt 1: water, open land, forest, park, garden city, suburban, urban, city core (*Stadtkern*), commercial, industrial, railway; its colours are atlas defaults, not VDI values (V). LfU Rheinland-Pfalz derives 12 operational classes from ATKIS, sealing and height (V).
- UTCI limits −40/−27/−13/0/9/26/32/38/46 °C (V); PET 4/8/13/18/23/29/35/41 °C (S). No standard colour scale exists.

**How ulg uses it**

- `settings.categories`: `klimatop` (11 classes in a house version of the usual hue order: water blue → pale mint → green → apricot → orange → light red → red → magenta/dark red); `utci` (10) and `pet` (9) in the house `cool` and `heat` ramp colours; `ulg.category_of()` classifies values.

**Limits and open points**

- "Class names follow VDI 3787 Blatt 1" rests on the atlases' statement. ulg says *Innenstadt-Klimatop* where Stuttgart has *Stadtkern-Klimatop* (RLP: *Innenstadtklima*).
- Cold-air hatches and air-flow arrows are not catalog elements; revisit colours when Blatt 12 appears.

### 3.11 Rendering, interoperability and accessibility

**What the standard says** [07]

- QGIS (V): latest 4.2.3, LTR 3.44.15, LTR 4.4.0 scheduled 2026-10-30 (a 2025 blog had named 4.2 as the first 4.x LTR); no documented XML change between 3.x and 4.x; `<prop>` and `<Option>` both read; `RandomMarkerFill` needs a non-zero seed; `wave_randomized` (3.24) draws seeded waves; SVG can be embedded. Files were not loaded in QGIS during the research.
- OGC (V): SLD 1.0 and SE 1.1 are the only widely implemented encodings; no standard spacing, randomness or hatching; GeoServer vendor options fill the gap. INSPIRE view services (TG 3.3.0): harmonised layers keep their default style; additional styles are recommended, with legends per language.
- Converters carry no random fills, SVG tiles, seeds or generators (V/S). MapLibre (V): power-of-two patterns; pattern fills need a separate outline layer; no random expression.
- Hand-drawn rendering: rough.js caps jitter at a tenth of a segment and can keep vertices (V); SVG displacement filters fail in Qt SVG and CairoSVG and move the fill edge, so use geometric wobble (V/D); a prototype showed shared edges drawn twice with different seeds read as double lines (T).
- DTCG 2025.10 is stable; colours are objects with colour space, components and optional hex; no pattern type (V).
- Accessibility (V): WCAG 2.2 SC 1.4.1 (G111 colour and pattern), SC 1.4.11 (3:1; G209 boundaries), SC 1.4.3 (text 4.5:1). EN 301 549 V4.1.1 adopts WCAG 2.2 but is not yet cited; V3.2.1 remains the reference. ΔE00 = 10 recommended (Brychtová & Çöltekin 2016); Machado et al. (2009) CVD matrices in linear RGB.

**How ulg uses it**

- QGIS: categorized or rule-based QML (`lod="auto"`: LOD child rules with `scalemindenom`/`scalemaxdenom`), style-library XML, GPL palette; each fill = `SimpleFill` + embedded `SVGFill` tile + outline; hand-drawn outline = `GeometryGenerator` with `wave_randomized($geometry, 4, 12, 0.03, 0.09, $id + 1)`; crowns as SVG markers in map units. `tools/qgis_render.py` loads and renders the styles in QGIS as a smoke test.
- SLD 1.0.0: solid fill, `GraphicFill` tile, outline, external SVG points. MapLibre: 128 px sprite plus `@2x`; fill → pattern (from z 15.5) → outline; tree circles sized in metres by base-2 zoom interpolation. Tokens: DTCG colour objects with aliases, CSS `--ulg-<element>-<role>`, `catalog.json`.
- Renderer: exact fills; outline wobble from a ground-anchored noise field (shared edges wobble identically), amplitude 0.09 mm for the 0.18 mm line; hash-based randomness anchored to world coordinates.
- `check.py` at the time of writing: 112 land-cover elements; 2,162 pairs below ΔE00 10, none without a texture or outline difference; 3,438 / 3,436 / 3,171 close pairs under protanopia / deuteranopia / tritanopia, again none. `Options.accessible()` darkens outlines and marks to 3:1.

**Limits and open points**

- QML is written in `<Option>` form only (stream 07 suggests the dual form); SLD has no SE 1.1 variant, vendor options or per-LOD scale limits.
- Stream 07 proposes an amplitude strictly below half the stroke, capped at a tenth of each edge, with a Hausdorff test; ulg uses exactly half and bounds x and y separately, so a diagonal offset can reach about 0.13 mm.
- `check.py` does not require texture ink ≥ 3:1 (weakest default mark 1.08:1, `sports_turf`) or test labels; no legend table for non-visual use.

## 4. Design decisions that follow from the research

1. **Official colours only where published and verified.** Official themes name source and evidence (a test enforces the source); crosswalk `color` fields hold only a publisher's own legend colours. The documented exception: EUNIS colours sampled from legend swatches (V*).
2. **Law gives words, the convention gives numbers.** `planzv` uses xPlanBox values, never the scan samples.
3. **Codes are never guessed.** An element gets a code only through a crosswalk entry with a fit grade; classes without an equivalent are `nearest` or `none`. `crosswalk.validate()` checks ids, grades, colours and duplicates.
4. **Editions travel with codes.** Every crosswalk carries its version; AAA, NAK and LB/LN are separate files; EUNIS entries name their generation; `din276` flags the 2008 renumbering.
5. **An element stands for a code family.** Valuation crosswalks store values per age class and condition instead of multiplying elements.
6. **Coefficients are never interpolated.** Missing values appear as coverage below 1 (`analysis.py`; test `test_unknown_coefficients_are_reported_not_guessed`).
7. **Every coefficient names source, edition and evidence** in `settings.json`; BFF 2021 and 1990 sit side by side.
8. **Indicators are not derived from each other.** BFF and runoff stay separate where they disagree.
9. **Permeability, not paving colour, carries ecological meaning.** Light and dark paving share coefficients; `sealing`, `bdla_class`, `belagsklasse` and `bff` separate sealed, permeable and vegetated surfaces.
10. **The fill is the exact geometry.** Wobble moves only the outline, by about half the default line width (0.09 mm for 0.18 mm, renderer and QGIS), so the ink stays on the true boundary and the data stay GIS-exact; official themes set `handdrawn` to 0.
11. **Randomness is deterministic and anchored to the ground**, so neighbours share one texture, tiles do not change it, and QGIS gets non-zero seeds.
12. **Texture is the second channel.** Fill pairs closer than ΔE00 10 – in normal vision and three simulated CVDs – must differ in texture or outline; an accessible option gives 3:1.
13. **Status uses motif and colour together**: ISO 11091 weights, PlanZV centres, the BauVorlV colour triad; colour always comes with a hatch or symbol motif (the hatches differ from the BauVorlV signs, see 3.9).
14. **Overlays are not land cover**; roof elements replace the building surface in indicators.
15. **Canopy is measured separately from ground cover**, as the NRR does.
16. **Legal protection is an overlay**, never a replacement fill.
17. **Scale drives detail**: LOD breaks 1:750 / 1:2,500 / 1:10,000; marks in paper millimetres, paving modules in metres; tiny polygons stay flat.
18. **Line widths come from the ISO 128 series.**
19. **Symbols are drawn by the library**; no BfN, xPlanBox or UKHab symbol files are bundled.
20. **Each target is written natively**; what a format cannot express degrades to fill, tile and plain outline.

## 5. Open points and licences

### 5.1 Not verified

- **Planning and cadastre:** numeric PlanZV colours in Länder guides; legal force of XPlanung; AdV reference version; ATKIS SK25–100; signature shapes; LBM-DE cross table [01 §6].
- **Biotopes:** content of the BKompV amendment of 22.12.2025; four odd BKompV codes; other Länder keys (R); Berlin class names; Art. 23 definition ordinance; date of the § 30 extension (R); BfN deciduous-forest value; BfN 461/1 [02 §10].
- **Europe:** CLC 2024 release; LCZ palette of other tools; official EUNIS crosswalks; newer LUCAS; WorldCover successors; EAGLE numbering; INSPIRE LU SLDs [03 §12].
- **National models:** UKHab palette and v2.1 status; DMAV files; Austrian drawing key; OSM values read through extraction [04 §9].
- **Open space:** OK FREI 2025 codes; DIN 276 notes; DIN 18917 table; product-standard editions; tree-pit figures; bond geometry; HOAI successor [05].
- **Coefficients and drawing:** DWA-A 138-1 original table; DIN 1986-100 successor; DWA-M 102-4 shares; climate colours; minimum sizes (R); DIN 18920:2026-06 wording; ISO 7518 content [06].
- **Rendering:** QGIS round trip not done in the research; QGIS 4 compatibility inferred; MapLibre pattern behaviour from issue threads; accessibility reading interpretive [07 §8].

### 5.2 Paywalled or purchase-only

DIN 276, 18916, 18917, 18919, 18920:2026-06, 1986-100, 1356-1, ISO 11091 (preview only), DWA-A 138-1, VDI 3787 Blatt 1:2026-10, the FLL rules, the OK FREI 2025 file (10 €) and SK FREI (500 € per platform) [05, 06]. Values from reproductions are marked S.

### 5.3 Licences

| Source | Licence as recorded in the streams | Consequence |
|---|---|---|
| PlanZV | official work (§ 5 UrhG) (V) [01 §1.2] | free to reuse |
| xPlanBox styles | GNU AGPL v3 (V) [01 §2.6] | hex values are facts; symbols not copied |
| basemap.de | "© 2026 basemap.de / BKG \| Datenquellen: © GeoBasis-DE" (V) [01 §4.3] | attribute when using the theme |
| BfN-Skripten 461/2 / 486 | CC BY-ND 4.0 (V*) / all rights reserved (V); GIS package unclear (V*) [02 §7.1] | cite values; do not bundle symbols |
| Berlin biotope map | Datenlizenz Deutschland – Zero 2.0 (V*) [02 §8.3] | free use |
| LfU Bayern biotope WMS; RLP and LfU climate data | CC BY 4.0 (V*; V) [02 §8.1, 06 §C10] | attribution |
| OS MasterMap style workbook | Open Government Licence 3.0 (V) [04 §7.1] | attribution |
| UKHab | licence-gated; no onward licence via the metric (V / V-img) [04 §6] | codes for reference only |
| Swiss "Cadastra" font | open source, may be modified if renamed (V-img) [04 §4.2] | not bundled |

The streams record no licence for the ALKIS/ATKIS catalogues, OSM Carto or the EEA/Copernicus legends; ulg uses only codes and colour values from them.

### 5.4 What to re-check when standards change

| Watch | State on 2026-09-30 |
|---|---|
| PlanZV; XPlanung | amended 12.08.2025; 6.1, removals announced for 7 |
| AAA / LB / LN; ALKIS-SK; ATKIS-SK; basemap.de; LBM-DE | 7.1.2 / 1.0.1 / 1.0.2; 2.1.0; 2.1.3; style 5.0.3; 2021, 3-year cycle |
| BKompV; Biotopwertliste; Art. 23 BayNatSchG | amended 22.12.2025; 2014, update announced; changed 26.03.2026 |
| OK FREI; RSM Rasen; FLL roof rules; DIN 276; HOAI | 2025 codes unknown; annual; revision since 10/2025 (S); 2018-12; successor in preparation (S) |
| CORINE; Urban Atlas; CLC+; NRR | CLC 2024 due Q3 2026; UA 2021 (manual names 2024); biennial; framework due 31.12.2028 |
| EUNIS; LUCAS; WorldCover; LCZ | C, J, X unrevised; 2022; v200; v3.0.0 |
| OSM Carto; BGT; Swiss AV; UK metric; UKHab | v6.1.0; rules 2.3; DMAV 1.0; tool v1.0.4; v2.1 unclear |
| BFF; DIN 1986-100; DWA-A 138-1 | 02/2021; draft 2025-06; 10/2024 (M 138-2 draft 10/2025) |
| DIN 18920; DIN 1356-1; BS 5837; VDI 3787 | 2026-06; E 2026-09; revision 11/2026; Blatt 12 possible 2027-03 |
| QGIS; DTCG; EN 301 549 | LTR 4.4.0 due 2026-10-30; 2025.10; V4.1.1 awaiting OJEU citation |

## 6. Sources

All sources are the research streams in [`streams/`](streams/); primary URLs are listed there.

- **Stream 01** – [01_de_planning_cadastre.md](streams/01_de_planning_cadastre.md): §1 PlanZV (1.1 version, 1.2 § 2, 1.4 open-space Planzeichen, 1.5 sampled colours); §2 XPlanung (2.1, 2.3 enumerations, 2.5 landscape-plan model, 2.6 xPlanBox); §3 ALKIS/ATKIS (3.2, 3.3b NAK, 3.6 LB/LN); §4 official colours (4.1 ALKIS-SK, 4.2 ATKIS-SK10, 4.3 basemap.de); §5 LBM-DE; §6 open points; §7 implications.
- **Stream 02** – [02_de_biotope_landscape_planning.md](streams/02_de_biotope_landscape_planning.md): §0 key findings; §1 Red List; §2 BKompV; §3 BayKompV; §4 other Länder; §5 protected biotopes; §6 FFH; §7 BfN Planzeichen; §8 official map conventions; §9 lawn–meadow criteria; §10 open points; §11 implications. Notes: [02_biotope_working_notes.md](streams/notes/02_biotope_working_notes.md).
- **Stream 03** – [03_eu_classifications.md](streams/03_eu_classifications.md): §0.3 versions; §1 CORINE; §2 Urban Atlas; §3 CLC+; §4 NRR; §5 EUNIS; §6 ecosystem typologies; §7 INSPIRE; §8 LUCAS/EAGLE; §9 LCZ, WorldCover; §10 crosswalks; §11 portrayal; §12 open points; §13 implications.
- **Stream 04** – [04_osm_national_topo_prior_art.md](streams/04_osm_national_topo_prior_art.md): §0 versions; §1 OSM tags; §2 OSM Carto; §3 BGT; §4 Swiss AV; §5 DKM; §6 prior art; §7 other conventions; §8 implications; §9 open points. Notes: [04_osm_topo_working_notes.md](streams/notes/04_osm_topo_working_notes.md).
- **Stream 05** – [05_de_freianlagen_typologies.md](streams/05_de_freianlagen_typologies.md): §1 OK FREI; §2 DIN 276; §3 lawns; §4 planting and greening; §5 trees; §6 surfaces; §7 bonds; §8 HOAI; open points; implications.
- **Stream 06** – [06_coefficients_drawing_standards.md](streams/06_coefficients_drawing_standards.md): watchlist; §A1–A4 coefficients; §B5–B9 drawing standards; §C10–C11 climate maps, minimum sizes; open points; implications.
- **Stream 07** – [07_rendering_interop.md](streams/07_rendering_interop.md): §0 versions; §1 QGIS; §2 OGC, GeoServer, INSPIRE; §3 web libraries; §4 hand-drawn rendering; §5 tokens; §6 accessibility; §8 open points; recommendations.
- **Library** – `src/ulg/data/elements/`, `settings.json`, `palette.json`, `themes/`, `crosswalks/` ([format](../reference/crosswalk-format.md), [element list](../reference/element-list.md)); code in `src/ulg/` (`analysis.py`, `check.py`, `colormath.py`, `crosswalk.py`, `export/`, `render/`).

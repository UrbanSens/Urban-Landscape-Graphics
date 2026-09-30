# 03 – European / international land-cover, land-use and habitat classifications

Research stream 3 for the standards conformance of **Urban Landscape Graphics** (house style "UrbanSens – Ecological Vector Style").
Research date: **2026-09-30**. Scope: CORINE Land Cover, Urban Atlas, CLC+ Backbone, Nature Restoration Regulation, EUNIS, MAES / EU ecosystem typology, INSPIRE (LC, LU/HILUCS, HB), LUCAS, EAGLE, Local Climate Zones, ESA WorldCover, and the crosswalks between them.

## 0. How to read this file

### 0.1 Evidence marks

| Mark | Meaning |
|---|---|
| **V** | Verified by me in a primary source during this session (raw page text, registry JSON, map-service style JSON, or a legend image I looked at). Source URL given. |
| **S** | Taken from a secondary source or from a machine summary of a primary source (not read raw). Source URL given. |
| **R** | Recalled from memory, **not verified** this session. Treat as a hypothesis. |
| **A** | Author's assessment / interpretation (e.g. "relevant inside cities", name-based correspondences). Not a statement of any source. |

Colour values carry **V only if I saw the numbers** in an official legend, style file, service renderer or specification. Hex values are my own conversion of verified RGB triples.

### 0.2 Method notes

- Primary sources were read as raw text through a browser (not through a summarising model) wherever possible; legend tables that exist only as images were opened and read visually.
- Official colours for CLC and Urban Atlas were taken from the **renderer definitions of the EEA's own ArcGIS map services** (JSON `drawingInfo`), which carry numeric RGBA values per class code; the Urban Atlas 2021 legend from the **SLD returned by `GetStyles`** of the CLMS web map service. Where a service offers only legend swatch images (EEA ecosystem-type map, section 5.6), the centre pixel of each swatch was sampled and the value is marked V*.
- All RGB/hex pairs in this file were checked by script for internal consistency, and the CLC and Urban Atlas tables were compared by script against the saved service responses (44 of 44 and 27 of 27 classes identical).
- The web-search budget of the session was exhausted part-way through; remaining gaps were closed by opening known primary URLs directly. Items that could not be verified are listed in section 12 (Open points).
- Class names, codes and RGB triples are nomenclature facts and are reproduced exactly. Definitions from product manuals are paraphrased. Legal definitions of Regulation (EU) 2024/1991 are quoted verbatim with article numbers, as requested.

### 0.3 Version status on 2026-09-30

| Scheme | Current state found | Mark | Source |
|---|---|---|---|
| CORINE Land Cover | Latest published status layer is **CLC 2018**; product page lists 1990, 2000, 2006, 2012, 2018 (+ change layers). Roadmap tab: production for reference year **2024** started Q1 2025, planned to finish Q1 2026, publication "scheduled for … Q3 2026"; "thematic scope and the geographical coverage will remain the same". CLC 2024 was **not yet listed** among the datasets on the day of research. | V | https://land.copernicus.eu/en/products/corine-land-cover (tabs Datasets, Roadmap) |
| Urban Atlas | **UA 2021** is published (status 2021, change 2018–2021, revised 2018, Street Tree Layer 2021, Building Block Height 2021). 790 FUAs. Update cycle now **3 years** (was 6). Manual title already refers to "Urban Atlas 2021 and 2024". PUM published 2026-02-05, version 1.0.2. | V | https://library.land.copernicus.eu/products/Urban_Atlas_CLMS_UA2021_LULC_PUM_v1.html |
| CLC+ Backbone | Raster products for **2018, 2021 (without UK), 2023** (UK re-included). From 2023 **biennial**. PUM 2023 published 2025-04-01 (v1.3.1); PUM 2021 published 2025-06-12 (v1.2.2). | V | https://library.land.copernicus.eu/products/CLCplus_Backbone_2023_PUM_v1.html |
| Nature Restoration Regulation | Regulation (EU) 2024/1991 of 24 June 2024, OJ L of 29.7.2024. Commission/EEA methodological note on Art. 8 datasets: document version 2.0, last update 07/07/2026. | V | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401991 |
| EUNIS | The EUNIS web application (eunis.eea.europa.eu) is **retired**; content now lives in BISE. Revised classification "2021/2022" (terrestrial 2021, marine 2022) published alongside EUNIS 2012; inland waters and habitat complexes are **not yet revised**. SDI metadata last revised 2026-09-25. | V | https://eunis.eea.europa.eu/ (retirement notice); https://sdi.eea.europa.eu/catalogue/srv/api/records/638330ea-90e6-4e41-81ea-e70f25ae7117 |
| EU ecosystem typology | Eurostat Technical Note "EU ecosystem typology", **version July 2026**. Level 1 is fixed in Annex IX of Regulation (EU) No 691/2011 as amended by Regulation (EU) 2024/3024 of 27 November 2024. | V | https://ec.europa.eu/eurostat/documents/1798247/12357920/EU-ecosystem-typology.pdf/265ef6e5-b146-e501-499a-d1467f7a6a90 |
| INSPIRE Technical Guidelines | LC: D2.8.II.2 v3.1.0 (2024-01-31). LU: D2.8.III.4 (published 2024-07-31). HB: D2.8.III.18 v4.0.0 (2024-01-31). | V | https://inspire-mif.github.io/technical-guidelines/ |
| LUCAS | Latest survey with published reference documents: **LUCAS 2022** (C3 "Classification", issue 3.0 of 2022-03-01). Whether a newer survey round has published documents: not verified. | V / open | https://ec.europa.eu/eurostat/web/lucas/database/2022 |
| Local Climate Zones | Typology of Stewart & Oke (2012), 17 classes. Global LCZ map (Demuzere et al.), Zenodo version 3.0.0 published 2023-10-08, 100 m, nominal year 2018; its readme defines the "official" hex colours. | V | https://zenodo.org/records/8419340 |
| ESA WorldCover | 10 m global maps for 2020 (v100) and 2021 (v200); Product User Manual v2.0, last modified 2022-10-24. Successor products were not checked. | V / open | https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/docs/WorldCover_PUM_V2.0.pdf |

---

## 1. CORINE Land Cover (CLC)

**Product facts (V):** pan-European inventory with 44 thematic classes in three levels; minimum mapping unit **25 ha**, minimum mapping width **100 m**; change layers with 5 ha MMU; vector and 100 m raster. Source: https://land.copernicus.eu/en/products/corine-land-cover. With a 25 ha MMU, CLC is a *context* dataset for cities — it does not resolve single parks, street trees or squares.

**Official legend (V):** RGB values below are the fill colours of the unique-value renderer (field `Code_18`) of the EEA map service `Corine/CLC2018_WM`, layer 0 "Corine Land Cover 2018 vector". They are identical in all sub-layers of that service. Source: https://image.discomap.eea.europa.eu/arcgis/rest/services/Corine/CLC2018_WM/MapServer/layers?f=pjson. Class labels are taken from the same renderer. (The Copernicus nomenclature guideline at https://land.copernicus.eu/content/corine-land-cover-nomenclature-guidelines/html/ spells a few names slightly differently: "Natural grassland", "Bare rock", "Peatbogs", "Transitional woodland/shrub" — S.)

Column "City": **U** = typical inside settlements; **P** = typical in the peri-urban fringe of Central European cities; **–** = rarely relevant there (A = author's assessment).

| Code | Level 1 / level 2 | Level 3 name | R,G,B | Hex | City (A) | Mark |
|---|---|---|---|---|---|---|
| 111 | 1 Artificial surfaces / 1.1 Urban fabric | Continuous urban fabric | 230,0,77 | #E6004D | U | V |
| 112 | 1.1 | Discontinuous urban fabric | 255,0,0 | #FF0000 | U | V |
| 121 | 1.2 Industrial, commercial and transport units | Industrial or commercial units | 204,77,242 | #CC4DF2 | U | V |
| 122 | 1.2 | Road and rail networks and associated land | 204,0,0 | #CC0000 | U | V |
| 123 | 1.2 | Port areas | 230,204,204 | #E6CCCC | U | V |
| 124 | 1.2 | Airports | 230,204,230 | #E6CCE6 | U | V |
| 131 | 1.3 Mine, dump and construction sites | Mineral extraction sites | 166,0,204 | #A600CC | P | V |
| 132 | 1.3 | Dump sites | 166,77,0 | #A64D00 | P | V |
| 133 | 1.3 | Construction sites | 255,77,255 | #FF4DFF | U | V |
| 141 | 1.4 Artificial, non-agricultural vegetated areas | Green urban areas | 255,166,255 | #FFA6FF | U | V |
| 142 | 1.4 | Sport and leisure facilities | 255,230,255 | #FFE6FF | U | V |
| 211 | 2 Agricultural areas / 2.1 Arable land | Non-irrigated arable land | 255,255,168 | #FFFFA8 | P | V |
| 212 | 2.1 | Permanently irrigated land | 255,255,0 | #FFFF00 | – | V |
| 213 | 2.1 | Rice fields | 230,230,0 | #E6E600 | – | V |
| 221 | 2.2 Permanent crops | Vineyards | 230,128,0 | #E68000 | P | V |
| 222 | 2.2 | Fruit trees and berry plantations | 242,166,77 | #F2A64D | P | V |
| 223 | 2.2 | Olive groves | 230,166,0 | #E6A600 | – | V |
| 231 | 2.3 Pastures | Pastures | 230,230,77 | #E6E64D | P | V |
| 241 | 2.4 Heterogeneous agricultural areas | Annual crops associated with permanent crops | 255,230,166 | #FFE6A6 | – | V |
| 242 | 2.4 | Complex cultivation patterns | 255,230,77 | #FFE64D | P | V |
| 243 | 2.4 | Land principally occupied by agriculture, with significant areas of natural vegetation | 230,204,77 | #E6CC4D | P | V |
| 244 | 2.4 | Agro-forestry areas | 242,204,166 | #F2CCA6 | – | V |
| 311 | 3 Forest and semi-natural areas / 3.1 Forests | Broad-leaved forest | 128,255,0 | #80FF00 | P | V |
| 312 | 3.1 | Coniferous forest | 0,166,0 | #00A600 | P | V |
| 313 | 3.1 | Mixed forest | 77,255,0 | #4DFF00 | P | V |
| 321 | 3.2 Shrub and/or herbaceous vegetation associations | Natural grasslands | 204,242,77 | #CCF24D | P | V |
| 322 | 3.2 | Moors and heathland | 166,255,128 | #A6FF80 | P | V |
| 323 | 3.2 | Sclerophyllous vegetation | 166,230,77 | #A6E64D | – | V |
| 324 | 3.2 | Transitional woodland-shrub | 166,242,0 | #A6F200 | P | V |
| 331 | 3.3 Open spaces with little or no vegetation | Beaches, dunes, sands | 230,230,230 | #E6E6E6 | P | V |
| 332 | 3.3 | Bare rocks | 204,204,204 | #CCCCCC | – | V |
| 333 | 3.3 | Sparsely vegetated areas | 204,255,204 | #CCFFCC | – | V |
| 334 | 3.3 | Burnt areas | 0,0,0 | #000000 | – | V |
| 335 | 3.3 | Glaciers and perpetual snow | 166,230,204 | #A6E6CC | – | V |
| 411 | 4 Wetlands / 4.1 Inland wetlands | Inland marshes | 166,166,255 | #A6A6FF | P | V |
| 412 | 4.1 | Peat bogs | 77,77,255 | #4D4DFF | P | V |
| 421 | 4.2 Coastal wetlands | Salt marshes | 204,204,255 | #CCCCFF | – | V |
| 422 | 4.2 | Salines | 230,230,255 | #E6E6FF | – | V |
| 423 | 4.2 | Intertidal flats | 166,166,230 | #A6A6E6 | – | V |
| 511 | 5 Water bodies / 5.1 Inland waters | Water courses | 0,204,242 | #00CCF2 | U | V |
| 512 | 5.1 | Water bodies | 128,242,230 | #80F2E6 | U | V |
| 521 | 5.2 Marine waters | Coastal lagoons | 0,255,166 | #00FFA6 | – | V |
| 522 | 5.2 | Estuaries | 166,255,230 | #A6FFE6 | – | V |
| 523 | 5.2 | Sea and ocean | 230,242,255 | #E6F2FF | – | V |

**Convention notes (A):** artificial surfaces are reds, magentas and pinks (including the *vegetated* artificial classes 141/142, which are pink — not green); agriculture is yellow to orange; forests saturated greens; grass/heath yellow-greens; open ground greys; wetlands blue-violets; water cyan to pale blue.

---

## 2. Copernicus Urban Atlas (UA) and Street Tree Layer (STL)

### 2.1 Product facts (V)

Sources: UA 2021 PUM https://library.land.copernicus.eu/products/Urban_Atlas_CLMS_UA2021_LULC_PUM_v1.html; UA 2012/2018 PUM (mapping guide v6.3) https://library.land.copernicus.eu/products/Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6.html

- Vector LC/LU maps per Functional Urban Area (FUA): ~300 cities for 2006; 788 FUAs for 2012 and 2018; **790 FUAs for 2021**. Coverage EEA-38 (without Liechtenstein) + UK.
- Mapping scale 1:10 000; MMU **0.25 ha** for urban classes (class 1) and **1 ha** for rural classes (2–5); minimum mapping width 10 m (6 m for class 12220). Change layer MMU 0.1 ha / 0.25 ha.
- Thematic accuracy targets: ≥ 85 % urban classes, ≥ 80 % rural classes and overall.
- Delivery: GeoPackage (2018, 2021) with "layer styles in qml format" according to the manual; the UA 2021 download page offers FlatGeobuf files per FUA (V, https://land.copernicus.eu/en/products/urban-atlas/urban-atlas-2021); attribute fields `code_2018` / `code_2021` (5-character string) and `class_2018` / `class_2021`.
- The nomenclature is "derived from CORINE Land Cover": four hierarchical levels for artificial surfaces, two for the rest. The five-digit code encodes the levels (11210 = 1.1.2.1).
- Urban fabric classes are separated **only by degree of soil sealing** (from the HRL Imperviousness layer), not by building type.
- New in 2021: **Green urban areas are split by accessibility** (14110 public, 14120 private, 14130 unknown), derived with OpenStreetMap and commercial road data.

### 2.2 Nomenclature with official legend colours

Codes and names: **V** from the PUM nomenclature tables. RGB: **V** for the 2018 legend, read from the renderer (field `code_2018`) of the EEA map service `UrbanAtlas/UA_UrbanAtlas_2018`, layer 2 "Land Use vector": https://image.discomap.eea.europa.eu/arcgis/rest/services/UrbanAtlas/UA_UrbanAtlas_2018/MapServer/layers?f=pjson

The **2021 legend** was read (**V**) from the SLD that the CLMS web map service returns for `GetStyles` on the layers `UA_LCU_2021_VECTOR` and `UA_LCU_2018_VECTOR`: https://mapserver.dataspace.copernicus.eu/ogc?service=WMS&request=GetCapabilities&version=1.3.0 — all classes that exist in both years have exactly the 2018 colours; the 2021 style adds the three access classes and the two no-data classes. The product page counts 19 urban classes (MMU 0.25 ha) and 9 rural classes (MMU 1 ha) for 2021.

| Code | UA no. | Name | R,G,B (2018 legend; 2021 style for the 2021-only and no-data codes) | Hex | Mark |
|---|---|---|---|---|---|
| 11100 | 1.1.1 | Continuous urban fabric (S.L. > 80 %) | 128,0,0 | #800000 | V |
| 11210 | 1.1.2.1 | Discontinuous dense urban fabric (S.L. 50 % – 80 %) | 191,0,0 | #BF0000 | V |
| 11220 | 1.1.2.2 | Discontinuous medium density urban fabric (S.L. 30 % – 50 %) | 255,64,64 | #FF4040 | V |
| 11230 | 1.1.2.3 | Discontinuous low density urban fabric (S.L. 10 % – 30 %) | 255,128,128 | #FF8080 | V |
| 11240 | 1.1.2.4 | Discontinuous very low density urban fabric (S.L. < 10 %) | 255,191,191 | #FFBFBF | V |
| 11300 | 1.1.3 | Isolated structures | 204,102,102 | #CC6666 | V |
| 12100 | 1.2.1 | Industrial, commercial, public, military and private units | 204,77,242 | #CC4DF2 | V |
| 12210 | 1.2.2.1 | Fast transit roads and associated land | 149,149,149 | #959595 | V |
| 12220 | 1.2.2.2 | Other roads and associated land | 179,179,179 | #B3B3B3 | V |
| 12230 | 1.2.2.3 | Railways and associated land | 89,89,89 | #595959 | V |
| 12300 | 1.2.3 | Port areas | 230,204,204 | #E6CCCC | V |
| 12400 | 1.2.4 | Airports | 230,204,230 | #E6CCE6 | V |
| 13100 | 1.3.1 | Mineral extraction and dump sites | 115,77,55 | #734D37 | V |
| 13300 | 1.3.3 | Construction sites | 185,165,110 | #B9A56E | V |
| 13400 | 1.3.4 | Land without current use | 135,69,69 | #874545 | V |
| 14100 | 1.4.1 | Green urban areas (2006–2018; still used in the revised 2018 layer) | 140,220,0 | #8CDC00 | V |
| 14110 | 1.4.1 | Green urban areas (Public access) — 2021 only | 140,220,0 | #8CDC00 | V |
| 14120 | 1.4.1 | Green urban areas (Private access) — 2021 only | 116,184,0 | #74B800 | V |
| 14130 | 1.4.1 | Green urban areas (Unknown access conditions) — 2021 only | 90,143,0 | #5A8F00 | V |
| 14200 | 1.4.2 | Sports and leisure facilities | 175,210,165 | #AFD2A5 | V |
| 21000 | 2.1 | Arable land (annual crops) | 255,255,168 | #FFFFA8 | V |
| 22000 | 2.2 | Permanent crops (vineyards, fruit trees, olive groves) | 242,166,77 | #F2A64D | V |
| 23000 | 2.3 | Pastures | 230,230,77 | #E6E64D | V |
| 24000 | 2.4 | Complex and mixed cultivation patterns | 255,230,77 | #FFE64D | V |
| 25000 | – | Orchards — **legacy entry**: present only in the legend of the older EEA service `UA_UrbanAtlas_2018`; absent from the nomenclature tables of the manuals and from the current CLMS styles for 2018 and 2021 | 242,204,128 | #F2CC80 | V (legacy legend) |
| 31000 | 3.1 | Forests | 0,140,0 | #008C00 | V |
| 32000 | 3.2 | Herbaceous vegetation associations (natural grassland, moors …) | 204,242,77 | #CCF24D | V |
| 33000 | 3.3 | Open spaces with little or no vegetation (beaches, dunes, bare rocks, glaciers) | 204,255,204 | #CCFFCC | V |
| 40000 | 4 | Wetlands | 166,166,255 | #A6A6FF | V |
| 50000 | 5 | Water | 128,242,230 | #80F2E6 | V |
| 91000 | 9.1 | No data (Clouds and shadows) | 255,255,255 | #FFFFFF | V (2021 style) |
| 92000 | 9.2 | No data (Missing imagery) | 0,0,0 | #000000 | V (2021 style) |

**Convention notes (A):** UA keeps the CLC colours where classes coincide (12100, 12300, 12400, 21000, 22000, 23000, 24000, 32000, 33000, 40000, 50000) but departs for the urban detail: urban fabric is a **five-step dark-red-to-pale-pink ramp by sealing degree**, transport is **grey** (three greys), and green urban areas are a **strong yellow-green** (not CLC's pink). In 2021 the access split is drawn as **three steps of the same green**: public = the familiar bright green, private = darker, unknown = darkest.

### 2.3 Class content that matters for the element catalog (V, paraphrased from the PUM annex)

| UA class | What it contains (paraphrase) |
|---|---|
| 1.1 Urban fabric | Built-up land with its gardens, small parks and planted areas that are below the MMU; private gardens within housing areas stay in 1.1. |
| 1.2.1 | Industry, commerce, public and military units incl. schools, hospitals, places of worship, energy and water-treatment plants, greenhouses/farming industry; their lawns and parking areas are included. |
| 1.2.2 | Roads and railways **with associated land**: embankments, enclosed areas, noise barriers, rest areas, parallel foot/cycle paths, green strips and alleys with trees or bushes. |
| 1.3.4 Land without current use | Transitional land waiting to be used: brownfields, gaps between new construction, left-over land; no maintenance, secondary ruderal vegetation. |
| 1.4.1 Green urban areas | Public green for mainly recreational use: gardens, playgrounds, zoos, parks, castle parks, **cemeteries** (since the UA 2006 revision); forests reaching into the city are mapped here if bordered by urban structures on at least two sides and showing recreational use. Private gardens are excluded. |
| 1.4.2 Sports and leisure | Golf courses, sports fields, campgrounds, leisure parks, riding grounds, racecourses, amusement parks, swimming resorts, holiday villages, **allotment gardens**, glider airfields, marinas. |
| 3.1 Forests | Tree canopy cover > 30 %, tree height > 5 m; includes transitional woodland, clear cuts, plantations, nurseries. Urban forests under high human pressure go to 1.4.1. |
| 3.2 Herbaceous vegetation associations | Natural grassland, scrub, abandoned land under natural colonisation; vegetation cover > 50 %, trees > 5 m below 30 % cover. |
| 3.3 | Beaches, dunes, sand, gravel along rivers; bare rock; sparsely vegetated areas (10–50 % cover); burnt areas; snow and ice. |
| 4 Wetlands | Inland and coastal wetlands, including water-fringe vegetation, reed beds, sedge beds, peat bogs, shallow water covered with reed. |
| 5 Water | Sea, lakes, fishponds, rivers, canals; MMU 1 ha; water courses wider than 10 m. |

### 2.4 Street Tree Layer (V)

| Item | STL 2012 / 2018 | STL 2021 |
|---|---|---|
| Definition (paraphrase) | Separate layer produced within the level-1 "urban mask" of each FUA: contiguous rows or patches of trees of **≥ 500 m²** and **≥ 10 m** minimum width over "Artificial surfaces" (nomenclature class 1). Trees along roads outside urban areas and forest adjacent to urban areas are excluded. | Presence of trees within the FUA: contiguous rows or patches of **≥ 500 m²** over artificial surfaces (class 1), excluding trees along road/rail links between cities and villages. The 10 m minimum width is stated to be "no longer necessary" in the text (the specification table of the same manual still lists 10 m). Derived from the HRL Small Landscape Features and UA 2021. |
| Coding | `STL` = 1 (tree), 99 (no data); 2012 also 0 | `STL` = 1 |
| Geometry / scale | vector; 2012 partial coverage | vector, equivalent scale 1:5 000 |
| Accuracy target | ≥ 80 % | ≥ 80 % producer's and user's |
| Official colour (V) | 56,168,0 = #38A800, no outline (simple renderer of the EEA service `UA_StreetTreeLayer_2018`) | fill #75DD00 = 117,221,0 with stroke #232323 (CLMS WMS style of `UA_STL_2021_VECTOR`, rule "1: Street tree layer") |

Source: section 4.2.9 of the 2012/2018 PUM and section 7.2.5 of the 2021 PUM (URLs above). Colours: https://image.discomap.eea.europa.eu/arcgis/rest/services/UrbanAtlas/UA_StreetTreeLayer_2018/MapServer/layers?f=pjson and the CLMS WMS named in section 2.2.

---

## 3. CLC+ Backbone (raster, 10 m)

Sources: PUM 2023 https://library.land.copernicus.eu/products/CLCplus_Backbone_2023_PUM_v1.html; PUM 2021 https://library.land.copernicus.eu/products/CLCplus_Backbone_2021_PUM_v1.html

### 3.1 Product facts (V)

- 10 m pixel-based raster, **11 land-cover classes**, no MMU (each pixel gets the dominant land cover); 8-bit unsigned; ETRS89-LAEA (EPSG:3035).
- Reference years 2018 (Sentinel-2 window ± 6 months), 2021 and 2023 (reference year ± 3 months; for 2023: 1 Oct 2022 – 31 Mar 2024). UK missing in 2021. Biennial from 2023.
- 2023 delivered as cloud-optimised GeoTIFF tiles (897 tiles of 100 × 100 km) with embedded colour map, plus symbology files `.lyr`, `.qml`, `.sld`; 2018/2021 delivered with `.clr` colour tables.
- Target accuracy: 90 % overall, max. 15 % omission/commission per class (lower regionally for "Low-growing woody plants" and "Lichens and mosses").
- Class logic is **pure land cover** following the **EAGLE** land-cover components; mixed pixels are resolved with a decision tree (water > 50 %? biotic > 50 %? woody > 50 %? …; biotic cover below 30 % leads to class 9).

### 3.2 Classes, EAGLE link and official colours

Codes and names: V (technical specification tables of both manuals). RGB: **V** — read from the colour-palette tables printed (as images) in the annexes of the 2021 and the 2023 manuals; both years are identical. EAGLE references: V (section 6.1.2 of the 2023 manual).

| Code | Class name | EAGLE reference given in the 2023 manual | R,G,B | Hex | Mark |
|---|---|---|---|---|---|
| 1 | Sealed | LCC 1.1.1 Sealed Artificial Surfaces and Constructions | 255,0,0 | #FF0000 | V |
| 2 | Woody needle leaved trees | LCC 2.1.1, LCH 3.1.1 | 34,139,34 | #228B22 | V |
| 3 | Woody broadleaved deciduous trees | LCC 2.1.1, LCH 3.2.2 | 128,255,0 | #80FF00 | V |
| 4 | Woody broadleaved evergreen trees | LCC 2.1.1, LCH 3.2.1 | 0,255,8 | #00FF08 | V |
| 5 | Low-growing woody plants | LCC 2.1.2 Bushes, Shrubs | 128,64,0 | #804000 | V |
| 6 | Permanent herbaceous | LCC 2.2 Herbaceous Vegetation | 204,242,77 | #CCF24D | V |
| 7 | Periodically herbaceous | LCC 2.2 Herbaceous Vegetation | 255,255,128 | #FFFF80 | V |
| 8 | Lichens and mosses | LCC 2.4 Lichens, Mosses, Algae | 255,128,255 | #FF80FF | V |
| 9 | Non and sparsely vegetated | LCC 1.2 Natural Material Surfaces; LCC 1.1.2 Non-Sealed Artificial Surfaces | 191,191,191 | #BFBFBF | V |
| 10 | Water | LCC 3.1 Liquid Water Bodies | 0,128,255 | #0080FF | V |
| 11 | Snow and ice | LCC 3.2 Solid Waters | 0,255,255 | #00FFFF | V |
| 253 | Coastal seawater buffer (since 2021) | technical class | 191,223,255 | #BFDFFF | V |
| 254 | Outside area | technical class | 230,230,230 | #E6E6E6 | V |
| 255 | No data | technical class | 0,0,0 | #000000 | V |

### 3.3 Class definitions that decide where library elements fall (V, paraphrased)

| Class | Decisive rules |
|---|---|
| 1 Sealed | All impervious surfaces: buildings and constructions, flat surfaces of asphalt, concrete, tarmacadam. Also mapped here: **vegetated rooftops**, railway tracks, greenhouses present for more than half of the year, solar parks. **Excluded** (→ class 9): waste materials, non-sealed and semi-sealed artificial surfaces such as storage areas, fairgrounds, **non-vegetated sport fields, grass pavers and permeable paving**. |
| 2–4 Woody – trees | Perennial woody plants with a single self-supporting stem. 2 = needle-leaved (gymnosperms; Ginkgo counts as broadleaved deciduous); 3 = broadleaved, leafless for part of the year; 4 = broadleaved never entirely without foliage (includes palms). |
| 5 Low-growing woody plants | Shrub growth form, multiple stems, height usually below 5 m. Includes bushes, dwarf shrubs (Calluna, Erica), Pinus mugo, Alnus viridis, **vines (Vitis) and hops**. Excludes low fruit trees and young tree regrowth (→ trees). |
| 6 Permanent herbaceous | Continuous herbaceous cover (more than 30 %) throughout the year, no bare-soil phase: natural and managed grassland, set-aside, permanent fodder. Includes grasses, **reeds** and forbs. |
| 7 Periodically herbaceous | At least one change between bare soil and herbaceous cover within the observation period — in practice mostly arable land; grassland ploughed in the reference year also ends up here. |
| 8 Lichens and mosses | Essentially a northern-European tundra class. |
| 9 Non and sparsely vegetated | Non-vegetated share ≥ 70 %: rock, scree, sand, gravel, permanent bare soil, quarries, sparsely vegetated ground (vegetation below 30 %), and any non-sealed artificial surface with vegetation below 30 %. |
| 10 Water | Inland water in liquid state, running and standing, natural or artificial; under water for at least half of the observation period. Coastal seawater is separated as code 253. |
| 11 Snow and ice | Permanent snow (more than 90 % of the period) and glacier ice. |

---

## 4. Nature Restoration Regulation (EU) 2024/1991 — urban ecosystems

Primary source (all quotes V): Regulation (EU) 2024/1991 of the European Parliament and of the Council of 24 June 2024 on nature restoration and amending Regulation (EU) 2022/869, OJ L, 2024/1991, 29.7.2024 — https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401991 (ELI: http://data.europa.eu/eli/reg/2024/1991/oj).

### 4.1 Definitions in Article 3 (verbatim)

| Art. 3 point | Text |
|---|---|
| (20) | "‘urban green space’ means the total area of trees, bushes, shrubs, permanent herbaceous vegetation, lichens and mosses, ponds and watercourses found within cities or towns and suburbs, calculated on the basis of data provided by the Copernicus Land Monitoring Service under the Copernicus component of the Union Space Programme, established by Regulation (EU) 2021/696, and, if available for the Member State concerned, other appropriate supplementary data provided by that Member State;" |
| (21) | "‘urban tree canopy cover’ means the total area of tree cover within cities and towns and suburbs, calculated on the basis of the Tree Cover Density data provided by the Copernicus Land Monitoring Service under the Copernicus component of the Union Space Programme, established by Regulation (EU) 2021/696, and, if available for the Member State concerned, other appropriate supplementary data provided by that Member State;" |
| (15) | "‘local administrative unit’ or ‘LAU’ means a low-level administrative division of a Member State, below that of a province, region or state, established in accordance with Article 4 of Regulation (EC) No 1059/2003 …" |
| (16) | "‘urban centres’ and ‘urban clusters’ means territorial units classified in cities and towns and suburbs using the grid-based typology established in accordance with Article 4b(2) of Regulation (EC) No 1059/2003;" |
| (17) | "‘cities’ means LAUs where at least 50 % of the population lives in one or more urban centres, measured using the degree of urbanisation …" |
| (18) | "‘towns and suburbs’ means LAUs where less than 50 % of the population lives in an urban centre, but at least 50 % of the population lives in an urban cluster, measured using the degree of urbanisation …" |
| (19) | "‘peri-urban areas’ means areas adjacent to urban centres or urban clusters, including at least all areas within 1 kilometre measured from the outer limits of those urban centres or urban clusters, and located in the same city or the same town and suburb as those urban centres or urban clusters;" |

### 4.2 Article 8 "Restoration of urban ecosystems" (verbatim) and related provisions

| Provision | Text / content | Mark |
|---|---|---|
| Art. 8(1) | "By 31 December 2030, Member States shall ensure that there is no net loss in the total national area of urban green space and of urban tree canopy cover in urban ecosystem areas, determined in accordance with Article 14(4), compared to 2024. For the purposes of this paragraph, Member States may exclude from those total national areas the urban ecosystem areas in which the share of urban green space in the urban centres and urban clusters exceeds 45 % and the share of urban tree canopy cover exceeds 10 %." | V |
| Art. 8(2) | "From 1 January 2031, Member States shall achieve an increasing trend in the total national area of urban green space, including through the integration of urban green space into buildings and infrastructure, in urban ecosystem areas, determined in accordance with Article 14(4), measured every six years from 1 January 2031, until a satisfactory level as set in accordance with Article 14(5) is reached." | V |
| Art. 8(3) | "Member States shall achieve, in each urban ecosystem area, determined in accordance with Article 14(4), an increasing trend of urban tree canopy cover, measured every six years from 1 January 2031, until the satisfactory level identified as set in accordance with Article 14(5) is reached." | V |
| Art. 14(4) — urban ecosystem area | Member States "shall determine and map urban ecosystem areas as referred to in Article 8 for all their cities and towns and suburbs." The area "shall include: (a) the entire city or town and suburb; or (b) parts of the city or of the town and suburb, including at least its urban centres, urban clusters and, if deemed appropriate by the Member State concerned, peri-urban areas." Adjacent cities/towns may be aggregated into one common urban ecosystem area. | V |
| Art. 14(5) | By 2030 Member States set **satisfactory levels** for, among others, (d) urban green space (Art. 8(2)) and (e) urban tree canopy cover (Art. 8(3)). | V |
| Art. 20(1)(b), 20(6) | Member States monitor "the area of urban green space and urban tree canopy cover within urban ecosystem areas"; this monitoring is carried out **at least every six years**. | V |
| Art. 20(10) | By 31 December 2028 the Commission establishes, by implementing acts, a guiding framework for setting the satisfactory levels referred to in Art. 8(2) and (3). | V |
| Recital 47 | Urban ecosystems are about 22 % of the Union's land surface; urban green spaces "include, inter alia, urban forests, parks and gardens, urban farms, tree-lined streets, urban meadows and urban hedges". | V |
| Recital 48 | Loss of urban green space should be stopped; integration of green infrastructure "such as green roofs and green walls" in building design can maintain and increase urban green space and, if trees are included, tree canopy cover. | V |
| Last annex (examples of restoration measures), item 31 | Increase urban green spaces with ecological features such as parks, trees and woodland patches, green roofs, wildflower grasslands, gardens, city horticulture, tree-lined streets, urban meadows and hedges, ponds and watercourses, considering species diversity, native species, local conditions and climate resilience. (Annex number not captured — it is the final annex of the act; paraphrased.) | V (content) |

**Key distinction (V):** the no-net-loss target of Art. 8(1) and the green-space trend of Art. 8(2) are assessed on the **total national area**; the tree-canopy trend of Art. 8(3) is assessed **in each urban ecosystem area**.

### 4.3 Which data and classes measure the targets

Source (V): "Methodological support on datasets to be used under Article 8 of the Nature Restoration Regulation", informal discussion document of DG Environment with EEA logo, document version 2.0, portal date 07/07/2026 — https://biodiversity.europa.eu/europes-biodiversity/nature-restoration/reference-portal-for-nature-restoration-regulation/documentation/nrp-urban-explantory-notes-v2_07072026.pdf/@@display-file/file (linked from the NRR Reference Portal, https://biodiversity.europa.eu/europes-biodiversity/nature-restoration/reference-portal-for-nature-restoration-regulation). The document states that it is not legally binding.

| NRR term | Dataset to be used | Reference / baseline | Update | Type | Mark |
|---|---|---|---|---|---|
| LAU boundaries | Eurostat/GISCO Local Administrative Units | 2024 | yearly | vector | V |
| Cities, towns and suburbs | LAU "degree of urbanisation" classification (based on the 2021 census population grid) | 2024 | yearly | table | V |
| Urban centres and urban clusters | Eurostat grid clusters | 2021 (must be used) | every 10 years | raster 1 km | V |
| **Urban green space** | **CLCplus Backbone** | **2023** version for the baseline | every two years | raster 10 m | V |
| **Urban tree canopy cover** | **CLMS HRL Tree Cover Density** | **2024** version for the baseline | yearly | raster 10 m | V |
| Tree canopy – supplementary | CLMS HRL Woody Vegetation Layer (5 m) | 2021 for draft plans; 2024 for final plans | every three years | raster 5 m | V |

**CLCplus Backbone classes counted as urban green space (V):** trees = classes **2, 3 and 4**; bushes, shrubs = class **5**; permanent herbaceous vegetation = class **6**; lichens and mosses = class **8**; ponds and watercourses = class **10**. The note recommends reclassifying these to 1 and everything else to no-data. Consequently **not counted**: 1 Sealed, 7 Periodically herbaceous, 9 Non and sparsely vegetated, 11 Snow and ice, 253 coastal seawater.

**Urban tree canopy cover (V):** the HRL Tree Cover Density layer gives a tree-cover percentage per 10 m pixel; the canopy area is obtained by summing the percentages over the urban ecosystem area. It has to be reported per urban ecosystem area. The CLMS product family "High Resolution Layer Tree Cover and Forests" consists of Tree Cover Density (0–100 % per pixel), Dominant Leaf Type (broadleaved / coniferous) and Forest Type; only Forest Type applies the FAO forest definition and filters out street trees, orchards and patches below half a hectare — Tree Cover Density therefore **includes street trees and orchard trees** (V, https://land.copernicus.eu/en/products/high-resolution-layer-tree-cover-density).

**Thresholds used in the note (V):** urban centre = contiguous 1 km² cells with at least 1,500 inhabitants/km² and at least 50,000 inhabitants in total; urban cluster = contiguous cells with at least 300 inhabitants/km² and at least 5,000 inhabitants. Peri-urban area: no obligation to delineate; if included, at least 1 km around centres and clusters, clipped to the LAU.

**Supplementary data (V):** allowed to improve or complement the official datasets if temporally consistent (2024 baseline, 2030, later), spatially consistent and documented; bottom-up inventories are named as the way to capture features "such as green roofs that won't be captured by the official data".

**Consequences for a style library (A):**
1. The legal notion of "urban green space" is a **land-cover mask**, independent of ownership, use or quality: a lawn, a hedge, a pond and a wood all count; arable plots (class 7), bare ground, water-bound and permeable paving (class 9) and green roofs (mapped as class 1) do not count in the Copernicus baseline.
2. Tree canopy is a **separate, overlapping measure** (a canopy over asphalt counts as canopy), so trees need to exist as an overlay element in addition to ground-surface elements.

### 4.4 Related: ecosystem-accounting indicator for settlements (V)

Regulation (EU) 2024/3024, Annex IX, Section 3(3)(a): condition accounts for "settlements and other artificial areas" report **green areas in cities and adjacent towns and suburbs** in % of total area, and the PM2.5 concentration in cities. Cities, towns and suburbs are LAUs categorised by degree of urbanisation (Regulation (EU) 2017/2391). Source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202403024

---

## 5. EUNIS habitat classification

### 5.1 Status and where it lives now (V)

- The former EUNIS web application is retired; the classification trees are served by BISE: https://biodiversity.europa.eu/resources/search-habitat
- Revised classification ("EUNIS habitat types hierarchical view 2021/2022"): https://biodiversity.europa.eu/resources/search-habitat/eunis-habitat-types-hierarchical-view-2021-2022
- EUNIS 2012 (includes the groups not yet revised): https://biodiversity.europa.eu/resources/search-habitat/eunis-habitat-types-hierarchical-view-2012
- EEA SDI series "EUNIS habitat classification and crosswalks (tabular data)": the review covers marine habitats, coastal habitats, grasslands, heathland, forest, sparsely vegetated, vegetated man-made habitats and wetlands; the remaining groups (**inland waters and complex habitats**) are to be revised later; the 2012 version "includes the not yet revised groups". https://sdi.eea.europa.eu/catalogue/srv/api/records/638330ea-90e6-4e41-81ea-e70f25ae7117
- **Constructed habitats (2012 group J) do not appear in the revised tree at all** and are not named among the pending groups in the current metadata (an older EEA text listed them as pending — S). For buildings, roads, artificial waters and waste deposits the **2012 J codes remain the only EUNIS codes** (A).

Code syntax differs between generations: **2012 uses a dot after the second character (E2.6, E2.64); the 2021/2022 revision has no dot (V31, R22)**. Both generations must be stored in separate fields.

### 5.2 Revised classification 2021/2022 — level 1 (V)

| Code | Name | Replaces 2012 group (A) |
|---|---|---|
| M | Marine benthic habitats | A (part) |
| MH | Pelagic water column | A (part) |
| MJ | Ice-associated marine habitats | A (part) |
| N | Coastal habitats | B |
| Q | Wetlands | D (+ parts of C3) |
| R | Grasslands and lands dominated by forbs, mosses or lichens | E |
| S | Heathland, scrub and tundra | F |
| T | Forest and other wooded land | G |
| U | Inland habitats with no or little soil and mostly with sparse vegetation | H |
| V | Vegetated man-made habitats | I (+ E2.6, FA, FB, parts of G1, G5) |
| (not revised) | Inland surface waters → use 2012 group **C** | – |
| (not revised) | Constructed, industrial and other artificial habitats → use 2012 group **J** | – |
| (not revised) | Habitat complexes → use 2012 group **X** | – |

### 5.3 Revised group V "Vegetated man-made habitats" — complete (V)

Source: BISE tree (URL above). The name of V31 is truncated in BISE after the first comma; the full name is taken from FloraVeg.EU (S): https://floraveg.eu/habitat/overview/V3

| Level 2 | Level 3 codes and names |
|---|---|
| **V1** Arable land and market gardens | V11 Intensive unmixed crops · V12 Mixed crops of market gardens and horticulture · V13 Arable land with unmixed crops grown by low-intensity agricultural methods · V14 Inundated or inundatable croplands, including rice fields · V15 Bare tilled, fallow or recently abandoned arable land |
| **V2** Cultivated areas of gardens and parks | V21 Large-scale ornamental garden areas · V22 Small-scale ornamental and domestic garden areas · V23 Recently abandoned garden areas |
| **V3** Artificial grasslands and herb dominated habitats | V31 Agriculturally-improved, re-seeded and heavily fertilised grassland, including sports fields and grass lawns (full name S) · V32 Mediterranean subnitrophilous annual grasslands · V33 Dry mediterranean lands with unpalatable non-vernal herbaceous vegetation · V34 Trampled xeric grasslands with annuals · V35 Trampled mesophilous grasslands with annuals · V36 Alpine and subalpine enriched grassland · V37 Annual anthropogenic herbaceous vegetation · V38 Dry perennial anthropogenic herbaceous vegetation · V39 Mesic perennial anthropogenic herbaceous vegetation |
| **V4** Hedgerows | V41 Hedgerows of non-native species · V42 Highly-managed hedgerows of native species · V43 Species-rich hedgerows of native species · V44 Species-poor hedgerows of native species |
| **V5** Shrub plantations | V51 Shrub plantations for whole-plant harvesting · V52 Shrub plantations for leaf or branch harvest · V53 Shrub plantations for ornamental purposes or for fruit, other than vineyards · V54 Vineyards |
| **V6** Tree dominated man-made habitats | V61 Broadleaved fruit and nut tree orchards · V62 Evergreen orchards and groves · V63 Lines of planted trees · V64 Small deciduous broadleaved planted other wooded land · V65 Small evergreen broadleaved planted other wooded land · V66 Small coniferous planted other wooded land |

### 5.4 Revised groups R, S, T, Q, U, N — level 2 complete, level 3 selected for temperate urban / peri-urban use (V)

All codes and names V from the BISE tree; the *selection* of level-3 codes is mine (A). Mediterranean, Macaronesian, alpine and boreal level-3 units are omitted here.

| Group | Level 2 (complete) | Selected level 3 |
|---|---|---|
| **R** Grasslands … | R1 Dry grasslands · R2 Mesic grasslands · R3 Seasonally wet and wet grasslands · R4 Alpine and subalpine grasslands · R5 Forest fringes and clearings and tall forb stands · R6 Inland salt steppes and salt marshes · R7 Sparsely wooded grasslands | R18 Perennial rocky calcareous grassland of subatlantic-submediterranean Europe · R1A Semi-dry perennial calcareous grassland (meadow steppe) · R1B Continental dry grassland (true steppe) · R1M Lowland to montane, dry to mesic grassland usually dominated by Nardus stricta · R1P Oceanic to subcontinental inland sand grassland on dry acid and neutral soils · R1Q Inland sanddrift and dune with siliceous grassland · R1S Heavy-metal grassland in Western and Central Europe · **R21 Mesic permanent pasture of lowlands and mountains** · **R22 Low and medium altitude hay meadow** · R23 Mountain hay meadow · R35 Moist or wet mesotrophic to eutrophic hay meadow · R36 Moist or wet mesotrophic to eutrophic pasture · R37 Temperate and boreal moist or wet oligotrophic grassland · R51 Thermophilous forest fringe of base-rich soils · R52 Forest fringe of acidic nutrient-poor soils · R54 Pteridium aquilinum vegetation · R55 Lowland moist or wet tall-herb and fern fringe · R57 Herbaceous forest clearing vegetation · R63 Temperate inland salt marsh · R71 Temperate wooded pasture and meadow |
| **S** Heathland, scrub and tundra | S1 Tundra · S2 Arctic, alpine and subalpine scrub · S3 Temperate and mediterranean-montane scrub · S4 Temperate shrub heathland · S5 Maquis, arborescent matorral and thermo-Mediterranean scrub · S6 Garrigue · S7 Spiny Mediterranean heaths (phrygana, hedgehog-heaths and related coastal cliff vegetation) · S8 Thermo-Atlantic xerophytic scrub · S9 Riverine and fen scrubs | S31 Lowland to montane temperate and submediterranean Juniperus scrub · **S32 Temperate Rubus scrub** · S33 Lowland to montane temperate and submediterranean genistoid scrub · **S35 Temperate and submediterranean thorn scrub** · S37 Corylus avellana scrub · S38 Temperate forest clearing scrub · S41 Wet heath · S42 Dry heath · S91 Temperate riparian scrub · S92 Salix fen scrub |
| **T** Forest and other wooded land | T1 Deciduous broadleaved forest · T2 Broadleaved evergreen forest · T3 Coniferous forest · T4 Lines of trees, small anthropogenic forests, recently felled forest, early-stage forest and coppice | T11 Temperate Salix and Populus riparian forest · T12 Alnus glutinosa-Alnus incana forest on riparian and mineral soils · T13 Temperate hardwood riparian forest · T15 Broadleaved swamp forest on non-acid peat · T16 Broadleaved mire forest on acid peat · T17 Fagus forest on non-acid soils · T18 Fagus forest on acid soils · T19 Temperate and submediterranean thermophilous deciduous forest · T1B Acidophilous Quercus forest · T1C Temperate and boreal mountain Betula and Populus tremula forest on mineral soils · T1E Carpinus and Quercus mesic deciduous forest · T1F Ravine forest · **T1H Broadleaved deciduous plantation of non site-native trees** · **T1J Deciduous self sown forest of non site-native trees** · T1K Broadleaved deciduous plantation of site-native trees · T35 Temperate continental Pinus sylvestris forest · T3J Pinus and Larix mire forest · T3L Coniferous self sown forest of non site-native trees · T3M Coniferous plantation of non site-native trees · T3N Coniferous plantation of site-native trees · T41 Early-stage natural and semi-natural forest and regrowth · T42 Coppice and early stage plantations · T43 Recently felled areas |
| **Q** Wetlands | Q1 Raised and blanket bogs · Q2 Valley mires, poor fens and transition mires · Q3 Palsa mires · Q4 Base-rich fens and calcareous spring mires · Q5 Helophyte beds · Q6 Periodically exposed shores | Q11 Raised bog · Q22 Poor fen · Q24 Intermediate fen and soft-water spring mire · Q41 Alkaline, calcareous, carbonate-rich small-sedge spring fen · Q43 Tall-sedge base-rich fen · **Q51 Tall-helophyte bed** · Q52 Small-helophyte bed · **Q53 Tall-sedge bed** · Q54 Inland saline or brackish helophyte bed · Q61 / Q62 Periodically exposed shore with stable, eutrophic / mesotrophic sediments with pioneer or ephemeral vegetation |
| **U** Inland habitats with no or little soil … | U1 Terrestrial underground caves, cave systems, passages and waterbodies · U2 Screes · U3 Inland cliffs, rock pavements and outcrops · U4 Snow or ice-dominated habitats · U5 Miscellaneous inland habitats usually with very sparse or no vegetation · U6 Recent volcanic features | U11 Cave · U12 Disused underground mines and tunnels · U23 Temperate, lowland to montane siliceous scree · U27 Temperate, lowland to montane base-rich scree · U33 Temperate, lowland to montane siliceous inland cliff · U37 Temperate, lowland to montane base-rich inland cliff · U3D Wet inland cliff · U3E Limestone pavement · U51 Fjell field · U52 Polar desert · U53 Glacial moraines with very sparse or no vegetation |
| **N** Coastal habitats | N1 Coastal dunes and sandy shores · N2 Coastal shingle · N3 Rock cliffs, ledges and shores, including the supralittoral | N11 Atlantic, Baltic and Arctic sand beach · N13 Atlantic and Baltic shifting coastal dune · N15 Atlantic and Baltic coastal dune grassland (grey dune) · N21 Atlantic, Baltic and Arctic coastal shingle beach |

Observations (A): the revised group U lists at level 3 only fjell fields, polar desert and moraines under U5 — the 2012 units for **bare clay, sand and gravel (H5.3x), burnt areas (H5.5) and trampled areas (H5.6)** have no visible level-3 successor in the BISE tree; the official crosswalk table should be consulted before assigning 2021 codes to bare urban ground. Group T4 keeps "Lines of trees" in its title, but planted tree lines are V63.

### 5.5 EUNIS 2012 — codes still in wide use for urban greens and constructed habitats (V)

Source: BISE EUNIS 2012 tree (URL above). "→ 2021" gives the revised code with the **same or near-identical name** (A, name-based; not taken from the official crosswalk).

| 2012 code | Name | → 2021 (A) |
|---|---|---|
| **C** | Inland surface waters (not revised — current) | – |
| C1 / C1.1–C1.7 | Surface standing waters: C1.1 Permanent oligotrophic, C1.2 mesotrophic, C1.3 eutrophic, C1.4 dystrophic lakes, ponds and pools; C1.5 Permanent inland saline and brackish lakes, ponds and pools; C1.6 Temporary lakes, ponds and pools; C1.7 Permanent lake ice | – |
| C2 / C2.1–C2.6 | Surface running waters: C2.1 Springs, spring brooks and geysers; C2.2 Permanent non-tidal, fast, turbulent watercourses; C2.3 Permanent non-tidal, smooth-flowing watercourses; C2.4 Tidal rivers, upstream from the estuary; C2.5 Temporary running waters; C2.6 Films of water flowing over rocky watercourse margins | – |
| C3 / C3.1–C3.8 | Littoral zone of inland surface waterbodies: C3.1 Species-rich helophyte beds; **C3.2 Water-fringing reedbeds and tall helophytes other than canes** (C3.21 Phragmites australis beds, C3.23 Typha beds, C3.26 Phalaris arundinacea beds, C3.29 Water-fringing large sedge communities); C3.3 Water-fringing beds of tall canes; C3.4 Species-poor beds of low-growing water-fringing or amphibious vegetation; C3.5 Periodically inundated shores with pioneer and ephemeral vegetation; C3.6 / C3.7 Unvegetated or sparsely vegetated shores with soft or mobile sediments / with non-mobile substrates; C3.8 Inland spray- and steam-dependent habitats | Q51, Q53, Q6x (part) |
| D5 / D5.1–D5.3 | Sedge and reedbeds, normally without free-standing water: D5.1 Reedbeds (D5.11 Phragmites, D5.13 Typha), D5.2 Beds of large sedges, D5.3 Swamps and marshes dominated by Juncus effusus or other large Juncus spp. | Q51, Q53 |
| E1.D | Unmanaged xeric grassland | – |
| E1.E | Trampled xeric grasslands with annuals | V34 |
| E2.1 | Permanent mesotrophic pastures and aftermath-grazed meadows (E2.11 Unbroken pastures, E2.13 Abandoned pastures) | R21 |
| E2.2 | Low and medium altitude hay meadows (E2.22 Sub-Atlantic lowland hay meadows) | R22 |
| **E2.6** | **Agriculturally-improved, re-seeded and heavily fertilised grassland, including sports fields and grass lawns** | V31 |
| E2.61 | Dry or moist agriculturally-improved grassland | V31 |
| E2.62 | Wet agriculturally-improved grassland, often with drainage ditches | V31 |
| **E2.63** | **Turf sports fields** | V31 |
| **E2.64** | **Park lawns** | V31 |
| **E2.65** | **Small-scale lawns** | V31 |
| E2.7 | Unmanaged mesic grassland | – |
| E2.8 | Trampled mesophilous grasslands with annuals | V35 |
| E5.1 | Anthropogenic herb stands (E5.11 Lowland habitats colonised by tall nitrophilous herbs; **E5.12 Weed communities of recently abandoned urban and suburban constructions**; E5.13 … rural constructions; E5.14 … extractive industrial sites; E5.15 Land reclamation forb fields) | V37 / V38 / V39 |
| E7.1 / E7.2 | Atlantic parkland / Sub-continental parkland | R71 |
| F3.1 | Temperate thickets and scrub (F3.11 Medio-European rich-soil thickets, F3.14 Temperate Cytisus scoparius fields, F3.17 Corylus thickets …) | S3x |
| F9.1 / F9.2 | Riverine scrub / Salix carr and fen scrub | S91 / S92 |
| **FA** | **Hedgerows**: FA.1 Hedgerows of non-native species; FA.2 Highly-managed hedgerows of native species; FA.3 Species-rich hedgerows of native species; FA.4 Species-poor hedgerows of native species | V41–V44 |
| FB | Shrub plantations: FB.1 for whole-plant harvesting; FB.2 for leaf or branch harvest; FB.3 for ornamental purposes or for fruit, other than vineyards; FB.4 Vineyards | V51–V54 |
| G1.C | Highly artificial broadleaved deciduous forestry plantations (G1.C1 Populus plantations, G1.C3 Robinia plantations …) | T1H / T1K |
| G1.D | Fruit and nut tree orchards (G1.D4 Fruit orchards, G1.D5 Other high-stem orchards) | V61 |
| G3.F | Highly artificial coniferous plantations (G3.F1 native, G3.F2 exotic) | T3N / T3M |
| **G5** | **Lines of trees, small anthropogenic woodlands, recently felled woodland, early-stage woodland and coppice** | V6 / T4 |
| **G5.1** | **Lines of trees** | V63 |
| G5.2 | Small broadleaved deciduous anthropogenic woodlands | V64 |
| G5.3 | Small broadleaved evergreen anthropogenic woodlands | V65 |
| G5.4 | Small coniferous anthropogenic woodlands | V66 |
| G5.5 | Small mixed broadleaved and coniferous anthropogenic woodlands | – |
| G5.6 | Early-stage natural and semi-natural woodlands and regrowth (G5.61 Deciduous scrub woodland …) | T41 |
| G5.7 | Coppice and early-stage plantations (G5.71 Coppice, G5.72–G5.75 early-stage plantations) | T42 |
| G5.8 | Recently felled areas | T43 |
| H5.3 | Sparsely- or un-vegetated habitats on mineral substrates not resulting from recent ice activity: H5.31 Clay and silt, **H5.32 Stable sand**, H5.34 Inland non-lacustrine dunes, **H5.35 Gravel**, H5.36 Shallow rocky soils, H5.37 Boulder fields (each "with very sparse or no vegetation") | open |
| H5.5 | Burnt areas with very sparse or no vegetation | open |
| H5.6 | Trampled areas (**H5.61 Unsurfaced pathways**) | open |
| I1 | Arable land and market gardens: I1.1 Intensive unmixed crops; I1.2 Mixed crops of market gardens and horticulture; I1.3 Arable land with unmixed crops grown by low-intensity agricultural methods; I1.4 Inundated or inundatable croplands, including rice fields; I1.5 Bare tilled, fallow or recently abandoned arable land (I1.51–I1.55) | V11–V15 |
| **I2** | **Cultivated areas of gardens and parks** | V2 |
| I2.1 | Large-scale ornamental garden areas (I2.11 Park flower beds, arbours and shrubbery; I2.12 Botanical gardens) | V21 |
| I2.2 | Small-scale ornamental and domestic garden areas (I2.21 Ornamental garden areas; I2.22 Subsistence garden areas; I2.23 Small parks and city squares) | V22 |
| I2.3 | Recently abandoned garden areas | V23 |
| **J1** | Buildings of cities, towns and villages: J1.1 Residential buildings of city and town centres; J1.2 Residential buildings of villages and urban peripheries; J1.3 Urban and suburban public buildings (J1.31 Old town walls); J1.4 Urban and suburban industrial and commercial sites still in active use (J1.41 commercial units, J1.42 factories); J1.5 Disused constructions of cities, towns and villages (J1.51 Urban and suburban derelict spaces); J1.6 Urban and suburban construction and demolition sites; J1.7 High density temporary residential units | not revised |
| **J2** | Low density buildings: J2.1 Scattered residential buildings; J2.2 Rural public buildings; J2.3 Rural industrial and commercial sites still in active use; J2.4 Agricultural constructions (J2.43 Greenhouses); J2.5 Constructed boundaries (J2.51 Fences, J2.52 Field walls, J2.53 Sea walls); J2.6 Disused rural constructions; J2.7 Rural construction and demolition sites | not revised |
| **J3** | Extractive industrial sites: J3.1 Active underground mines; J3.2 Active opencast mineral extraction sites, including quarries; J3.3 Recently abandoned above-ground spaces of extractive industrial sites | not revised |
| **J4** | Transport networks and other constructed hard-surfaced areas: J4.1 Disused road, rail and other constructed hard-surfaced areas; **J4.2 Road networks**; **J4.3 Rail networks**; J4.4 Airport runways and aprons; J4.5 Hard-surfaced areas of ports; **J4.6 Pavements and recreation areas**; J4.7 Constructed parts of cemeteries | not revised |
| **J5** | Highly artificial man-made waters and associated structures: J5.1 / J5.2 saline and brackish standing / running waters; **J5.3 Highly artificial non-saline standing waters** (J5.31 Ponds and lakes with completely man-made substrate; J5.32 Intensively managed fish ponds; J5.33 Water storage tanks); **J5.4 Highly artificial non-saline running waters** (J5.41 Non-saline water channels with completely man-made substrate; J5.43 Subterranean artificial watercourses); **J5.5 Highly artificial non-saline fountains and cascades** | not revised |
| **J6** | Waste deposits: J6.1 Waste resulting from building construction or demolition; J6.2 Household waste and landfill sites; J6.3 Non-agricultural organic waste; J6.4 Agricultural and horticultural waste; J6.5 Industrial waste | not revised |
| X06, X07, X09, X10 | Crops shaded by trees; Intensively-farmed crops interspersed with strips of natural and/or semi-natural vegetation; Pasture woods (with a tree layer overlying pasture); Mosaic landscapes with a woodland element (bocages) | not revised |
| **X11** | **Large parks** | not revised |
| X13–X16 | Land sparsely wooded with broadleaved deciduous / broadleaved evergreen / coniferous / mixed broadleaved and coniferous trees | not revised |
| **X22** | **Small city centre non-domestic gardens** | not revised |
| **X23** | **Large non-domestic gardens** | not revised |
| **X24** | **Domestic gardens of city and town centres** | not revised |
| **X25** | **Domestic gardens of villages and urban peripheries** | not revised |

2012 level 1 for reference (V): A Marine habitats · B Coastal habitats · C Inland surface waters · D Mires, bogs and fens · E Grasslands and lands dominated by forbs, mosses or lichens · F Heathland, scrub and tundra · G Woodland, forest and other wooded land · H Inland unvegetated or sparsely vegetated habitats · I Regularly or recently cultivated agricultural, horticultural and domestic habitats · J Constructed, industrial and other artificial habitats · X Habitat complexes.

### 5.6 Official legend colours for EUNIS

The classification itself (BISE trees, EEA tables) defines no colours. **An official map legend does exist for EUNIS 2012 level 1 and level 2:** the EEA dataset "Ecosystem types of Europe" (terrestrial part, version 3.1, reference year 2012, 100 m, derived from CORINE Land Cover and further layers) is published as the map service `Ecosystem/EcosystemTypeMap_v3_1_Terrestrial` with one legend entry per class: https://bio.discomap.eea.europa.eu/arcgis/rest/services/Ecosystem/EcosystemTypeMap_v3_1_Terrestrial/MapServer/legend?f=pjson

**V\*** = the service delivers its legend as swatch images, not as numbers; the RGB values below were **sampled from the centre pixel of each official swatch**. The older service `MAES/MAES_ecosystem_type_maps_WM` (map version 2.1) returns identical colours for the classes compared (groups B to E). Limits: the legend covers only classes present in the map (no E5, FA, X …), only the 2012 codes, and it is not collision-free (D5 = F6, D6 = F7). Many values are re-used CLC colours (C1, C2, E2, E3, G1, G3, G4, I1, J3, J6 …).

**Level 1** (service layer 1):

| Code | Name | R,G,B | Hex | Mark |
|---|---|---|---|---|
| B | Coastal habitats | 255,211,127 | #FFD37F | V* |
| C | Inland surface waters | 0,112,255 | #0070FF | V* |
| D | Mires, bogs and fens | 223,115,255 | #DF73FF | V* |
| E | Grasslands and land dominated by forbs, mosses or lichens | 85,255,0 | #55FF00 | V* |
| F | Heathland, scrub and tundra | 255,170,0 | #FFAA00 | V* |
| G | Woodland, forest and other wooded land | 38,115,0 | #267300 | V* |
| H | Inland unvegetated or sparsely vegetated habitats | 178,178,178 | #B2B2B2 | V* |
| I | Arable land and market gardens (label as given by the service) | 255,255,115 | #FFFF73 | V* |
| J | Constructed, industrial and other artificial habitats | 255,0,0 | #FF0000 | V* |

**Level 2** (service layer 0, 45 classes):

| Code | Name | R,G,B | Hex | Mark |
|---|---|---|---|---|
| B1 | Coastal dunes and sandy shores | 230,230,230 | #E6E6E6 | V* |
| B2 | Coastal shingle | 200,200,200 | #C8C8C8 | V* |
| B3 | Rock cliffs, ledges and shores, including the supralittoral | 170,170,170 | #AAAAAA | V* |
| C1 | Surface standing waters | 128,242,230 | #80F2E6 | V* |
| C2 | Surface running waters | 0,204,242 | #00CCF2 | V* |
| C3 | Littoral zone of inland surface waterbodies | 0,204,153 | #00CC99 | V* |
| D1 | Raised and blanket bogs | 64,49,81 | #403151 | V* |
| D2 | Valley mires, poor fens and transition mires | 96,73,122 | #60497A | V* |
| D3 | Aapa, palsa and polygon mires | 177,160,199 | #B1A0C7 | V* |
| D4 | Base-rich fens and calcareous spring mires | 204,192,218 | #CCC0DA | V* |
| D5 | Sedge and reedbeds, normally without free-standing water | 218,238,243 | #DAEEF3 | V* |
| D6 | Inland saline and brackish marshes and reedbeds | 183,222,232 | #B7DEE8 | V* |
| E1 | Dry grasslands | 240,240,150 | #F0F096 | V* |
| E2 | Mesic grasslands | 230,230,77 | #E6E64D | V* |
| E3 | Seasonally wet and wet grasslands | 204,242,77 | #CCF24D | V* |
| E4 | Alpine and subalpine grasslands | 153,255,153 | #99FF99 | V* |
| E6 | Inland salt steppes | 204,255,255 | #CCFFFF | V* |
| E7 | Sparsely wooded grasslands | 242,204,166 | #F2CCA6 | V* |
| F1 | Tundra | 151,71,6 | #974706 | V* |
| F2 | Arctic, alpine and subalpine scrub | 226,107,10 | #E26B0A | V* |
| F3 | Temperate and mediterranean-montane scrub | 250,191,143 | #FABF8F | V* |
| F4 | Temperate shrub heathland | 252,213,180 | #FCD5B4 | V* |
| F5 | Maquis, arborescent matorral and thermo-Mediterranean brushes | 253,233,217 | #FDE9D9 | V* |
| F6 | Garrigue | 218,238,243 | #DAEEF3 | V* |
| F7 | Spiny Mediterranean heaths (phrygana, hedgehog-heaths and related coastal cliff vegetation) | 183,222,232 | #B7DEE8 | V* |
| F8 | Thermo-Atlantic xerophytic scrub | 146,205,220 | #92CDDC | V* |
| F9 | Riverine and fen scrubs | 49,200,155 | #31C89B | V* |
| FB | Shrub plantations | 230,128,0 | #E68000 | V* |
| G1 | Broadleaved deciduous woodland | 128,255,0 | #80FF00 | V* |
| G2 | Broadleaved evergreen woodland | 230,166,0 | #E6A600 | V* |
| G3 | Coniferous woodland | 0,166,0 | #00A600 | V* |
| G4 | Mixed deciduous and coniferous woodland | 77,255,0 | #4DFF00 | V* |
| G5 | Lines of trees, small anthropogenic woodlands, recently felled woodland, early-stage woodland and coppice | 79,98,40 | #4F6228 | V* |
| H2 | Screes | 242,242,242 | #F2F2F2 | V* |
| H3 | Inland cliffs, rock pavements and outcrops | 204,204,204 | #CCCCCC | V* |
| H4 | Snow or ice-dominated habitats | 255,255,255 | #FFFFFF | V* |
| H5 | Miscellaneous inland habitats with very sparse or no vegetation | 204,255,204 | #CCFFCC | V* |
| I1 | Arable land and market gardens | 255,255,168 | #FFFFA8 | V* |
| I2 | Cultivated areas of gardens and parks | 255,255,0 | #FFFF00 | V* |
| J1 | Buildings of cities, towns and villages | 255,0,0 | #FF0000 | V* |
| J2 | Low density buildings | 255,125,125 | #FF7D7D | V* |
| J3 | Extractive industrial sites | 166,0,204 | #A600CC | V* |
| J4 | Transport networks and other constructed hard-surfaced areas | 255,85,0 | #FF5500 | V* |
| J5 | Highly artificial man-made waters and associated structures | 230,230,255 | #E6E6FF | V* |
| J6 | Waste deposits | 166,77,0 | #A64D00 | V* |

No legend exists for the revised 2021/2022 codes or for level 3 and below. The INSPIRE default style for habitats is a uniform grey (section 7.3).

---

## 6. EU ecosystem typologies

### 6.1 MAES typology (2013) (V)

Source: BISE "Typology of ecosystems" https://biodiversity.europa.eu/europes-biodiversity/ecosystems/typology-of-ecosystems (table from the first MAES report, Maes et al. 2013).

| Level 1 | Level 2 ecosystem type | Land-cover representation |
|---|---|---|
| Terrestrial | **Urban** | Urban, industrial, commercial and transport areas, urban green areas, mines, dump and construction sites |
| Terrestrial | Cropland | Annual and permanent crops |
| Terrestrial | Grassland | Pastures and (semi-)natural grasslands |
| Terrestrial | Woodland and forest | Forests |
| Terrestrial | Heathland and shrub | Moors, heathland and sclerophyllous vegetation |
| Terrestrial | Sparsely vegetated land | Open spaces with little or no vegetation |
| Terrestrial | Wetlands | Inland wetlands (marshes and peatbogs) |
| Fresh water | Rivers and lakes | Water courses and bodies |
| Marine | Marine inlets and transitional waters · Coastal · Shelf · Open ocean | – |

The BISE table itself notes that CLC is too coarse for the Urban type and "needs to be complemented e.g. by Urban atlas … and HRL Imperviousness".

### 6.2 CLC → MAES level 2 (official correspondence, V)

Source: https://biodiversity.europa.eu/europes-biodiversity/ecosystems/correspondence-between-corine-land-cover-classes-and-ecosystem-types

| CLC classes | MAES ecosystem type |
|---|---|
| 111, 112, 121, 122, 123, 124, 131, 132, 133, 141, 142 | Urban |
| 211, 212, 213, 221, 222, 223, 241, 242, 243, 244 | Cropland |
| 231, 321 | Grassland |
| 311, 312, 313, 324 | Woodland and forest |
| 322, 323 | Heathland and shrub |
| 331, 332, 333, 334, 335 | Sparsely vegetated areas |
| 411, 412 | Wetlands |
| 421, 422, 423, 521, 522 | Marine inlets and transitional waters |
| 511, 512 | Rivers and lakes |
| 523 | Marine |

### 6.3 Ecosystem types of Regulation (EU) No 691/2011 as amended by Regulation (EU) 2024/3024 — level 1 (V)

Source: Annex IX "Module for ecosystem accounts", Section 3, point 5 — https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202403024. First reference year 2024; extent and condition accounts every 3 years; transmission within 24 months; extent reported in thousand hectares.

| Category | Ecosystem type |
|---|---|
| 1 | Settlements and other artificial areas |
| 2 | Cropland |
| 3 | Grassland (pastures, semi-natural and natural grassland) |
| 4 | Forest and woodland |
| 5 | Heathland and shrub |
| 6 | Sparsely vegetated ecosystems |
| 7 | Inland wetlands |
| 8 | Rivers and canals |
| 9 | Lakes and reservoirs |
| 10 | Marine inlets and transitional waters |
| 11 | Coastal beaches, dunes and wetlands |
| 12 | Marine ecosystems (coastal waters, shelf and open ocean) |

### 6.4 EU ecosystem typology (EUET), levels 2 and 3 (V)

Source: Eurostat, "EU ecosystem typology – Technical Note", version July 2026 (URL in section 0.3). Level 1 is legally fixed (above); level 2 is in the questionnaire for voluntary reporting and "aligns, where feasible, with Corine Land Cover"; level 3 is "inspired by EUNIS". Names were extracted from the PDF text layer (multi-line cells re-joined by script; terrestrial names checked against the raw text).

**Type 1 "Settlements and other artificial areas" — complete (V)**

| Level 2 | Level 3 | Defining points (paraphrase) |
|---|---|---|
| 1.1 Continuous settlement area | 1.1.1 Continuous residential area · 1.1.2 Continuous commercial and industrial area | At least 80 % of the surface is impermeable (buildings, roads, other artificial surfaces). |
| 1.2 Discontinuous settlement area | 1.2.1 Discontinuous residential area · 1.2.2 Discontinuous commercial and industrial area | Impermeable features cover 30–80 %. |
| 1.3 Infrastructure and industrial areas | 1.3.1 Road and rail networks and associated land · 1.3.2 Port areas · 1.3.3 Airports · 1.3.4 Other infrastructure · 1.3.5 Mineral extraction sites · 1.3.6 Dump areas · 1.3.7 Construction sites | Transport infrastructure including associated green (tree lines, verges), extraction, dump and construction sites. |
| **1.4 Urban greenspace** | **1.4.1 Parks · 1.4.2 Sports and recreation sites · 1.4.3 Other urban green · 1.4.4 Urban blue** | Vegetated areas within or partly embraced by urban fabric; includes small urban water bodies; **excludes areas with soil sealing above 30 %**. Parks include lawns, small woods, flowerbeds, shrubberies, zoological and botanical gardens, community gardens. Other urban green includes tree alleys. Urban blue = lakes or substantial ponds in parks and other water bodies in settlements. |
| 1.5 Other artificial areas | 1.5.1 Permanent Greenhouses · 1.5.2 Cemeteries · 1.5.3 Archaeological sites | Urban-character land not in 1.1–1.4; cemeteries are placed here "even if predominantly green". |

**Other types — level 2 complete, level 3 for the types that occur in and around cities (V)**

| Level 1 | Level 2 | Level 3 (selected) |
|---|---|---|
| 2 Cropland | 2.1 Annual cropland · 2.2 Rice fields · 2.3 Permanent crops · 2.4 Agro-forestry areas · 2.5 Mixed farmland · 2.6 Other farmland | 2.1.7 Flowers and ornamental plants · 2.1.8 Fallow land · 2.1.9 Temporary grasses · 2.3.3 Pome fruits · 2.3.4 Stone fruits · 2.3.2 Grapes · 2.5.1 Mosaic farmland · 2.6.1 Nurseries · 2.6.2 Christmas tree plantations |
| 3 Grassland | 3.1 Sown pastures and other grass (modified grasslands) · 3.2 Natural and semi-natural grasslands | 3.1.1 Sown pastures used for grazing · 3.1.2 Sown grassland mown frequently for fodder or silage · 3.2.1 Mesic grassland · 3.2.2 Dry grassland · 3.2.3 Seasonally wet and wet grassland · 3.2.5 Woodland fringes and clearings and tall forb stands · 3.2.8 Wooded pastures |
| 4 Forest and woodland | 4.1 Broadleaved deciduous forest · 4.2 Coniferous forests · 4.3 Broadleaved evergreen forest · 4.4 Mixed forests · 4.5 Transitional forest and woodland shrub · 4.6 Plantations | 4.1.1 Riparian forest and woodland · 4.1.2 Broadleaved swamp forest on non-acid and acid peat · 4.1.3 Beech-dominated forest · 4.1.5 Acidophilous oak-dominated forests · 4.1.7 Other broadleaved deciduous forest, excluding highly modified plantations · 4.1.8 Highly modified broadleaved deciduous forests, including multi-species plantations · 4.2.4 Pine forest (excluding mires, non-thermophilous) · 4.2.9 Highly modified coniferous forests, in particular plantations · 4.4.1 / 4.4.2 Mixed forests dominated by coniferous / broadleaved species · 4.5.1 Transitional woodland/forest land · 4.6.1 Monoculture or mixed plantations of non-native species |
| 5 Heathland and shrub | 5.1 Tundra · 5.2 Scrub and heathland · 5.3 Sclerophyllous vegetation | 5.2.2 Temperate and Mediterranean montane scrub · 5.2.3 Temperate shrub heathland |
| 6 Sparsely vegetated ecosystems | 6.1 Bare rocks · 6.2 Semi-desert, desert and other sparsely vegetated areas · 6.3 Ice sheets, glaciers and perennial snowfields | 6.1.1 Rocky pavements, outcrops, and screes · 6.2.3 Other sparsely vegetated areas |
| 7 Inland wetlands | 7.1 Inland marshes and other wetlands on mineral soil · 7.2 Mires, bogs and fens | 7.1.1 Inland marshes · 7.1.2 Inland salt marshes · **7.1.3 Reedbeds** · 7.1.4 Springs · 7.2.1 Raised bogs · 7.2.3 Valley mires, poor fens and transition mires · 7.2.5 Base-rich fens and calcareous spring mires · 7.2.6 Peat extraction sites |
| 8 Rivers and canals | 8.1 Rivers and streams · 8.2 Canals, ditches and drains | 8.1.1 Permanent, non-tidal, fast, turbulent water courses · 8.1.2 Permanent non-tidal, smooth-flowing watercourses · 8.2.1 Canals · 8.2.2 Ditches and drains |
| 9 Lakes and reservoirs | 9.1 Lakes and ponds · 9.2 Artificial reservoirs · 9.3 Geothermal pools and wetlands (Iceland) | 9.1.1 Lakes · 9.1.2 Inland saline or brackish lakes and pools · 9.1.3 Ponds and natural small standing water bodies · 9.2.1 Artificial reservoirs |
| 10 Marine inlets and transitional waters | 10.1 Macrophyte communities and biogenic reefs (of class 10) · 10.2 Transitional waters · 10.3 Intertidal areas · 10.4 Anthropogenic structures and modified ecosystems (of class 10) | (not relevant here; names of marine sub-types script-reconstructed, not individually checked) |
| 11 Coastal beaches, dunes and wetlands | 11.1 Coastal dunes and fine sediment shores · 11.2 Rocky, boulder and coarse sediment shores · 11.3 Coastal halophytic wetlands · 11.4 Artificial shorelines | 11.1.1 Coastal dunes · 11.3.1 Coastal saltmarshes · 11.4.1 Sea walls and fortified shorelines |
| 12 Marine ecosystems | 12.1–12.10 (macrophyte communities, reefs, sublittoral sediments and rock, slope, deep sea, coastal inlets, anthropogenic structures, pelagic zone, sea ice) | – |

### 6.5 General ecosystem typology for National Restoration Plans (V)

Source: DG Environment "Technical background note" (rev. 02-10-25), "Use of a general ecosystem typology as part of the National Restoration Plan" — https://biodiversity.europa.eu/europes-biodiversity/nature-restoration/reference-portal-for-nature-restoration-regulation/documentation/technical-background-note-typology-of-ecosystems.pdf (informal, non-binding).

| NRP general ecosystem type | Link to EU ecosystem typology given in the note |
|---|---|
| Wetland ecosystems (coastal and inland) | Inland wetlands (ET7), Coastal marshes and salines (ET11.4 as written in the note), Marine inlets and transitional waters (ET10) + some level-3 sub-types |
| Grassland ecosystems | Grassland (ET3) + parts of 5.2.3 |
| Rivers, lakes, alluvial, riparian ecosystems | Rivers and canals (ET8), Lakes and reservoirs (ET9) + 4.1.1 riparian forest, part of 3.2.3 |
| Forests and woodland ecosystems | Forest and woodland (ET4) except 4.1.1 and 4.1.2 |
| Heath, shrub and scrub ecosystems | Heathland and shrub (ET5, except parts of 5.2.3) |
| Rocky, dune and sparsely vegetated ecosystems | Sparsely vegetated ecosystems (ET6), Coastal beaches, dunes and wetlands (ET11) |
| Cropland ecosystems | Cropland (ET2) |
| **Urban ecosystems (Settlements and other artificial areas)** | Settlements and other artificial areas (ET1) |
| Marine ecosystems | Marine ecosystems (ET12) |
| Others | n/a (caves etc.) |

The note's guidance definition of urban ecosystems: settlements and other artificial areas strongly modified by people and characterised by buildings, other man-made structures and vegetation or aquatic elements created or modified by human intervention, including residential, industrial, commercial and transport areas, mining sites, urban green areas, parks and small ponds (paraphrase).

---

## 7. INSPIRE

### 7.1 Land Cover theme (Annex II) (V)

Source: D2.8.II.2 Data Specification on Land Cover – Technical Guidelines, v3.1.0 (2024-01-31): https://inspire-mif.github.io/technical-guidelines/data/lc/dataspecification_lc.html

- INSPIRE prescribes **no land-cover nomenclature**. The code list `LandCoverClassValue` is empty and extensible with any values (registry: https://inspire.ec.europa.eu/codelist/LandCoverClassValue).
- **Default portrayal carries no thematic colours:** `LC.LandCoverPoints.Default` = 3-pixel circle, black fill and outline (#000000); `LC.LandCoverSurfaces.Default` = white fill (#FFFFFF), black outline (#000000) of 3 pixels; `LC.LandCoverRaster.Default` = opaque raster. The guideline *recommends* filling polygons with the colour of the nomenclature's own legend (its example is CORINE Land Cover).
- **Pure Land Cover Components (PLCC)** — Annex H, *informative*, developed with the EAGLE group; not mandatory. The annex provides a colour map; the values below were read from the table image in the guideline (V).

| Code | Pure land cover component | R/G/B | Hex | Mark |
|---|---|---|---|---|
| 001 | Artificial constructions | 255/99/133 | #FF6385 | V |
| 002 | Consolidated bare surface | 156/156/156 | #9C9C9C | V |
| 003 | Unconsolidated bare surface | 204/210/165 | #CCD2A5 | V |
| 004 | Arable land | 255/255/168 | #FFFFA8 | V |
| 005 | Permanent woody and shrubby crops | 247/200/100 | #F7C864 | V |
| 006 | Coniferous forest trees | 68/150/0 | #449600 | V |
| 007 | Broadleaved forest trees | 0/220/0 | #00DC00 | V |
| 008 | Shrubs | 150/190/0 | #96BE00 | V |
| 009 | Herbaceous plants | 202/242/77 | #CAF24D | V |
| 010 | Lichens and mosses | 166/255/160 | #A6FFA0 | V |
| 011 | Wetlands and marshes | 0/214/178 | #00D6B2 | V |
| 012 | Organic deposits (Peatland) | 156/127/120 | #9C7F78 | V |
| 013 | Chemical deposits | 227/212/255 | #E3D4FF | V |
| 014 | Intertidal flats | 173/138/167 | #AD8AA7 | V |
| 015 | Fresh water course | 0/190/255 | #00BEFF | V |
| 016 | Fresh water bodies | 90/214/255 | #5AD6FF | V |
| 017 | Salt or brackish water | 0/148/194 | #0094C2 | V |
| 018 | Permanent snow and ice | 180/255/255 | #B4FFFF | V |

PLCC content notes (V, paraphrased): 001 covers all sealed man-made constructions (buildings, other constructions, linear networks) and excludes parks and gardens; 002 is solid rock including quarries; 003 is loose natural material (boulders to clay) and unvegetated fallow land; 008 includes dwarf shrubs; 009 is all grass and forb vegetation except arable crops; 011 and 012 describe growing conditions and are meant to be combined with a vegetation component; components may be combined with percentages (e.g. mixed forest = 006 + 007). LUCAS 2022 reproduces these 18 components as Annex 9.11 of its surveyor instructions (V): https://ec.europa.eu/eurostat/documents/205002/13686460/C1-Annex-9.11-LUCAS-2022.pdf

### 7.2 Land Use theme (Annex III) — HILUCS (V)

Sources: INSPIRE registry code list `HILUCSValue` (98 values, all "Valid", governance level "Legal (EU)") https://inspire.ec.europa.eu/codelist/HILUCSValue; portrayal from D2.8.III.4 Data Specification on Land Use – Technical Guidelines (published 2024-07-31) https://inspire-mif.github.io/technical-guidelines/data/lu/dataspecification_lu.html

**HILUCS levels 1 and 2 (complete) with level 3 (complete list of registry values):**

| Level 1 | Level 2 | Level 3 |
|---|---|---|
| 1_PrimaryProduction | 1_1_Agriculture | 1_1_1_CommercialAgriculturalProduction · 1_1_2_FarmingInfrastructure · 1_1_3_AgriculturalProductionForOwnConsumption |
| | 1_2_Forestry | 1_2_1_ForestryBasedOnShortRotation · 1_2_2_ForestryBasedOnIntermediateOrLongRotation · 1_2_3_ForestryBasedOnContinuousCover |
| | 1_3_MiningAndQuarrying | 1_3_1_MiningOfEnergyProducingMaterials · 1_3_2_MiningOfMetalOres · 1_3_3_OtherMiningAndQuarrying |
| | 1_4_AquacultureAndFishing | 1_4_1_Aquaculture · 1_4_2_ProfessionalFishing |
| | 1_5_OtherPrimaryProduction | 1_5_1_Hunting · 1_5_2_ManagementOfMigratoryAnimals · 1_5_3_PickingOfNaturalProducts |
| 2_SecondaryProduction | 2_1_RawIndustry | 2_1_1 … 2_1_9 (textiles; wood; pulp and paper; coke, petroleum, nuclear fuel; chemicals; basic and fabricated metals; non-metallic mineral products; rubber and plastic; other raw materials) |
| | 2_2_HeavyEndProductIndustry | 2_2_1_ManufacturingOfMachinery · 2_2_2_ManufacturingOfVehiclesAndTransportEquipment · 2_2_3_ManufacturingOfOtherHeavyEndProducts |
| | 2_3_LightEndProductIndustry | 2_3_1 … 2_3_5 (food, beverages and tobacco; clothes and leather; publishing and printing; electrical and optical equipment; other light end products) |
| | 2_4_EnergyProduction | 2_4_1_NuclearBasedEnergyProduction · 2_4_2_FossilFuelBasedEnergyProduction · 2_4_3_BiomassBasedEnergyProduction · 2_4_4_RenewableEnergyProduction |
| | 2_5_OtherIndustry | – |
| 3_TertiaryProduction | 3_1_CommercialServices | 3_1_1_WholesaleAndRetailTradeAndRepairOfVehiclesAndPersonalAndHouseholdGoods · 3_1_2_RealEstateServices · 3_1_3_AccommodationAndFoodServices · 3_1_4_OtherCommercialServices |
| | 3_2_FinancialProfessionalAndInformationServices | 3_2_1 … 3_2_5 |
| | 3_3_CommunityServices | 3_3_1_PublicAdministrationDefenceAndSocialSecurityServices · 3_3_2_EducationalServices · 3_3_3_HealthAndSocialServices · 3_3_4_ReligiousServices · 3_3_5_OtherCommunityServices |
| | 3_4_CulturalEntertainmentAndRecreationalServices | 3_4_1_CulturalServices · 3_4_2_EntertainmentServices · **3_4_3_SportsInfrastructure** · **3_4_4_OpenAirRecreationalAreas** · 3_4_5_OtherRecreationalServices |
| | 3_5_OtherServices | – |
| 4_TransportNetworksLogisticsAndUtilities | 4_1_TransportNetworks | 4_1_1_RoadTransport · 4_1_2_RailwayTransport · 4_1_3_AirTransport · 4_1_4_WaterTransport · 4_1_5_OtherTransportNetwork |
| | 4_2_LogisticalAndStorageServices | – |
| | 4_3_Utilities | 4_3_1_ElectricityGasAndThermalPowerDistributionServices · 4_3_2_WaterAndSewageInfrastructure · 4_3_3_WasteTreatment · 4_3_4_OtherUtilities |
| 5_ResidentialUse | 5_1_PermanentResidentialUse · 5_2_ResidentialUseWithOtherCompatibleUses · 5_3_OtherResidentialUse | – |
| 6_OtherUses | 6_1_TransitionalAreas · 6_2_AbandonedAreas · 6_3_NaturalAreasNotInOtherEconomicUse · 6_4_AreasWhereAnyUseAllowed · 6_5_AreasWithoutAnySpecifiedPlannedUse · 6_6_NotKnownUse | 6_3_1_LandAreasNotInOtherEconomicUse · 6_3_2_WaterAreasNotInOtherEconomicUse |

**INSPIRE default portrayal for Land Use (V — colour tables are images in section 11.2 of the guideline):** style `LandUse.ExistingLandUse.Default` (and the identical `LandUse.ZoningElement.Default`): objects filled by **HILUCS level 1**, boundaries black, 2 pixels. Data providers may apply the limited level-2 "adjustments" listed second.

| HILUCS value (spelling as in the guideline's table) | R | G | B | Hex | Mark |
|---|---|---|---|---|---|
| 1_PrimaryProduction | 180 | 230 | 110 | #B4E66E | V |
| 2_SecondaryProduction | 100 | 100 | 100 | #646464 | V |
| 3_TertiaryProduction | 150 | 150 | 150 | #969696 | V |
| 4_TransportNetworksLogisticsAndUtilities | 180 | 120 | 240 | #B478F0 | V |
| 5_ResidentialUse | 240 | 120 | 100 | #F07864 | V |
| 6_OtherUses | 220 | 220 | 220 | #DCDCDC | V |
| adjustment: 1_1_AgriculturalUse (registry: 1_1_Agriculture) | 230 | 230 | 110 | #E6E66E | V |
| adjustment: 1_2_Forestry | 110 | 230 | 110 | #6EE66E | V |
| adjustment: 4_1_4_WaterTraffic (registry: 4_1_4_WaterTransport) | 140 | 120 | 240 | #8C78F0 | V |
| adjustment: 6_3_1_LandAreasInNaturalUse (registry: 6_3_1_LandAreasNotInOtherEconomicUse) | 200 | 255 | 200 | #C8FFC8 | V |
| adjustment: 6_3_2_WaterAreasInNaturalUse (registry: 6_3_2_WaterAreasNotInOtherEconomicUse) | 200 | 200 | 255 | #C8C8FF | V |

Other LU styles: `LandUse.SpatialPlan.Default` = plan extent as black line, 2 pixels; `LandUse.SupplementaryRegulation.Default` = coloured 2-pixel line by regulation type. The SLD files are distributed separately from the guideline (not inspected).

### 7.3 Habitats and Biotopes theme (Annex III) (V)

Source: D2.8.III.18 v4.0.0 (2024-01-31) https://inspire-mif.github.io/technical-guidelines/data/hb/dataspecification_hb.html; registry https://inspire.ec.europa.eu/codelist/ReferenceHabitatTypeSchemeValue

- Reference habitat type schemes (`ReferenceHabitatTypeSchemeValue`, not extensible): **eunis** (EUNIS habitat classification), **habitatsDirective** (Annex I to Directive 92/43/EEC), **marineStrategyFrameworkDirective** (Table 1 of Annex III to Directive 2008/56/EC).
- Code lists: `EunisHabitatTypeCodeValue` (values as published by the EEA; the registry lists none itself), `HabitatsDirectiveCodeValue`, `MarineStrategyFrameworkDirectiveCodeValue`, `LocalNameCodeValue` with `QualifierLocalNameValue` for the relation between a local type and the pan-European reference type — five values (V, https://inspire.ec.europa.eu/codelist/QualifierLocalNameValue): **congruent** (conceptually the same), **includedIn** (the local type is a subtype of the pan-European type), **includes** (the pan-European type is a subtype of the local type), **overlaps** (partial overlap, none of the other relations holds), **excludes**.
- Layers: `HB.Habitat`, `HB.HabitatDistribution`. **Default style `HB.Habitat.Default`:** points as 6-pixel squares and surfaces filled 50 % grey with black 1-pixel outline; the guideline gives the grey as "#808080" in the SLD abstract and as "RGB 80,80,80" in the prose (internally inconsistent). No per-habitat colours are prescribed; a layer per habitat type is recommended.

**Conclusion (V):** among the three INSPIRE themes only **Land Use** prescribes thematic default colours (six HILUCS level-1 colours); Land Cover offers an informative PLCC colour map; Habitats and Biotopes prescribes a uniform grey.

---

## 8. LUCAS and EAGLE

### 8.1 LUCAS land cover (Eurostat) (V)

Source: LUCAS 2022 Technical reference document C3 "Classification (Land cover & Land use)" https://ec.europa.eu/eurostat/documents/205002/13686460/C3-LUCAS-2022.pdf (linked from https://ec.europa.eu/eurostat/web/lucas/database/2022). LUCAS is an in-situ point survey (2 km grid, about 1 million points; a sample is visited) — a nomenclature and validation source, not a map product. **No official legend colours were found for LUCAS** (not verified either way → open point).

| Code | Name | Key definition (paraphrase) |
|---|---|---|
| **A00** | **Artificial land** | Artificial, often impervious cover of constructions and pavement |
| A10 | Roofed built-up areas | |
| A11 | Buildings with one to three floors | up to 3 floors or below 10 m; at least 3 m wide |
| A12 | Buildings with more than three floors | more than 3 floors or above 10 m |
| A13 | Greenhouses | glass or plastic; crop inside is double-coded |
| A20 | Artificial non-built up areas | hard artificial materials, concrete, gravel |
| A21 | Non built-up area features | yards, farmyards, **cemeteries**, car parks (even if grass-covered), quays, storage areas |
| A22 | Non built-up linear features | roads (even unsealed), railways, runways — if wider than 3 m |
| A30 | Other artificial areas | bridges and viaducts, mobile homes, solar panels, power plants, substations, pipelines, sewage plants, open dump sites |
| **B00** | **Cropland** | B10 Cereals (B11 Common wheat, B12 Durum wheat, B13 Barley, B15 Oats, …) · B20 Root crops (B21–B23) · B30 Non-permanent industrial crops (B31–B37) · B40 Dry pulses, vegetables and flowers (B41–B45; B44 Floriculture and ornamental plants) · B50 Fodder crops (B51–B55; B55 Temporary grasslands) · B70 Permanent crops: fruit trees (B71 Apple, B72 Pear, B73 Cherry, B76 Oranges, B77 Other citrus, …) · B80 Other permanent crops (B81 Olive groves, B82 Vineyards, B83 Nurseries, B84 Permanent industrial crops). Codes B14, B16–B19, B74, B75 exist in the series but were not captured in my extraction. |
| **C00** | **Woodland** | tree canopy at least 10 %; woody hedges and palm trees included |
| C10 | Broadleaved woodland | more than 75 % broadleaved |
| C20 | Coniferous woodland | C21 Spruce dominated · C22 Pine dominated · C23 Other coniferous woodland |
| C30 | Mixed woodland | C31 Spruce dominated mixed · C32 Pine dominated mixed · C33 Other mixed woodland |
| **D00** | **Shrubland** | shrubs on at least 10 % of the surface, tree canopy below 10 % |
| D10 | Shrubland with sparse tree cover | tree canopy 5 to below 10 % |
| D20 | Shrubland without tree cover | trees below 5 % |
| **E00** | **Grassland** | grasses, grass-like plants and forbs; permanent (not in rotation) |
| E10 | Grassland with sparse tree/shrub cover | tree + shrub canopy 5–18 % |
| E20 | Grassland without tree/shrub cover | tree + shrub canopy below 5 %; includes public gardens, golf courses, sports fields via land use U36x |
| E30 | Spontaneously re-vegetated surfaces | set-aside and abandoned land, brownfields and unused artificial land with spontaneous vegetation |
| **F00** | **Bare land and lichens/moss** | no dominant vegetation on at least 90 % of the area |
| F10 | Rocks and stones | |
| F20 | Sand | sand, shingle and mud: beaches, dunes; gravel or sand banks |
| F30 | Lichens and moss | |
| F40 | Other bare soil | |
| **G00** | **Water areas** | |
| G10 | Inland water bodies | G11 Inland fresh water bodies · G12 Inland salty water bodies |
| G20 | Inland running water | G21 Inland fresh running water · G22 Inland salty running water |
| G30 | Transitional water bodies | as in the Water Framework Directive |
| G40 | Sea and ocean | |
| G50 | Glaciers, permanent snow | |
| **H00** | **Wetlands** | |
| H10 | Inland wetlands | H11 Inland marshes · H12 Peatbogs |
| H20 | Coastal wetlands | H21 Salt marshes · H22 Salines and other chemical deposits · H23 Intertidal flats |

LUCAS land-use codes (separate axis, V): U110 Agriculture (U111, U112 Fallow land, U113 Kitchen garden) · U120 Forestry · U130 Aquaculture and fishing · U140 Mining and quarrying · U150 Other primary production · U210 Energy production · U220 Industry and manufacturing (U221–U228) · U310 Transport, communication networks, storage, protection works (U311 Railway, U312 Road, U313 Water, U314 Air transport, U315 pipelines, U316 Telecommunication, U317 Logistics and storage, U318 Protection infrastructures, U319 Electricity, gas and thermal power distribution) · U320 Water and waste treatment (U321, U322) · U330 Construction · U340 Commerce, financial, professional and information services (U341, U342) · U350 Community services · U360 Recreation, leisure, sport (U361 Amenities, museums, leisure; U362 Sport) · U370 Residential · U410 Abandoned areas (U411–U415) · U420 Semi-natural and natural areas not in use.

**Useful LUCAS principle (V):** land cover and land use are coded on two independent axes, and the manual lists the admissible combinations (e.g. E20 + U362 = sports turf; A21 + U370 = residential yard). This is the same cover/use separation as EAGLE and INSPIRE (PLCC + HILUCS).

### 8.2 EAGLE concept (V)

Sources: https://land.copernicus.eu/en/eagle (tabs "Introduction and context" and "Technical implementation"; matrix figure https://land.copernicus.eu/en/eagle/eagle-matrix-1-2.jpg/@@images/image/huge) and the CLC+ Backbone 2023 manual.

- EAGLE is the Eionet Action Group on Land monitoring in Europe (active since 2008). It is **not another nomenclature** but a semantic tool for *characterising* land units and for translating between nomenclatures. EAGLE compliance is required of new CLMS products and the concept is a central component of CLCplus.
- The **EAGLE matrix** has three blocks: **Land Cover Components (LCC)**, subdivided into Abiotic, Biotic and Water; **Land Use Attributes (LUA)**; **Land Characteristics (LCH)** (management type, spatial pattern, (bio-)physical characteristics, ecosystem types, status …). Elements are hierarchical, down to six levels.
- In the UML data model a **Land Unit** is composed of one or several LCCs, can be enriched by LUAs, and each LCC or the whole unit can be described further by LCHs.
- Design criteria named on the page: clear separation of land cover and land use plus further characteristics; object-oriented description instead of classification; inclusion of seasonal phenomena; scale independence.

Land Cover Components — upper levels as drawn in the official matrix figure (V):

| Level 1 | Level 2 | Level 3 | Next level (as far as legible in the figure) | Code cited in the CLC+ Backbone 2023 manual |
|---|---|---|---|---|
| ABIOTIC | Artificial | Sealed | Buildings · Specific Structures · Open Sealed | 1.1.1 |
| ABIOTIC | Artificial | Non-Sealed | Open Non-Sealed · Waste | 1.1.2 |
| ABIOTIC | Natural | Consolidated | Bare Rock · Hard Pan | 1.2 |
| ABIOTIC | Natural | Un-Consolidated | Mineral Fragments · Bare Soil · Natural Deposits | 1.2 |
| BIOTIC | Woody | Trees | – | 2.1.1 |
| BIOTIC | Woody | Bushes | Regular Bushes · Dwarf Shrubs | 2.1.2 |
| BIOTIC | Herbaceous | Grass-like | Grass, Cereals · Reeds, Bamboo | 2.2 |
| BIOTIC | Herbaceous | Forbs, Ferns | – | 2.2 |
| BIOTIC | Succulents | – | – | not cited |
| BIOTIC | Lichen, Mosses, Algae | Lichens · Mosses · Algae | – | 2.4 |
| WATER | Liquid | Inland · Marine | – | 3.1 |
| WATER | Solid | Snow · Ice | – | 3.2 |

The CLC+ manual additionally cites LCC 1.1.1.3 (the node from which railway tracks deviate — by position "Open Sealed", A) and the Land Characteristics LCH 3.1.1, 3.2.1 and 3.2.2 for needle-leaved, evergreen and deciduous trees (codes V, meanings inferred from the class definitions, A).

**Why this matters for the catalog (A):** the library's surface elements are EAGLE land-cover components in all but name — sealed (asphalt, concrete, paving), non-sealed artificial (gravel, water-bound surfaces), unconsolidated natural (soil, sand), woody (trees, bushes), herbaceous (grass-like, forbs), water. Tagging each element with its LCC node gives a single pivot from which CLC+ Backbone, INSPIRE PLCC and LUCAS codes follow.

---

## 9. Local Climate Zones and ESA WorldCover

### 9.1 Local Climate Zones (LCZ)

Typology: Stewart, I. D. & Oke, T. R. (2012), "Local Climate Zones for Urban Temperature Studies", Bulletin of the American Meteorological Society 93(12), 1879–1900, doi:10.1175/BAMS-D-11-00019.1 (the paper itself was not opened; class names below are those of the WUDAPT data product). 17 classes: 10 built types and 7 land-cover types.

**Two colour tables are in circulation and they differ slightly:**

- **Palette A — the "official hex color" of the global LCZ map (V).** Listed in the `readme.txt` (updated 2023-10-08) of Demuzere et al., "Global map of Local Climate Zones", Zenodo, version 3.0.0, and embedded in the GeoTIFF `lcz_filter_v3.tif`: https://zenodo.org/records/8419340 (described in Demuzere et al. 2022, Earth Syst. Sci. Data 14, 3835–3873, doi:10.5194/essd-14-3835-2022).
- **Palette B — class table of the Earth Engine Data Catalog** for the same dataset (producer: Bochum Urban Climate Lab) (S — a catalogue page, numbers seen): https://developers.google.com/earth-engine/datasets/catalog/RUB_RUBCLIM_LCZ_global_lcz_map_latest. This is the palette commonly quoted as "the WUDAPT colours". Which of the two the LCZ Generator and older WUDAPT level-0 maps use was not checked.

| Value | LCZ | Name (Zenodo readme) | Palette A R,G,B | Palette A hex (V) | Palette B hex (S) |
|---|---|---|---|---|---|
| 1 | LCZ 1 | Compact highrise | 145,6,19 | #910613 | #8C0000 |
| 2 | LCZ 2 | Compact midrise | 217,8,28 | #D9081C | #D10000 |
| 3 | LCZ 3 | Compact lowrise | 255,10,34 | #FF0A22 | #FF0000 |
| 4 | LCZ 4 | Open highrise | 197,79,30 | #C54F1E | #BF4D00 |
| 5 | LCZ 5 | Open midrise | 255,102,40 | #FF6628 | #FF6600 |
| 6 | LCZ 6 | Open lowrise | 255,152,94 | #FF985E | #FF9955 |
| 7 | LCZ 7 | Lightweight low-rise | 253,237,63 | #FDED3F | #FAEE05 |
| 8 | LCZ 8 | Large lowrise | 187,187,187 | #BBBBBB | #BCBCBC |
| 9 | LCZ 9 | Sparsely built | 255,203,171 | #FFCBAB | #FFCCAA |
| 10 | LCZ 10 | Heavy Industry | 86,86,86 | #565656 | #555555 |
| 11 | LCZ A | Dense trees | 0,106,24 | #006A18 | #006A00 |
| 12 | LCZ B | Scattered trees | 0,169,38 | #00A926 | #00AA00 |
| 13 | LCZ C | Bush, scrub | 98,132,50 | #628432 | #648525 |
| 14 | LCZ D | Low plants | 181,218,127 | #B5DA7F | #B9DB79 |
| 15 | LCZ E | Bare rock or paved | 0,0,0 | #000000 | #000000 |
| 16 | LCZ F | Bare soil or sand | 252,247,177 | #FCF7B1 | #FBF7AE |
| 17 | LCZ G | Water | 101,107,250 | #656BFA | #6A6AFF |

Notes:
- Raster value coding 1–17 (A–G = 11–17) is the convention of the global map (V). RGB triples are my conversion of the readme's hex values.
- The dataset authors themselves advise combining the ten built classes with another land-cover product where a wider range of natural classes is needed (V, Zenodo description) — for this library that means: LCZ 1–10 style *urban structure*, the library's own elements style the land cover.
- Convention (A): compact built types run dark red → red, open built types brown-orange → light orange, lightweight yellow, large low-rise light grey, heavy industry dark grey, trees two greens, scrub olive, low plants light green, paved black, bare soil pale yellow, water blue-violet.
- The Urban Atlas 2021 manual cites France's national LCZ map (Cerema), built on Urban Atlas areas, as a use case (V).

### 9.2 ESA WorldCover (V)

Source: ESA WorldCover **Product User Manual**, document WorldCover_PUM_v2.0, version 2.0, last modified 2022-10-24, Table 3 "Coding of the Map layer and definition of the classes": https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/docs/WorldCover_PUM_V2.0.pdf. The hex values (my conversion) agree with the class table of the Earth Engine Data Catalog entry `ESA/WorldCover/v200` (S): https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v200

Product facts (V; the Sentinel-1/Sentinel-2 basis and the version labels v100/v200 are taken from the catalogue entry, S): 10 m global land cover from Sentinel-1 and Sentinel-2; map for 2020 (v100) and 2021 (v200); 11 classes defined with the UN FAO Land Cover Classification System (LCCS); cloud-optimised GeoTIFF, one byte per pixel.

| Map code | Class | R,G,B | Hex | Definition (paraphrase) | Mark |
|---|---|---|---|---|---|
| 10 | Tree cover | 0,100,0 | #006400 | trees with at least 10 % cover, including plantations and tree crops; other covers may lie below the canopy | V |
| 20 | Shrubland | 255,187,34 | #FFBB22 | natural shrubs with at least 10 % cover, below 5 m | V |
| 30 | Grassland | 255,255,76 | #FFFF4C | natural herbaceous plants with at least 10 % cover; woody plants below 10 % | V |
| 40 | Cropland | 240,150,255 | #F096FF | annual cropland; perennial woody crops fall under tree cover or shrubland; greenhouses count as built-up | V |
| 50 | Built-up | 250,0,0 | #FA0000 | buildings, roads and other man-made structures such as railroads; **urban green (parks, sport facilities) is not included**; waste dumps and extraction sites count as bare | V |
| 60 | Bare / sparse vegetation | 180,180,180 | #B4B4B4 | exposed soil, sand or rock with never more than 10 % vegetation | V |
| 70 | Snow and ice | 240,240,240 | #F0F0F0 | persistent snow or glaciers | V |
| 80 | Permanent water bodies | 0,100,200 | #0064C8 | covered by water for more than 9 months a year | V |
| 90 | Herbaceous wetland | 0,150,160 | #0096A0 | herbaceous vegetation permanently or regularly flooded | V |
| 95 | Mangroves | 0,207,117 | #00CF75 | salt-tolerant woody vegetation of tropical intertidal zones | V |
| 100 | Moss and lichen | 250,230,160 | #FAE6A0 | land covered by lichens and/or mosses | V |

Convention (A): built-up red; trees dark green; shrubland orange; grassland yellow; cropland pink-violet; bare grey; water strong blue; wetland teal. Compared with the Copernicus legends only "red = built-up", "dark green = trees", "grey = bare" and "blue = water" carry over.

---

## 10. Crosswalks — what exists and where

| Crosswalk | Where | Mark |
|---|---|---|
| CLC level 3 → MAES ecosystem type (level 2) | BISE table, reproduced in section 6.2: https://biodiversity.europa.eu/europes-biodiversity/ecosystems/correspondence-between-corine-land-cover-classes-and-ecosystem-types | V |
| MAES typology ↔ EUNIS level 1 (habitat representation per ecosystem type) | BISE "Typology of ecosystems" table: https://biodiversity.europa.eu/europes-biodiversity/ecosystems/typology-of-ecosystems | V |
| EUNIS 2021/2022 ↔ Habitats Directive Annex I, ↔ European Red List of Habitats, ↔ Bern Convention Res. 4, ↔ EUNIS 2012 | EEA SDI series "EUNIS habitat classification and crosswalks (tabular data)" (Excel tables): https://sdi.eea.europa.eu/catalogue/srv/api/records/638330ea-90e6-4e41-81ea-e70f25ae7117; per-habitat relations are also shown on the BISE habitat pages (`/habitats_eunis_revised/EUNISrev_<code>`) | V (existence and description); tables not opened |
| EUNIS level 2 ↔ CLC (+ other Copernicus layers) | Rule set behind the EEA "Ecosystem types of Europe" maps: the service description states that it "builds on the crosswalk between EUNIS nomenclature and CORINE Land Cover nomenclature" (V, https://bio.discomap.eea.europa.eu/arcgis/rest/services/MAES/MAES_ecosystem_type_maps_WM/MapServer); details in ETC/BD Technical Paper 11/2018 "Ecosystem Type Map v3.1" (S, not opened); dataset page https://www.eea.europa.eu/data-and-maps/data/ecosystem-types-of-europe-1 | V (existence) / S (content) |
| Crosswalks between European marine habitat typologies | BISE PDF: https://biodiversity.europa.eu/europes-biodiversity/ecosystems/crosswalks-between-european-marine-habitat-typologies_10-04-14_v3.pdf | V (link exists; not opened) |
| EU ecosystem typology ↔ IUCN Global Ecosystem Typology (levels 1–2) | Annex 2 of the Eurostat technical note (July 2026) | V (existence) |
| EU ecosystem typology ↔ CLC (level 2 "aligns, where feasible") and ↔ EUNIS (level 3 "inspired by EUNIS") | stated design principle in the Eurostat technical note; no explicit table seen | V (statement) |
| NRP general ecosystem typology ↔ EUET ↔ NRR Annex I/II groups ↔ PAF categories | Table 1 of the DG ENV technical background note (section 6.5) | V |
| Urban Atlas ↔ CLC | No separate official table found. UA is "derived from CORINE Land Cover"; the first three digits of the UA code follow CLC level 3 for class 1 (111, 121, 122, 123, 124, 133, 141, 142). Differences: UA merges CLC 131 + 132 into 13100, adds 13400 (no CLC equivalent), splits 112 into four sealing classes plus 11300, splits 122 into three transport classes, and keeps only level 2 for classes 2–3 and level 1 for 4–5. | V (statement) + A (comparison) |
| CLC+ Backbone ↔ EAGLE LCC | Section 6.1.2 of the 2023 manual (section 3.2 above) | V |
| CLC+ Backbone ↔ NRR "urban green space" | Commission/EEA methodological note (section 4.3 above) | V |
| LUCAS ↔ INSPIRE PLCC | LUCAS 2022 C1 Annex 9.11 (component definitions) and the C1 cross tables (Annexes 9.3–9.7, xlsx, not opened) | V (existence) |
| CLC ↔ LCML / PLCC | Worked examples (CLC 213, CLC 243) in the INSPIRE LC guideline annex | V |
| WUDAPT LCZ ↔ land cover / Urban Atlas | not researched (France's national LCZ map is built on Urban Atlas areas according to the UA 2021 manual, use case 2) | V (use case only) |

---

## 11. Official portrayal — availability per scheme

| Scheme | Official / quasi-official colours available? | Form | Usable for an "official colours" theme |
|---|---|---|---|
| CORINE Land Cover | **Yes** — one RGB per level-3 class | EEA map-service renderer; legend files shipped with the data | Yes (44 values in section 1) |
| Urban Atlas | **Yes** — 2018 and 2021 legends, including the access sub-classes 14110–14130 and the Street Tree Layer | EEA map-service renderer (2018); SLD of the CLMS WMS (2021); QML shipped with the data | Yes (sections 2.2 and 2.4) |
| CLC+ Backbone | **Yes** | colour palette table in the manuals; `.clr`, `.qml`, `.sld`, `.lyr`, embedded colour map | Yes (section 3.2) |
| INSPIRE Land Cover | Default style is colourless; PLCC colour map is *informative* | guideline annex | Optional "INSPIRE PLCC" theme (section 7.1) |
| INSPIRE Land Use (HILUCS) | **Yes** — six level-1 colours plus five permitted adjustments | guideline section 11.2; SLD distributed separately | Yes (section 7.2) |
| INSPIRE Habitats and Biotopes | Uniform grey only | guideline | No thematic theme possible |
| EUNIS | For the **2012 codes at level 1 and level 2 only**, via the legend of the EEA "Ecosystem types of Europe" map; nothing for the 2021/2022 codes or for level 3 and below | swatch images of the EEA map service (values sampled) | Partly (section 5.6): an "EEA ecosystem map" theme for level-2 habitat data; house colours for everything finer |
| MAES / EU ecosystem typology | None found for the 12 MAES types or for the EU ecosystem typology; the EEA ecosystem-type maps are drawn in the EUNIS level-2 legend instead | – | No official theme |
| LUCAS | None found | – | No official theme |
| Local Climate Zones | **Yes** — "official hex color" table of the global LCZ map (palette A); a slightly different palette B circulates | Zenodo readme; colour table embedded in the GeoTIFF | Yes (section 9.1): ship palette A, offer B as an alias |
| ESA WorldCover | **Yes** | Table 3 of the Product User Manual v2.0 | Yes (section 9.2) |

**Hue conventions shared across the European schemes (A, derived from the verified values):**

| Theme | CLC | Urban Atlas | CLC+ Backbone | INSPIRE PLCC | Convention to respect |
|---|---|---|---|---|---|
| Sealed / built-up | reds, magentas | dark-to-pale reds by sealing; roads grey | pure red | pinkish red | **red family = sealed/built**; grey is read as *bare/non-vegetated* or as *roads* |
| Trees / forest | saturated greens (broadleaf lighter, conifer darker) | dark green | three greens (conifer darkest) | two greens (conifer darker) | green; conifer darker than broadleaf |
| Shrubs | yellow-greens | (in 32000) | **brown** | olive | not settled — olive/brownish green is the safest bridge |
| Herbaceous / grassland | 204,242,77 (natural grassland); pasture yellow 230,230,77 | 204,242,77 | 204,242,77 | 202,242,77 | **light yellow-green** is shared by all four |
| Arable | 255,255,168 | 255,255,168 | 255,255,128 | 255,255,168 | **pale yellow** |
| Bare / sparse | greys, pale green | pale green | grey 191 | grey / beige | light grey or beige |
| Wetlands | blue-violet 166,166,255 | 166,166,255 | (in class 6 or 10) | turquoise | blue-violet (CLC family) or turquoise (INSPIRE) |
| Water | cyan / pale turquoise 128,242,230 | 128,242,230 | blue 0,128,255 | blues | blue-cyan family |
| Urban green | **pink** 255,166,255 | **yellow-green** 140,220,0 | (by land cover) | (by land cover) | conflict between CLC and UA — follow UA/green for city-scale maps |

---

## 12. Open points (not verified)

| # | Open point | What would close it |
|---|---|---|
| 1 | **LCZ palette choice:** two slightly different colour tables exist (section 9.1). Palette A is declared official by the dataset authors; which palette the LCZ Generator and older WUDAPT level-0 products apply was not checked. The Stewart & Oke (2012) paper was not opened, so class definitions and the original spelling of the names ("high-rise" vs. "highrise") are not verified. | LCZ Generator documentation; the 2012 paper. |
| 2 | **CLC 2024:** announced for Q3 2026, not listed on the product page on 2026-09-30; nomenclature stated to remain unchanged. | Re-check the product page; confirm that the legend is unchanged. |
| 3 | **EUNIS:** official colours exist only for the 2012 level-1 and level-2 codes (section 5.6); the successor codes of the 2012 bare-ground units H5.3 / H5.5 / H5.6 and the status of group J in the revision are unclear; the 2012 → 2021 correspondences in section 5.5 are name-based and not taken from the official crosswalk; the EEA ecosystem-map colours in section 5.6 were sampled from legend swatch images rather than read from a colour table. | EEA crosswalk Excel tables; the dataset's symbology file. |
| 4 | **MAES 2013 original report** (annex with the CLC correspondence) was not opened (old URL redirects); the BISE reproductions were used. | Publications Office copy of the report. |
| 5 | **LUCAS:** existence of a survey round after 2022 with changed codes not checked; level-3 crop codes incomplete (B14, B16–B19, B74, B75); no legend colours found. | Eurostat LUCAS pages; ShowVoc "LUCAS Classification 2022". |
| 6 | **ESA WorldCover successors:** only v100 (2020) and v200 (2021) were checked; a newer global 10 m product would need its own legend check. The v100 manual was not opened (same legend assumed). | ESA WorldCover / CLMS global land-cover pages. |
| 7 | **HRL Tree Cover Density 2024 edition:** resolution and yearly cycle are taken from the NRR methodological note; the product manual was not opened. | CLMS HRL Tree Cover and Forests manual. |
| 8 | **EAGLE numbering:** only the nodes cited in the CLC+ manual carry verified codes; the Excel matrix and the explanatory documentation in the EAGLE document archive were not opened. | EAGLE document archive. |
| 9 | **INSPIRE:** the SLD files for the Land Use default styles are distributed separately and were not inspected; the Habitats default grey is given inconsistently in the guideline (#808080 vs. "RGB 80,80,80"). | INSPIRE portrayal register / GitHub repository. |
| 10 | **EUET marine names** (types 10 and 12) were reconstructed by script from the PDF layout and not checked one by one. | Read the PDF tables. |
| 11 | **NRR:** the number of the annex that lists example restoration measures was not captured (it is the final annex). Satisfactory levels (Art. 14(5)) and the Commission's guiding framework (Art. 20(10), due end of 2028) do not exist yet. | EUR-Lex; later implementing acts. |
| 12 | **Urban Atlas ↔ CLC:** no separate official crosswalk table was found; the comparison in section 10 is derived from the two nomenclatures. | CLMS helpdesk / UA mapping guide annexes. |

---

## 13. Implications for the element catalog

### 13.1 Mapping of the 16 existing elements to the European schemes

All codes are verified codes from the sections above; the *assignment* of a library element to a code is my proposal (A). "NRR UGS" = counts as urban green space under the Copernicus baseline (CLC+ Backbone classes 2, 3, 4, 5, 6, 8, 10).

| Library element | CLC+ Backbone | NRR UGS | Urban Atlas | CLC | EUNIS 2021 (2012) | EU ecosystem typology | INSPIRE PLCC | LUCAS LC (+LU) |
|---|---|---|---|---|---|---|---|---|
| Lawn | 6 | yes | inside 14100 / 14200 / 11xxx (no own class) | inside 141 / 142 | V31 (E2.6; E2.64 park lawns, E2.65 small-scale lawns, E2.63 turf sports fields) | 1.4.1, 1.4.2, 1.4.3 | 009 | E20 (+U36x, U370) |
| Meadow | 6 | yes | 23000; 32000 | 231; 321 | R22, R21; wet: R35, R36 (E2.2, E2.1; E3.4) | 3.1.x, 3.2.1, 3.2.3 | 009 | E10, E20 (+U111, U420) |
| Wildflower meadow | 6 | yes | inside 14100; 32000 | 321 | R22, R1A, R1P (species-rich); sown or ruderal stands: V39, V38 (E5.1) | 3.2.1, 3.2.2; 1.4.3 | 009 | E20; E30 if spontaneous |
| Shrub | 5 | yes | 32000; inside 14100 | 322, 324 | S32, S35, S37, S38 (F3.1); ornamental: V53 (FB.3); park shrubbery (I2.11) | 5.2.x; 1.4.x | 008 | D10, D20 |
| Woodland | 2, 3, 4 | yes (+ canopy) | 31000; urban forest with recreation: 14100 | 311, 312, 313 | T1x, T3x (G1, G3, G4); small planted woods V64–V66 (G5.2–G5.5) | 4.1–4.6; 1.4.1 | 006, 007 | C10, C2x, C3x |
| Urban trees | 2, 3, 4 where canopy dominates the pixel | yes (+ canopy via HRL Tree Cover Density) | **Street Tree Layer** (STL = 1) | – | V63 Lines of planted trees (G5.1); sparsely wooded land (X13–X16) | 1.4.3 (tree alleys) | 006, 007 | C10 (woody features), else not captured |
| Reed / wetland | 6 (reeds are "permanent herbaceous"); 10 if under water for half the period | yes | 40000 | 411 (412 peat bogs) | Q51, Q53 (C3.2, C3.21, D5.1); mires Q1, Q2, Q4 | 7.1.3 Reedbeds, 7.1.1; 7.2.x | 011 (+009); 012 | H11, H12 |
| Water body | 10 | yes ("ponds and watercourses") | 50000 | 511, 512 | C1, C2 (2012, current); artificial: J5.3, J5.4, J5.5 | 8.x, 9.x; 1.4.4 Urban blue | 015, 016 | G11, G21 |
| Soil / bare ground | 9 (7 if periodically vegetated or tilled) | no | 33000; 13300; 13400 | 333; 133 | (H5.31, H5.6, H5.61 unsurfaced pathways); tilled: V15 (I1.5) | 6.2.3; 1.3.7 | 003 | F40 |
| Sand | 9 | no | 33000 | 331 | (H5.32 stable sand, H5.34 inland dunes); coastal N1x | 6.2.3; 11.1 | 003 | F20 |
| Gravel | 9 (loose / water-bound / permeable); 1 if bound and impervious | no | inside the use class | – | (H5.35 gravel); constructed: J4.x | 6.2.3; 1.1–1.3 | 003 (natural) / 001 (constructed) | A21, A22 (artificial cover incl. gravel); F10/F20 if natural |
| Paving (light) | 1 (impervious); 9 (permeable paving, grass pavers) | no | inside 11xxx, 12100; 12220 for roads and car parks | inside 111–124 | J4.6 Pavements and recreation areas; J4.2 | 1.1, 1.2, 1.3 | 001 | A21 (areas), A22 (linear) |
| Paving (dark) | as above | no | as above | as above | as above | as above | 001 | A21, A22 |
| Asphalt | 1 | no | 12210, 12220 (roads); inside other class-1 units | inside 122, 111–124 | J4.2 Road networks; J4.4; J4.5 | 1.3.1; 1.1, 1.2 | 001 | A22 (roads), A21 (car parks) |
| Concrete | 1 | no | inside class-1 units | inside 111–124 | J4.x; J1.x, J2.x for structures | 1.1–1.3 | 001 | A21, A30 |
| Wood decking | 1 (artificial construction) — no scheme distinguishes the material | no | inside class-1 units | – | J4.6 (nearest) | 1.1–1.4 | 001 | A21 / A30 |

**Reading of the table (A):**
- The European schemes distinguish **sealed vs. non-sealed**, **woody vs. herbaceous**, **permanent vs. periodic** and **tree leaf type** — they do **not** distinguish paving materials. Asphalt, concrete, light and dark paving and decking all collapse into one class (CLC+ 1, PLCC 001, LUCAS A2x). Material stays a house-level attribute.
- Lawn, meadow and wildflower meadow also collapse into one land-cover class (CLC+ 6, PLCC 009, LUCAS E20). Only **EUNIS** separates them (V31 vs. R22/R21 vs. R1x/V38/V39) — EUNIS is therefore the scheme that justifies the library's fine vegetation split.
- Reed sits in an awkward position: land-cover products put it into "permanent herbaceous" (or water), land-use/habitat schemes into wetlands. The element needs both codes.

**Global / climate schemes (assignments A; LCZ land-cover semantics not re-read in the 2012 paper):**

| Library element | Local Climate Zone | ESA WorldCover |
|---|---|---|
| Lawn, Meadow, Wildflower meadow | D Low plants | 30 Grassland |
| Shrub | C Bush, scrub | 20 Shrubland |
| Woodland | A Dense trees | 10 Tree cover |
| Urban trees | B Scattered trees | 10 Tree cover (where canopy dominates the pixel) |
| Reed / wetland | no own class (D or G) | 90 Herbaceous wetland |
| Water body | G Water | 80 Permanent water bodies |
| Soil / bare ground, Sand | F Bare soil or sand | 60 Bare / sparse vegetation |
| Gravel | F or E | 60 Bare / sparse vegetation |
| Paving, Asphalt, Concrete, Wood decking | E Bare rock or paved | 50 Built-up |
| Buildings (missing element) | LCZ 1–10 by compactness, height and construction | 50 Built-up |
| Cropland (missing element) | D Low plants | 40 Cropland |
| Moss / lichen (missing element) | – | 100 Moss and lichen |

### 13.2 Elements the European schemes require that the 16-class sheet lacks

| Missing element | Required by (verified classes) | Note |
|---|---|---|
| **Building / roof** (footprint) | CLC+ 1; PLCC 001; LUCAS A11, A12 (height split), A13; EUNIS J1, J2; LCZ built types | Height class attribute (low / mid / high) serves LUCAS and LCZ. |
| **Green roof / green wall** | NRR recital 48 and restoration-measure list; Art. 8(2) "integration of urban green space into buildings and infrastructure"; CLC+ maps vegetated rooftops as class 1 | Needs its own element precisely because the Copernicus baseline does not see it (supplementary data). |
| **Urban fabric / block by sealing degree** (5 steps) and **isolated structures** | UA 11100–11240, 11300; CLC 111, 112; EUET 1.1, 1.2 (thresholds 80 % and 30 %) | A sequential ramp, not a single swatch. |
| **Industrial / commercial / public unit** | UA 12100; CLC 121; EUET 1.1.2, 1.2.2; HILUCS 2, 3 | Land-use block colour. |
| **Road, railway (ballast/track), port, airport** | UA 12210, 12220, 12230, 12300, 12400; CLC 122–124; EUNIS J4.2, J4.3; LUCAS A22; HILUCS 4_1_x | Railway is absent from the sheet; note that CLC+ counts tracks as sealed. |
| **Semi-sealed / permeable surface** (grass pavers, water-bound surface, non-vegetated sports field) | CLC+ 9 via EAGLE 1.1.2 Non-Sealed Artificial Surfaces | Distinct from "sealed" in every sealing statistic; currently only approximated by "gravel". |
| **Land without current use / brownfield, ruderal vegetation** | UA 13400; LUCAS E30; EUNIS V37, V38, V39 (E5.1, E5.12); J1.51 | Spontaneous vegetation is a core urban-ecology category. |
| **Construction site; extraction and dump site** | UA 13300, 13100; CLC 131–133; EUET 1.3.5–1.3.7; EUNIS J3, J6 | |
| **Park / green urban area as composite**, with **access** attribute | UA 14100 → 14110 / 14120 / 14130; CLC 141; EUET 1.4.1; EUNIS X11, X22, X23 | UA 2021 makes public/private/unknown access a class-level distinction. |
| **Sports and leisure facility; sports turf vs. artificial pitch** | UA 14200; CLC 142; EUET 1.4.2; EUNIS E2.63; HILUCS 3_4_3, 3_4_4 | Turf pitch = CLC+ 6; non-vegetated pitch = CLC+ 9. |
| **Allotment garden / domestic garden / vegetable plot** | UA (in 14200 resp. 1.1); EUNIS V22 (I2.2, I2.22 subsistence garden areas), X24, X25; LUCAS U113 kitchen garden | |
| **Ornamental planting / flower bed** | EUNIS V21, V22 (I2.11 park flower beds, arbours and shrubbery; I2.21); LUCAS B44 | |
| **Cemetery** | EUET 1.5.2; UA (in 14100); LUCAS A21; EUNIS J4.7 | Classified differently by every scheme — needs explicit crosswalk entries. |
| **Hedgerow** (linear) | EUNIS V4, V41–V44 (FA); NRR recital 47 "urban hedges" | Linear symbol. |
| **Tree row / avenue** (linear) and **single tree / canopy overlay** | EUNIS V63 (G5.1); UA Street Tree Layer; NRR tree canopy cover; EUET 1.4.3 | Canopy must be drawable *over* any ground surface. |
| **Orchard; vineyard; permanent crops** | EUNIS V61, V54; CLC 221, 222; UA 22000 (25000); PLCC 005; LUCAS B7x, B8x | |
| **Arable land / cropland; fallow** | CLC+ 7; CLC 211; UA 21000; PLCC 004; EUNIS V1x; LUCAS Bxx | The class that is *not* urban green space under NRR. |
| **Pasture** (as distinct from meadow) | CLC 231; UA 23000; EUNIS R21; EUET 3.1.1 | |
| **Heath / dwarf shrub** | CLC 322; EUNIS S41, S42; EUET 5.2.3; CLC+ 5 | |
| **Moss / lichen cover** | CLC+ 8; PLCC 010; LUCAS F30; WorldCover 100 | Counts as urban green space under NRR. |
| **Bog / fen / mire (peat)** | CLC 412; EUNIS Q1–Q4; EUET 7.2; PLCC 012; LUCAS H12 | |
| **Rock / consolidated bare surface; scree** | CLC 332; PLCC 002; LUCAS F10; EUNIS U2, U3; EUET 6.1 | |
| **Watercourse vs. standing water; pond; canal/ditch; fountain** | CLC 511 / 512; PLCC 015 / 016; EUET 8.1, 8.2, 9.1.3, 1.4.4; LUCAS G1x / G2x; EUNIS C1 / C2, J5.3–J5.5 | One "water body" element is too coarse for every scheme that splits running from standing water. |
| **Greenhouse** | LUCAS A13; EUET 1.5.1; EUNIS J2.43; CLC+ 1 | |
| **Forest leaf type** (broadleaved deciduous, broadleaved evergreen, needle-leaved, mixed) | CLC 311–313; CLC+ 2–4; PLCC 006 / 007; LUCAS C10–C3x; EUET 4.1–4.4 | Variant or attribute of "Woodland" and "Urban trees". |
| **Transitional woodland / young stand / coppice** | CLC 324; EUNIS T41–T43; EUET 4.5 | |
| Optional (completeness of official themes) | snow and ice; sea and transitional waters; salt marsh; dunes; burnt area | Needed only to style full CLC / CLC+ / WorldCover rasters without gaps. |

### 13.3 Attributes every element should carry

| Attribute | Purpose | Values / source |
|---|---|---|
| `clcplus_bb` | automatic styling of CLC+ Backbone rasters; NRR accounting | 1–11 |
| `nrr_urban_green_space` (bool) and `nrr_tree_canopy` (bool) | direct NRR Art. 8 reporting layers | derived: true for CLC+ 2, 3, 4, 5, 6, 8, 10; canopy for tree elements |
| `sealed` (bool) and `sealing_class` | sealing statistics; UA urban-fabric ramp; EUET thresholds | sealed / semi-sealed / unsealed; 0–10, 10–30, 30–50, 50–80, > 80 % |
| `eagle_lcc` | pure land-cover component, bridge to CLC+ and INSPIRE | e.g. 1.1.1, 1.1.2, 1.2, 2.1.1, 2.1.2, 2.2, 2.4, 3.1 |
| `inspire_plcc` | INSPIRE-conformant land-cover description | 001–018 |
| `hilucs` | land **use**, kept separate from cover (as LUCAS, EAGLE, INSPIRE do) | HILUCS value, e.g. 3_4_4_OpenAirRecreationalAreas |
| `clc` , `urban_atlas` | coarse crosswalks for official themes | 3-digit / 5-digit codes; many elements are "inside" a class rather than equal to it |
| `eunis_2021`, `eunis_2012` | habitat crosswalk in both generations (different code syntax) | e.g. V31 / E2.64 |
| `euet` | EU ecosystem typology level 2/3 (ecosystem accounts, NRP typology) | e.g. 1.4.1 |
| `lucas_lc`, `lucas_lu` | validation against LUCAS points | e.g. E20 + U362 |
| `leaf_type`, `phenology` | tree classes of CLC, CLC+, PLCC, LUCAS | needle-leaved / broadleaved; deciduous / evergreen |
| `herbaceous_permanence` | CLC+ 6 vs. 7 | permanent / periodic |
| `water_type` | running / standing; natural / artificial | CLC 511/512; EUNIS C vs. J5 |
| `access` | Urban Atlas 2021 | public / private / unknown |
| `building_height_class` | LUCAS A11/A12; LCZ | 1–3 floors / more than 3 floors; low / mid / high-rise |
| `match` per crosswalk entry | honesty of the mapping | use the five INSPIRE relations: congruent, includes, includedIn, overlaps, excludes (V, section 7.3) |

### 13.4 Themes the library can ship from verified values

1. **House theme** (mellow pastel) — keep the shared conventions of section 11: light yellow-green for herbaceous, darker greens for woody (conifer darkest), pale yellow for arable, blue-cyan for water, blue-violet or turquoise for wetlands. Be aware that the house greys for asphalt/concrete/paving read as "bare / non-vegetated" or "roads" in European land-cover legends, where **red means sealed**; for city-scale landscape plans grey hardscape is fine, but a toggle to a red-family "sealed" rendering is needed for sealing and land-cover maps.
2. **Official CLC theme** (44 colours, section 1).
3. **Official Urban Atlas theme** (section 2.2: 2018 and 2021 legends with the three access greens; Street Tree Layer greens in section 2.4).
4. **Official CLC+ Backbone theme** (section 3.2) including an **NRR mask** variant (classes 2, 3, 4, 5, 6, 8, 10 vs. the rest).
5. **INSPIRE themes**: HILUCS level-1 land-use colours (section 7.2) and the informative PLCC colour map (section 7.1).
6. **LCZ theme** (palette A of section 9.1, palette B as an alias) and **WorldCover theme** (section 9.2).
7. **EEA ecosystem-map theme for EUNIS 2012 level 2** (section 5.6) — possible, but coarse; note that it draws I2 "gardens and parks" pure yellow and J1 buildings pure red. For the revised EUNIS codes, MAES / EU ecosystem typology and LUCAS no official theme exists; these are **semantic crosswalks only** and are rendered with the house theme.

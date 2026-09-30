# Stream 02 – German biotope / habitat classification and landscape-planning symbology

Research date: 2026-09-30 · Scope: Germany (federal) + Bavaria first, other Länder in overview · Purpose: make the "Urban Landscape Graphics / UrbanSens – Ecological Vector Style" element catalog conformant in (1) semantics (crosswalk codes), (2) convention (hue families, motifs), (3) knowledge of where symbology is prescribed or recommended.

## Evidence marks

| Mark | Meaning |
|---|---|
| **V** | Verified by me this session directly in the primary source (page images of the official PDF, or pixels of the official legend PNG). |
| **V\*** | Primary source, but the text reached me through the WebFetch extraction model (I did not see the raw page). Very likely correct; spot-check before hard-coding. Suspicious cells are flagged individually. |
| **S** | Secondary source. |
| **R** | Recalled from prior knowledge, **not** verified this session. Treat as a lead, not a fact. |

Method limits: the session's web-search budget ran out part-way; all later work used direct fetches of known official URLs and reading of the official pages in a browser pane. The law portals of Hessen and Baden-Württemberg and the agency pages of Sachsen, Hamburg and NRW delivered no content, so those parts stay R / open (section 10). Berlin and Niedersachsen were verified on the agencies' own pages.

---

## 0. Key findings in one page

1. **Two federal reference layers exist and they share one code space.** The BfN standard list (Finck et al. 2017, *Rote Liste der gefährdeten Biotoptypen Deutschlands*, 3rd ed.) uses two-digit groups 01–70 with dotted sub-codes (e.g. `34.09 Tritt- und Parkrasen`). **BKompV Anlage 2** (2020) re-uses these codes, adds value-relevant splits (suffixes `a`, `b`, `.01`, age classes `J/M/A`) and assigns a **Biotopwert 0–24**. Urban complexes that the Red List does not rate (parks, gardens, cemeteries, sports grounds, settlement structure types) exist **only** in BKompV (`51.06a …`, `53.01 …`).
2. **Bavaria uses a different code space**: the *Biotop- und Nutzungstypen (BNT)* of the **BayKompV Biotopwertliste** (letter + up to 3 digits, **0–15 Wertpunkte**), which is explicitly built on the Bavarian biotope mapping key. A BNT can carry a hyphenated **biotope-mapping sub-type** (e.g. `G214-GU651E`, `P12-UP00BK`), which is how § 30 / Art. 23 protection and FFH habitat types are attached.
3. **Lawn / meadow / species-rich meadow are separated by hard criteria in Bavaria** (cover of nutrient-poverty indicators, cover and number of typical meadow forbs per 25 m², mowing frequency): `G4` (3 WP) → `G11` (3) → `G211` (6) → `G212` (8) → `G213` (8) → `G214` (12, always protected / FFH 6510/6520). Federal equivalents: `34.09` (8) → `34.08a.01` (8) → `34.08a.02` (11) → `34.07b.01` (15) → `34.07a.01` (20).
4. **A published, numeric colour system exists**: BfN *Planzeichen für die Landschaftsplanung* (BfN-Skripten 461/1, 461/2, 486). For every *Biotoptypengruppe* it gives RAL-Design + RGB values in **two series** – a **pastel "Kulisse" series** (low–moderate value, no outline) and a **saturated series with 2 pt black outline** (high–outstanding value) – plus overlay conventions (blue dashed lines = wet, brown vertical dashes = fallow, red dot grid = orchard). It is a **recommendation** from an R+D project, not a legal norm. The pastel series is very close to the intended house style.
5. **Neither BKompV nor the BayKompV Biotopwertliste prescribes map colours.** The official Bavarian biotope viewer does not colour by biotope type at all; it colours by **share of legally protected area** in one magenta/pink family (values sampled, section 8).
6. **Green roofs / façade greening have no code** in BKompV Anlage 2 (checked) and none in the BayKompV list (checked). Wood decking has no explicit type either; it must be mapped by sealing class.
7. **Berlin publishes exact colours for its biotope map** (Umweltatlas 05.08, edition 2024): an SLD and legend with 24 legend classes (section 8.3, values verified by pixel sampling). Several hues differ from the BfN catalogue (reeds, ruderal vegetation, raw soil, parks, built-up areas). There is therefore **no single German colour standard for biotope maps**; only a small core is stable across the three verified sources: water blue, woodland green, shrubs and tree rows bright yellow-green, grassland pale yellow-green, arable pale yellow/beige, heath pink/magenta, traffic grey.
8. **Currency of the legal texts**: BKompV last amended by Art. 4 of the act of 22 December 2025; BayKompV last amended 2021; the Bavarian Biotopwertliste is still the 2014 list (update announced), while the mapping key it points to was revised in 2020/2022 – the biotope sub-type codes printed in the 2014 list are partly outdated (GE → GX / GU, WÜ → BS / BX; section 3.6).

---

## 1. BfN standard biotope list (Rote Liste Biotoptypen, 3rd ed. 2017)

**Source (V):** Finck, P., Heinze, S., Raths, U., Riecken, U. & Ssymank, A. (2017): *Rote Liste der gefährdeten Biotoptypen Deutschlands. Dritte fortgeschriebene Fassung 2017.* – Naturschutz und Biologische Vielfalt 156, 637 S. Short list ("Kurzliste", 16 pp., © BfN 2017): <https://www.bfn.de/sites/default/files/2021-06/RL_Biotope_Kurzliste_2017_deutsch_barrierefrei.pdf>. The full book (all third/fourth-level codes, descriptions) was not accessible; 863 biotope types in total (S: search-result abstract of BfN/NuL pages).

**Code structure (V):** `GG.` two-digit group → `GG.NN` → `GG.NN.NN` (→ further levels in the book). Groups 01–11 marine/coastal, 21–24 waters, 31–44 terrestrial inland, 51–54 "technical" biotopes of settlements, 60–70 Alps.

**Columns of the Kurzliste (V):** Code | Biotoptyp | regional threat in 8 regions (Meere/Küsten, NW-Tiefland, NO-Tiefland, W-Mittelgebirge, Ö-Mittelgebirge, SW-Mittelgebirge/Schichtstufenland, Alpenvorland, Alpen) | **nG** Nationale Langfrist-Gefährdung | **TE** aktuelle Entwicklungstendenz | **SE** Seltenheit | **RLD** Rote-Liste-Status | **RE** Regenerierbarkeit.

- RLD categories: `0` vollständig vernichtet · `1!` akut von vollständiger Vernichtung bedroht · `1` von vollständiger Vernichtung bedroht · `1-2` · `2` stark gefährdet · `2-3` · `3` gefährdet · `3-V` akute Vorwarnliste · `V` Vorwarnliste · `*` aktuell kein Verlustrisiko · `?` Daten defizitär · `#` Gefährdungseinstufung nicht sinnvoll.
- RE categories: `N` nicht regenerierbar · `K` kaum regenerierbar (> 150 Jahre) · `S` schwer regenerierbar (15–150 Jahre) · `B` bedingt regenerierbar (etwa bis 15 Jahre) · `X` keine Einstufung sinnvoll.

### 1.1 Top-level groups (all V, names exactly as printed in the Kurzliste)

| Code | Name (German) | Gloss |
|---|---|---|
| 01 | Pelagial der Nordsee | North Sea open water |
| 02 | Benthal der Nordsee | North Sea sea floor |
| 03 | Saisonales Meereis der Nordsee | seasonal sea ice |
| 04 | Pelagial der Ostsee | Baltic open water |
| 05 | Benthal der Ostsee | Baltic sea floor |
| 06 | Saisonales Meereis der Ostsee | seasonal sea ice |
| 07 | Salzgrünland der Nordseeküste (Supralitoral) | salt marsh |
| 08 | Salzgrünland, Brackwasserröhrichte und -Hochstaudenfluren des Geolitorals der Ostseeküste | Baltic salt grassland, brackish reeds |
| 09 | Sände, Sand-, Geröll- und Blockstrände | beaches |
| 10 | Küstendünen | coastal dunes |
| 11 | Fels- und Steilküsten | cliffs |
| 21 | Grundwasser und Höhlengewässer | groundwater, cave waters |
| 22 | Quellen (inkl. Quellabfluss [Krenal]) | springs |
| 23 | Fließende Gewässer | running waters |
| 24 | Stehende Gewässer | standing waters |
| 31 | Höhlen (einschl. Stollen, Brunnenschächte etc.) | caves, adits |
| 32 | Felsen, Block- und Schutthalden, Geröllfelder, offene Bereiche mit sandigem oder bindigem Substrat | rock, scree, open sand/loam |
| 33 | Äcker und Ackerbrache | arable and arable fallow |
| 34 | Trockenrasen sowie Grünland trockener bis frischer Standorte | dry grassland and dry-to-mesic grassland |
| 35 | Waldfreie Niedermoore und Sümpfe, Grünland nasser bis feuchter Standorte (ohne Röhrichte und Großseggenrieder) | fens, swamps, wet grassland |
| 36 | Hoch-, Zwischen- und Übergangsmoore | raised and transition bogs |
| 37 | Großseggenriede | tall-sedge swamps |
| 38 | Röhrichte (ohne Brackwasserröhrichte) | reeds |
| 39 | Wald- und Ufersäume, Staudenfluren | fringes, tall-forb stands (incl. ruderal sites) |
| 40 | Zwergstrauchheiden | dwarf-shrub heath |
| 41 | Feldgehölze, Gebüsche, Hecken und Gehölzkulturen | copses, scrub, hedges, woody crops (incl. single trees, orchards, vineyards) |
| 42 | Waldmäntel und Vorwälder, spezielle Waldnutzungsformen | forest edges, pioneer woods, coppice etc. |
| 43 | Laub(misch)wälder und -forste (Laubbaumanteil > 50 %) | deciduous forests |
| 44 | Nadel(misch)wälder und -forste | coniferous forests |
| 51 | Kleine, unbefestigte Freiflächen des besiedelten Bereiches | small unpaved open spaces in settlements |
| 52 | Verkehrsanlagen und Plätze | traffic areas and squares |
| 53 | Bauwerke | built structures |
| 54 | Deponien und Rieselfelder | landfills, sewage fields |
| 60 | Gewässer der subalpinen bis alpinen Stufe | alpine waters |
| 61 | Firn, permanente Schneefelder und Gletscher | firn, glaciers |
| 62 | Felsen der subalpinen bis nivalen Stufe | alpine rock |
| 63 | Steinschutthalden und Schotterflächen der subalpinen bis alpinen Stufe | alpine scree |
| 64 | Schneeböden, Schneetälchen | snow beds |
| 65 | Moore der subalpinen bis alpinen Stufe | alpine mires |
| 66 | Gebirgsrasen (subalpine bis alpine Stufe) | alpine grassland |
| 67 | Stauden- und Lägerfluren der hochmontanen bis alpinen Stufe | alpine tall-forb stands |
| 68 | Zwergstrauchheiden der subalpinen bis alpinen Stufe | alpine heath |
| 69 | Gebüsche der hochmontanen bis subalpinen Stufe | subalpine scrub |
| 70 | Subalpine Wälder | subalpine forests |

Note: BKompV prints group 51 as "Freiflächen des besiedelten Bereichs" and group 53 as "Bauwerke mit zugeordneter typischer Freiraumstruktur" (V\*) – the ordinance widened both groups.

### 1.2 Types occurring in urban / peri-urban areas (all V from the Kurzliste; RLD = national Red List status, RE = regenerability)

| Code | Biotoptyp | RLD | RE |
|---|---|---|---|
| 22.05 | Künstlich gefasste Quellen | * | X |
| 23.01 | Natürliche und naturnahe Fließgewässer | 1-2 | K |
| 23.02 | Anthropogen mäßig beeinträchtigte Fließgewässer | 2-3 | S |
| 23.03 | Anthropogen stark beeinträchtigte Fließgewässer | * | X |
| 23.04 | Anthropogen sehr stark veränderte Fließgewässer | * | X |
| 23.05.01 | Graben mit ganzjährigem Fließgewässercharakter (unter 23.05 Fließgewässer technischer Art) | 3-V | B |
| 23.05.02 | Technische Rinne, Halbschale | * | X |
| 23.05.03 | Verrohrung | # | X |
| 24.04 | Eutrophe stehende Gewässer (24.04.01 See · .02 Altwasser · .03 Weiher und Flachsee inkl. naturnahe Teiche · .04 sich selbst überlassenes Abbaugewässer · .05 Tümpel) | 3-V | B |
| 24.05 | Poly-hypertrophe stehende Gewässer | * | X |
| 24.07.03 | Kanäle (unter 24.07 Stehende Gewässer anthropogenen Ursprungs) | * | X |
| 24.07.04 | Gräben mit sehr langsam fließendem bis stehendem Wasser | 2-3 | X |
| 24.07.05 | Zier- und Löschteich | * | X |
| 24.07.06 | Klär- bzw. Schönungsteich | * | X |
| 24.07.08 | Offene Wasserrückhaltebecken | * | X |
| 24.07.09 | Hafenbecken | * | X |
| 32.05.01 | Steinriegel und Steinhaufen | 1-2 | B |
| 32.05.02 | Trockenmauern | 1-2 | B |
| 32.05.03 | Verfugte Natursteinmauern (auch von Ruinen) | * | B |
| 32.08 | Vegetationsarme Kies- und Schotterfläche | 1-2 | B |
| 32.09 | Vegetationsarme Sandfläche | 1-2 | B |
| 32.10 | Vegetationsarme Fläche mit bindigem Substrat | 1-2 | B |
| 32.11 | Abbaubereiche und Abraumhalden | * | X |
| 34.04 | Sandtrockenrasen | 1-2 | S |
| 34.02 | Halbtrockenrasen | 1-2 | S |
| 34.07 | Artenreiches Grünland frischer Standorte (34.07.01 in tieferen Lagen · 34.07.02 in höheren Lagen) | 1-2 | S |
| 34.08 | Artenarmes Grünland frischer Standorte | * | X |
| 34.09 | **Tritt- und Parkrasen** | * | X |
| 35.02.03 | Sonstiges extensives Feucht- und Nassgrünland in tieferen Lagen | 1-2 | S |
| 35.02.05 | Flutrasen | 2-3 | B |
| 35.02.06 | Artenarmes, intensiv genutztes Feuchtgrünland | * | X |
| 37.02 | Nährstoffreiche Großseggenriede | 3-V | S |
| 38.02.01 | Schilf-Wasserröhricht | 1-2 | S |
| 38.02.02 | Schilf-Landröhricht | 3-V | S |
| 38.03 | Rohrkolbenröhricht | 3-V | B |
| 38.05 / 38.06 | Wasserschwadenröhricht / Rohrglanzgrasröhricht | * | B |
| 39.01 | Wald- und Gehölzsäume (ohne Ufersäume) | 2-3 | B |
| 39.03.01 | Krautige und grasige Säume und Fluren der offenen Landschaft oligo- bis eutropher Standorte | 3-V | B |
| 39.03.02 | … hypertropher Standorte | * | X |
| 39.04 | Krautige Ufersäume oder -fluren an Gewässern | 2-3 | B |
| 39.05 | Neophyten-Staudenfluren | # | X |
| 39.06 | **Ruderalstandorte** | 2-3 | B |
| 39.07 | Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) | * | B |
| 41.01.04 | Gebüsche frischer Standorte | 3-V | B-S |
| 41.01.06 | Gebüsch stickstoffreicher, ruderaler Standorte | * | X |
| 41.02 | Feldgehölze mit überwiegend autochthonen Arten (.01 nass–feucht · .02 frisch · .03 trocken-warm) | 3-V | B-S |
| 41.03 | Hecken mit überwiegend autochthonen Arten (.01 Wallhecke, Knick · .02 Hecke auf Lesesteinriegel · .03 Hecken auf ebenerdigen Rainen oder Böschungen) | 2-3 | B-S |
| 41.04 | Gebüsche, Hecken und Feldgehölze aus überwiegend nicht autochthonen Arten | # | X |
| 41.05 | **Einzelbäume, Baumreihen und Baumgruppen** | 2-3 | B-S |
| 41.06 | Streuobstbestand [Komplex] (.01 auf Grünland 1-2 · .02 auf Acker 1!) | 1-2 | B-S |
| 41.07 | Gehölzplantagen und Hopfenkulturen | * | X |
| 42.02 | Rubus-Gestrüppe und -Vormäntel | V | B |
| 42.03 | Vorwälder (.01 nass–feucht · .02 frisch · .03 trocken-warm) | * | B |
| 43.09 | Laub(misch)holzforste einheimischer Baumarten | * | X |
| 43.10 | Laub(misch)holzforste eingeführter Baumarten | # | X |
| 44.04 | Nadel(misch)forste heimischer Baumarten | * | X |
| 44.05 | Nadel(misch)forste eingeführter Baumarten | # | X |
| 51.01 | Kleine, vegetationsfreie Freifläche | * | X |
| 51.02 | Kleine Freiflächen mit Spontanvegetation | 3-V | X |
| 51.03 | Anpflanzungen und Rabatten | * | X |
| 52.01 | Straßen | # | X |
| 52.02 | Rad- und Fußwege bzw. Pfade (rated sub-types: 52.02.06 Unbefestigter Weg 2-3 · 52.02.07 Hohlweg [Komplex] 1-2) | – | – |
| 52.03 | Plätze, befestigte Freiflächen | # | X |
| 52.04 | Übrige Verkehrsanlagen (.01 Gleiskörper · .02 Hafenanlage, Kai · .03 Sonstige Verkehrsanlagen) | # | X |
| 53.01 | Gebäude | (not rated) | – |
| 53.02 | Mauern | * | X |
| 54.01–54.04 | Feststoffdeponien · Deponien flüssiger Stoffe · Rieselfelder [Komplex] · Kanalisation | # / # / * / # | X |

Observations (V): in the Kurzliste **parks, gardens, cemeteries, sports grounds and building-structure types are not separate biotope types**; walls are split between `32.05` (dry-stone / natural stone) and `53.02` (Mauern). BKompV rearranges this (walls all under `53.02.x`).

---

## 2. BKompV (Bundeskompensationsverordnung) – Anlage 2 "Liste der Biotoptypen und -werte"

**Source (V\*):** <https://www.gesetze-im-internet.de/bkompv/anlage_2.html> – heading "Anlage 2 (zu § 5 Absatz 1) Liste der Biotoptypen und -werte (Fundstelle: BGBl. I 2020, 1100 - 1122)". Full text: <https://www.gesetze-im-internet.de/bkompv/BJNR108800020.html>.

**Ordinance (V\*):** "Verordnung über die Vermeidung und die Kompensation von Eingriffen in Natur und Landschaft im Zuständigkeitsbereich der Bundesverwaltung (Bundeskompensationsverordnung - BKompV)", Ausfertigungsdatum 14.05.2020. Vollzitat: "Bundeskompensationsverordnung vom 14. Mai 2020 (BGBl. I S. 1088), die durch Artikel 4 des Gesetzes vom 22. Dezember 2025 (BGBl. 2025 I Nr. 351) geändert worden ist"; text record from 3.6.2020. What the December 2025 amendment changed was not determined; the annex heading still cites the 2020 gazette pages.

**Scope (V\*, § 1):** "Diese Verordnung findet Anwendung, soweit die Vorschriften des Dritten Kapitels des Bundesnaturschutzgesetzes … ausschließlich durch die Bundesverwaltung ausgeführt werden." It therefore covers federal projects only and does not replace Länder methods (e.g. BayKompV) or municipal practice – but its annex is the only nationwide valued list in the BfN code space.

**§ 5 Abs. 1 (V\*):** "… ist jedes Biotop im Einwirkungsbereich des Vorhabens zunächst einem der in der Anlage 2 Spalte 2 aufgeführten Biotoptypen und anschließend dem zugehörigen Biotoptypenwert nach Anlage 2 Spalte 3 zuzuordnen."

**Value scale (V\*, § 5):** each biotope gets the *Biotoptypenwert* of its type, which "um bis zu drei Wertpunkte erhöht … oder … verringert" can be for above/below-average condition. Classes:

| Wertstufe | Biotopwert |
|---|---|
| sehr gering | 0–4 |
| gering | 5–9 |
| mittel | 10–15 |
| hoch | 16–18 |
| sehr hoch | 19–21 |
| hervorragend | 22–24 |

**Code structure (V\*):** BfN code + optional lower-case letter marking a BKompV-specific split or merger (`34.07a`, `51.06a`) + further `.01/.02` + optional age-class suffix **J / M / A** = *junge / mittlere / alte Ausprägung* (for hedges: *ohne Überhälter / mit Überhältern mittlerer / alter Ausprägung*). The annex itself prints no legend for the suffixes (V\*); the meaning follows from the row texts. `[Komplex]` marks complex types.

**Top-level groups present in Anlage 2 (V\*):** 02, 05, 06a (Anthropogene Strukturen im Meeres- und Küstenbereich), 07–11, 12a (Fließgewässer der Brackwasser-Ästuare), 22, 23, 24, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 54, 60–70.

**Checked explicitly (V\*):** Anlage 2 contains **no entry** mentioning Dach / Dachbegrünung / Fassade / begrünt → green roofs and façade greening are not biotope types of the BKompV.

> Spot-check: the urban-critical rows (34.07a.01 – 34.09, 39.06.x, 41.05a/b, 51.02, 51.06a.04, 51.08a.02, 52.01.01a, 52.02.04a, 52.03.02, all 53.02.x) were extracted two or three times independently with identical results. One run swapped the text of `53.02.03a`; a third run confirmed `53.02.02` Betonmauer = 0 and `53.02.03a` Unverfugte Natursteinmauer bzw. Trockenmauer = 17. Four odd codes came out identically in two runs and therefore seem to be printed like this on gesetze-im-internet.de: `52.01.08n.03`, a second `44.03.02J` (for the "Mittlere Ausprägung" row), `35.02.05.01a`, and the name of `41.01.04.01`. They are marked ⚠; check the gazette PDF before hard-coding.

### 2.1 Grassland – group 34 "Trockenrasen sowie Grünland trockener bis frischer Standorte" (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 34.01 | Trockenrasen auf karbonatischem oder silikatischem Untergrund | 21 |
| 34.02a | Halbtrockenrasen, beweidet oder gemäht | 21 |
| 34.02b | Halbtrockenrasen, brachgefallen bzw. ungenutzt | 17 |
| 34.03.01a | Steppenrasen, beweidet oder gemäht | 22 |
| 34.03.03 | Steppenrasen, brachgefallen bzw. ungenutzt | 19 |
| 34.04.01a | Annuelle Sandtrockenrasen und Silbergrasfluren | 20 |
| 34.04.03.01a | Ausdauernde Sandtrockenrasen mit weitgehend geschlossener Narbe – beweidet oder gemäht | 21 |
| 34.04.03.03 | Ausdauernde Sandtrockenrasen mit weitgehend geschlossener Narbe – ungenutzt | 16 |
| 34.05.01 | Natürlicher und halbnatürlicher Schwermetallrasen | 21 |
| 34.05.02 | Schwermetallrasen junger Abraumhalden des Bergbaus | 15 |
| 34.06.01a / b | Borstgrasrasen trockener bis frischer Standorte, beweidet oder gemäht / brachgefallen | 21 / 18 |
| 34.06.02a / b | Borstgrasrasen feuchter Standorte, beweidet oder gemäht / brachgefallen | 22 / 19 |
| **34.07a.01** | **Artenreiche, frische Mähwiese** | **20** |
| 34.07a.02 | Artenreiche, frische (Mäh-)Weide | 18 |
| 34.07a.03 | Artenreiche, frische Grünlandbrache | 16 |
| **34.07b.01** | **Mäßig artenreiche, frische Mähwiese** | **15** |
| 34.07b.02 | Mäßig artenreiche, frische (Mäh-)Weide | 13 |
| 34.07b.03 | Mäßig artenreiche, frische Grünlandbrache | 11 |
| **34.08a.01** | **Intensiv genutztes, frisches Dauergrünland** | **8** |
| 34.08a.02 | Extensiv genutztes, frisches Dauergrünland | 11 |
| 34.08.02 | Frisches Ansaatgrünland | 7 |
| 34.08.03 | Artenarme, frische Grünlandbrache | 9 |
| **34.09** | **Tritt- und Parkrasen** | **8** |

### 2.2 Wet grassland and fens – group 35 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 35.01a / b | Waldfreie, oligo- bis mesotrophe kalkarme oder kalkreiche Niedermoore und Sümpfe – weitgehend intakt / degeneriert (teilentwässert) | 24 / 16 |
| 35.02.01a / 35.02.01.03 | Pfeifengraswiesen – bewirtschaftet / brachgefallen | 23 / 20 |
| 35.02.02a / 35.02.02.03 | Brenndolden-Auenwiesen – bewirtschaftet / brachgefallen | 23 / 21 |
| 35.02.03a.01 / .02 | Sonstiges extensives Feucht- und Nassgrünland – bewirtschaftet / brachgefallen | 20 / 16 |
| 35.02.05.01 | Flutrasen – extensiv bewirtschaftet | 18 |
| 35.02.05.01a ⚠ | Flutrasen – brachgefallen | 16 |
| 35.02.05.02 | Flutrasen – intensiv bewirtschaftet | 12 |
| 35.02.06.01 | Feuchtes, intensiv genutztes Dauergrünland | 10 |
| 35.02.06.02 | Feuchtes Ansaatgrünland | 10 |
| 35.02.06.03 | Brachgefallenes, artenarmes Feuchtgrünland | 12 |
| 35.03 | Salzgrünland des Binnenlandes | 22 |

### 2.3 Sedge swamps and reeds – groups 37, 38 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 37.01 / 37.02 | Nährstoffarmes / Nährstoffreiches Großseggenried | 20 / 16 |
| 38.01 | Teichsimsenröhricht | 19 |
| 38.02.01 | Schilf-Wasserröhricht | 19 |
| 38.02.02 | Schilf-Landröhricht | 15 |
| 38.03 | Rohrkolbenröhricht | 16 |
| 38.04 | Schneidenröhricht | 20 |
| 38.05 | Wasserschwadenröhricht | 13 |
| 38.06 | Rohrglanzgrasröhricht | 13 |
| 38.07 | Sonstiges Röhricht | 16 |

### 2.4 Fringes, tall-forb and ruderal vegetation – group 39 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 39.01.01 | Wald- und Gehölzsäume oligo- bis eutropher, trockener bis nasser Standorte | 16 |
| 39.01.02 | Wald- und Gehölzsäume hypertropher, trockener bis nasser Standorte | 10 |
| 39.02 | Kahlschläge und Fluren der Lichtungen | 10 |
| 39.03.01a | Krautige und grasige Säume und Fluren der offenen Landschaft – trocken-warmer Standorte mit wertgebenden Merkmalen | 17 |
| 39.03.01b | … – frischer bis nasser Standorte mit wertgebenden Merkmalen | 16 |
| 39.03.02 | Sonstige krautige und grasige Säume und Fluren der offenen Landschaft | 8 |
| 39.04a.01 / .02 | Krautige Ufersäume oder -fluren an Gewässern – naturnahe / naturferne Ausprägung | 17 / 8 |
| 39.05 | Neophyten-Staudenfluren | 7 |
| **39.06.01** | **Trocken-warme Ruderalstandorte auf Sand-, Kies- und Schotterböden** | **16** |
| **39.06.02** | **Trocken-warme Ruderalstandorte auf bindigem Boden** | **14** |
| **39.06.03** | **Frische bis nasse Ruderalstandorte** | **12** |
| 39.07 | Artenarme Dominanzbestände von Poly-Kormonbildnern | 10 |

### 2.5 Woody structures outside forest – group 41 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 41.01.01 | Gebüsch nasser bis feuchter mineralischer Standorte außerhalb von Auen | 16 |
| 41.01.02 | (Weiden-)Gebüsch in Auen | 16 |
| 41.01.03.01 / .02 | Moor-Gebüsch (z. B. mit Weiden, Gagel) / Zwergbirken-Gebüsch | 16 / 18 |
| 41.01.04.01 ⚠ | Wacholder- und Besenginster-Gebüsch (name as extracted; verify) | 16 |
| 41.01.04.02 | Sonstiges Gebüsch frischer Standorte | 13 |
| 41.01.05.01–.04a | Buxus-Gebüsch 20 · Wacholder-Gebüsch 19 · Trockenes Zwerg- und Weichselkirschen-Gebüsch 18 · Sonstiges Gebüsch trocken-warmer Standorte 16 | – |
| 41.01.06 | Gebüsch stickstoffreicher, ruderaler Standorte | 12 |
| 41.02.01 J/M/A | Feldgehölz nasser bis feuchter Standorte | 13 / 15 / 18 |
| 41.02.02 J/M/A | Feldgehölz frischer Standorte | 13 / 14 / 17 |
| 41.02.03 J/M/A | Feldgehölz trocken-warmer Standorte | 14 / 15 / 18 |
| 41.03.01 J/M/A | Wallhecke, Knick | 12 / 16 / 19 |
| 41.03.02 J/M/A | Hecke auf Lesesteinriegel | 12 / 16 / 19 |
| 41.03.03 J/M/A | Sonstige Hecken – J = junge Ausprägung (ohne Überhälter) **sowie Schnitthecken** | 12 / 16 / 19 |
| 41.04 J/M/A | Gehölzanpflanzungen und Hecken aus überwiegend nicht autochthonen Arten – J incl. Schnitthecken | 8 / 11 / 14 |
| **41.05a J/M/A** | **Einzelbäume, Baumreihen und Baumgruppen aus überwiegend autochthonen Arten** | **11 / 15 / 18** |
| **41.05b J/M/A** | **… aus überwiegend nicht autochthonen Arten** | **8 / 11 / 14** |
| 41.05.02 J/M/A | Kopfbaum / Kopfbaumreihe | 12 / 15 / 18 |
| 41.05.04 J/M/A | Allee | 11 / 16 / 19 |
| 41.05.05 J/M/A | Obstbaumallee, -reihe oder einzelner Obst- bzw. Nussbaum | 11 / 19 / 21 |
| 41.06.01 J / MA | Streuobstbestand auf Grünland – junger / mittlerer bis alter Baumbestand | 12 / 19 |
| 41.06.02 J / MA | Streuobstbestand auf Acker | 12 / 18 |
| 41.07 | Gehölzplantagen und Hopfenkulturen | 6 |
| 41.08.01–.04 | Rebkulturen in Steillage 17 · in ebener bis schwach geneigter Lage 9 · Rebbrachen in Steillage 14 · in ebener Lage 10 | – |

### 2.6 Forest edges, pioneer woods and forests – groups 42–44, rows relevant near cities (V\*)

| Code | Biotoptyp | Wert (J/M/A) |
|---|---|---|
| 42.01 | Waldmäntel | 17 |
| 42.02 | Rubus-Gestrüppe und -Vormäntel | 12 |
| 42.03.01 / .02 / .03 | Vorwald nasser bis feuchter / frischer / trocken-warmer Standorte | 14 / 13 / 13 |
| 42.06a | Kurzumtriebsplantagen mit heimischen oder nicht heimischen Baumarten | 6 |
| 43.03.01 / .02 | Intakter / degradierter Sumpfwald | 15·18·21 / 11·13·15 |
| 43.04.01 | Fließgewässerbegleitende Erlen- und Eschenwälder | 14 / 17 / 20 |
| 43.04.02.01 / .02 | Weichholzauenwälder mit natürlicher/naturnaher / ohne oder mit gestörter Überflutungsdynamik | 14·20·23 / 11·14·17 |
| 43.04.03.01 / .02 | Hartholzauenwälder mit … / ohne … Überflutungsdynamik | 14·20·22 / 11·15·18 |
| 43.06 | Schlucht-, Blockhalden- und Hangschuttwälder | 15 / 17 / 20 |
| 43.07.02 | Eichen-Hainbuchenwald staunasser bis frischer Standorte | 15 / 20 / 23 |
| 43.07.03 | Eichenwald feuchter bis frischer Standorte | 15 / 20 / 23 |
| 43.07.04 | Buchen(misch)wälder frischer, basenarmer Standorte | 14 / 17 / 20 |
| 43.07.05 | Buchen(misch)wälder frischer, basenreicher Standorte | 14 / 16 / 18 |
| 43.08.01 | Trockene Eichen-Hainbuchenwälder | 15 / 20 / 23 |
| 43.08.05 | Eichen-Trockenwälder | 15 / 18 / 21 |
| **43.09** | **Laub(misch)holzforste einheimischer Baumarten** | **11 / 13 / 16** |
| 43.10 | Laub(misch)holzforste eingeführter Baumarten | 9 / 12 / 14 |
| 44.02.03 | Trockene Sandkiefernwälder | 14 / 19 / 22 |
| 44.04 | Nadel(misch)forste einheimischer Baumarten | 9 / 11 / 14 |
| 44.05 | Nadel(misch)forste eingeführter Baumarten | 6 / 10 / 12 |

(The extraction of group 43/44 is complete in my notes; the row printed as a second `44.03.02J` with "Mittlere Ausprägung 18" ⚠ is almost certainly `44.03.02M`.)

### 2.7 Waters – groups 22–24 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 22.01.01 / .02 | Kalkarme / Kalkreiche Sicker- und Sumpfquellen (Helokrenen) | 22 / 20 |
| 22.02 / 22.03 / 22.04 | Grundquellen / Sturzquellen / Salz- oder Solquellen | 22 / 22 / 23 |
| 22.05 | künstlich gefasste Quellen | 11 |
| 23.01 | Natürliche und naturnahe Fließgewässer | 22 |
| 23.02 | Anthropogen mäßig beeinträchtigte Fließgewässer | 17 |
| 23.03a.01 / .02 | Anthropogen stark beeinträchtigte Fließgewässer – typische Ausprägung / besondere Ausprägung mit Flachwasserzonen oder Wasserpflanzen | 8 / 13 |
| 23.04a.01 / .02 | Anthropogen sehr stark veränderte Fließgewässer – typische / besondere Ausprägung | 5 / 9 |
| 23.05.01a.01 / .02 | Graben mit periodischer oder dauerhafter Wasserführung – naturnahe Ausbildung bzw. ohne oder mit extensiver Unterhaltung / naturferne Ausbildung, intensive Unterhaltung | 13 / 8 |
| 23.05.02 | Technische Rinne, Halbschale | 3 |
| 23.05.03 | Verrohrung | 1 |
| 23.05.04a.01 / .02 | Kanäle – naturnahe / naturferne Ausprägung | 10 / 4 |
| 23.05.05a | Technische Uferbefestigungen und -vorschüttungen, Regelungsbauwerke | 3 |
| 23.05.06a | Technische-biologische Ufersicherungen | 8 |
| 23.05.07a | Spundwand | 1 |
| 23.05.08a.01 / .02 | Sonstige lineare Gewässerstrukturen – naturnahe / naturferne Ausbildung | 11 / 4 |
| 23.06 | Mündungen in Binnengewässer | 17 |
| 23.07.01–.05 | Wasserfall 21 · Altarm 21 · Seeabfluss (natürlich oder naturnah) 17 · Staustrecke 6 · Salzbach 22 | – |
| 23.08a.01 / .02 | Zeitweilig trockenfallende Lebensräume unterhalb des Mittelwasserbereichs – natürliche oder naturnahe / bedingt naturnahe Ausprägung | 20 / 14 |
| 23.09 | Natürliche und naturnahe temporäre Fließgewässer | 20 |
| 24.01a / b | Natürliche / naturnahe dystrophe Gewässer (b inkl. sich selbst überlassene Abbaugewässer) | 20 / 16 |
| 24.02a / b | Natürliche / naturnahe oligotrophe Gewässer | 22 / 17 |
| 24.03a / b / c | Natürliche mesotrophe Altwasser / sonstige natürliche mesotrophe Gewässer / naturnahe mesotrophe Gewässer | 20 / 19 / 17 |
| **24.04a / b / c** | **Natürliches eutrophes Altwasser und eutrophe Tümpel / sonstige natürliche eutrophe Gewässer / naturnahe eutrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer** | **19 / 16 / 15** |
| 24.05 | Poly-hypertrophe stehende Gewässer | 7 |
| 24.07.02 / 24.07.02a | Fischzuchtgewässer (intensive Nutzung) / naturnahe Fischzuchtgewässer (extensive Nutzung) | 6 / 11 |
| **24.07.05** | **Zier- und Löschteich** | **5** |
| 24.07.06 | Klär- bzw. Schönungsteich | 4 |
| 24.07.07 | Industrielles Absetzbecken, Spülfeld und Flüssigdeponie | 3 |
| **24.07.08** | **Offene Wasserrückhaltebecken** | **5** |
| 24.07.10 | Speicherseen mit hohen Wasserstandsschwankungen | 6 |
| 24.07.11 | Wasseraufbereitungsanlage (offener Sickerteich) | 5 |
| 24.07.12a / b / c | Abbaugewässer im Abbau befindlich / nach Beendigung mit extremem Chemismus / junge Abbaugewässer mit Flachwasserzonen oder Tümpeln | 4 / 3 / 10 |
| 24.07.13a | Sonstige stehende Gewässer (naturfern) | 5 |
| 24.08a.01 / .02 | Zeitweilig trockenfallende Lebensräume unterhalb des Mittelwasserbereichs – natürlich oder naturnah / bedingt naturnah | 18 / 13 |
| 24.09a | Natürliche und naturnahe temporäre stehende Gewässer (ohne Salztümpel) | 19 |

### 2.8 Rock, raw ground, extraction and construction sites – group 32; arable – group 33 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 32.01a / b / c | Natürliche Felsen / naturnah entwickelte Felsen in alten, stillgelegten Steinbrüchen / an Verkehrsanlagen | 20 / 16 / 12 |
| 32.02 | Solitärer Felsblock, Findling | 16 |
| 32.06 / 32.07 | Wände aus Sand und Lockergestein / Lehm- und Lösswände | 18 / 18 |
| **32.08** | **Vegetationslose bzw. -arme Kies- und Schotterfläche** | **18** |
| **32.09** | **Vegetationslose bzw. -arme Sandfläche** | **18** |
| **32.10** | **Vegetationslose bzw. -arme Fläche mit bindigem Substrat** | **18** |
| 32.11.01a.01 / .02 | Junge Halden nach Beendigung der Aufschüttung mit naturnaher Entwicklung / in Aufschüttung befindlich | 10 / 3 |
| 32.11.06a.01 / .02 | Junge ebenerdige Abbauflächen mit naturnaher Entwicklung / im Abbau befindlich | 10 / 3 |
| **32.11.09a** | **Bauflächen und Baustelleneinrichtungsflächen** | **3** |
| 33.0x.02 | Acker mit artenreicher Segetalvegetation (by soil: Kalk 17 · Silikat 16 · Sand 16 · Lehm/Ton 16 · Löss 17 · Torf/Anmoor 8) | – |
| 33.0x.03 | Acker mit stark verarmter oder fehlender Segetalvegetation (6 · 6 · 6 · 6 · 7 · 5) | – |
| 33.0x.04 | Ackerbrache (11 · 11 · 11 · 8 · 9 · 8) | – |

Caution: `32.08–32.10` (value 18) mean *natural or near-natural* sparsely vegetated gravel/sand/loam (Red List 1-2), **not** a gravel path or playground sand. Technical surfaces are in group 52.

### 2.9 Settlement open spaces – group 51 "Freiflächen des besiedelten Bereichs" (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 51.01 | Kleine vegetationsfreie Freiflächen | 5 |
| 51.02 | Kleine unbefestigte Freiflächen mit Spontanvegetation | 11 |
| 51.04a.01 | Brachflächen z. B. ehemalige Baukomplexe, Industrie- und Verkehrsanlagen – mit wesentlichen Anteilen struktur-/artenreicher Ausprägung | 12 |
| 51.04a.02 | … – ohne wesentliche Anteile struktur-/artenreicher Ausprägung | 7 |
| 51.06a.01 | Parkanlagen – Historische Garten- und Parkanlage | 19 |
| 51.06a.02.01 | Parkanlagen – Extensiv gepflegte Parkanlage mit altem Baumbestand | 16 |
| 51.06a.02.02 | Parkanlagen – Extensiv gepflegte Parkanlage ohne alten Baumbestand | 13 |
| 51.06a.03 | Parkanlagen – Intensiv gepflegte Parkanlage mit altem Baumbestand | 13 |
| 51.06a.04 | Parkanlagen – Intensiv gepflegte Parkanlage ohne alten Baumbestand | 10 |
| 51.06a.05 | Parkanlagen – Parkwald | 14 |
| 51.06a.06 | Parkanlagen – Botanischer Garten (differenzierte Objektbewertung) | 13 |
| 51.07a.01 / .02 | Sonstige Grünanlage mit / ohne alten Baumbestand | 13 / 9 |
| 51.08a.01 / .02 | Kleingartenanlagen, Grabeland, Gärten und private Grünflächen – strukturreich / strukturarm | 11 / 7 |
| 51.09a.01 / .02 | Friedhof mit / ohne alten Baumbestand | 14 / 9 |
| 51.10a | Zoo/Tierpark/Tiergehege (differenzierte Objektbewertung) | 11 |
| 51.11a.01 | Sport-/Spiel-/Erholungsanlage mit geringem Versiegelungsgrad – Sportrasenplatz | 7 |
| 51.11a.02 | … – Freibad | 7 |
| 51.11a.03 | … – Golfplatz | 9 |
| 51.11a.04 | … – Campingplatz | 7 |
| 51.11a.05 | … – Sonstige Sport-, Spiel- und Freizeitanlage | 7 |

### 2.10 Traffic areas and squares – group 52 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| **52.01.01a** | Straßen und Verkehrswege – **versiegelter oder sonstiger gepflasterter** Verkehrs- und Betriebsweg (z. B. Straße, Start-, Landebahn) | **0** |
| 52.01.03 | … – teilbefestigter Verkehrsweg (z. B. Rasengitter, Spurplatten) | 2 |
| 52.01.04a | … – unbefestigte Straße / Feld- und Forstweg bzw. Verkehrsweg mit wassergebundener Decke | 3 |
| 52.01.07a | … – Verkehrsweg mit Natursteinpflaster | 6 |
| 52.01.08a.01 | Funktionsgrün an Verkehrswegen – Bankette, Mittelstreifen | 3 |
| 52.01.08a.02 | Funktionsgrün mit artenarmer Krautschicht oder mit Gehölzbestand junger Ausprägung | 7 |
| 52.01.08n.03 ⚠ (probably `52.01.08a.03`) | Funktionsgrün mit artenreicher Krautschicht oder mit Gehölzbestand mittlerer bis alter Ausprägung | 11 |
| **52.02.01a** | Rad- und Fußwege bzw. Pfade – versiegelter oder sonstiger gepflasterter Weg | **0** |
| 52.02.03 | … – teilbefestigter Weg (z. B. Rasengitter, Spurplatten) | 3 |
| 52.02.04a | … – geschotterter Weg oder Weg mit wassergebundener Decke | 4 |
| 52.02.06 | … – unbefestigter Weg | 10 |
| 52.02.07 | … – Hohlweg [Komplex] | 18 |
| 52.02.08a | … – Weg mit Natursteinpflaster | 7 |
| **52.03.01** | Plätze, befestigte Freiflächen – versiegelter Platz oder sonstiger gepflasterter Platz | **0** |
| 52.03.02 | … – teilbefestigter Platz (z. B. Rasengitter) | 3 |
| 52.03.03a | … – Platz mit geschottertem Belag oder wassergebundener Decke (z. B. Aschensportplatz) | 4 |
| 52.03.05a | … – Platz mit Natursteinpflaster | 7 |
| 52.04.01 | Übrige Verkehrsanlagen in Betrieb – Gleiskörper | 1 |
| 52.04.02 | … – Hafenanlage an Land, Kai | 1 |
| 52.04.04a | … – Hafenbecken und Marinas | 6 |
| 52.04.05a | … – Wasserbauliche Anlagen z. B. Schleusen, Wehre, Leitwerke | 2 |
| 52.04.06a | … – Sonstige Verkehrsanlagen | 0 |

### 2.11 Buildings, walls – group 53; landfills – group 54 (V\*)

| Code | Biotoptyp | Wert |
|---|---|---|
| 53.01.01a | Gebäude – Historischer Gebäudekomplex, z. B. Kirche, Kloster, Burg, Schloss | 13 |
| 53.01.03a / b / c | Einzel- und Reihenhausbebauung inkl. typischen Freiräumen – altes Villengebiet mit altem Baumbestand / lockeres Einzelhausgebiet / verdichtetes Einzel- und Reihenhausgebiet | 13 / 5 / 4 |
| 53.01.05a / b | Hochhaus- und Großformbebauung inkl. typischen Freiräumen – Wohnnutzung / öffentliche oder gewerbliche | 4 / 4 |
| 53.01.07a.01 / .02 | Sonstige Einzelgebäude z. B. Scheunen, Stallungen, Speichergebäude – alt bzw. traditionelle Bauweise (genutzt) oder verfallen (ungenutzt) / moderne Bauweise | 11 / 2 |
| 53.01.14a | Industrie- und Gewerbefläche inkl. typischen Freiräumen | 2 |
| 53.01.15a.01 / .02 | Kerngebiet inkl. typischen Freiräumen – historische Altstadt / moderne Innenstadt | 12 / 3 |
| 53.01.16a.01 / .02 / .03 | Block- und Zeilenbebauung inkl. typischen Freiräumen – historische Blockbebauung / sonstige Blockbebauung / Zeilenbebauung | 9 / 4 / 5 |
| 53.01.17a.01 / .02 | Dorfgebiet – historisches Dorfgebiet z. B. Dorfkern, Dorfanger, Dorfplatz / sonstiges Dorfgebiet inkl. Neubaugebiete | 13 / 4 |
| 53.01.18a.01 / .02 | Einzelgebäude im Außenbereich – historische / sonstige Einzelgebäude/-gehöfte | 10 / 2 |
| 53.01.19a | Tierproduktionsanlage und Gewächshäuser | 0 |
| 53.01.20a | Ver- und Entsorgungsanlage, z. B. Kläranlage, Wasserwerk, Staudamm | 2 |
| 53.02.01.01 / .02 | Mauern und Steinriegel – Ziegelsteinmauern, alt bzw. traditionelle Bauweise / moderne Bauweise | 10 / 4 |
| 53.02.02 | Betonmauer | 0 |
| **53.02.03a** | **Unverfugte Natursteinmauer bzw. Trockenmauer** | **17** |
| 53.02.04a | Verfugte Natursteinmauer (auch von Ruinen) | 9 |
| **53.02.05a** | **Steinriegel** | **17** |
| 53.02.06a | Gabionen | 2 |
| 54.01a / b | Feststoffdeponien (z. B. Hausmüll, Bauschuttdeponie) – in Betrieb / begrünte Bereiche | 0 / 2 |
| 54.02 | Deponien flüssiger Stoffe (z. B. Schlammdeponie) | 0 |
| 54.03 | Rieselfelder [Komplex] | 8 |
| 54.04 | Kanalisation | 0 |

Other groups (V\*, for completeness): 31.01a natürliche Höhlen … 20 · 31.02.01 sich selbst überlassene Stollen, Schächte und Bunkerruinen 12 · 31.02.02 in Betrieb befindliche Stollen 6 · 36.01 Hochmoore (weitgehend intakt) 24 · 36.02 Übergangs- und Zwischenmoore 23 · 40.03.01 Calluna-Heiden weitgehend intakt 19.

---

## 3. Bavaria

### 3.1 BayKompV and its Biotopwertliste – status

- **BayKompV (V\*)**: "Verordnung über die Kompensation von Eingriffen in Natur und Landschaft (Bayerische Kompensationsverordnung – BayKompV) vom 7. August 2013 (GVBl. S. 517, BayRS 791-1-4-U), die durch § 2 des Gesetzes vom 23. Juni 2021 (GVBl. S. 352) geändert worden ist"; portal header "Text gilt ab: 03.06.2020". <https://www.gesetze-bayern.de/Content/Document/BayKompV/true>
- **Scope (V\*)**: applies to impacts under § 14/§ 17 BNatSchG and Art. 6 BayNatSchG; "Die Verordnung findet keine Anwendung auf Bauleitpläne und Satzungen im Sinn von § 18 Abs. 1 BNatSchG". (R: in municipal practice the BNT list is nevertheless the usual vocabulary, because the 2021 Bavarian guideline for the impact regulation in urban land-use planning uses the same list – not verified this session.)
- **Value classes (V\*, Anlage 3.1)**: gering 1–5 · mittel 6–10 · hoch 11–15 Wertpunkte; impairment factors 1,0 / 0,7 / 0,4 / 0; forecast horizon 25 years.
- **Biotopwertliste (V)**: "Biotopwertliste zur Anwendung der Bayerischen Kompensationsverordnung (BayKompV)", StMUV, **Stand 28.02.2014 (mit redaktionellen Änderungen vom 31.03.2014)**, 24 pp. <https://www.stmuv.bayern.de/themen/naturschutz/eingriffe/doc/biotopwertliste.pdf>. The LfU page offers no newer list (V\*); an update is announced ("Die Änderungen werden bei der geplanten Aktualisierung der BWL und Arbeitshilfe umgesetzt", LfU 09/2021, V).
- **Arbeitshilfe (V)**: LfU (2014): *BayKompV – Arbeitshilfe zur Biotopwertliste – Verbale Kurzbeschreibungen*, Stand Juli 2014 (Bosch & Partner, IVL, LfU), 107 pp. <https://www.lfu.bayern.de/publikationen/get_pdf.htm?art_nr=lfu_nat_00320&pdf_nr=0>
- **Re-mapping of biotope sub-types (V)**: LfU, "Änderungen der Biotoptypen-Zuordnungen bei folgenden BNT: G2 Extensivgrünland, B4 Streuobstbestände", Stand 09/2021. <https://www.lfu.bayern.de/natur/kompensationsverordnung/doc/biotoptypen_zuordnungen.pdf>

### 3.2 Structure and scoring of the Biotopwertliste (V)

- **Code** = one capital letter (Obergruppe) + up to three digits (`G`, `G2`, `G21`, `G214`). If the stand is also a legally protected biotope, a type of the Bavarian biotope mapping (BK) or an FFH habitat type, the BK sub-type code is appended with a hyphen: `S112-SU00BK`, `S112-SU3160`, `G214-GE6510`; priority habitat types carry `*`.
- **Grundwert (0–15 WP)** = unweighted sum of three criteria, each 0–5: **G** Seltenheit/Gefährdung + **W** Wiederherstellbarkeit/Ersetzbarkeit + **N** Natürlichkeit. The Arbeitshilfe prints the triple per type, e.g. `G4: G 1 • W 1 • N 1 = 3`.
- **N scale**: 5 natürlich/naturnah (a-/oligohemerob) · 4 bedingt naturnah (mesohemerob) · 3 bedingt naturfern (β-euhemerob) · 2 naturfern (α-euhemerob) · 1 naturfremd (polyhemerob) · 0 künstlich (metahemerob).
- **W scale**: 5 = ≥ 80 years · 4 = 26–79 years · 3 = 10–25 years · 2 = 5–9 years · 1 = < 5 years · 0 = sealed surfaces.
- **Markers in the WP column**: `*` = W 4, `**` = W 5 → time-lag deduction of 1–2 / 1–3 WP when the type is a *target* state after 25 years.
- **Column "+ 1 WP"**: `+` = the type is upgraded by one point if the concrete stand is a § 30 / Art. 23 biotope, a BK type or an FFH habitat type (`(x)` = may be one). `x` = the type always is one (no upgrade).
- **Column 8**: BK sub-types; **bold** = § 30 BNatSchG / Art. 23 BayNatSchG biotope; *italic* = BK type without legal protection.
- **Wertstufen**: hoch 11–15 · mittel 6–10 · gering 1–5 · keine naturschutzfachliche Bedeutung 0.
- **Age classes** used for woody types (Arbeitshilfe): junge Ausprägung = stand age ≤ 25 years · mittlere = 26–79 years (or BHD < 50 cm for trees) · alte = ≥ 80 years (or BHD > 50 cm).
- **Rule for the settlement block (V, heading of the list)**: "mit Ausnahme von P1, P43, V23, V33 und V5 sind alle nachfolgenden Typen nur bei der Ermittlung des Kompensationsbedarfs auf der Eingriffsseite zu verwenden und können nicht als Zielbiotope herangezogen werden" – i.e. sealed and built types are impact-side only.
- Reeds/sedges up to 5 m wide are recorded as part of the water body; only > 5 m separately (Arbeitshilfe, V).

### 3.3 Main headings and Obergruppen (V)

| Heading | Obergruppen |
|---|---|
| GEWÄSSER | **Q** Quellen und Quellbereiche · **F** Fließgewässer · **S** Stillgewässer |
| ÄCKER, GRÜNLAND, VERLANDUNGSBEREICHE, RUDERALFLUREN, HEIDEN UND MOORE | **A** Äcker/Felder · **G** Grünland (Dauergrünland) · **R** Röhrichte und Großseggenriede · **K** Ufersäume, Säume, Ruderal- und Staudenfluren (Gras- und Krautfluren) · **M** Moore · **Z** Zwergstrauch- und Ginsterheiden |
| HÖHLEN, VEGETATIONSFREIE/-ARME STANDORTE UND GLETSCHER | **H** Höhlen · **O** Felsen, Block- und Schutthalden, Geröllfelder, vegetationsfreie/-arme offene Bereiche |
| WÄLDER UND GEHÖLZSTRUKTUREN | **B** Feldgehölze, Hecken, Gebüsche, Gehölzkulturen · **W** Waldmäntel, Vorwälder, spezielle Waldnutzungsformen · **L** Laub(misch)wälder (Laubbaumanteil > 50 %) · **N** Nadel(misch)wälder (Nadelbaumanteil > 50 %) |
| SIEDLUNGSBEREICH, INDUSTRIE-/GEWERBEFLÄCHEN UND VERKEHRSANLAGEN | **P** Freiflächen des Siedlungsbereichs · **X** Siedlungsbereich, Industrie-, Gewerbe- und Sondergebiete · **V** Verkehrsfläche |

### 3.4 Full BNT table (all rows V, transcribed from the list pp. 16–24; WP = Grundwert; "+" = +1 WP possible; BK = biotope-mapping sub-types as printed 2014)

**Q – Quellen und Quellbereiche**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT |
|---|---|---|---|---|---|
| Q11 | Künstlich gefasste Quellen und Quellbereiche, naturfern | gering | 5 | | – |
| Q12 | – mit naturnaher Entwicklung | mittel | 9 | + | (x) QF00BK |
| Q21 | Kalkarme Quellen, natürlich oder naturnah | hoch | 14\*\* | | x QF00BK, MF00BK, SU00BK, VU00BK, SU3130, VU3130 |
| Q221 | Kalktuff-Quellen, natürlich oder naturnah | hoch | 15\*\* | | x QF00BK, MF00BK, QF7220\*, MF7230 |
| Q222 | Sonstige kalkreiche Quellen, natürlich oder naturnah | hoch | 14\*\* | | x |

**F – Fließgewässer**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT |
|---|---|---|---|---|---|
| F11 | Sehr stark bis vollständig veränderte Fließgewässer (Gewässerstruktur 6–7) | gering | 2 | | – |
| F12 | Stark veränderte Fließgewässer (Gewässerstruktur 5) | gering | 5 | | – |
| F13 | Deutlich veränderte Fließgewässer (Gewässerstruktur 4) | mittel | 8 | + | (x) FW00BK, FW3220–FW3270, *LR3260, LR3270* |
| F14 | Mäßig veränderte Fließgewässer (Gewässerstruktur 3) | hoch | 11\* | + | (x) same |
| F15 | Nicht oder gering veränderte Fließgewässer (Gewässerstruktur 1–2) | hoch | 14\*\* | | x FW00BK, FW3220–FW3270 |
| F211 | Gräben, naturfern (mit intensiver Unterhaltung) | gering | 5 | | – |
| F212 | Gräben mit naturnaher Entwicklung (ohne oder mit extensiver Unterhaltung) | mittel | 10 | + | (x) VU3140, VU3150, *LR3140, LR3150, LR3260* |
| F221 | Kanäle (mit künstlichen Uferbefestigungen), naturfern | gering | 2 | | – |
| F222 | Kanäle mit naturnaher Entwicklung | mittel | 8 | + | (x) |
| F231 | Sonstige künstlich angelegte Fließgewässer (z. B. Fischpässe und Umgehungsgerinne), naturfern | gering | 5 | | – |
| F232 | – mit naturnaher Entwicklung | mittel | 10 | + | (x) |
| F31 | Wechselwasserbereiche an Fließgewässern, bedingt naturnah | mittel | 9 | + | (x) |
| F32 | Wechselwasserbereiche an Fließgewässern, natürlich oder naturnah | hoch | 14\*\* | | x |

**S – Stillgewässer**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT |
|---|---|---|---|---|---|
| S111 | Dystrophe Stillgewässer (Moorgewässer), bedingt naturnah | mittel | 10 | + | (x) SU00BK, SU3160, VU3160, MO3160 |
| S112 | Dystrophe Stillgewässer, natürlich oder naturnah | hoch | 14\*\* | | x |
| S121 | Oligo- bis mesotrophe Stillgewässer, bedingt naturfern bis naturfern | mittel | 7 | | – |
| S122 | Oligo- bis mesotrophe Stillgewässer, bedingt naturnah | mittel | 10 | + | (x) SU00BK, VU3130, VU3140, SU3130, SU3140, *LR3130, LR3140* |
| S123 | Oligo- bis mesotrophe Stillgewässer, natürlich oder naturnah | hoch | 14\* | | x |
| **S131** | **Eutrophe Stillgewässer, bedingt naturfern bis naturfern** | mittel | 6 | | – |
| **S132** | **Eutrophe Stillgewässer, bedingt naturnah** | mittel | 9 | + | (x) SU00BK, VU3150, SU3150, *LR3150* |
| **S133** | **Eutrophe Stillgewässer, natürlich oder naturnah** | hoch | 13\* | | x SU00BK, VU3150, SU3150 |
| S14 | Poly- bis hypertrophe Stillgewässer | gering | 5 | | – |
| S21 | Abbaugewässer (vgl. auch S1) | gering | 1 | | – |
| **S22** | **Sonstige naturfremde bis künstliche Stillgewässer** | gering | 3 | | – |
| S31 | Wechselwasserbereiche an Stillgewässern, bedingt naturnah | mittel | 9 | + | (x) |
| S32 | Wechselwasserbereiche an Stillgewässern, natürlich oder naturnah | hoch | 14\*\* | | x |

**A – Äcker/Felder**

| Code | Biotop-/Nutzungstyp | Stufe | WP |
|---|---|---|---|
| A11 | Intensiv bewirtschaftete Äcker ohne oder mit stark verarmter Segetalvegetation | gering | 2 |
| A12 | Bewirtschaftete Äcker mit standorttypischer Segetalvegetation (z. B. bei PIK-Maßnahmen für Blühstreifen, Ackerrandstreifen, Lerchenfenster usw.) | gering | 4 |
| A13 | Extensiv bewirtschaftete Äcker mit seltener Segetalvegetation | mittel | 9 |
| A2 | Ackerbrachen (ohne einjährige Brachestadien) | gering | 5 |

**G – Grünland (Dauergrünland)**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT (2014 → re-mapped 2021) |
|---|---|---|---|---|---|
| **G11** | **Intensivgrünland (genutzt)** (inkl. einjährig brachgefallenes Intensivgrünland; Wechselgrünland wird unter A1-2 gefasst) | gering | 3 | | – |
| G12 | Intensivgrünland, brachgefallen (mit hohem Anteil an Brachezeigern, Verbuschung < 50 %) | gering | 5 | | – |
| **G211** | **Mäßig extensiv genutztes, artenarmes Grünland** | mittel | 6 | | – |
| **G212** | **Mäßig extensiv genutztes, artenreiches Grünland** (z. B. Glatt-/Goldhaferwiesen oder Weiden) | mittel | 8 | + | (x) *LR6510* → **GU651L** |
| G213 | Artenarmes Extensivgrünland (z. B. Rotschwingel-Rotstraußgras-Wiesen oder Weiden) | mittel | 8 | + | (x) *GE00BK* → GX00BK |
| **G214** | **Artenreiches Extensivgrünland** (z. B. magere Glatt-/Goldhaferwiesen oder Magerweiden) (extensiv genutzt) | hoch | 12\* | | x AD00BK, AI00BK, AI6520, *GE00BK, GE6510, GE6520*, GI00BK, GI6520 → **AD00BK**, GX00BK, **GU651E, GY6520** |
| G215 | Mäßig extensiv bis extensiv genutztes Grünland, brachgefallen | mittel | 7 | + | (x) *GB00BK* |
| G221 | Mäßig artenreiche seggen- oder binsenreiche Feucht- und Nasswiesen (extensiv genutzt) | mittel | 9 | + | (x) GN00BK |
| G222 | Artenreiche seggen- oder binsenreiche Feucht- und Nasswiesen | hoch | 13\* | | x GN00BK, MF00BK |
| G223 | Seggen- oder binsenreiche Feucht- und Nasswiese, brachgefallen | mittel | 10 | | x GH00BK, GN00BK, GG00BK, GR00BK, *GB00BK* |
| G231 | Flutrasen, extensiv genutzt | mittel | 9 | + | (x) GN00BK |
| G232 | Flutrasen, brachgefallen | mittel | 7 | + | (x) GN00BK |
| G24 | Stromtalwiesen (Brenndoldenwiesen) | hoch | 14\* | | x GA6440 |
| G25 | Salzwiesen | hoch | 14\* | | x GZ1340\* |
| G311 | Steppenrasen (extensiv genutzt) | hoch | 15\*\* | | x GT6240\* |
| G312 | Basiphytische Trocken-/Halbtrockenrasen und Wacholderheiden (extensiv genutzt) | hoch | 13\* | | x GT5130, GT6210, GT6210\* |
| **G313** | **Sandmagerrasen (basenarm oder basenreich) (extensiv genutzt)** | hoch | 13\* | | x GL00BK, GL2330, GL6120\*, SD2330 |
| G314 | Magerrasen / Wacholderheiden, brachgefallen | hoch | 11 | | x |
| G321 | Artenarme oder brachgefallene Pfeifengraswiesen | mittel | 10 | | x GP00BK, GP6410, *GB00BK* |
| G322 | Artenreiche Pfeifengraswiesen (extensiv genutzt) | hoch | 13\* | | x GP00BK, GP6410 |
| G331 | Artenarme oder brachgefallene Borstgrasrasen | mittel | 10 | | x GO00BK, GO5130, GO6150, GO6230\*, *GB00BK* |
| G332 | Artenreiche Borstgrasrasen (extensiv genutzt) | hoch | 13\* | | x |
| G341 | Gebirgsrasen und Schneebodenvegetation | hoch | 14\*\* | | x |
| G342 | Alpine/Subalpine Rieselflur- und Schwemmbodenvegetation | hoch | 14\*\* | | x |
| **G4** | **Tritt- und Parkrasen (mit hoher Schnittfrequenz und/oder Trittbelastung)** | gering | **3** | | – |

**R – Röhrichte und Großseggenriede**

| Code | Biotop-/Nutzungstyp | Stufe | WP | BK / LRT |
|---|---|---|---|---|
| R111 | Schilf-Landröhrichte | mittel | 10 | x GR00BK |
| R112 | Schneidried- und Simsen-Landröhrichte | hoch | 13\* | x GJ7210\*, GR00BK |
| R113 | Sonstige Landröhrichte (z. B. aus Rohrkolben, Rohrglanzgras oder Wasser-Schwaden) | mittel | 10 | x GR00BK |
| R121 | Schilf-Wasserröhrichte | hoch | 11 | x VH00BK, VH3130, VH3140, VH3150, *LR3130, LR3140, LR3150* |
| R122 | Schneidried- und Simsen-Wasserröhrichte | hoch | 13\* | x |
| R123 | Sonstige Wasserröhrichte (z. B. aus Rohrkolben, Wasser-Schwaden, Rohrglanzgras, Kalmus usw.) | hoch | 11 | x |
| R21 | Kleinröhrichte oligo- bis mesotropher Gewässer | hoch | 12 | x VK00BK, VK3130, VK3140 |
| R22 | Kleinröhrichte eutropher Gewässer | hoch | 11 | x VK00BK, VK3150, *LR3150* |
| R31 | Großseggenriede außerhalb der Verlandungsbereiche (inkl. Wald-Simsen-Bestände) | mittel | 10 | x GG00BK |
| R321 | Großseggenriede oligo- bis mesotropher Gewässer | hoch | 13\* | x VC00BK, VC3130, VC3140 |
| R322 | Großseggenriede eutropher Gewässer | hoch | 12\* | x VC00BK, VC3150, *LR3150* |

**K – Ufersäume, Säume, Ruderal- und Staudenfluren (Gras- und Krautfluren)** (Verbuschung < 50 %)

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT |
|---|---|---|---|---|---|
| **K11** | **Artenarme Säume und Staudenfluren** (z. B. hypertrophe Bestände mit Brennnessel, Neophyten-Staudenfluren oder Dominanzbestände von Adlerfarn) | gering | 4 | | – |
| K121 | Mäßig artenreiche Säume und Staudenfluren trocken-warmer Standorte | mittel | 8 | + | (x) GW00BK, *GB00BK, RF00BK* |
| K122 | Mäßig artenreiche Säume und Staudenfluren frischer bis mäßig trockener Standorte | mittel | 6 | + | (x) *GB00BK* |
| K123 | Mäßig artenreiche Säume und Staudenfluren feuchter bis nasser Standorte | mittel | 7 | + | (x) GH00BK, GH6430, *GB00BK* |
| K131 | Artenreiche Säume und Staudenfluren trocken-warmer Standorte | hoch | 11 | | x GW00BK, GT6210, GT6210\*, *RF00BK* |
| K132 | Artenreiche Säume und Staudenfluren frischer bis mäßig trockener Standorte | mittel | 8 | + | (x) *GB00BK* |
| K133 | Artenreiche Säume und Staudenfluren feuchter bis nasser Standorte | hoch | 11 | | x GH00BK, GH6430, *GB00BK* |
| K21 | Alpine/Subalpine Hochstaudenfluren eutropher bis oligotropher Standorte | hoch | 12\* | | x AH00BK, AH4080, AH6430 |
| K22 | Alpine/Subalpine Hochstaudenfluren hypertropher Standorte (z. B. Lägerfluren) | gering | 4 | | – |

**M – Moore · Z – Heiden · H – Höhlen**

| Code | Biotop-/Nutzungstyp | Stufe | WP |
|---|---|---|---|
| M111 / M112 | Geschädigte Hochmoore, nicht mehr / noch regenerierbar | mittel / hoch | 9 (+) / 13\*\* |
| M12 | Lebende Hochmoore | hoch | 15\*\* |
| M21 / M22 | Übergangs- und Zwischenmoore, geschädigt / weitgehend intakt | hoch | 11 / 15\*\* |
| M31 / M32 | Abtorfungsflächen / Bunkerde- und Torfhalden | gering | 2 / 4 |
| M411 / M412 | Kalkreiche Flach- und Quellmoore, geschädigt / weitgehend intakt | hoch | 11\* / 15\*\* |
| M421 / M422 | Kalkarme Flach- und Quellmoore, geschädigt / weitgehend intakt | hoch | 11\* / 15\*\* |
| Z111 / Z112 | Zwergstrauch- und Ginsterheiden, geschädigt (Verbuschung < 50 %) / weitgehend intakt | mittel / hoch | 9 (+) / 13\* |
| Z12 | Felsbandheiden | hoch | 13\* |
| Z13 | Besenginsterheiden | mittel | 9 (+) |
| Z2 | Alpine Heiden | hoch | 14\*\* |
| H1 | Natürliche Höhlen, Halbhöhlen (Balmen) und Eingangsbereiche von Höhlen | hoch | 12\* (+) |
| H2 | Stollen, Schächte, Bunker- und Kelleranlagen | mittel | 6 |

**O – Felsen, Block- und Schutthalden, Geröllfelder, vegetationsfreie/-arme offene Bereiche**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT |
|---|---|---|---|---|---|
| O111 | Natürliche und naturnahe Felsen ohne Felsspaltenvegetation (inkl. sehr junge Pionierstadien) | hoch | 11 | + | (x) FN00BK |
| O112 | Natürliche und naturnahe Felsen mit Felsspaltenvegetation | hoch | 13\* | + | (x) FH6110\*, FH8110, FH8220, FH8230 |
| O12 | Natürliche und naturnahe Block- und Schutthalden | hoch | 13\* | + | (x) SG8110, SG8120, SG8150, SG8160\* |
| **O21** | **Lesesteinriegel** | mittel | 10 | + | (x) SG8150, SG8160\*, *ST00BK* |
| **O22** | **Natursteinmauern** | mittel | 9 | + | (x) *RF00BK, UR00BK* |
| O31 | Natürliche und naturnahe Steilwände und Abbruchkanten aus Lockergestein oder Sand | mittel | 9 | + | (x) *ST00BK* |
| O32 | – aus Lehm oder Löss | mittel | 10 | | x LL00BK |
| **O41** | **Natürliche und naturnahe vegetationsfreie/-arme Kies- und Schotterflächen** | mittel | 9 | + | (x) *RF00BK, ST00BK* |
| **O421** | **Natürliche und naturnahe vegetationsfreie/-arme Sandflächen ohne eiszeitlichen Ursprung** | mittel | 9 | + | (x) *RF00BK*, SI00BK, *ST00BK* |
| O422 | – eiszeitlichen Ursprungs (z. B. Binnendüne) | hoch | 12 | + | (x) SD2330 |
| **O43** | **Natürliche und naturnahe vegetationsfreie/-arme Flächen aus bindigem Substrat** | mittel | 8 | + | (x) SI00BK, *ST00BK* |
| O5 | Gletscher und Firnfelder | hoch | 15\*\* | | x SE (list prints "SE8430"; the mapping key 2022 has "SE … (8340)" – FFH code is 8340) |
| O611 / O621 / O631 / O641 | Abgrabungs- und Aufschüttungsflächen (Felsen / Block- und Schutthalden, Halden / Steilwände aus Lockergestein / ebenerdige Abbauflächen, Rohbodenstandort), naturfern | gering | 1 | | – |
| O612 / O622 / O632 / O642 | – mit naturnaher Entwicklung | mittel | 7 | + | (x) *ST00BK* |
| O651 | Deponien (z. B. Hausmüll, Bauschutt, Schlamm), naturfern | keine | 0 | | – |
| O652 | Deponien, sich selbst überlassen oder begrünt | gering | 1 | | – |
| **O7** | **Bauflächen und Baustelleneinrichtungsflächen (Rohbodenstandorte)** | gering | 1 | | – |

**B – Feldgehölze, Hecken, Gebüsche, Gehölzkulturen**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK / LRT |
|---|---|---|---|---|---|
| B111 | Gebüsche / Hecken trocken-warmer Standorte (z. B. mit Berberitze, Felsenbirne, Felsenkirsche) | hoch | 12 | | WD00BK, WD40A0\*, GT6210 (always § / LRT per Arbeitshilfe) |
| **B112** | **Mesophile Gebüsche / Hecken** (z. B. mit Schlehe, Weißdorn, Hasel) | mittel | 10 | | x *WI00BK, WH00BK, WX00BK* |
| B113 | Sumpfgebüsche (z. B. mit Faulbaum, Ohr-Weide, Trauben-Kirsche) | hoch | 11 | | x WG00BK |
| B114 | Auengebüsche (z. B. mit Mandel-Weide, Korb-Weide, Purpur-Weide) | hoch | 12 | | x WG00BK, FW3230, FW3240, WA91E0\* |
| B115 | Moorgebüsche | hoch | 12 | | x WG00BK, MO00BK, MF00BK, MF7230 |
| **B116** | **Gebüsche / Hecken stickstoffreicher, ruderaler Standorte** (z. B. mit Holunder, inkl. Rubus-Gestrüppe) | mittel | 7 | | – |
| **B12** | **Gebüsche / Hecken mit überwiegend gebietsfremden Arten** (z. B. Armenische Brombeere, Götterbaum, Eschen-Ahorn, Schneebeere) | gering | 5 | | – |
| B13 | Stark verbuschte Grünlandbrachen (Verbuschung > 50 %) und initiales Gebüschstadium (u. a. auf anthropogenen Sekundärstandorten) | mittel | 6 | + | (x) *WI00BK* |
| **B141** | **Schnitthecken (intensiver jährlicher Formschnitt) mit überwiegend einheimischen, standortgerechten Arten** | gering | 5 | | – |
| **B142** | **Schnitthecken mit überwiegend fremdländischen Arten** | gering | 3 | | – |
| B211 / B212 / B213 | Feldgehölze mit überwiegend einheimischen, standortgerechten Arten – junge / mittlere / alte Ausprägung | mittel / mittel / hoch | 6 / 10\* / 12\*\* | | x *WO00BK, WN00BK* |
| B221 / B222 / B223 | Feldgehölze mit überwiegend gebietsfremden Arten – jung / mittel / alt | gering / mittel / hoch | 5 / 8\* / 11\*\* | | – |
| **B311 / B312 / B313** | **Einzelbäume / Baumreihen / Baumgruppen mit überwiegend einheimischen, standortgerechten Arten (inkl. Alleen) – jung / mittel / alt** | gering / mittel / hoch | **5 / 9\* / 12\*\*** | + (B313) | (x) *UA00BK, UE00BK* |
| **B321 / B322 / B323** | **… mit überwiegend gebietsfremden Arten (inkl. Alleen) – jung / mittel / alt** | gering / mittel / hoch | **4 / 8\* / 11\*\*** | + (B323) | (x) *UA00BK, UE00BK* |
| B331 / B332 / B333 | Kopfbäume / Kopfbaumreihen – jung / mittel / alt | gering / mittel / hoch | 5 / 9\* / 12\*\* | + (B333) | (x) *UA00BK, UE00BK* |
| B411 / B412 | Streuobstbestände im Komplex mit Äckern ohne oder mit standorttypischer Segetalvegetation – junge / mittlere bis alte Ausbildung | gering / mittel | 5 / 8\* | + (B412) | (x) *WÜ00BK* → BX |
| B421 / B422 | Streuobstbestände im Komplex mit Äckern mit seltener Segetalvegetation – jung / mittel bis alt | mittel | 9 / 10\* | + (B422) | (x) *WÜ00BK* → BX |
| B431 / B432 | Streuobstbestände im Komplex mit intensiv bis extensiv genutztem Grünland – jung / mittel bis alt | mittel | 8 / 10\* | + | (x) → GX00BK, GB00BK, **GU651L**, -BX, **-BS** |
| B441 | Streuobstbestände im Komplex mit artenreichem Extensivgrünland (junge bis alte Ausbildung) | hoch | 12\* | | x → GX00BK, **GU651E, GY6520**, -BX, **-BS** |
| B442 | Streuobstbestände im Komplex mit Halbtrockenrasen (junge bis alte Ausbildung) | hoch | 13\* | | x **GT6210, GT621P** (-BX / -BS) |
| B51 | Weihnachtsbaumkulturen | gering | 3 | | – |
| B52 | Baumschulen, Obstplantagen und -kulturen | gering | 3 | | – |
| B531 / B532 | Kurzumtriebsplantagen (KUP), strukturarm / strukturreich | gering / mittel | 3 / 7 | | – |
| B54 | Gehölzplantagen, brachgefallen | mittel | 7 | + | (x) *UK00BK* |
| B611 / B612 | Rebkulturen, intensiv / extensiv bewirtschaftet | gering / mittel | 3 / 7 | | – |
| B62 | Rebbrachen | mittel | 8 | + | (x) *UK00BK* |

**W – Waldmäntel, Vorwälder, spezielle Waldnutzungsformen**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK |
|---|---|---|---|---|---|
| W11 | Waldmäntel trocken-warmer Standorte | hoch | 12 | | x WD00BK |
| W12 | Waldmäntel frischer bis mäßig trockener Standorte | mittel | 9 | + | (x) *WX00BK* |
| W13 | Waldmäntel feuchter bis nasser Standorte | hoch | 12 | | x WG00BK |
| W14 | Waldmäntel stickstoffreicher, ruderaler Standorte | mittel | 7 | | – |
| W21 | Vorwälder auf natürlich entwickelten Böden | mittel | 7 | | – |
| **W22** | **Vorwälder auf urban-industriellen Standorten** (z. B. Industrie-/Gewerbeflächen, Häfen, Bahnhöfe, brach liegende Abbaubereiche; z. B. mit Sand-Birke, Zitter-Pappel oder Sal-Weide) | mittel | 6 | + | (x) *WI00BK* |
| W3 | Niederwälder / Mittelwälder / Hutewälder mit traditioneller Nutzung | hoch | 12\* | + | (x) |

**L – Laub(misch)wälder · N – Nadel(misch)wälder** (WP for junge / mittlere / alte Ausprägung)

| Code | Biotop-/Nutzungstyp | WP J / M / A | LRT / BK |
|---|---|---|---|
| L111–L113 | Eichen-Hainbuchenwälder wechseltrockener Standorte | 8 / 12\* / 14\*\* | WW, 9170 |
| L121–L123 | Eichenwälder trockener Standorte | 9 / 13\* / 15\*\* | WW, 9190 |
| L131–L133 | Wärmeliebende Kalkbuchenwälder | 9 / 13\* / 15\*\* | WK, 9150 |
| L211–L213 | Eichen-Hainbuchenwälder frischer bis staunasser Standorte | 8 / 12\* / 14\*\* | 9160 |
| L221–L223 | Eichen-Birkenwälder frischer bis feuchter Standorte | 9 / 13\* / 15\*\* | 9190 |
| L231–L233 | Buchenwälder basenarmer Standorte (inkl. montane Tannen-Fichten-Buchenwälder mit Buchenanteil > 50 %) | 8 / 12\* / 14\*\* | 9110 |
| L241–L243 | Buchenwälder basenreicher Standorte | 8 / 12\* / 14\*\* | 9130 |
| L251–L253 | Hochmontane-subalpine Bergahorn-Buchenwälder | 8 / 12\* / 14\*\* | 9140 |
| L311–L313 | Schluchtwälder | 8 / 12\* / 14\*\* | WJ, 9180\* |
| L321–L323 | Block- und Hangschuttwälder | 8 / 12\* / 14\*\* | WÖ, 9180\* |
| L411–L413 | Birken-Moorwälder | 9 / 13\* / 15\*\* | MW91D0\* |
| L421–L423 | Schwarzerlen-Bruchwälder | 9 / 13\* / 15\*\* | WB |
| L431–L433 | Sumpfwälder | 8 / 12\* / 14\*\* | WQ, WQ91E0\* |
| L511–L513 | Quellrinnen, Bach- und Flussauenwälder | 8 / 12\* / 14\*\* | WA91E0\* |
| L521 / L522 | Weichholzauenwälder – junge bis mittlere / alte Ausprägung | 13\* / 15\*\* | WA91E0\* |
| L531–L533 | Hartholzauenwälder | 9 / 13\* / 15\*\* | WA91F0 |
| L541–L543 | Sonstige gewässerbegleitende Wälder (z. B. Eschenmischwald) | 6 / 10\* / 12\*\* (+) | (x) *WN00BK* |
| **L61 / L62 / L63** | **Sonstige standortgerechte Laub(misch)wälder** | **6 / 10\* / 12\*\*** | – |
| L711–L713 | Nicht standortgerechte Laub(misch)wälder einheimischer Baumarten | 5 / 8\* / 10\*\* | – |
| L721–L723 | Nicht standortgerechte Laub(misch)wälder gebietsfremder Baumarten (z. B. Rot-Eiche, Hybrid-Pappel oder Robinie) | 4 / 6\* / 8\* | – |
| N111–N113 | Kiefernwälder nährstoffarmer, stark saurer Standorte | 9 / 13\* / 15\*\* | WP, 91U0, 91T0 |
| N121–N123 | Kiefernwälder nährstoffarmer, carbonatischer Standorte | 9 / 13\* / 15\*\* | WE, 91U0 |
| N211–N213 · N221–N223 | Fichten-Blockschuttwälder · Fichtenwälder silikatischer und carbonatischer Standorte | 8 / 12\* / 14\*\* | 9410 |
| N311–N313 · N321–N323 | Beerstrauchreiche Fichten-Tannenwälder · Krautreiche Buchen-Fichten-Tannenwälder | 8 / 12\* / 14\*\* | 9410 · 9130 |
| N41–N43 | Alpine Lärchen-Zirbenwälder | 9 / 13\* / 15\*\* | WY, 9420 |
| N511–N533 | Fichten- / Kiefern- / Bergkiefern-Moorwälder | 9 / 13\* / 15\*\* | MW91D0\* (91D4\* / 91D2\* / 91D3\*) |
| N61 / N62 / N63 | Sonstige standortgerechte Nadel(misch)wälder | 6 / 10\* / 12\*\* | – |
| N711–N713 | Strukturarme Altersklassen-Nadelholzforste | 3 / 4 / 6\*\* | – |
| N721–N723 | Strukturreiche Nadelholzforste | 5 / 7\* / 8\*\* | – |

**P – Freiflächen des Siedlungsbereichs**

| Code | Biotop-/Nutzungstyp | Stufe | WP | + | BK |
|---|---|---|---|---|---|
| **P11** | **Park- und Grünanlagen (inkl. Friedhöfe) ohne Baumbestand oder mit Baumbestand junger bis mittlerer Ausprägung** | gering | 5 | | – |
| **P12** | **Park- und Grünanlagen mit Baumbestand alter Ausprägung** | mittel | 10\*\* | | x *UP00BK* |
| **P21** | **Privatgärten und Kleingartenanlagen, strukturarm** | gering | 5 | | – |
| **P22** | **Privatgärten und Kleingartenanlagen, strukturreich** | mittel | 7 | + | (x) *UK00BK* |
| **P31** | **Sport-/Spiel-/Erholungsanlagen mit hohem Versiegelungsgrad** (z. B. Aschesportplatz, versiegelte Spiel-/Sportflächen) | keine | 0 | | – |
| **P32** | **Sport-/Spiel-/Erholungsanlagen mit geringem Versiegelungsgrad** (z. B. Naturrasensportplatz, Spielplatz) | gering | 2 | | – |
| P411 | Sonderflächen der Land- und Energiewirtschaft (z. B. Fahrsilo, Schutt- oder Lagerplatz, Fotovoltaikfläche, Windkraftanlage), versiegelt | keine | 0 | | – |
| P412 | – teilversiegelt | gering | 1 | | – |
| P42 | Land- und forstwirtschaftliche Lagerflächen | gering | 2 | | – |
| **P431** | **Ruderalflächen im Siedlungsbereich** (z. B. Brachen der Industrie-/Gewerbegebiete, Häfen, Bahnhöfe oder Tiergehege, häufig mit stark verdichtetem Boden), **vegetationsarm / -frei** | gering | 2 | | – |
| **P432** | **– mit artenarmen Ruderal- und Staudenfluren** | gering | 4 | | – |
| **P433** | **– mit artenreichen Ruderal- und Staudenfluren** | mittel | 8 | + | (x) *RF00BK* |
| P44 | Kleingebäude der Land- und Energiewirtschaft (z. B. Umspanngebäude, Stadel, Hochsilo) | keine | 0 | | – |
| **P5** | **Sonstige versiegelte Freiflächen** | keine | 0 | | – |

**X – Siedlungsbereich, Industrie-, Gewerbe- und Sondergebiete** (areas by BauNVO use type, "inkl. typischer Freiräume")

| Code | Biotop-/Nutzungstyp | Stufe | WP |
|---|---|---|---|
| X11 | Dorf-, Kleinsiedlungs- und Wohngebiete (inkl. typischer Freiräume) | gering | 2 |
| X12 | Misch- und Kerngebiete (inkl. typischer Freiräume) | gering | 1 |
| X131 | Historische Gebäudekomplexe (inkl. typischer Freiräume) (z. B. Kirchen, Kloster, Burgen) | gering | 3 |
| X132 | Einzelgebäude im Außenbereich (z. B. landwirtschaftliche Betriebsanlagen, Einzelgehöfte, Scheunen, Stallungen, Speichergebäude) | gering | 1 |
| X2 | Industrie- und Gewerbegebiete (inkl. typische Freiräume) | gering | 1 |
| X3 | Sondergebiete (inkl. typischer Freiräume) | gering | 2 |
| **X4** | **Gebäude der Siedlungs-, Industrie- und Gewerbegebiete** | keine | 0 |

**V – Verkehrsfläche**

| Code | Biotop-/Nutzungstyp | Stufe | WP |
|---|---|---|---|
| **V11** | Verkehrsflächen des Straßen- und Flugverkehrs, **versiegelt** (mit wasserundurchlässiger Beton-, Asphalt- oder Pflasterdecke) | keine | 0 |
| **V12** | – **befestigt** (mit wasserdurchlässiger Pflasterdecke, geschottert oder mit wassergebundener Decke; Bankette, Mittelstreifen) | gering | 1 |
| V21 | Gleisanlagen und Zwischengleisflächen, versiegelt (schotterloses Gleis) | keine | 0 |
| V22 | – geschottert (Schottergleis) | gering | 1 |
| **V23** | – begrünt (Grüne Gleise) | gering | 4 |
| **V31** | Rad-/Fußwege und Wirtschaftswege, **versiegelt** (mit wasserundurchlässiger Beton-, Asphalt- oder Pflasterdecke) | keine | 0 |
| **V32** | – **befestigt** (mit wasserdurchlässiger Pflasterdecke, geschottert oder mit wassergebundener Decke) | gering | 1 |
| **V331** | – unbefestigt, nicht bewachsen (mit offenem Boden) | gering | 2 |
| **V332** | – unbefestigt, bewachsen (Grünwege) | gering | 3 |
| V4 | Hohlwege | mittel | 10\* |
| **V51** | **Grünflächen und Gehölzbestände junger bis mittlerer Ausprägung entlang von Verkehrsflächen** (z. B. auf Böschungen und weiteren Nebenflächen) | gering | 3 |
| **V52** | **Gehölzbestände alter Ausprägung entlang von Verkehrsflächen** | mittel | 7\* |

### 3.5 Definitions from the Arbeitshilfe that matter for urban elements (V)

- **P1**: "Öffentliche und private Grünanlagen, die entweder intensiv gepflegt werden (z. B. Zier-Parks) oder relativ naturnah gestaltet sind (z. B. waldartige Parkanlagen) … Auch Friedhöfe, kleinere Grünflächen, Haine, Schloss- und alte Villengärten sowie Botanische und Zoologische Gärten". **P11** = tree stock predominantly < 100 years; **P12** = "höherer Anteil angepflanzter, markanter alter Bäume (Bestandsalter ≥ 80 Jahre)".
- **P21** = newer gardens without old trees, "vielfach höherem Rasenanteil"; **P22** = older gardens with old trees, hedges; also abandoned gardens.
- **P31 / P32**: high vs. low share of sealed surface (P32 "insbesondere Rasenfläche oder Sandflächen … Naturrasensportplätze, Spielplätze, Golfplätze, Freibäder, Campingplätze, Minigolfplätze").
- **P43**: "Ruderale, stark anthropogen überformte Flächen mit Schwerpunkt im Siedlungsbereich … Der Gehölzanteil beträgt stets < 50 %"; P433 typically with *Echium vulgare, Anchusa officinalis, Melilotus officinalis, Daucus carota, Erodium cicutarium, Picris hieracioides*; railway yards are named as valuable.
- **X**: areas are classified by the use categories of the BauNVO; "Soweit begründete naturschutzfachliche Besonderheiten vorliegen, können Biotop- und Nutzungstypen … auch mit Bezug zu den anderen Obergruppen erfasst und bewertet werden" – i.e. a lawn or tree inside a residential area may be mapped as `G4` / `B31x` instead of being absorbed in `X11`.
- **V1**: sealed = "wasserundurchlässiger Beton-, Asphalt- und Pflasterdecke"; befestigt = "wasserdurchlässiger Pflasterdecke (mit Fugenvegetation, z. B. Rasengittersteine), geschottert oder mit wassergebundener Decke"; verges and central reservations are recorded with the traffic area. **V23** green tracks = "Rasengleis" or "Sedumgleis". **V5** = roadside greenery that cannot be assigned to a woody type B; V51 stand age < 80 years, V52 ≥ 80 years; tree rows and avenues are mapped separately as B3.
- **B14 Schnitthecken**: "Intensiv gepflegte und regelmäßig beschnittene, schmale Gehölzreihen … mit jährlichem Formschnitt … Elemente der Städte und Siedlungen"; B141 e.g. *Ligustrum vulgare, Carpinus betulus, Taxus baccata*; B142 e.g. *Ligustrum ovalifolium, Cotoneaster, Thuja, Buxus sempervirens, Prunus laurocerasus*.
- **B1**: shrubs mostly up to 6 m high; hedges always linear, max. 10 m wide. **B2 Feldgehölze**: usually up to 1 ha. **B12**: dominance stands of neophytes such as *Buddleja davidii, Symphoricarpos albus, Acer negundo, Ailanthus altissima, Rubus armeniacus*.
- **G4**: see section 9.

### 3.6 Bavarian biotope mapping (Biotopkartierung Bayern) – codes of the mapping key

**Source (V):** LfU (2022): *Kartieranleitung Biotopkartierung Bayern (inkl. Kartierung der Offenland-Lebensraumtypen der Fauna-Flora-Habitat-Richtlinie), Teil 2 – Biotoptypen*, Stand April 2022 (Lang & Zintl; continuation of LfU 2007, 2010, 2018, 2020). <https://www.lfu.bayern.de/natur/doc/kartieranleitungen/biotoptypen_teil2.pdf>

**Code logic (V):** biotope type = two letters (`GO` Borstgrasrasen); sub-type = two letters + FFH code (`GO6230*`) or `00BK` = no habitat type (`GO00BK`); forest types without LRT mapping get `0000` (`WK0000`). Since the 2020 edition orchard types `BS` / `BX` can be combined with grassland sub-types (`GU651E-BX`, `GX00BK-BS`). Cover classes (modified Braun-Blanquet): 1 = 1–5 % · 2a = >5–12,5 % · 2b = >12,5–25 % · 3a = >25–37,5 % · 3b = >37,5–50 % · 4 = >50–75 % · 5 = >75–100 % (this is where the 12,5 % and 25 % thresholds of the grassland rules come from).

**Overview of biotope types and legal protection (V; § 30 = § 30 BNatSchG and/or Art. 23 BayNatSchG; § 39 = § 39 (5) BNatSchG and/or Art. 16 BayNatSchG; `+` = normally recorded only in the *Stadtbiotopkartierung*)**

| Group | Code – name – protection |
|---|---|
| Wälder | MW Moorwälder (§30) · WA Auwälder (§30) · WB Bruchwälder (§30) · WE Kiefernwälder, basenreich (§30) · WJ Schluchtwälder (§30) · WK Buchenwälder, wärmeliebend (§30) · WÖ Block- und Hangschuttwälder (§30) · WP Kiefernwälder, bodensauer (§30) · WQ Sumpfwälder (§30) · WW Eichenmischwälder, wärmeliebend (§30) · **WL⁺ Laubwälder, bodensauer** · **WM⁺ Laubwälder, mesophil** |
| Gebüsche, Hecken, Gehölze | BS Hochstämmige Streuobstwiesen und -weiden (§30) · BX Streuobstbestände (ohne gesetzlichen Schutz) · WD Wärmeliebende Gebüsche (§30, §39) · WG Feuchtgebüsche (§30, §39) · WH Hecken, naturnah (§39) · WI Initiale Gebüsche und Gehölze (§39) · WN Gewässer-Begleitgehölze, linear (§39) · WO Feldgehölze, naturnah (§39) · WX Mesophile Gebüsche, naturnah (§39) |
| Gewässer | FW Natürliche und naturnahe Fließgewässer (§30) · LR3130 / LR3140 / LR3150 Stillgewässer … ohne § 30-Schutz · LR3260 Fließgewässer mit flutender Wasservegetation ohne § 30-Schutz · LR3270 · SI Initialvegetation, kleinbinsenreich (§30) · SU Vegetationsfreie Wasserflächen in geschützten Gewässern (§30) · VC Großseggenriede der Verlandungszone (§30) · VH Großröhrichte (§30, §39) · VK Kleinröhrichte (§30, §39) · VU Unterwasser- und Schwimmblattvegetation (§30) |
| Feuchtstandorte des Offenlandes | GA Brenndoldenwiesen (§30) · GG Großseggenriede außerhalb der Verlandungszone (§30) · GH Feuchte und nasse Hochstaudenfluren, planar bis montan (§30) · GJ Schneidried-Sümpfe (§30) · GN Seggen- oder binsenreiche Nasswiesen, Sümpfe (§30) · GP Pfeifengraswiesen (§30) · GR Landröhrichte (§30) · GZ Salzwiesen im Binnenland (§30) · MF Flachmoore und Quellmoore (§30) · MO Offene Hoch- und Übergangsmoore (§30) · QF Quellen und Quellfluren, naturnah (§30) |
| Trocken- und/oder Magerstandorte des Offenlandes | FH Felsen mit Bewuchs, Felsvegetation (§30) · **GB Magere Altgrasbestände und Grünlandbrachen (§39 only)** · GC Zwergstrauch- und Ginsterheiden (§30) · GL Silikat- und Sandmagerrasen (§30) · GO Borstgrasrasen (§30) · GT Magerrasen, basenreich (§30) · **GU Artenreiche Flachland-Mähwiesen (§30)** – GU651E (magere bis mittlere Standorte), GU651L (mittlere bis nährstoffreiche Standorte) · GW Wärmeliebende Säume (§30) · **GX Sonstiges Extensivgrünland / kein LRT (§39 only)** · GY Artenreiche Berg-Mähwiesen (6520) (§30) · LL Löss- und Lehmwände (§30) · LR8310 Höhlen und Halbhöhlen (§30) · SD Binnendünen, offen (§30) · SG Schuttfluren und Blockhalden (§30) · **ST Initialvegetation, trocken (§39 only)** |
| Alpen | AD Alpenmagerweiden · AH Alpine Hochstaudenfluren · AR Alpine Rasen · AT Schneebodenvegetation · AZ Alpine und boreale Heiden · FN Fels ohne Bewuchs, alpin · SE Gletscher / Firnfeld · WU Latschengebüsche · WV Grünerlengebüsche · WY Lärchen-Zirbenwald |
| **Biotoptypen mit Schwerpunkt im Siedlungsbereich** | **RF Wärmeliebende Ruderalfluren (§39)** · **UA⁺ Alleen, Baumreihen, Baumgruppen (§39)** · **UE⁺ Einzelbäume (§39)** · **UK Kulturbestände, aufgelassen (§39)** · **UP Parks, Haine, Grünanlagen mit Baumbestand (§39)** · **UR⁺ Mauer- und Ritzenvegetation ((§39))** |
| Sonstige Flächenanteile innerhalb kartierter Biotope | XR Rohboden · XS Sonstige Flächenanteile · XU Vegetationsfreie Wasserflächen in nicht geschützten Gewässern · XW Wald |

**City-relevant types – recording criteria (V, chapter 4.4 of the key)**

| Code | Criteria |
|---|---|
| **RF00BK** Wärmeliebende Ruderalfluren | perennial ruderal vegetation on mostly man-made dry-warm sites: fills and excavations, dry wall bases and embankments, rubble sites, railway embankments and stations, industrial and commercial areas, other fallow land; substrates gravel, sand, ballast, rubble. Only thermophilous, drought-tolerant stands in typical **species-rich** form (thistles, *Melilotus*, *Solidago*, *Echium*, *Verbascum*, many annuals); species-poor *Melilotus*, *Aegopodium* or *Petasites* stands are **not** recorded. Alliances *Onopordion*, *Dauco-Melilotion*. Versus GB: if perennial ruderal species cover > 50 % → RF. Versus ST: ruderal pioneer vegetation with total cover ≤ 50 % → ST. |
| **UA00BK** Alleen, Baumreihen, Baumgruppen | avenues, rows and small groups (≥ 3 trees) of **deciduous** trees, also non-native; predominantly older trees with **≥ 50 cm BHD** (poplars ≥ 75 cm); conifers not considered; gaps of up to two crown widths still count as continuous; groups > 0,5 ha or with integrated green space → UP. |
| **UE00BK** Einzelbäume | mighty single trees with **BHD > 75 cm**, all deciduous species incl. pollards, fruit trees and non-native species; no conifers; in inner cities the minimum diameter may exceptionally be undercut (not for fast-growing poplar/willow). "Stadtbiotopkartierung" does not replace a tree cadastre. |
| **UK00BK** Kulturbestände, aufgelassen | abandoned allotments, gardens, nurseries, orchards, vineyards with a fine mosaic of scrub, ruderal vegetation, old grass, single trees. |
| **UP00BK** Parks, Haine, Grünanlagen mit Baumbestand | public and private parks, groves, green spaces, cemeteries, castle and old villa gardens with a tree layer containing a higher share of striking deciduous trees (**stem diameter > 50 cm**); **rich meadows ("Fettwiesen") and intensively used lawns should take up less than 50 % of the biotope**; mapped areas should have **< 10 % sealing**. |
| **UR00BK** Mauer- und Ritzenvegetation | wall-joint communities on secondary sites with **minimum length 20 m and minimum height 2 m**, typically natural-stone walls (cemetery and town walls, ruins); *Asplenietum trichomano-rutae murariae*, *Cymbalarietum muralis*. |

**Re-mapping 2018 → 2020 that affects the BNT crosswalk (V, LfU 09/2021):** GE00BK → **GX00BK** (Sonstiges Extensivgrünland / kein LRT) · LR6510 → **GU651L** · GE6510 → **GU651E** · GE6520, GI6520, GI00BK, AI6520 → **GY6520** · WÜ00BK → **BS** (legally protected tall-stem orchards) / **BX** (orchards without legal protection).

---

## 4. Other Länder keys – structural overview

Status: **Berlin and Niedersachsen were verified** on the agencies' own pages. For NRW, Hessen, Baden-Württemberg, Sachsen and Hamburg the official pages delivered no content this session; their rows are **R** (leads only – do not hard-code any code or value from them).

| Land | Key / valuation list | Code structure | Official map colours? |
|---|---|---|---|
| **Berlin** (V) | Standards named by the Umweltatlas: "Liste der Berliner Biotoptypen (SenMVKU 2023b)", "Beschreibung der Biotoptypen Berlins (SenMVKU 2023a)", "Kartieranleitung für Biotoptypenkartierung in Berlin (SenMVKU 2023c)". The list "enthält rund 7.480 Biotoptypen". Umweltatlas map 05.08 *Biotoptypen*: editions **2024** (Bearbeitungsstand Mai 2025, more than 80 000 biotopes; aerial images 2023, field surveys 2015–2022) and 2013. Protection: § 30 BNatSchG with § 28 NatSchGBln ("In Berlin sind 19 Biotoptypen gesetzlich geschützt"); dataset field `schutz_ges`: 0 = kein Schutz, 1 = sicher geschützt, 2 = Verdachtsfläche. <https://www.berlin.de/umweltatlas/biotope/biotoptypen/2024/methode/> | "Jedem Biotoptyp ist ein Zifferncode zugeordnet, der je nach hierarchischer Ebene fünf- bis achtstellig sein kann" (dataset field `bt_code`, varchar(8)). Twelve *Biotopklassen* 01–12; verified details: example "05120 = Trocken- und Magerrasen"; moor forests are placed under *Wälder (08)*; classes 10–12 ("anthropogene Biotope, Sonderbiotope, Siedlungen etc.") are structured by type of use. Names of all twelve classes (R): 01 Fließgewässer · 02 Standgewässer · 03 Anthropogene Rohbodenstandorte und Ruderalfluren · 04 Moore und Sümpfe · 05 Gras- und Staudenfluren · 06 Zwergstrauchheiden · 07 Laubgebüsche, Feldgehölze, Alleen, Baumreihen und Baumgruppen · 08 Wälder und Forsten · 09 Äcker · 10 Biotope der Grün- und Freiflächen · 11 Sonderbiotope · 12 Bebaute Gebiete, Verkehrsanlagen und Sonderflächen. Each object has a *Hauptbiotop* plus optional *Zusatzbiotop* (applies to the whole area, e.g. a use) and *Begleitbiotop* (small accompanying biotope). Mapping rules at 1 : 5 000: areas ≥ 1 000 m²; narrower than 10 m → line biotope; lines ≥ 100 m; smaller objects → points; parks and green spaces > 3 ha are resolved into single biotopes. | **Yes** – SLD and legend per WMS layer, 24 legend classes, data licence "Datenlizenz Deutschland – Zero – Version 2.0" (section 8.3) |
| **Niedersachsen** (V) | "DRACHENFELS, O. v. (2021): Kartierschlüssel für Biotoptypen in Niedersachsen unter besonderer Berücksichtigung der gesetzlich geschützten Biotope sowie der Lebensraumtypen von Anhang I der FFH-Richtlinie, Stand März 2021. – Naturschutz Landschaftspfl. Niedersachs. Heft A/4, 336 Seiten". "Aktuell gültiger Stand: März 2021" (12th edition; corrected reprint = 13th ed. 2022; interactive PDF/Word version, Stand 01.03.2023). First edition 1991; designed for scales 1 : 5 000 and 1 : 10 000; basis of nearly all biotope mapping in the state and of valuation in impact regulation and landscape planning. Since the 2021 edition further grassland types are protected under § 24 Abs. 2 NNatSchG. Supplement with values: "DRACHENFELS, O. v. (2024): Rote Liste der Biotoptypen in Niedersachsen – Regenerationsfähigkeit, Biotopwerte, Grundwasserabhängigkeit, Nährstoffempfindlichkeit, Gefährdung. – Inform.d. Naturschutz Niedersachs. 43 (2) (2/24): 69-140". <https://www.nlwkn.niedersachsen.de/naturschutz/biotopschutz/biotopkartierung/kartierschluessel/kartierschluessel-fuer-biotoptypen-in-niedersachsen-45164.html> | (R) 2–3 capital letters per type in 13 Obergruppen; urban green in a group "Grünanlagen" with separate lawn types (Scherrasen, Trittrasen); value classes I–V | not stated on the page |
| **Nordrhein-Westfalen** (R) | LANUV (2008): *Numerische Bewertung von Biotoptypen für die Eingriffsregelung in NRW* (and a variant for urban land-use planning), value scale 0–10. The agency is now **LANUK** – the old URL redirects to `lanuk.nrw.de` (V: HTTP redirect observed), where the old PDF path returned 404. | letter codes of the NRW biotope mapping key with attribute suffixes | not known |
| **Hessen** (R) | *Kompensationsverordnung (KV)* 2018, Anlage 3 "Wertliste nach Nutzungstypen"; points per m². Portal <https://www.rv.hessenrecht.hessen.de> did not load the document. | numeric `NN.NNN` Nutzungstyp numbers in groups 01–11; the list is known to contain roof-surface types incl. extensive green roofs – worth checking, because BKompV and BayKompV have none | none in the ordinance |
| **Baden-Württemberg** (R) | LUBW: *Arten, Biotope, Landschaft – Schlüssel zum Erfassen, Beschreiben, Bewerten*; valuation: *Ökokonto-Verordnung (ÖKVO)* 2010, Anlage 2 (Ökopunkte per m²) | numeric `NN.NN` (11–13 waters, 21–23 morphological, 31–37 open land, 41–45 woody, 51–59 forests, 60 settlement and infrastructure) | not known |
| **Sachsen** (R) | Biotoptypen- und Landnutzungskartierung (BTLNK) from CIR aerial images; *Handlungsempfehlung zur Bewertung und Bilanzierung von Eingriffen im Freistaat Sachsen*. Site sections exist (V: links `natur.sachsen.de/biotope-und-biotopverbund-7720.html`, `…/eingriffsregelung-handlungsempfehlung-8109.html`), page text not retrievable. | numeric hierarchical | BTLNK is published as a coloured map service |
| **Hamburg** (R) | *Kartieranleitung und Biotoptypenschlüssel für die Biotopkartierung in Hamburg*; Biotopkataster with value classes. Old URL `hamburg.de/biotopkartierung/` → 404 (V). | letter codes close to the Lower Saxony key | not known |

Why this matters for the library: the code families (BfN dotted numeric; Bavarian letter + digits; Berlin 5–8-digit numeric; Lower-Saxony-type letter codes) cannot be converted by pattern; crosswalks must be explicit per element. Berlin's data model (main + additional + accompanying biotope, protection flag 0/1/2, point/line/area rules) is a good template for attribute design.

---

## 5. Legally protected biotopes

### 5.1 § 30 BNatSchG (V\* – wording extracted from gesetze-im-internet.de, <https://www.gesetze-im-internet.de/bnatschg_2009/__30.html>)

Abs. 2 Satz 1: "Handlungen, die zu einer Zerstörung oder einer sonstigen erheblichen Beeinträchtigung folgender Biotope führen können, sind verboten:"

1. "natürliche oder naturnahe Bereiche fließender und stehender Binnengewässer einschließlich ihrer Ufer und der dazugehörigen uferbegleitenden natürlichen oder naturnahen Vegetation sowie ihrer natürlichen oder naturnahen Verlandungsbereiche, Altarme und regelmäßig überschwemmten Bereiche"
2. "Moore, Sümpfe, Röhrichte, Großseggenrieder, seggen- und binsenreiche Nasswiesen, Quellbereiche, Binnenlandsalzstellen"
3. "offene Binnendünen, offene natürliche Block-, Schutt- und Geröllhalden, Lehm- und Lösswände, Zwergstrauch-, Ginster- und Wacholderheiden, Borstgrasrasen, Trockenrasen, Schwermetallrasen, Wälder und Gebüsche trockenwarmer Standorte"
4. "Bruch-, Sumpf- und Auenwälder, Schlucht-, Blockhalden- und Hangschuttwälder, subalpine Lärchen- und Lärchen-Arvenwälder"
5. "offene Felsbildungen, Höhlen sowie naturnahe Stollen, alpine Rasen sowie Schneetälchen und Krummholzgebüsche"
6. "Fels- und Steilküsten, Küstendünen und Strandwälle, Strandseen, Boddengewässer mit Verlandungsbereichen, Salzwiesen und Wattflächen im Küstenbereich, Seegraswiesen und sonstige marine Makrophytenbestände, Riffe, sublitorale Sandbänke, Schlickgründe mit bohrender Bodenmegafauna sowie artenreiche Kies-, Grobsand- und Schillgründe im Meeres- und Küstenbereich"
7. "**magere Flachland-Mähwiesen und Berg-Mähwiesen nach Anhang I der Richtlinie 92/43/EWG, Streuobstwiesen, Steinriegel und Trockenmauern**"

Satz 2–4: "Die Verbote des Satzes 1 gelten auch für weitere von den Ländern gesetzlich geschützte Biotope. Satz 1 Nummer 5 gilt nicht für genutzte Höhlen- und Stollenbereiche sowie für Maßnahmen zur Verkehrssicherung von Höhlen und naturnahen Stollen. Satz 1 Nummer 7 gilt nicht für die Unterhaltung von Funktionsgrünland auf Flugbetriebsflächen." Abs. 8: existing Länder rules on the biotopes of Nr. 7 remain unaffected.

The 2022 additions (R for the date and act: in force 1 March 2022, *Gesetz zum Schutz der Insektenvielfalt* of 18 Aug 2021) are Nr. 7 as a whole and, in Nr. 5, "Höhlen sowie naturnahe Stollen".

### 5.2 Bavaria – Art. 23 Abs. 1 BayNatSchG (V\*, <https://www.gesetze-bayern.de/Content/Document/BayNatSchG-23>; portal: "Text gilt ab: 01.04.2026", law last amended by § 15 of the act of 26 March 2026, GVBl. S. 75 – what that act changed in Art. 23 was not determined)

"Gesetzlich geschützte Biotope im Sinn des § 30 Abs. 2 Satz 2 BNatSchG sind auch
1. Landröhrichte, Pfeifengraswiesen,
2. Moorwälder,
3. wärmeliebende Säume,
4. Magerrasen, Felsheiden,
5. alpine Hochstaudenfluren,
6. extensiv genutzte Obstbaumwiesen oder -weiden aus hochstämmigen Obstbäumen mit einer Fläche ab 2.500 Quadratmetern (Streuobstbestände) mit Ausnahme von Bäumen, die weniger als 50 Meter vom nächstgelegenen Wohngebäude oder Hofgebäude entfernt sind und
7. arten- und strukturreiches Dauergrünland.

Die Staatsregierung wird ermächtigt, durch Rechtsverordnung Einzelheiten zur fachlichen Abgrenzung der in Satz 1 Nr. 6 und 7 genannten Biotope zu bestimmen."

Further (V\*, summarised): Abs. 2 exemptions (e.g. biotopes arising on land covered by a Bebauungsplan, or during agri-environment contracts), Abs. 3–4 exceptions, Abs. 5 meadow-bird habitats, Abs. 6 EIA duty for intensification.

**Art. 16 Abs. 1 BayNatSchG** (V\*, beginning only): "Es ist verboten, in der freien Natur 1. Hecken, lebende Zäune, Feldgehölze oder -gebüsche einschließlich Ufergehölze …" – this is the "§ 39 / Art. 16" protection column of the mapping key (hedges, field copses, etc.).

### 5.3 Which catalog elements can be legally protected (synthesis of sections 3 and 5)

| Element | Protection basis | Bavarian BK type |
|---|---|---|
| Species-rich hay meadow (LRT 6510 / 6520) | § 30 Abs. 2 Nr. 7; Art. 23 Nr. 7 | GU651E, GU651L, GY6520 |
| Orchard meadow (tall-stem, ≥ 2 500 m², > 50 m from dwellings) | § 30 Nr. 7; Art. 23 Nr. 6 | BS |
| Dry-stone wall, stone ridge | § 30 Nr. 7 | (UR, SG/ST) |
| Dry / sand grassland, heath, open inland dune | § 30 Nr. 3; Art. 23 Nr. 4 | GT, GL, GO, GC, SD |
| Reeds, tall sedges, wet meadows, fens, springs | § 30 Nr. 2; Art. 23 Nr. 1 | VH, VK, VC, GR, GG, GN, MF, QF |
| Near-natural waters with banks and silting zones | § 30 Nr. 1 | FW, SU, VU, SI |
| Wet tall-forb stands, thermophilous fringes | § 30 (as part of Nr. 1/2); Art. 23 Nr. 3 | GH, GW |
| Alluvial, swamp, carr, ravine forests; dry-warm woods and scrub | § 30 Nr. 3, 4; Art. 23 Nr. 2 | WA, WQ, WB, WJ, WÖ, WD, WG, MW |
| Hedges, field copses, natural scrub, old trees, parks with old trees, ruderal vegetation | **not** § 30; partly § 39 (5) BNatSchG / Art. 16 BayNatSchG | WH, WO, WX, WI, UA, UE, UP, UK, RF, GB, GX, ST |

---

## 6. FFH Annex I habitat types relevant around Central European cities

**Source (V):** BfN, "Liste der in Deutschland vorkommenden Lebensraumtypen der FFH-Richtlinie" (names as in Annex I, version of 13.05.2013, Directive 2013/17/EU; PDF dated 25.09.2018). <https://www.bfn.de/sites/default/files/2022-05/5_lebensraumtypenliste_20180925_pac.pdf> – 93 of the 231 EU habitat types occur in Germany (V\*, BfN page).

| Code | Name in Annex I (German) | BfN short name | Bavarian BNT ↔ BK sub-type (V, from the Biotopwertliste) |
|---|---|---|---|
| 2310 | Trockene Sandheiden mit Calluna und Genista [Dünen im Binnenland] | Sandheiden mit Besenheide und Ginster auf Binnendünen | Z111/Z112 ↔ GC2310 |
| 2330 | Dünen mit offenen Grasflächen mit Corynephorus und Agrostis [Dünen im Binnenland] | Offene Grasflächen mit Silbergras und Straußgras auf Binnendünen | G313 ↔ GL2330; O422 ↔ SD2330 |
| 3130 | Oligo- bis mesotrophe stehende Gewässer mit Vegetation der Littorelletea uniflorae und/oder der Isoeto-Nanojuncetea | Nährstoffarme bis mäßig nährstoffreiche Stillgewässer mit Strandlings- oder Zwergbinsen-Gesellschaften | S122/S123, R21, R321 |
| 3140 | Oligo- bis mesotrophe kalkhaltige Gewässer mit benthischer Vegetation aus Armleuchteralgen | … kalkhaltige Stillgewässer mit Armleuchteralgen | S122/S123 |
| **3150** | Natürliche eutrophe Seen mit einer Vegetation des Magnopotamions oder Hydrocharitions | Natürliche und naturnahe nährstoffreiche Stillgewässer mit Laichkraut- oder Froschbiss-Gesellschaften | S132/S133 ↔ SU3150, VU3150; R121–R123, R22, R322 |
| 3160 | Dystrophe Seen und Teiche | Dystrophe Stillgewässer | S111/S112 |
| **3260** | Flüsse der planaren bis montanen Stufe mit Vegetation des Ranunculion fluitantis und des Callitricho-Batrachion | Fließgewässer mit flutender Wasservegetation | F13–F15 ↔ FW3260 / LR3260; F212 |
| 3270 | Flüsse mit Schlammbänken mit Vegetation des Chenopodion rubri p.p. und des Bidention p.p. | Flüsse mit Gänsefuß- und Zweizahn-Gesellschaften auf Schlammbänken | F13–F15, F31/F32 |
| 4030 | Trockene europäische Heiden | Trockene Heiden | Z111/Z112, Z12 ↔ GC4030 |
| 40A0\* | Subkontinentale peripannonische Gebüsche | – | B111 ↔ WD40A0\* |
| 5130 | Formationen von Juniperus communis auf Kalkheiden und -rasen | Wacholderbestände auf Zwergstrauchheiden oder Kalkrasen | G312 ↔ GT5130 |
| 6110\* | Lückige basophile oder Kalk-Pionierrasen (Alysso-Sedion albi) | Basenreiche oder Kalk-Pionierrasen | O112 ↔ FH6110\* |
| 6120\* | Trockene, kalkreiche Sandrasen | Subkontinentale basenreiche Sandrasen | G313 ↔ GL6120\* |
| **6210(\*)** | Naturnahe Kalk-Trockenrasen und deren Verbuschungsstadien (Festuco-Brometalia) (\* besondere Bestände mit bemerkenswerten Orchideen) | Kalk-(Halb-)Trockenrasen und ihre Verbuschungsstadien | G312, K131, B442 ↔ GT6210 / GT621P |
| 6230\* | Artenreiche montane Borstgrasrasen (und submontan auf dem europäischen Festland) auf Silikatböden | Artenreiche Borstgrasrasen | G331/G332 ↔ GO6230\* |
| 6240\* | Subpannonische Steppen-Trockenrasen | Steppenrasen | G311 ↔ GT6240\* |
| **6410** | Pfeifengraswiesen auf kalkreichem Boden, torfigen und tonig-schluffigen Böden (Molinion caeruleae) | Pfeifengraswiesen | G321/G322 ↔ GP6410 |
| **6430** | Feuchte Hochstaudenfluren der planaren und montanen bis alpinen Stufe | Feuchte Hochstaudenfluren | K123/K133 ↔ GH6430 |
| 6440 | Brenndolden-Auenwiesen (Cnidion dubii) | Brenndolden-Auenwiesen | G24 ↔ GA6440 |
| **6510** | Magere Flachland-Mähwiesen (Alopecurus pratensis, Sanguisorba officinalis) | Magere Flachland-Mähwiesen | G212 ↔ GU651L; G214 ↔ GU651E |
| **6520** | Berg-Mähwiesen | Berg-Mähwiesen | G214 ↔ GY6520 |
| 7220\* | Kalktuffquellen (Cratoneurion) | Kalktuffquellen | Q221 ↔ QF7220\* |
| 7230 | Kalkreiche Niedermoore | Kalkreiche Niedermoore | M411/M412 ↔ MF7230 |
| 8210 / 8220 / 8230 | Kalkfelsen / Silikatfelsen mit Felsspaltenvegetation / Silikatfelsen mit Pioniervegetation des Sedo-Scleranthion oder des Sedo albi-Veronicion dillenii | – | O112 ↔ FH82xx |
| 8310 | Nicht touristisch erschlossene Höhlen | – | H1 ↔ LR8310 |
| **9110** | Hainsimsen-Buchenwald (Luzulo-Fagetum) | Hainsimsen-Buchenwälder | L231–L233 |
| **9130** | Waldmeister-Buchenwald (Asperulo-Fagetum) | Waldmeister-Buchenwälder | L241–L243 (N321–N323) |
| 9150 | Mitteleuropäischer Orchideen-Kalk-Buchenwald (Cephalanthero-Fagion) | Orchideen-Kalk-Buchenwälder | L131–L133 ↔ WK |
| **9160** | Subatlantischer oder mitteleuropäischer Stieleichenwald oder Eichen-Hainbuchenwald (Carpinion betuli) [Stellario-Carpinetum] | Sternmieren-Eichen-Hainbuchenwälder | L211–L213 |
| **9170** | Labkraut-Eichen-Hainbuchenwald Galio-Carpinetum | Labkraut-Eichen-Hainbuchenwälder | L111–L113 ↔ WW |
| 9180\* | Schlucht- und Hangmischwälder Tilio-Acerion | Schlucht- und Hangmischwälder | L311–L323 ↔ WJ, WÖ |
| 9190 | Alte bodensaure Eichenwälder auf Sandebenen mit Quercus robur | Alte bodensaure Eichenwälder auf Sandböden mit Stieleiche | L121–L123, L221–L223 |
| 91D0\* | Moorwälder | Moorwälder | L411–L413, N511–N533 ↔ MW91D0\* |
| **91E0\*** | Auen-Wälder mit Alnus glutinosa und Fraxinus excelsior (Alno-Padion, Alnion incanae, Salicion albae) | Erlen-Eschen- und Weichholzauenwälder | L511–L522, L431–L433 (WQ91E0\*), B114 ↔ WA91E0\* |
| **91F0** | Hartholzauewälder mit Quercus robur, Ulmus laevis, Ulmus minor, Fraxinus excelsior oder Fraxinus angustifolia (Ulmenion minoris) | Hartholzauenwälder | L531–L533 ↔ WA91F0 |
| 91G0\* | Pannonische Wälder mit Quercus petraea und Carpinus betulus [Tilio-Carpinetum] | Subkontinentale bis pannonische Eichen-Hainbuchenwälder | – |
| 91T0 / 91U0 | Mitteleuropäische Flechten-Kiefernwälder / Kiefernwälder der sarmatischen Steppe | – | N111–N123 |

Correction to the brief: 6210 is printed "6210\*" in the BfN list because only orchid-rich stands are priority; 9160 and 9170 names verified as above.

---

## 7. BfN "Planzeichen für die Landschaftsplanung"

### 7.1 Products, availability, licence

| Item | Details | Status |
|---|---|---|
| R+D project | "Planzeichen für die Landschaftsplanung", BfN; run time 01.07.2011 – 31.12.2012; FKZ 3511 82 0900 (catalogue) and 3516 82 2100 (GIS implementation). <https://www.bfn.de/projektsteckbriefe/planzeichen-fuer-die-landschaftsplanung> | V\* |
| BfN-Skripten 461/1 | Hoheisel, Mengel, Heiland, Mertelmeyer, Meurer & Rittel (2017): *Planzeichen für die Landschaftsplanung – Fachlich-methodische Grundlagen* | V\* (not read) |
| **BfN-Skripten 461/2** | same authors (2017): *Planzeichen für die Landschaftsplanung – Planzeichenkatalog*, 131 pp., ISBN 978-3-89624-198-6, DOI 10.19217/skr4612. PDF: <https://bfn.bsz-bw.de/frontdoor/deliver/index/docId/270/file/Skript461_2.pdf> | **V** (read) |
| BfN-Skripten 486 | Hachmann, Cassar-Pieper, Schründer & Lipski (IP SYSCON, 2018): *Planzeichen für die Landschaftsplanung – Dokumentation zur Anwendung in geografischen Informationssystemen*, DOI 10.19217/skr486. PDF: <https://bfn.bsz-bw.de/frontdoor/deliver/index/docId/206/file/Skript_486.pdf> | **V** (read) |
| BfN-Skripten 266 | earlier study on the systematics of plan symbols | V\* |
| GIS package | `GIS_Planzeichen_Download.zip` via the BfN project page; contents: **ArcGIS** `PlanZ_LP_BfN.style`, map/layer packages `Planzeichen-Vorlagen10.2_Landschaftsplan_BfN.mpk/.lpk`; **QGIS** `PlanZ_QGIS_LP_BfN.xml` + SVG archive (`PlanZ_SVG_LP_BfN.ZIP` / `BfN_LP_PlanZ_SVG.ZIP`); **WMS/SLD** `PlanZ_Punkte_LP_BfN.sld`, `PlanZ_Linien_LP_BfN.sld`, `PlanZ_Flaechen_LP_BfN.sld`; **fonts** `PlanZ_LP_BfN.ttf`, `PlanZ_2_LP_BfN.ttf` | V (486) / V\* (web page) |
| Licence | Repository record of 461/2: **CC BY-ND 4.0** (V\*). Imprint of 486: "Das Werk einschließlich aller seiner Teile ist urheberrechtlich geschützt. … Nachdruck, auch in Auszügen, nur mit Genehmigung des BfN." (V). GIS package: "kostenfreie Nutzung zum Download", no explicit licence text found (V\*). | mixed |
| XPlanung | BfN states that the XPlanung standard has been binding for landscape-planning procedures since February 2023 and documents landscape-planning extensions in BfN-Schriften 646 (2023) (V\*, <https://www.bfn.de/digitalisierung-der-landschaftsplanung>) | V\* |

**Legal character:** recommendation of a federal R+D project for landscape plans (örtliche und überörtliche Landschaftsplanung). It is not a statutory symbology like the PlanZV for Bauleitpläne. The QGIS files were produced with QGIS 2.18 (V), so the XML/SVG set is old but usable as reference.

**Consequence for an open library:** colour values, line widths and the logic are facts and can be cited. The BfN SVG/TTF symbol files themselves should **not** be bundled or modified without clarifying the licence (ND clause / all-rights-reserved imprint); draw own symbols that follow the same conventions.

### 7.2 What the catalogue contains (V, table of contents of 461/2)

- **Kartensatz I – Bestand, Bewertung, Konfliktanalyse** per Schutzgut: 1 Klima und Luft · 2 Wasser · 3 Boden und Geotope · 4 Biotoptypengruppen als räumliche Kulisse für die Karte "Tiere und Pflanzen" (und Kartensatz III) · 5 Tiere und Pflanzen · 6 Biotoptypengruppen als räumliche Kulisse für die Karten "Lebensräume und Biotope" und "Landschaft" · 7 Lebensräume und Biotope · 8 Landschaft. Each with "Bestand und Bewertung" and "Beeinträchtigungen und Gefährdungen".
- **Kartensatz II – Abgestimmtes Zielkonzept**: 1.1 Leitbildräume · 1.2 Zielkonforme Flächen und Einzelelemente – Erhaltung und Sicherung · 1.3 Bedeutsame Flächen und Räume mit Entwicklungspotenzial · 1.4 Flächen und Räume mit besonderen Funktionen und/oder Empfindlichkeiten · 1.5 Weitere Flächen und Räume: umzusetzende Grundanforderungen · 1.6 Physische Maßnahmen.
- **Kartensatz III – Vorbereitung der instrumentellen Umsetzung**: 1.1 Naturschutzrechtliche Instrumente (Schutzgebiete; § 30-Biotope und FFH-LRT; streng geschützte Arten; Biotoptypengruppen) · 1.2 Gute fachliche Praxis, Förderprogramme und Kompensationsmaßnahmen; in 486 additionally sheets for addressees of Raumordnung and Bauleitplanung.
- The groups are the **Biotoptypengruppen of Finck et al. 2017** ("Der zweistellige Code hinter der jeweiligen Überschrift steht für den Schlüssel der Biotoptypengruppe gemäß Finck et al. 2017", 486, V).

### 7.3 System rules (V)

| Rule | Content |
|---|---|
| Two value series | **Low–moderate value / backdrop**: light tint, "Flächige Darstellung", **no outline** (chapters 4 and 6). **High–outstanding value**: saturated colour, "Flächige Darstellung mit Kontur", **Kontur schwarz, 2 pt** (chapter 7.1.1, every entry labelled "(hohe bis hervorragende Bedeutung)"). |
| Small objects | below the size threshold a **point symbol** replaces the area: "Punktuelle Darstellung mit Kontur", **Größe 16 pt**. Thresholds: grassland and standing waters **< 1 ha**; protected-area categories **< 5 ha**; hazards and hatched themes **> 5 ha** as areas. |
| Overlays on the group colour | **wet / moist sites** = "Schraffur aus horizontalen Linien, gestrichelt, versetzt" in water blue, 0,5 pt, spacing 2 pt · **fallow (Brache)** = "Schraffur aus vertikalen Linien, gestrichelt" in brown · **orchards** = red dot grid 2 pt / 3 pt spacing · **vineyards** = violet dot grid · **hop and woody plantations** = green dot grid · **rock / raw ground** = grey with dark dashed offset lines · **extraction sites** = border line of filled triangles, 32 pt. |
| Trees | point symbols with outline for single trees, tree groups, tree rows (SVG/EMF supplied); saturated series: fill RAL 120 60 63, outline RAL 140 40 50, size 4 pt. |
| Springs, caves | point symbols ("Qu" in a blue circle; cave pictogram), SVG/EMF. |
| Running waters | lines in the water colour; width by water-body order: Bundeswasserstraße 3,5 pt with cross ticks (2 mm) · Strom/Fluss (Gewässer I. Ordnung) 3 pt · Fluss (II. Ordnung) 2 pt · Bach (II. Ordnung) 1,5 pt · Bach (III. Ordnung) 1 pt · ephemeral = dashed. |
| Cartographic conventions (486) | 1 pt = 0,35 mm; standard point symbol 16 pt; standard stroke in point symbols 1 pt; minimum stroke for area outlines 0,5 pt; simple outlines up to 2 pt centred on the boundary, complex outlines completely inside; demo reference scale 1 : 20 000. |
| Legally protected biotopes | no own colour: "Sofern es sich um einen Biotop unter besonderem gesetzlichem Schutz handelt, ist dieser manuell mit Biotoptyp, Schutzstatus und/oder Gebietsnummer zu beschriften." Kartensatz III: symbology as the saturated series, **label** black (RGB 0/0/0), Arial 8 pt, halo 2.0 white for *existing*; grey label RGB 104/104/104 with halo RGB 204/204/204 for *potential*. Same logic for FFH habitat types. |
| Existing vs. target vs. proposal | **Target-conform areas** (Kartensatz II): light series with **50 % transparency**. **Areas with development potential**: line hatching "mit assoziativer Farbgebung und Beschriftung" (examples: Auen blue horizontal, Wälder green vertical, Grünlandtäler yellow-green horizontal, extensive Streuobstbestände orange-red horizontal; no numeric values). **Physical measures**: "sind die entsprechenden Signaturen jeweils individuell zu entwickeln" – the catalogue defines **no measure symbols**. **Existing vs. proposed instruments** (Kartensatz III): same motif **with contour = vorhanden**, **without contour = vorgeschlagen** (funding programmes: orange dots RGB 230/152/0; compensation areas: violet rectangles RGB 112/68/137). Protected areas: four states per category – *Beibehaltung* solid double line · *Qualifizierung* dashed with yellow second colour RGB 242/252/0 · *Erweiterung* dashed · *Rücknahme* dashed inner line (bird sanctuaries: red-violet RGB 209/58/120). |
| GIS caveat (486) | multi-layer fills (point grids, hatches) are not rendered identically in all systems; point patterns get lost in ArcGIS Server feature services; SLD versions are simplified. |

### 7.4 Colour values – pastel "Kulisse" series (V; catalogue chapter 4.1.1, printed pp. 49–56; hex computed from the printed RGB)

| No. | Biotoptypengruppe / element | RAL Design | RGB | Hex | Overlay / remark |
|---|---|---|---|---|---|
| 4.1.1.1 | Gewässer der Nord- und Ostsee | 210 90 20 | 210/246/255 | #D2F6FF | |
| 4.1.1.2 | Watt der Nordsee | 110 90 20 | 228/232/200 | #E4E8C8 | |
| 4.1.1.3 | Sande und Strände | 100 90 40 | 255/255/181 | #FFFFB5 | |
| 4.1.1.4 | Dünen | 095 90 50 | 255/226/138 | #FFE28A | |
| 4.1.1.5 | **Stehende Gewässer** | 240 80 20 | 197/233/255 | #C5E9FF | outline 0,5 pt RAL 280 20 30 = 22/37/81 (#162551) |
| 4.1.1.6 | **Felsen, Block- und Schutthalden, Sand-/Lehm- und Lösswände, vegetationsarme Flächen** | 000 90 00 | 226/226/226 | #E2E2E2 | horizontal dashed offset lines RAL 080 50 05 = 122/119/112 (#7A7770); 0,5 pt; 2 pt |
| 4.1.1.7 | Abbaubereiche | 080 50 05 | 122/119/112 | #7A7770 | border of filled triangles, 32 pt |
| 4.1.1.8 | **Acker** | 085 90 30 | 242/223/176 | #F2DFB0 | |
| 4.1.1.9 | Ackerbrache | 085 90 30 | 242/223/176 | #F2DFB0 | vertical dashed lines RAL 060 50 30 = 158/109/79 (#9E6D4F); 0,5 pt; 2 pt |
| 4.1.1.10 | Obstkultur auf Acker | 085 90 30 | 242/223/176 | #F2DFB0 | dot grid RAL 040 60 60 = 236/109/83 (#EC6D53); 2 pt; 3 pt |
| 4.1.1.11 | **Trockenrasen und Gebirgsrasen** | 100 90 50 | 255/255/161 | #FFFFA1 | |
| 4.1.1.12 | **Grünland** | 110 90 40 | 210/240/152 | #D2F098 | (printed "210/240/15" on p. 50 – truncated; the three following entries print 210/240/152) |
| 4.1.1.13 | Grünland auf nassen bis feuchten Standorten | 110 90 40 | 210/240/152 | #D2F098 | horizontal dashed offset lines RAL 250 80 20 = 166/202/231 (#A6CAE7) |
| 4.1.1.14 | Obstkultur auf Grünland | 110 90 40 | 210/240/152 | #D2F098 | dot grid 236/109/83 |
| 4.1.1.15 | Grünlandbrache | 110 90 40 | 210/240/152 | #D2F098 | vertical dashed lines 158/109/79 |
| 4.1.1.16 | Moore | 100 80 30 | 209/203/148 | #D1CB94 | horizontal dashed lines 166/202/231 |
| 4.1.1.17 | **Großseggenried und Röhricht** | 070 80 60 | 255/175/94 | #FFAF5E | horizontal dashed lines 166/202/231 |
| 4.1.1.18 | **Säume und Staudenfluren** | 310 80 15 | 221/192/236 | #DDC0EC | |
| 4.1.1.19 | Zwergstrauchheiden | 010 80 20 | 255/181/194 | #FFB5C2 | |
| 4.1.1.20 | **Feldgehölze, Gebüsche, Hecken** | 120 80 60 | 190/245/131 | #BEF583 | |
| 4.1.1.21 | Hopfenkulturen und Gehölzplantagen | 085 90 30 | 242/223/176 | #F2DFB0 | dot grid RAL 130 60 60 = 76/161/62 (#4CA13E) |
| 4.1.1.22 | Rebkultur | 085 90 30 | 242/223/176 | #F2DFB0 | dot grid RAL 310 60 35 = 169/131/190 (#A983BE) |
| 4.1.1.23 | Rebbrache | 085 90 30 | 242/223/176 | #F2DFB0 | violet dots + brown vertical lines |
| 4.1.1.24 | **Laub(misch)wälder und -forste** | printed 110 90 40 | printed 210/240/152 | – | ⚠ identical to Grünland as printed, but the swatch in the PDF is a visibly darker green → probable editorial error in the catalogue; take the value from the QGIS/ArcGIS style file instead |
| 4.1.1.25 | Laub(misch)wälder und -forste auf feuchten bis nassen Standorten | printed 110 90 40 | printed 210/240/152 | – | ⚠ same; + horizontal dashed lines 166/202/231 |
| 4.1.1.26 | **Nadel(misch)wälder und -forste** | 130 70 40 | 135/186/120 | #87BA78 | |
| 4.1.1.27 | Nadel(misch)wälder und -forste auf feuchten bis nassen Standorten | 130 70 40 | 135/186/120 | #87BA78 | + horizontal dashed lines |
| 4.1.1.28 | **Siedlungsflächen** | 050 80 20 | 235/193/176 | #EBC1B0 | |
| 4.1.1.29 | **Industrie-/Gewerbeflächen, Verkehrsanlagen und Plätze, Deponien und Rieselfelder** | 050 80 10 | 230/206/197 | #E6CEC5 | |
| 4.1.1.30 | **Grünflächen und weitere Freiflächen im Siedlungsraum** | 140 80 40 | 171/246/180 | #ABF6B4 | |
| 4.1.1.31–37 | Running waters (Bundeswasserstraße … ephemerer Bach III. Ordnung) | 240 80 20 | 197/233/255 | #C5E9FF | widths 3,5 / 3 / 2 / 1,5 / 1,5 dashed / 1 / 1 dashed pt |
| 4.1.1.38 | Fels- und Steilküsten | 110 80 20 | 197/201/166 | #C5C9A6 | contour line with raster band; 4 pt; 8 pt |
| 4.1.1.39–41 | Einzelbäume, Baumgruppen, Baumreihen · Höhle · Quelle ("geringe bis mäßige Bedeutung") | – | – | – | point symbols (SVG/EMF) |

### 7.5 Colour values – saturated series "hohe bis hervorragende Bedeutung" (V; catalogue chapter 7.1.1, printed pp. 77–92; all areas with black 2 pt outline)

| No. | Biotoptypengruppe / element | RAL Design | RGB | Hex | Overlay |
|---|---|---|---|---|---|
| 7.1.1.1 | Gewässer der Nord- und Ostsee | 250 60 20 | 105/144/175 | #6990AF | |
| 7.1.1.3 | Watt der Nordsee | 110 50 20 | 118/122/89 | #767A59 | |
| 7.1.1.5 | Sande und Strände | 095 90 59 | 247/228/58 | #F7E43A | |
| 7.1.1.7 | Dünen | 085 80 85 | 245/193/20 | #F5C114 | |
| 7.1.1.9 | **Stehende Gewässer > 1 ha** | 250 60 30 | 82/151/192 | #5297C0 | outline RAL 5026 = 22/37/81, 2 pt; < 1 ha: point symbol "K" |
| 7.1.1.11 | **Felsen, Block- und Schutthalden, …, vegetationsarme Flächen** | 000 65 00 | 158/158/158 | #9E9E9E | dashed lines RAL 080 30 05 = 73/71/65 (#494741) |
| 7.1.1.13 | Abbaubereiche | 080 30 05 | 73/71/65 | #494741 | triangle border 32 pt |
| 7.1.1.15 | **Acker** | 080 60 60 | 186/137/37 | #BA8925 | |
| 7.1.1.17 | Ackerbrache | 080 60 60 | 186/137/37 | #BA8925 | vertical dashed lines RAL 060 30 27 = 100/63/37 (#643F25) |
| 7.1.1.19 | Obstkultur auf Acker | 080 60 60 | 186/137/37 | #BA8925 | dot grid RAL 040 40 67 = 182/48/30 (#B6301E); point-symbol variant prints base RAL 080 80 60 = 246/191/90 |
| 7.1.1.21 | **Trockenrasen und Gebirgsrasen** | 090 60 50 | 167/144/56 | #A79038 | |
| 7.1.1.23 | **Grünland** | 110 60 65 | 126/155/25 | #7E9B19 | |
| 7.1.1.25 | Grünland auf nassen bis feuchten Standorten | 110 60 65 | 126/155/25 | #7E9B19 | lines RAL 250 60 30 = 82/151/192 |
| 7.1.1.27 | Obstkultur auf Grünland | 110 60 65 | 126/155/25 | #7E9B19 | dot grid 182/48/30 |
| 7.1.1.29 | Grünlandbrache | 110 60 65 | 126/155/25 | #7E9B19 | vertical dashed lines 100/63/37 |
| 7.1.1.31 | Moore | 100 40 30 | 99/96/46 | #63602E | lines 82/151/192 |
| 7.1.1.33 | **Großseggenried und Röhricht** | 060 50 70 | 193/93/12 | #C15D0C | lines 82/151/192 |
| 7.1.1.35 | **Säume und Staudenfluren** | 310 40 25 | 111/85/125 | #6F557D | |
| 7.1.1.37 | Zwergstrauchheiden | 010 40 30 | 145/75/88 | #914B58 | |
| 7.1.1.39 | **Feldgehölze, Gebüsche, Hecken** | 120 60 63 | 102/159/43 | #669F2B | |
| 7.1.1.41 | Hopfenkulturen und Gehölzplantagen | 080 60 60 | 186/137/37 | #BA8925 | dot grid RAL 140 40 50 = 0/109/39 (#006D27) |
| 7.1.1.43 | Rebkultur | 080 60 60 | 186/137/37 | #BA8925 | dot grid RAL 310 30 35 = 91/58/111 (#5B3A6F) |
| 7.1.1.45 | Rebbrache | 080 60 60 | 186/137/37 | #BA8925 | violet dots + lines 100/63/37 |
| 7.1.1.47 | **Laub(misch)wälder und -forste** | 120 40 40 | 70/103/37 | #466725 | |
| 7.1.1.49 | – auf feuchten bis nassen Standorten | 120 40 40 | 70/103/37 | #466725 | lines 82/151/192 |
| 7.1.1.51 | **Nadel(misch)wälder und -forste** | 140 30 40 | 0/82/30 | #00521E | |
| 7.1.1.53 | – auf feuchten bis nassen Standorten | 140 30 40 | 0/82/30 | #00521E | lines 82/151/192 |
| 7.1.1.55 | **Siedlungsflächen** | 030 50 50 | 199/86/81 | #C75651 | |
| 7.1.1.57 | **Industrie-/Gewerbeflächen, Verkehrsanlagen und Plätze, Deponien und Rieselfelder** | 050 40 10 | 110/91/82 | #6E5B52 | |
| 7.1.1.59 | **Grünflächen und weitere Freiflächen im Siedlungsraum** | 140 50 40 | 59/132/75 | #3B844B | |
| 7.1.1.61 | Fels- und Steilküsten | 110 50 20 | 118/122/89 | #767A59 | contour with raster band |
| 7.1.1.63 | **Einzelbäume, Baumgruppen, Baumreihen** | 120 60 63 | 102/159/43 | #669F2B | point symbols, outline RAL 140 40 50 = 0/109/39, size 4 pt |
| 7.1.1.66–72 | Running waters | 250 60 30 | 82/151/192 | #5297C0 | widths as in 7.3 |

Additional colours of Kartensatz III (V): Nationalpark outline 38/115/0 + 176/146/0 · Biosphärenreservat 38/115/0 + 0/158/173 · Naturpark 38/115/0 + 56/168/0 · Nationales Naturmonument 64/133/52 + 169/144/33 · Vogelschutzgebiet 92/56/117 (hatch 45°) · flood zones: horizontal line hatch 0/92/230, 1 pt, separation 7 pt · bog sites: diagonal hatch 112/125/56 · high groundwater: vertical hatch 0/92/230 · erosion-prone soils: diagonal hatch 108/59/39 (wind = left-leaning, water = right-leaning).

### 7.6 Hue families to respect (derived from 7.4/7.5)

| Family | Hue | Notes for a pastel style |
|---|---|---|
| Waters | blue | standing waters with a dark-blue outline even in the light series |
| Grassland (group 34 incl. `34.09` lawns, meadows) | **yellow-green** | lawn, meadow and species-rich meadow belong to the same hue; differentiate by lightness/saturation, outline and motif |
| Dry / nutrient-poor grassland | **pale yellow → ochre** | clearly separated from mesic grassland |
| Settlement green (parks, gardens, cemeteries – group 51) | **mint / bluish green** | deliberately different from agricultural grassland |
| Shrubs, hedges, copses, single trees | **fresh mid green** | trees as point symbols |
| Deciduous / coniferous forest | **dark green / blue-dark green** | conifer darker and cooler |
| Reeds and tall sedges | **orange** with blue water dashes | counter-intuitive for non-planners; the blue dashes carry the "wet" meaning |
| Bogs | olive-brown with blue dashes | |
| Fringes, tall-forb and ruderal vegetation (group 39) | **violet** | |
| Heath | pink / rose | |
| Arable | beige → ochre | orchards/vineyards/plantations as dot grids on the arable colour |
| Rock, raw soil, sparsely vegetated sand/gravel | **grey with dashed lines** | |
| Settlement areas (built) | **salmon → red** | |
| Industry, traffic areas, squares, landfills | **grey-brown / pale pink-grey** | |

---

## 8. Colour conventions actually used in official biotope / land-use maps

### 8.1 Bavaria – LfU WMS "Biotopkartierung Bayern" (V)

- GetCapabilities: <https://www.lfu.bayern.de/gdi/wms/natur/biotopkartierung?REQUEST=GetCapabilities&SERVICE=WMS> – licence **CC BY 4.0**, attribution "Bayerisches Landesamt für Umwelt, www.lfu.bayern.de"; "Es gelten keine Zugriffsbeschränkungen" (V\*).
- Layers: `bio_fbk` Biotopkartierung Flachland · `bio_sbk` Biotopkartierung Stadt · `bio_abk` Biotopkartierung Alpen (V\*). Munich, Nuremberg etc. are therefore covered by the state's *Stadtbiotopkartierung* layer.
- Legend "§ 30-Anteile, Streuobst" (identical for `bio_sbk` and `bio_fbk`; RGB **sampled from the official legend PNG**, V):

| Class | Fill RGB | Hex | Outline |
|---|---|---|---|
| mit geschützten Anteilen | 217/126/176 | #D97EB0 | 238/90/199 (#EE5AC7) |
| möglicherweise mit geschützten Anteilen | 238/202/207 | #EECACF | 238/90/199 |
| ohne geschützte Anteile | 252/235/253 | #FCEBFD | 238/90/199 |
| + "(inkl. geschütztes Streuobst)" | black dots 0/0/0 on the class fill | | |
| + "(inkl. möglicherweise geschütztes Streuobst)" | grey dots 130/130/130 | | |
| + "(inkl. Streuobst ohne Schutz)" | light dots 235/235/235 | | |

→ The official Bavarian viewer uses **one magenta/pink family** for "mapped biotope", graded by the share of § 30 / Art. 23 area, and does **not** colour by biotope type. Magenta/pink as the signal colour for "kartiertes Biotop" is the Bavarian convention to respect for a *protection-status overlay*.

### 8.2 BfN Planzeichen – see section 7 (V)

Published numeric colours per biotope group, in a pastel and a saturated series; recommendation for landscape plans.

### 8.3 Berlin – Umweltatlas map 05.08 "Biotoptypen 2024" (V)

- WMS "Biotoptypen 2024 (Umweltatlas)": <https://gdi.berlin.de/services/wms/ua_biotoptypen_2024?REQUEST=GetCapabilities&SERVICE=WMS> – licence "Datenlizenz Deutschland – Zero – Version 2.0", no access restrictions (V\*). Layers for points / lines / areas of four themes: Biotoptypen (`aa_biotoptypen_p`, `ab_biotoptypen_l`, `ac_biotoptypen_f`), Gesetzlich geschützte Biotope (`ba_…`, `bb_…`, `bc_gesetzschutz_f`), Lebensraumtypen FFH (`ca_…`, `cb_…`, `cc_ffh_f`), Kartiermethode.
- The dataset carries a legend number (`bt_legende`) per object; "Für die Darstellung von Vektordaten in einem GIS kann eine SLD je Feature-Type bzw. Layer abgerufen werden", e.g. `…/ua_biotoptypen_2024?service=WMS&version=1.1.1&request=GetStyles&layers=ua_biotoptypen_2024:ac_biotoptypen_f` (V, technical description, Stand 01/2026: <https://gdi.berlin.de/data/ua_biotoptypen_2024/docs/Datenformatbeschreibung_05_08_Biotoptypen2024.pdf>).
- Legend classes and fills of the area layer (labels read from the legend PNG; hex **sampled from the PNG** and identical to the SLD, V; outline #6E6E6E, 0.1 wide, and label = biotope code from the SLD, V\*):

| No. | Legend class | Hex | RGB |
|---|---|---|---|
| 01 | Fließgewässer | #1483FA | 20/131/250 |
| 02 | Standgewässer | #96C8FA | 150/200/250 |
| 03 | Schwimmblatt- u. Unterwasservegetation | #962896 | 150/40/150 |
| 04 | Gewässerbegleitende Röhrichte | #DBA0E6 | 219/160/230 |
| 05 | Rohbodenstandorte | #FFFF28 | 255/255/40 |
| 06 | Ruderalfluren | #FAAA6E | 250/170/110 |
| 07 | Äcker | #FFFEAB | 255/254/171 |
| 08 | **Feucht- u. Frischgrünland, Zier- u. Trittrasen** | #D7FAB4 | 215/250/180 |
| 09 | Trocken- u. Magerrasen | #EDFFD6 | 237/255/214 |
| 10 | Grünlandbrache u. Staudenfluren | #D2D200 | 210/210/0 |
| 11 | Zwergstrauchheiden | #E646C9 | 230/70/201 |
| 12 | Moore u. Sümpfe | #A04500 | 160/69/0 |
| 13 | Moorgebüsche | #8FFFCD | 143/255/205 |
| 14 | Moor-, Bruch- u. Auenwälder | #00DCA9 | 0/220/169 |
| 15 | Gebüsche, Baumreihen u. Baumgruppen | #7DFF00 | 125/255/0 |
| 16 | Wälder u. Forsten | #00BA00 | 0/186/0 |
| 17 | Grün- u. Freiflächen | #828200 | 130/130/0 |
| 18 | Haus- u. Kleingarten | #F0C8C8 | 240/200/200 |
| 19 | Wohn- u. Mischbebauung | #E6F0F0 | 230/240/240 |
| 20 | Gewerbe- u. Dienstleistungsflächen | #BABABA | 186/186/186 |
| 21 | Verkehrsflächen | #8F8F8F | 143/143/143 |
| 22 | Sonstiges | #FFD773 | 255/215/115 |
| 24 | Quellen | #0000FF in the legend PNG (SLD extraction gave #0000E1) | 0/0/255 |
| 25 | unversiegelte Wege u. Stege | #585858 | 88/88/88 |

- Map 05.08.2 *Gesetzlich geschützte Biotope 2024* re-uses the same class colours for protected biotopes (classes 01–06, 08–16, 18, 24, 25) and adds **"Verdacht auf gesetzlichen Schutz" = red cross-hatch on white** (V, legend PNG; hatch colour not sampled). Map 05.08.3 shows FFH habitat types incl. "Entwicklungsflächen".
- Maps 06.01 / 06.02 (*Reale Nutzung der bebauten Flächen* / *Grün- und Freiflächenbestand*): not retrieved.

### 8.4 BfN catalogue vs. Berlin map – where conventions agree and where they do not (derived from the verified values)

| Theme | BfN pastel series (7.4) | Berlin 2024 (8.3) | Agreement |
|---|---|---|---|
| Running / standing water | #C5E9FF (standing with dark-blue outline) | #1483FA / #96C8FA | yes – blue |
| Mesic and wet grassland, lawns | #D2F098 | #D7FAB4 (incl. "Zier- u. Trittrasen") | yes – pale yellow-green; **both put lawns into the grassland colour** |
| Dry / nutrient-poor grassland | #FFFFA1 (pale yellow) | #EDFFD6 (very pale green) | partly – paler than mesic grassland in both |
| Arable | #F2DFB0 (beige) | #FFFEAB (pale yellow) | yes – pale yellow / beige |
| Shrubs, tree rows, tree groups | #BEF583 | #7DFF00 | yes – bright yellow-green |
| Forests | saturated #466725 / #00521E (pastel value misprinted) | #00BA00 | yes – green, darker than shrubs |
| Wet woods | forest colour + blue dashed lines | #00DCA9 / #8FFFCD (turquoise) | analogous – shift towards blue |
| Heath | #FFB5C2 (pink) | #E646C9 (magenta) | yes – pink / magenta |
| Traffic areas | #E6CEC5 (pale pink-grey) | #8F8F8F (grey) | roughly – grey family |
| **Reeds** | #FFAF5E orange + blue dashes | #DBA0E6 light violet | **no** |
| **Ruderal / tall-forb vegetation** | #DDC0EC violet (group 39) | #FAAA6E orange (Ruderalfluren); #D2D200 (Grünlandbrache u. Staudenfluren) | **no – the two systems swap orange and violet** |
| **Raw soil** | #E2E2E2 grey + dashes | #FFFF28 bright yellow | **no** |
| Bogs and swamps | #D1CB94 olive + blue dashes | #A04500 brown | partly – brown family |
| **Parks / public green** | #ABF6B4 mint | #828200 olive | **no** |
| Gardens | (settlement green or Siedlungsflächen) | #F0C8C8 light pink | – |
| **Residential / mixed built-up** | #EBC1B0 salmon | #E6F0F0 very light blue-grey | **no** |
| Commercial | #E6CEC5 | #BABABA grey | roughly |

### 8.5 München, Hamburg and other cities

- München: biotope data = LfU Stadtbiotopkartierung (8.1). City-specific legend conventions (Flächennutzungsplan mit integrierter Landschaftsplanung, Arten- und Biotopschutzprogramm) were not retrieved.
- Hamburg Biotopkataster: not retrieved (old URL 404).

### 8.6 Conclusion on conventions

No legal norm fixes colours for biotope maps (for Bauleitpläne the PlanZV applies – other stream). Verified practice shows a **stable core** (water blue · woodland green · shrubs and tree rows bright yellow-green · grassland pale yellow-green with lawns inside the grassland hue · arable pale yellow/beige · heath pink/magenta · traffic grey · wetness expressed by a blue shift or blue hatch · legal protection as an overlay in red/magenta) and a **variable periphery** (reeds, ruderal vegetation, raw soil, parks, gardens, built-up areas). A library should follow the core strictly and may choose freely – but consistently – in the periphery, offering the BfN and Berlin schemes as optional presets.

---

## 9. How practice separates Rasen – Wiese – artenreiches Grünland – Ruderalflur / Brache

### 9.1 Bavaria: quantitative criteria (V, LfU Arbeitshilfe 2014, Tab. 3, p. 23, and type descriptions)

| BNT | Cover of nutrient-poverty indicators (*Magerkeitszeiger*) | Cover of typical meadow forbs\* | Number of typical meadow forbs\* on a representative 25 m² plot | Fallow for several years | WP |
|---|---|---|---|---|---|
| **G4** Tritt- und Parkrasen | – (not part of the table) | – | – | – | 3 |
| **G11** Intensivgrünland | < 1 % | < 1 % | < 5 | n. r. | 3 |
| G12 Intensivgrünland, brachgefallen | < 1 % | n. r. | n. r. | x | 5 |
| **G211** mäßig extensiv, artenarm | 1 to < 25 % | 1 to < 12,5 % | 5–9 | n. r. | 6 |
| **G212** mäßig extensiv, artenreich (→ GU651L) | 1 to < 25 % | ≥ 12,5 % | ≥ 10\*\* | n. r. | 8 (9 as LRT) |
| G213 artenarmes Extensivgrünland (→ GX00BK) | ≥ 25 % | < 12,5 % | < 10 | n. r. | 8 (9 as BK) |
| **G214** artenreiches Extensivgrünland (→ GU651E, GY6520, AD00BK) | ≥ 25 % | ≥ 12,5 % | ≥ 10\*\* | n. r. | 12 |
| G215 brachgefallen | 1 to < 25 % (G215) / ≥ 25 % (G215-GB00BK) | n. r. | n. r. | x | 7 / 8 |

\* excluding nitrogen indicators and ruderal plants (e.g. *Taraxacum officinale, Anthriscus sylvestris, Rumex obtusifolius, Urtica dioica, Silene dioica, Cirsium arvense*). \*\* alternatively: at least about 20 meadow herbs or grasses of any kind (including nutrient indicators). n. r. = criterion not relevant.

Verbal criteria (V):

- **G4 Tritt- und Parkrasen**: "Aufgrund hoher Trittbelastung und/oder hoher Schnittfrequenz intensiv genutzte niedrigwüchsige Rasen … an Rändern unbefestigter Wege, im Eingangsbereich von Weideflächen, in Parkanlagen, Sportanlagen und Gärten. Auf nährstoffreicheren Böden oder durch verstärkten Dünger- und gezielten Pestizideinsatz sowie durch **sehr häufige Mahdtermine** artenarm und oft reich an Neophyten." (G 1 · W 1 · N 1 = 3)
- **G11 Intensivgrünland**: "Arten- und meist blütenarmes, von Süßgräsern dominiertes, **häufig gemähtes (mind. 3-schürig)** oder intensiv beweidetes Wirtschaftsgrünland" (G 1 · W 1 · N 1 = 3). Temporary grassland counts as arable (A1).
- **G211**: "extensive Wiesennutzung (**1- bis 3(4)-schürige Mahd** mit i. d. R. spätem erstem Schnitt und ohne bis geringe Stickstoffgaben)" (2 · 2 · 2 = 6).
- **G212 / G213 / G214 Mähwiesen**: "**1- bis 2-schürige (gelegentlich / selten bis 3-schürige) Wiesen** mit i. d. R. spätem erstem Schnitt, nicht vor der Hauptblüte der Gräser" with low or no fertilisation; pastures max. about 1 GVE/ha (G214). For `G212-LR6510` a recognisable current or former mowing use is decisive.
- **Fallow**: G12 = "Mindestens 2 Jahre aus der Nutzung genommenes Intensivgrünland"; G215 = formerly (moderately) extensive grassland out of use for several years; matted stands with old grass and litter; **woody cover < 50 %**. Above 50 % scrub → `B13`.
- **K – Säume, Ruderal- und Staudenfluren**: linear or areal stands of mainly herbaceous vegetation, "Der Gehölzanteil beträgt dabei stets < 50 %"; K11 species-poor (hypertrophic, neophyte stands, dominance stands of e.g. *Calamagrostis epigejos*, *Pteridium*) 4 WP; K12 moderately species-rich 6–8 WP; K13 species-rich 8–11 WP. K13 explicitly includes "langjährige Brachen ehemaliger Wiesen und Weiden, bei denen sich aus dem aktuellen Zustand die frühere Nutzung nicht mehr erschließen lässt" – i.e. **a fallow stays "Grünlandbrache" (G12/G215) only as long as its grassland origin is recognisable; afterwards it becomes a Saum/Staudenflur (K)**.
- **Ruderal areas in settlements** are not K but **P43** ("Anthropogen überprägte Ruderalfluren auf künstlich geschaffenen Standorten (z. B. Brachen der Industrie-/Gewerbegebiete, Häfen oder Bahnhöfe)"), graded vegetation-free (P431, 2) → species-poor (P432, 4) → species-rich (P433, 8; with BK type RF 9).
- **Biotope mapping thresholds (V, Kartieranleitung 2022)**: RF vs. GB – perennial ruderal species > 50 % cover → RF; ST – total vegetation cover ≤ 50 %; UP – lawns and rich meadows < 50 % of the area, sealing < 10 %.

### 9.1a Bavaria: when is a meadow a legally protected "artenreiche Flachland-Mähwiese" (type GU)? (V, Kartieranleitung Teil 2, 2022, pp. 73–76)

All three criteria must be met:

1. At least one *Arrhenatherion* character species is present (*Arrhenatherum elatius, Campanula patula, Centaurea jacea* agg., *Crepis biennis, Dichoropetalum carvifolia, Galium album, Geranium pratense, Helictotrichon pubescens, Knautia arvensis* s. str., *Pimpinella major, Tragopogon pratensis* agg. or *Sanguisorba officinalis*), and the stand does not belong to *Calthion, Molinion, Trisetion, Mesobromion* or *Cynosurion*.
2. "(Frühere) Mahdnutzung ist (noch) nachvollziehbar" – independent of the current use; included are mown pastures, young fallow stages, orchard meadows and areas with maintenance grazing; excluded are long-standing permanent pastures without supplementary mowing.
3. Species and flower richness: (a) in a representative strip of about **3 m × 10 m at least 12 typical herbaceous meadow species** (from the "Krautartenliste", Tafel 36 of the § 30 key); for nutrient-poor or moist variants **9** suffice; and (b) the total cover of nitrogen indicators and other degrading species stays **below cover class 3a (≤ 25 %)** – e.g. *Aegopodium podagraria, Anthriscus sylvestris, Calamagrostis epigejos, Cirsium arvense, Heracleum sphondylium, Lolium perenne, L. multiflorum, Phleum pratense, Poa trivialis, Rumex obtusifolius, Taraxacum* sect. *Ruderalia, Trifolium repens, Urtica dioica*.

Sub-types: **GU651E** (magere bis mittlere Standorte) – nutrient-poverty or moisture indicators with total cover ≥ 3a (> 25 %) and ≥ 9 herbaceous meadow species; **GU651L** (mittlere bis nährstoffreiche Standorte) – such indicators largely missing (cover < 3a) and ≥ 12 herbaceous meadow species in the 3 m × 10 m strip.

Mapping notes that matter for urban green:

- "Ausgeschlossen sind ungereifte Bestände, wie beispielsweise Ackerbegrünungen, die i.d.R. keine typische, gut durchmischte Wiesenstruktur aus Gräsern und Kräutern in unterschiedlichen Schichten aufweisen." → **a freshly sown flower meadow is not a protected GU meadow.**
- "Lineare Ausbildungen (z.B. Feldraine, Wegböschungen, -ränder oder Straßenbegleitgrün) werden i.d.R. nicht systematisch erfasst"; particularly species-rich stands are recorded nevertheless.
- GB (Magere Altgrasbestände und Grünlandbrachen) differs from GU by the declining share of low-growing herbs and by young woody plants or ruderal species.

Caution: the thresholds of the 2014 Arbeitshilfe (≥ 10 typical forbs on 25 m², table above) and of the 2022 mapping key (≥ 12 or 9 species on a 3 m × 10 m strip) are **not identical**; the Biotopwertliste has not yet been aligned.

### 9.2 Federal level (V\* BKompV values; V Red List status)

| Step | BKompV code | Wert | Red List (Finck 2017) |
|---|---|---|---|
| Tritt- und Parkrasen | 34.09 | 8 | 34.09: \* (no risk), regenerability X |
| Sportrasenplatz (complex) | 51.11a.01 | 7 | – |
| Frisches Ansaatgrünland (newly sown grassland) | 34.08.02 | 7 | under 34.08: \* |
| Intensiv genutztes, frisches Dauergrünland | 34.08a.01 | 8 | 34.08 Artenarmes Grünland frischer Standorte: \* |
| Extensiv genutztes, frisches Dauergrünland | 34.08a.02 | 11 | 34.08: \* |
| Mäßig artenreiche, frische Mähwiese | 34.07b.01 | 15 | (split introduced by BKompV) |
| **Artenreiche, frische Mähwiese** | 34.07a.01 | 20 | 34.07 Artenreiches Grünland frischer Standorte: **1-2**, S |
| Grünlandbrache – artenarm / mäßig artenreich / artenreich | 34.08.03 / 34.07b.03 / 34.07a.03 | 9 / 11 / 16 | – |
| Säume – sonstige / mit wertgebenden Merkmalen | 39.03.02 / 39.03.01a, b | 8 / 17, 16 | 39.03.02: \* · 39.03.01: 3-V |
| Neophyten-Staudenflur | 39.05 | 7 | # |
| Ruderalstandorte frisch–nass / trocken-warm bindig / trocken-warm auf Sand, Kies, Schotter | 39.06.03 / 39.06.02 / 39.06.01 | 12 / 14 / 16 | 39.06 Ruderalstandorte: **2-3**, B |
| Kleine unbefestigte Freiflächen mit Spontanvegetation | 51.02 | 11 | 51.02: 3-V |
| Brachflächen (ehem. Bau-, Industrie-, Verkehrsflächen) ohne / mit wesentlichen struktur-/artenreichen Anteilen | 51.04a.02 / 51.04a.01 | 7 / 12 | – |

Reading: in the federal list a lawn (8) and intensive grassland (8) are equal, a sown grassland is lower (7), and **spontaneous ruderal vegetation (11–16) ranks above lawn and intensive meadow** – the opposite of how many municipal green-space inventories treat "Brache".

### 9.3 Consequences for the three existing grass classes

| Library class | Meaning in the keys | Deciding attributes |
|---|---|---|
| **Lawn** | Tritt- und Parkrasen / Scherrasen: frequent cutting and/or trampling, low sward | cuts per year high (many); species-poor; BKompV 34.09; BayKompV G4 |
| **Meadow** | Wirtschafts- or Extensivwiese: 1–3(4) cuts, taller sward; species-poor to moderately rich | cuts 1–3; typical meadow forbs 5–9 (G211) or ≥ 10 (G212); BKompV 34.08a.x / 34.07b.x |
| **Wildflower meadow** | ambiguous: (a) *grown* species-rich hay meadow (LRT 6510/6520; G214 / 34.07a.01; legally protected) or (b) *sown* flower mix (on arable: A12 "Blühstreifen"; as grassland: 34.08.02 Ansaatgrünland until it fulfils meadow criteria) | origin (sown / grown), age, species count per 25 m², cover of nutrient-poverty indicators; protection flag |
| (missing) **Grünlandbrache / Altgras** | G12, G215 / 34.07x.03, 34.08.03; BK GB | years since last use ≥ 2; woody cover < 50 % |
| (missing) **Ruderalflur / Spontanvegetation** | P431–P433, K11–K13 / 39.06.x, 51.02, 51.04a; BK RF, ST | substrate, vegetation cover (≤ / > 50 %), species richness, neophyte dominance |
| (missing) **Saum / Staudenflur** | K1x / 39.01–39.05; BK GW, GH | site moisture (dry-warm / mesic / wet), species richness |

---

## 10. Open points (not verified this session)

1. **BKompV**: the annex rows are machine-extracted (V\*; urban rows spot-checked twice). Four odd codes need a look at the gazette PDF (`52.01.08n.03`, second `44.03.02J`, `35.02.05.01a`, name of `41.01.04.01`). Content of the amendment of 22 December 2025 unknown. The BfN guidance on applying the BKompV (type descriptions) was not read.
2. **Other Länder keys**: NRW, Hessen, Baden-Württemberg, Sachsen and Hamburg remain R (current editions, code structures, example codes, colour schemes). Hessen's roof types and Lower Saxony's lawn types should be checked, because they cover elements (green roof, lawn sub-types) that the federal and Bavarian lists lack.
3. **Berlin**: names of the twelve Biotopklassen and single codes (lawn, park, garden types) not verified; SLDs of the point and line layers not read; legends of maps 06.01 / 06.02 (Reale Nutzung, Grün- und Freiflächenbestand) not retrieved; hatch colour of "Verdacht auf gesetzlichen Schutz" not sampled.
4. **München / Hamburg** legend conventions.
5. **Bavarian definition ordinance for Art. 23 Nr. 6 and 7** (Streuobstbestände; arten- und strukturreiches Dauergrünland): title, date and thresholds not retrieved; what the act of 26 March 2026 changed in the BayNatSchG was not determined.
6. **BfN Planzeichen**: numeric colour of *Laub(misch)wald* in the pastel series (catalogue misprint – read it from the QGIS style XML); content of 461/1 (derivation of the colour logic) not read; licence of the GIS download package unclear.
7. Whether the **Vollzugshinweise to the BayKompV**, the Bavarian guideline for the impact regulation in urban land-use planning, or a Bavarian landscape-plan guideline contain drafting rules for Bestands- und Konfliktpläne was not checked (the statement that municipal practice uses the BNT list is R).
8. The **full BfN book** (Finck et al. 2017) with third/fourth-level codes of groups 51–53 was not accessible; only the Kurzliste was read.
9. **Threshold mismatch** between the 2014 Arbeitshilfe and the 2022 mapping key for species-rich meadows (section 9.1a); the announced update of the Biotopwertliste may change BK sub-type codes and possibly values.
10. The date and act of the 2022 extension of § 30 BNatSchG (Nr. 7) are R.

---

## 11. Implications for the element catalog

### 11.1 Principles

1. **Keep two code systems per element as first-class attributes**: `bkompv_code` (= BfN code space, 0–24) and `baykompv_bnt` (letter+digits, 0–15). Add `bfn_rl_code` (Finck group/type), `by_bk_type` (Bavarian biotope-mapping type), `ffh_lrt`, and free slots for other Länder keys. Never derive one from the other by pattern.
2. **One visual element ≠ one code.** Most urban elements map to a *family* of codes that differ by age class, naturalness, species richness or sealing. The library element should fix the family; attributes select the exact code.
3. **Three kinds of objects** exist in the lists and need different geometry: surface types (lawn, asphalt), structural elements (single tree, hedge, wall – often point/line) and **complexes** (park, garden, cemetery, residential area "inkl. typischer Freiräume"). A map must not double-count: either the complex (P11, 51.06a) or its parts (G4 + B312 + V32).

### 11.2 Crosswalk of the 16 existing classes (BKompV V\*, BayKompV V)

| Existing class | BKompV (Wert) | BayKompV BNT (WP) | Remarks |
|---|---|---|---|
| Lawn | 34.09 Tritt- und Parkrasen (8); sports: 51.11a.01 (7) | **G4** (3); sports: P32 (2) | clean match |
| Meadow | 34.08a.01 (8) · 34.08a.02 (11) · 34.07b.01 (15) | **G11** (3) · **G211** (6) · **G212** (8) | needs intensity / species-richness attribute |
| Wildflower meadow | 34.07a.01 (20) if grown and species-rich; 34.08.02 (7) if newly sown | **G214** (12) if criteria met; **G212** (8); on arable A12 (4) | ambiguous – split into "species-rich meadow" and "sown flower meadow" |
| Shrub | 41.01.04.02 (13) · 41.01.06 (12) · 41.04 J/M/A (8/11/14) | **B112** (10) · B116 (7) · **B12** (5) | add hedge and clipped hedge as own elements |
| Woodland | 43.09 J/M/A (11/13/16) · 43.10 (9/12/14) · 44.04 (9/11/14) · 44.05 (6/10/12) · natural types 43.07.x etc. · 51.06a.05 Parkwald (14) | **L61–L63** (6/10/12) · L71x/L72x · N61–N63 · N71x/N72x · natural types L1–L5 | needs leaf type, naturalness, age class; optionally FFH type |
| Urban trees | 41.05a J/M/A (11/15/18) · 41.05b J/M/A (8/11/14) · 41.05.04 Allee (11/16/19) · 41.05.02 Kopfbaum (12/15/18) · 41.05.05 Obstbaum (11/19/21) | **B311–B313** (5/9/12) · **B321–B323** (4/8/11) · B331–B333 (5/9/12) | age class and native/non-native are mandatory; BK types UA / UE only from 50 / 75 cm BHD |
| Reed/wetland | 38.02.01 (19) · 38.02.02 (15) · 38.03 (16) · 38.06 (13) · 38.07 (16) · 37.02 (16) | **R111** (10) · R113 (10) · **R121** (11) · R123 (11) · R22 (11) · R31 (10) · R322 (12) | always legally protected (§ 30 Nr. 2); split water reed / land reed / tall sedges |
| Water body | standing: 24.04a/b/c (19/16/15) · 24.05 (7) · 24.07.05 Zier- und Löschteich (5) · 24.07.08 Rückhaltebecken (5) · 24.07.13a (5); running: 23.01 (22) · 23.02 (17) · 23.03a.01 (8) · 23.04a.01 (5) · ditch 23.05.01a.01/.02 (13/8) · canal 23.05.04a.01/.02 (10/4) | standing: **S131–S133** (6/9/13) · S14 (5) · **S22** (3); running: **F11–F15** (2/5/8/11/14) · F211/F212 (5/10) · F221/F222 (2/8) | split standing / running; naturalness is the key attribute |
| Soil/bare ground | 32.10 (18, near-natural) · 51.01 (5) · 32.11.09a construction site (3) · 52.02.06 unbefestigter Weg (10) | **O43** (8) · **O7** (1) · P431 (2) · V331 (2) | semantics depend on origin: natural raw soil vs. construction site vs. trampled ground |
| Sand | 32.09 (18, near-natural) · playground sand inside 51.11a.05 (7) | **O421** (9) · O422 Binnendüne (12) · P32 (2) | open inland dunes are § 30 biotopes |
| Paving (light) / Paving (dark) | sealed or otherwise paved: 52.01.01a / 52.02.01a / 52.03.01 (0); natural-stone paving 52.01.07a (6) / 52.02.08a (7) / 52.03.05a (7); partly paved e.g. grass pavers 52.01.03 (2) / 52.02.03 (3) / 52.03.02 (3) | impermeable paving **V11 / V31 / P5** (0); permeable paving **V12 / V32** (1) | colour (light/dark) is irrelevant to every key; **permeability and material (natural stone)** decide |
| Asphalt | 52.01.01a / 52.02.01a / 52.03.01 (0) | **V11 / V31 / P5** (0) | clean match |
| Concrete | same as asphalt (0); concrete wall 53.02.02 (0) | **V11 / V31 / P5** (0) | clean match |
| Gravel | as surfacing: 52.01.04a (3) · 52.02.04a (4) · 52.03.03a (4); track ballast 52.04.01 (1); near-natural gravel area 32.08 (18) | **V12 / V32** (1) · V22 (1) · near-natural **O41** (9) | distinguish technical surfacing from near-natural gravel |
| Wood decking | no type; nearest: sealed/paved (0) or partly paved (2–3) | no type; nearest P5 / V31 (0) or V32 (1) | map by permeability attribute; flag "no explicit code" |

### 11.3 Proposed element list (additions in bold)

**A. Grass and herb layer**

| Element | BKompV | BayKompV | Bavarian BK / protection |
|---|---|---|---|
| Lawn (Zier-/Parkrasen, Trittrasen) | 34.09 | G4 | – |
| **Sports turf** | 51.11a.01 | P32 | – |
| Meadow, intensive (Fettwiese) | 34.08a.01 | G11 | – |
| **Meadow, extensive** (moderately species-rich) | 34.08a.02 · 34.07b.01 | G211 · G212 · G213 | GU651L / GX; G212 can be LRT 6510 |
| **Species-rich meadow** (LRT 6510/6520) | 34.07a.01 | G214 | GU651E, GY6520 – § 30 Nr. 7 / Art. 23 Nr. 7 |
| **Sown flower meadow / flower strip** | 34.08.02 | A12 (on arable) · G212 as target | – |
| **Wet meadow** | 35.02.06.01 · 35.02.03a.01 | G221 · G222 | GN – § 30 Nr. 2 |
| **Dry / sand grassland** (Magerrasen) | 34.02a · 34.04.03.01a · 34.04.01a | G312 · G313 | GT, GL – § 30 Nr. 3 / Art. 23 Nr. 4 |
| **Grassland fallow / old-grass strip** | 34.08.03 · 34.07b.03 · 34.07a.03 | G12 · G215 | GB (§ 39 / Art. 16) |
| **Ruderal vegetation** (dry-warm / mesic) | 39.06.01 · 39.06.02 · 39.06.03 · 51.02 | P432 · P433 · K11 · K12x | RF, ST |
| **Tall-forb stand / fringe** | 39.03.01a/b · 39.03.02 · 39.04a.01/.02 | K121–K123 · K131–K133 | GW (Art. 23 Nr. 3), GH (§ 30) |
| **Neophyte stand** | 39.05 · 39.07 | K11 · B12 | – |
| Reed (water / land) | 38.02.01 · 38.02.02 · 38.03 · 38.06 | R121–R123 · R111–R113 · R22 | VH, VK, GR – § 30 Nr. 2 / Art. 23 Nr. 1 |
| **Tall-sedge swamp** | 37.01 · 37.02 | R31 · R321 · R322 | GG, VC – § 30 Nr. 2 |

**B. Woody elements**

| Element | BKompV | BayKompV | Bavarian BK / protection |
|---|---|---|---|
| Shrubbery, native | 41.01.04.02 · 41.01.06 | B112 · B116 | WX, WI |
| **Shrubbery / planting, non-native (ornamental)** | 41.04 J/M/A | B12 | – |
| **Hedge, free-growing** | 41.03.03 J/M/A | B112 | WH (§ 39 / Art. 16) |
| **Hedge, clipped** | 41.03.03J ("sowie Schnitthecken") · 41.04J | B141 · B142 | – |
| Single tree (young / medium / old; native / non-native) | 41.05a · 41.05b J/M/A | B311–B313 · B321–B323 | UE (BHD > 75 cm) |
| **Tree row / avenue** | 41.05a/b · 41.05.04 J/M/A | B31x / B32x (inkl. Alleen) | UA (BHD ≥ 50 cm) |
| **Tree group** | 41.05a/b | B31x / B32x | UA; > 0,5 ha → UP |
| **Pollard tree** | 41.05.02 J/M/A | B331–B333 | – |
| **Fruit tree / orchard meadow** | 41.05.05 · 41.06.01 J/MA | B431 · B432 · B441 | BS (protected) / BX |
| **Copse (Feldgehölz)** | 41.02.02 J/M/A | B211–B213 · B221–B223 | WO |
| **Pioneer wood on urban-industrial site** | 42.03.02 | W22 · B13 | WI |
| Woodland, deciduous / mixed / coniferous; near-natural vs. plantation | 43.07.x · 43.09 · 43.10 · 44.04 · 44.05 | L2xx · L6x · L7xx · N6x · N7xx | optional FFH 9110 / 9130 / 9160 / 9170 |
| **Riparian / alluvial wood** | 43.04.01 · 43.04.02.x · 43.04.03.x | L51x · L52x · L53x · L54x | WA, WN – § 30 Nr. 4; FFH 91E0\*, 91F0 |

**C. Water**

| Element | BKompV | BayKompV | Protection |
|---|---|---|---|
| Pond / lake, near-natural | 24.04a/b/c | S132 · S133 | § 30 Nr. 1; FFH 3150 |
| **Pond, ornamental / technical; retention basin** | 24.07.05 · 24.07.08 · 24.07.06 · 24.07.13a | S22 · S131 | – |
| **Temporary water / puddle pond** | 24.09a · 24.04a (Tümpel) | S1 types · S31/S32 | § 30 Nr. 1 |
| Stream / river by naturalness class | 23.01 · 23.02 · 23.03a.x · 23.04a.x | F15 · F14 · F13 · F12 · F11 | § 30 Nr. 1; FFH 3260 |
| **Ditch** | 23.05.01a.01/.02 | F212 · F211 | – |
| **Canal; piped section; hard bank** | 23.05.04a.x · 23.05.03 · 23.05.05a · 23.05.07a | F222 · F221 | – |
| **Spring** (point) | 22.05 · 22.0x | Q11 · Q12 · Q2x | § 30 Nr. 2 |

**D. Open ground and stone structures**

| Element | BKompV | BayKompV | Protection |
|---|---|---|---|
| Bare soil (raw soil, construction site) | 32.10 · 51.01 · 32.11.09a | O43 · O7 · P431 | – |
| Sand, near-natural / inland dune | 32.09 | O421 · O422 | § 30 Nr. 3 (offene Binnendünen) |
| Gravel / ballast area, near-natural | 32.08 | O41 | – |
| **Dry-stone wall / natural-stone wall** | 53.02.03a · 53.02.04a | O22 | § 30 Nr. 7; BK UR |
| **Stone ridge (Lesesteinriegel)** | 53.02.05a | O21 | § 30 Nr. 7 |
| **Gabion; brick wall; concrete wall** | 53.02.06a · 53.02.01.x · 53.02.02 | (X4 / no type) | – |

**E. Green-space complexes**

| Element | BKompV | BayKompV | BK |
|---|---|---|---|
| **Park / public green** (intensive / extensive; with / without old trees; historic) | 51.06a.01–.05 · 51.07a.01/.02 | P11 · P12 | UP |
| **Cemetery** | 51.09a.01/.02 | P11 · P12 | UP |
| **Private garden / allotment** (structure-poor / -rich) | 51.08a.02/.01 | P21 · P22 | UK (abandoned) |
| **Sports / play / leisure area** | 51.11a.01–.05 · 52.03.03a | P31 · P32 | – |
| **Brownfield / urban wasteland** | 51.04a.01/.02 | P431–P433 | RF |
| **Roadside green** (verge, central reservation; herb-rich; with woody stock) | 52.01.08a.01 · .02 · .03 | V12 · V51 · V52 | – |
| **Green track** (Rasengleis / Sedumgleis) | – (52.04.01 Gleiskörper) | V23 | – |
| **Bed / ornamental planting** | – (Finck 51.03 Anpflanzungen und Rabatten; not in BKompV) | within P11 / P21 | – |
| **Green roof (extensive / intensive), façade greening** | **no code** | **no code** | extension element; check Hessen KV |
| **Arable / urban agriculture; allotment field** | 33.0x.03 · 33.0x.02 · 33.0x.04 | A11 · A12 · A13 · A2 | – |

**F. Surfaces and built structures**

| Element | BKompV | BayKompV |
|---|---|---|
| Asphalt (sealed) | 52.01.01a · 52.02.01a · 52.03.01 | V11 · V31 · P5 |
| Concrete (sealed) | same | same |
| Paving, impermeable (light / dark) | same | V11 · V31 · P5 |
| **Paving, permeable / with joints** | 52.01.03 · 52.02.03 · 52.03.02 | V12 · V32 |
| **Natural-stone paving** | 52.01.07a · 52.02.08a · 52.03.05a | V11/V31 or V12/V32 by permeability |
| **Grass pavers (Rasengitter)** | 52.01.03 · 52.02.03 · 52.03.02 | V12 · V32 |
| Gravel / water-bound surface | 52.01.04a · 52.02.04a · 52.03.03a | V12 · V32 |
| **Unpaved path / grass path** | 52.02.06 | V331 · V332 |
| Wood decking | no code (by sealing class) | no code (by sealing class) |
| **Building** | 53.01.x (structure types incl. open space) | X4 (building) · X11 / X12 / X2 / X3 (areas) |
| **Railway track (ballast / slab)** | 52.04.01 | V22 · V21 |

### 11.4 Attributes every element should be able to carry

| Attribute | Values | Needed for |
|---|---|---|
| `bkompv_code`, `bkompv_value` (0–24), `bkompv_class` | code; integer; sehr gering … hervorragend | federal crosswalk |
| `baykompv_bnt`, `baykompv_wp` (0–15), `baykompv_class` | code; integer; keine / gering / mittel / hoch | Bavarian crosswalk |
| `baykompv_target_allowed` | bool | P/X/V types other than P1, P43, V23, V33, V5 are impact-side only |
| `by_bk_type` | e.g. GU651E, UP00BK | hyphen suffix of the BNT; protection and LRT |
| `protection` | none · § 30 BNatSchG (Nr.) · Art. 23 BayNatSchG (Nr.) · § 39 (5) BNatSchG / Art. 16 BayNatSchG · potential | overlay symbol, label |
| `ffh_lrt` | e.g. 6510, 91E0\* (priority flag) | label |
| `red_list_de` (RLD) and `regenerability` (RE) | Finck categories | optional value display |
| `age_class` | J / M / A (BKompV); jung ≤ 25 a, mittel 26–79 a, alt ≥ 80 a (BayKompV); BHD in cm | all woody elements, parks |
| `origin_native` | native & site-appropriate / non-native | 41.05a vs. b; B31x vs. B32x; B141 vs. B142 |
| `naturalness` | BayKompV N 0–5 (künstlich … natürlich); for waters: Gewässerstrukturklasse 1–7 | waters, raw ground, forests |
| `management_intensity` | cuts per year; grazing; fertilised yes/no; fallow since (years) | lawn / meadow / fallow separation |
| `species_richness` | artenarm / mäßig artenreich / artenreich; forb count per 25 m²; cover of nutrient-poverty indicators (%) | G11 … G214, K11 … K13, P432/P433 |
| `site_moisture` | trocken-warm / frisch / feucht–nass | K-types, 39.x, 41.0x; drives the blue "wet" overlay |
| `sealing_class` | versiegelt (impermeable) / befestigt–teilversiegelt (permeable, water-bound) / unbefestigt; material | all surfaces; decides 0 vs. 1–7 points |
| `woody_cover_pct`, `vegetation_cover_pct` | % | < 50 % woody = grass/herb type; ≤ 50 % vegetation = pioneer/raw ground |
| `is_complex` | bool | parks, gardens, settlement areas "inkl. typischer Freiräume" |
| `size_ha` / `min_size_rule` | number | point-vs-area rule (< 1 ha), orchard 2 500 m², UR 20 m × 2 m |

### 11.5 Colour and symbol conventions to respect

1. **Hue families of the BfN catalogue (section 7.6).** The pastel "Kulisse" series (7.4) is a ready-made, citable pastel palette; the house style can sit on it or stay within its hues. Key separations: grassland yellow-green vs. settlement green mint; dry grassland pale yellow; shrubs fresh green; forests dark green; reeds orange + blue dashes; fringes/ruderal violet; built salmon; traffic/industry grey-brown; raw ground grey with dashes; water blue with dark outline. Official city maps do not follow it everywhere (Berlin: reeds violet, ruderal vegetation orange, raw soil yellow, parks olive – section 8.4); treat the **stable core** of section 8.6 as binding and the rest as a documented house choice, ideally with BfN and Berlin presets.
2. **Lawn, meadow and species-rich meadow share the grassland hue.** Separate them by (a) lightness/saturation, (b) texture motif (short even stipple → taller tufts → tufts with flower dots), and (c) the BfN value rule: high-value stands get the saturated colour plus outline.
3. **Overlays instead of new colours**: wet = blue dashed horizontal offset lines; fallow = brown dashed vertical lines; orchard = red dot grid; this fits hand-drawn textures well and keeps the hue reserved for the group.
4. **Value / status encoding**: low–moderate value = tint without outline; high–outstanding = saturated + dark outline; target state = 50 % transparency; development potential = associative hatch; proposed = same motif without contour (dashed allowed). Do not invent a measure-symbol "standard" – the BfN catalogue leaves measures to the individual plan.
5. **Legal protection as an overlay, not as a fill**: label-based in the BfN system (black = existing, grey = potential); in Bavaria the public viewer uses the magenta/pink family (#D97EB0 / #EECACF / #FCEBFD, outline #EE5AC7). A thin magenta outline or "§" marker for § 30 / Art. 23 biotopes would be read correctly by Bavarian users.
6. **Small objects as points**: below about 1 ha (BfN) use point symbols; single trees, springs, caves are always points; tree rows are marker lines. Line widths for running waters follow water-body order.
7. **Sealed surfaces**: every key treats asphalt, concrete and impermeable paving as one class (value 0); light/dark paving is a purely visual distinction. Give the *permeable* classes (water-bound, gravel, grass pavers, natural-stone paving with joints) their own visual language, because that is the distinction the valuation lists make.
8. **Where symbology is prescribed vs. recommended** (within this stream): BKompV and BayKompV prescribe **none**; BfN Planzeichen are a **recommendation**; the LfU viewer legend is **de-facto practice**. Binding symbology for Bauleitpläne (PlanZV) and the XPlanung data standard are outside this stream.

---

## Sources

| # | Source | URL | Read how |
|---|---|---|---|
| 1 | BfN, Rote Liste Biotoptypen 2017 – Kurzliste | <https://www.bfn.de/sites/default/files/2021-06/RL_Biotope_Kurzliste_2017_deutsch_barrierefrei.pdf> | page images (V) |
| 2 | BKompV Anlage 2; § 5 | <https://www.gesetze-im-internet.de/bkompv/anlage_2.html> · <https://www.gesetze-im-internet.de/bkompv/__5.html> | extraction (V\*) |
| 3 | § 30 BNatSchG | <https://www.gesetze-im-internet.de/bnatschg_2009/__30.html> | extraction (V\*) |
| 4 | StMUV, Biotopwertliste BayKompV (2014) | <https://www.stmuv.bayern.de/themen/naturschutz/eingriffe/doc/biotopwertliste.pdf> | page images (V) |
| 5 | LfU, Arbeitshilfe zur Biotopwertliste (2014) | <https://www.lfu.bayern.de/publikationen/get_pdf.htm?art_nr=lfu_nat_00320&pdf_nr=0> | page images (V) |
| 6 | LfU, Änderungen der Biotoptypen-Zuordnungen (09/2021) | <https://www.lfu.bayern.de/natur/kompensationsverordnung/doc/biotoptypen_zuordnungen.pdf> | page images (V) |
| 7 | LfU, Kartieranleitung Biotopkartierung Bayern Teil 2 (04/2022) | <https://www.lfu.bayern.de/natur/doc/kartieranleitungen/biotoptypen_teil2.pdf> | page images (V) |
| 8 | LfU, BayKompV overview page | <https://www.lfu.bayern.de/natur/kompensationsverordnung/index.htm> | extraction (V\*) |
| 9 | BayKompV; BayNatSchG Art. 16, 23 | <https://www.gesetze-bayern.de/Content/Document/BayKompV/true> · <https://www.gesetze-bayern.de/Content/Document/BayNatSchG-23> | extraction (V\*) |
| 10 | BfN, FFH-Lebensraumtypenliste | <https://www.bfn.de/sites/default/files/2022-05/5_lebensraumtypenliste_20180925_pac.pdf> | page images (V) |
| 11 | BfN-Skripten 461/2 Planzeichenkatalog | <https://bfn.bsz-bw.de/frontdoor/deliver/index/docId/270/file/Skript461_2.pdf> | page images (V) |
| 12 | BfN-Skripten 486 GIS documentation | <https://bfn.bsz-bw.de/frontdoor/deliver/index/docId/206/file/Skript_486.pdf> | page images (V) |
| 13 | BfN project and digitalisation pages | <https://www.bfn.de/projektsteckbriefe/planzeichen-fuer-die-landschaftsplanung> · <https://www.bfn.de/digitalisierung-der-landschaftsplanung> | extraction (V\*) |
| 14 | LfU WMS Biotopkartierung (capabilities, legend PNG) | <https://www.lfu.bayern.de/gdi/wms/natur/biotopkartierung?REQUEST=GetCapabilities&SERVICE=WMS> | extraction + pixel sampling (V) |
| 15 | Umweltatlas Berlin, Biotoptypen | <https://www.berlin.de/umweltatlas/biotope/biotoptypen/> | page text (V) |
| 16 | BKompV full text (title, § 1, § 5) | <https://www.gesetze-im-internet.de/bkompv/BJNR108800020.html> | extraction (V\*) |
| 17 | Umweltatlas Berlin, Biotoptypen 2024 – Methode, Karten | <https://www.berlin.de/umweltatlas/biotope/biotoptypen/2024/methode/> · <https://www.berlin.de/umweltatlas/biotope/biotoptypen/2024/karten/> | page text (V) |
| 18 | Berlin WMS Biotoptypen 2024: capabilities, SLD (GetStyles), legend PNGs | <https://gdi.berlin.de/services/wms/ua_biotoptypen_2024?REQUEST=GetCapabilities&SERVICE=WMS> | extraction (V\*) + pixel sampling (V) |
| 19 | Berlin, Technische Beschreibung Biotoptypen 2024 (Stand 01/2026) | <https://gdi.berlin.de/data/ua_biotoptypen_2024/docs/Datenformatbeschreibung_05_08_Biotoptypen2024.pdf> | PDF text (V) |
| 20 | NLWKN, Kartierschlüssel für Biotoptypen in Niedersachsen | <https://www.nlwkn.niedersachsen.de/naturschutz/biotopschutz/biotopkartierung/kartierschluessel/kartierschluessel-fuer-biotoptypen-in-niedersachsen-45164.html> | page text (V) |

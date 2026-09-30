# Stream 01: German planning-law symbology and official cadastral/topographic catalogs

Research date: 2026-09-30. Scope: PlanZV, XPlanung/XPlanGML, ALKIS/ATKIS (AAA model, GeoInfoDok 7.1), official German map colours (ALKIS-/ATKIS-Signaturenkatalog, basemap.de), BKG LBM-DE.

Evidence marks used in every table:

- **V** = verified in a primary source during this session (URL given).
- **S** = taken from a secondary source (URL given).
- **R** = recalled from prior knowledge, NOT verified this session.
- "n.v." = not verified / could not verify.

How the primary sources were read: legal text and images at gesetze-im-internet.de; XPlanGML 6.1 XSD + GML dictionaries + external code lists in the GDI-DE registry; AAA/NAS 7.1.2 XSD and the AdV enumeration register in the GDI-DE registry; ALKIS-OK 7.1.2 (Profil Hessen) PDF; AdV Signaturenkatalog XML/HTML at sg.geodatenzentrum.de; basemap.de style JSON; xPlanBox source (GitLab opencode.de). Colour values marked "sampled" were measured by me from the JPEG reproductions on gesetze-im-internet.de and are NOT normative.

---

## 1. PlanZV (Planzeichenverordnung 1990)

### 1.1 Current version

| Item | Value | St. | Source |
|---|---|---|---|
| Full title | "Verordnung über die Ausarbeitung der Bauleitpläne und die Darstellung des Planinhalts (Planzeichenverordnung - PlanZV)" | V | https://www.gesetze-im-internet.de/planzv_90/BJNR000580991.html |
| Ausfertigung | 18.12.1990 (BGBl. 1991 I S. 58) | V | same |
| Last amendment | "zuletzt durch Artikel 6 des Gesetzes vom 12. August 2025 (BGBl. 2025 I Nr. 189) geändert" | V | same |
| What the 2025 amendment did to the Anlage | new no. 1.5 "Beschleunigungsgebiete für die Windenergie an Land (§ 249c BauGB)" (Orange mittel); old 1.5 "Beschränkung der Zahl der Wohnungen" renumbered 1.6 | V | https://www.gesetze-im-internet.de/planzv_90/anlage.html (footnote + images in folder bgbl1_2025) |
| Earlier additions visible in the Anlage | 1.2.2 "Dörfliche Wohngebiete (§ 5a BauNVO)" (images in folder bgbl1_2021); 1.2.4 "Urbane Gebiete (§ 6a BauNVO)"; no. 7 pictograms "Erneuerbare Energien", "Kraft-Wärme-Kopplung" (images in folder bgbl1_2011) | V | same |
| Fundstelle of the Anlage | "(Fundstelle: BGBl. I 1991, 58 [Anlagenband]; bzgl. der einzelnen Änderungen vgl. Fußnote)" | V | same |

### 1.2 § 2 Planzeichen: wording and legal force

Text as retrieved from https://www.gesetze-im-internet.de/planzv_90/__2.html (V unless noted; the statute is an official work, § 5 UrhG):

(Full text of § 2 re-read verbatim in the browser on 2026-09-30, all five Absätze V.)

- **(1)** "Als Planzeichen in den Bauleitplänen sollen die in der Anlage zu dieser Verordnung enthaltenen Planzeichen verwendet werden. Dies gilt auch insbesondere für Kennzeichnungen, nachrichtliche Übernahmen und Vermerke. Die Darstellungsarten können miteinander verbunden werden. Linien können auch in Farbe ausgeführt werden. Kennzeichnungen, nachrichtliche Übernahmen und Vermerke sollen zusätzlich zu den Planzeichen als solche bezeichnet werden."
- **(2)** "Die in der Anlage enthaltenen Planzeichen können ergänzt werden, soweit dies zur eindeutigen Darstellung des Planinhalts erforderlich ist. Soweit Darstellungen des Planinhalts erforderlich sind, für die in der Anlage keine oder keine ausreichenden Planzeichen enthalten sind, können Planzeichen verwendet werden, die sinngemäß aus den angegebenen Planzeichen entwickelt worden sind."
- **(3)** "Die Planzeichen sollen in Farbton, Strichstärke und Dichte den Planunterlagen so angepaßt werden, daß deren Inhalt erkennbar bleibt."
- **(4)** "Die verwendeten Planzeichen sollen im Bauleitplan erklärt werden."
- **(5)** "Eine Verletzung von Vorschriften der Absätze 1 bis 4 ist unbeachtlich, wenn die Darstellung, Festsetzung, Kennzeichnung, nachrichtliche Übernahme oder der Vermerk hinreichend deutlich erkennbar ist."
- **§ 1 (1)** "Als Unterlagen für Bauleitpläne sind Karten zu verwenden, die in Genauigkeit und Vollständigkeit den Zustand des Plangebiets in einem für den Planinhalt ausreichenden Grade erkennen lassen (Planunterlagen)." **(2)** "Aus den Planunterlagen für Bebauungspläne sollen sich die Flurstücke mit ihren Grenzen und Bezeichnungen in Übereinstimmung mit dem Liegenschaftskataster, die vorhandenen baulichen Anlagen, die Straßen, Wege und Plätze sowie die Geländehöhe ergeben." (V)
- **§ 3** (Überleitung): "Die bis zum 31. Oktober 1981 sowie die bis zum Inkrafttreten dieser Verordnung geltenden Planzeichen können weiterhin verwendet werden..." (V, truncated)

Assessment (my reading of the verified text):

| Question | Answer | Basis |
|---|---|---|
| How binding? | Soll-Vorschrift ("sollen ... verwendet werden"), applies only to Bauleitpläne (Flächennutzungsplan, Bebauungsplan). Not a Muss; breach is "unbeachtlich" if the content is "hinreichend deutlich erkennbar" (Abs. 5). | § 2 Abs. 1, 5 |
| Deviations / additions allowed? | Yes: signs may be supplemented (Abs. 2 S. 1) and new signs developed "sinngemäß" from the given ones (Abs. 2 S. 2); hue, line weight and density are to be adapted to the base map (Abs. 3). | § 2 Abs. 2, 3 |
| Colour vs. black-and-white? | The Anlage has two columns, "schwarz/weiß" and "farbig"; both are equally admissible. "Die Darstellungsarten können miteinander verbunden werden. Linien können auch in Farbe ausgeführt werden." | § 2 Abs. 1; Anlage column heads |
| Legend duty | Used Planzeichen "sollen im Bauleitplan erklärt werden". | § 2 Abs. 4 |
| Numeric colour values? | None. Colours are given only as names ("Grün mittel", "Blau mittel", "Goldocker" ...) plus a printed sample. "Farbton" is explicitly adaptable (Abs. 3). | Anlage text |
| Consequence for an "official" theme | A strict theme can reproduce hue family + symbol geometry of the Anlage; exact RGB is a convention, not law. Outside Bauleitpläne (e.g. inventory/ecology maps) PlanZV does not apply at all. | n/a |

### 1.3 Structure of the Anlage ("Planzeichen für Bauleitpläne")

Numbers, sub-numbers and all 15 group titles verified verbatim at https://www.gesetze-im-internet.de/planzv_90/anlage.html (titles re-read in the browser on 2026-09-30; the "title R" marks in the last column below are therefore superseded, every title in this table is V). Footnote of the Anlage: "frühere Nr. 1.5. jetzt Nr. 1.6. gem. Art. 6 Nr. 2 G v. 12.8.2025 I Nr. 189 mWv 15.8.2025" (V).

| No. | Title | Legal basis quoted in the Anlage | St. |
|---|---|---|---|
| 1 | Art der baulichen Nutzung (1.1 Wohnbauflächen; 1.2 Gemischte Bauflächen; 1.3 Gewerbliche Bauflächen; 1.4 Sonderbauflächen; 1.5 Beschleunigungsgebiete für die Windenergie an Land; 1.6 Beschränkung der Zahl der Wohnungen) | § 5 Abs. 2 Nr. 1, § 9 Abs. 1 Nr. 1 BauGB, §§ 1 bis 11 BauNVO | V |
| 2 | Maß der baulichen Nutzung (2.1 Geschoßflächenzahl ... 2.8 Höhe baulicher Anlagen) | n/a | V |
| 3 | Bauweise, Baulinien, Baugrenzen (3.1 Offene Bauweise, 3.2 Geschlossene, 3.3 Abweichende, 3.4 Baulinie, 3.5 Baugrenze) | n/a | V |
| 4 | Einrichtungen und Anlagen zur Versorgung mit Gütern und Dienstleistungen des öffentlichen und privaten Bereichs, Flächen für den Gemeinbedarf, Flächen für Sport- und Spielanlagen (4.1 Flächen für den Gemeinbedarf; 4.2 Flächen für Sport- und Spielanlagen) | § 5 Abs. 2 Nr. 2 Buchst. a, § 9 Abs. 1 Nr. 5 BauGB | V |
| 5 | Flächen für den überörtlichen Verkehr und für die örtlichen Hauptverkehrszüge (5.1 Straßenverkehr; 5.2 Bahnen; 5.3 Überörtliche Wege und örtliche Hauptwege; 5.4 Umgrenzung der Flächen für den Luftverkehr) | § 5 Abs. 2 Nr. 3, Abs. 4 BauGB | V |
| 6 | Verkehrsflächen (6.1 Straßenverkehrsflächen; 6.2 Straßenbegrenzungslinie; 6.3 Verkehrsflächen besonderer Zweckbestimmung; 6.4 Ein- bzw. Ausfahrten ...; 6.5 Bahnen; 6.6 Luftverkehr) | § 9 Abs. 1 Nr. 11, Abs. 6 BauGB | V |
| 7 | Flächen für Versorgungsanlagen, für die Abfallentsorgung und Abwasserbeseitigung sowie für Ablagerungen; Anlagen, Einrichtungen und sonstige Maßnahmen, die dem Klimawandel entgegenwirken | § 5 Abs. 2 Nr. 2 Buchst. b, Nr. 4, Abs. 4; § 9 Abs. 1 Nr. 12, 14, Abs. 6 BauGB | V |
| 8 | Hauptversorgungs- und Hauptabwasserleitungen (oberirdisch / unterirdisch) | § 5 Abs. 2 Nr. 4, Abs. 4; § 9 Abs. 1 Nr. 13, Abs. 6 BauGB | V |
| 9 | Grünflächen | § 5 Abs. 2 Nr. 5 und Abs. 4, § 9 Abs. 1 Nr. 15 und Abs. 6 BauGB | V |
| 10 | Wasserflächen und Flächen für die Wasserwirtschaft, den Hochwasserschutz und die Regelung des Wasserabflusses (10.1–10.3) | § 5 Abs. 2 Nr. 7 und Abs. 4, § 9 Abs. 1 Nr. 16 und Abs. 6 BauGB | V |
| 11 | Flächen für Aufschüttungen, Abgrabungen oder für die Gewinnung von Bodenschätzen (11.1, 11.2) | § 5 Abs. 2 Nr. 8 und Abs. 4, § 9 Abs. 1 Nr. 17 und Abs. 6 BauGB | V |
| 12 | Flächen für die Landwirtschaft und Wald (12.1, 12.2) | § 5 Abs. 2 Nr. 9 und Abs. 4, § 9 Abs. 1 Nr. 18 und Abs. 6 BauGB | V |
| 13 | Planungen, Nutzungsregelungen, Maßnahmen und Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Natur und Landschaft (13.1, 13.2, 13.2.1, 13.2.2, 13.3) | § 5 Abs. 2 Nr. 10 und Abs. 4, § 9 Abs. 1 Nr. 20, 25 und Abs. 6 BauGB | V |
| 14 | Regelungen für die Stadterhaltung und für den Denkmalschutz (14.1–14.3) | § 172 Abs. 1; § 5 Abs. 4, § 9 Abs. 6 BauGB | V |
| 15 | Sonstige Planzeichen (15.1–15.14) | various | V |

### 1.4 Open-space relevant Planzeichen in detail

Symbol descriptions are my own descriptions of the images as depicted at gesetze-im-internet.de (image files `normengrafiken/bgbl1_1991_ab/jNNNN_NNNN.jpg`), viewed 2026-09-30 (V "as depicted"). Colour names are verbatim from the Anlage (V). "Sampled RGB" = median of the dominant colour bin of the official JPEG reproduction (non-normative, scan/JPEG artefacts; see 1.5).

#### Group 6: Verkehrsflächen (Bebauungsplan)

| No. | Planzeichen | Colour name (Anlage) | b/w depiction | colour depiction | Sampled RGB | St. |
|---|---|---|---|---|---|---|
| 6.1 | Straßenverkehrsflächen | Goldocker | two alternatives: blank (white) area with outline, or fine dot raster | flat yellow-ochre fill | #FEE223 (254,226,35) | V |
| 6.2 | Straßenbegrenzungslinie auch gegenüber Verkehrsflächen besonderer Zweckbestimmung | Permanentgrün hell | solid black line | black line accompanied by a light-green band | #5AE458 (90,228,88) | V |
| 6.3 | Verkehrsflächen besonderer Zweckbestimmung | Goldocker | blank, or diagonal stripes of dot raster | diagonal yellow-ochre stripes on white | #FDE333 (253,227,51) | V |
| 6.3 Zweckbestimmung | Öffentliche Parkfläche | n/a | white "P" on dark square | n/a | n/a | V |
| 6.3 Zweckbestimmung | Fußgängerbereich | n/a | white pedestrian figure on dark square | n/a | n/a | V |
| 6.3 Zweckbestimmung | Verkehrsberuhigter Bereich | n/a | white "V" on dark square | n/a | n/a | V |
| 6.4 | Einfahrt / Einfahrtbereich / Bereich ohne Ein- und Ausfahrt | n/a | solid triangle; dashed line between two triangles; row of filled semicircles | n/a | n/a | V |
| 5.1.1 / 5.1.2 (FNP) | Autobahnen ...; Sonstige überörtliche und örtliche Hauptverkehrsstraßen | Goldocker | n/a | yellow-ochre bands | #FEE333 (254,227,51) | V |
| 5.2.1 | Bahnanlagen | Violett mittel | n/a | violet fill | #D18CD3 (209,140,211) | V |
| 5.2.2 / 5.2.3 / 5.4 | Straßenbahnen; Seilbahnen; Umgrenzung der Flächen für den Luftverkehr | Violett dunkel | n/a | violet line / band | ≈ #BD5AC2 (189,90,194) (from 5.4) | V |
| 5.3 | Überörtliche Wege und örtliche Hauptwege, e.g. Hauptwanderweg | n/a | line of large dots with a diamond containing "W" | n/a | n/a | V |

#### Group 9: Grünflächen

| Item | Content | St. |
|---|---|---|
| Colour | "Grün mittel"; colour column shows a flat light green; sampled #92EB9B (146,235,155) | V |
| b/w | regular fine dot raster (dense stipple in slightly wavy rows) | V |
| Notes (verbatim) | "Im Bebauungsplan sind Grünflächen als öffentliche oder private Grünflächen besonders zu bezeichnen." / "Im Bebauungsplan kann die Flächensignatur auch als Randsignatur verwendet werden." / "Im Flächennutzungsplan können die vorstehenden Zeichen zur Kennzeichnung der Lage auch ohne Flächendarstellung verwendet werden." | V |

Zweckbestimmung pictograms (each drawn in a rectangular frame, black on white; no colour variant):

| Zweckbestimmung | Pictogram as depicted | Image | XPlanung code (XP_ZweckbestimmungGruen) | St. |
|---|---|---|---|---|
| Parkanlage (park) | three groups of three filled dots (tree clumps) | j0011_0030 | 1000 | V |
| Dauerkleingärten (allotments) | frame divided into 2 x 3 plots, one dot in each plot | j0011_0050 | 1200 | V |
| Sportplatz (sports ground) | stadium oval (rounded rectangle / running track) | j0011_0070 | 1400 | V |
| Spielplatz (playground) | sand bucket with handle | j0011_0090 | 1600 | V |
| Zeltplatz (camp site) | tent (triangle with crossed poles) | j0011_0040 | 1800 | V |
| Badeplatz, Freibad (bathing place) | six horizontal wavy lines | j0011_0060 | 2000 | V |
| Friedhof (cemetery) | three upright crosses | j0011_0080 | 2600 | V |

#### Group 10: Wasserflächen und Flächen für die Wasserwirtschaft

| No. | Planzeichen | Colour name | b/w depiction | colour depiction | Sampled RGB | St. |
|---|---|---|---|---|---|---|
| 10.1 | Wasserflächen | Blau mittel | horizontal wavy lines | flat light blue | #C4E3EC (196,227,236) | V |
| 10.1 | Zweckbestimmung Hafen | Blau mittel | "H" in circle on wave pattern | "H" in circle on light blue | #C5E3ED | V |
| 10.2 | Umgrenzung von Flächen für die Wasserwirtschaft, den Hochwasserschutz und die Regelung des Wasserabflusses | Blau dunkel | border line with wavy inner line | blue band with wavy inner edge | #44ABD4 (68,171,212) | V |
| 10.2 | Hochwasserrückhaltebecken / Überschwemmungsgebiet | Blau dunkel | "R" / "Ü" in circle inside the 10.2 border | same, blue band | n/a | V |
| 10.3 | Umgrenzung der Flächen mit wasserrechtlichen Festsetzungen | Blau dunkel | border with looped ("comb"/meander) inner line | plain blue band | #3BA4CD (59,164,205) | V |
| 10.3 | Schutzgebiet für Grund- und Quellwassergewinnung / Schutzgebiet für Oberflächengewässer | Blau dunkel | "GW" / "OW" in circle | same, blue band | n/a | V |

Note (verbatim, 10.1): "Die Flächensignatur kann auch als Randsignatur verwendet werden." (V)

#### Group 11: Aufschüttungen, Abgrabungen

| No. | Planzeichen | Depiction (b/w only) | St. |
|---|---|---|---|
| 11.1 | Flächen für Aufschüttungen | double frame; band of solid black triangles standing on the inner rectangle, tips pointing outward; centre: circle with horizontal diameter and a filled rectangle sitting ON the line | V |
| 11.2 | Flächen für Abgrabungen oder für die Gewinnung von Bodenschätzen | solid black triangles with bases on the outer frame, tips pointing inward; centre: circle with horizontal diameter and a filled rectangle hanging BELOW the line | V |
| note | "Bei kleinen Flächen kann die Randsignatur im Flächennutzungsplan entfallen." | V |
| 15.9 | Flächen für Aufschüttungen, Abgrabungen und Stützmauern, soweit sie zur Herstellung des Straßenkörpers erforderlich sind (§ 9 Abs. 1 Nr. 26) | slope hachures (thick top-edge line, alternating long/short hachures to a dashed foot line; for Abgrabung the short hachures rise from the foot line); Stützmauer = double line with oblique hatching | V |

#### Group 12: Landwirtschaft und Wald

| No. | Planzeichen | Colour name | b/w depiction | colour depiction | Sampled RGB | St. |
|---|---|---|---|---|---|---|
| 12.1 | Flächen für die Landwirtschaft | Gelbgrün | sparse regular grid of small dots | flat light yellow-green | #BCFC9C (188,252,156) | V |
| 12.2 | Flächen für Wald | Blaugrün | regular grid of larger filled dots | flat blue-green (teal) | #15ADAA (21,173,170) | V |
| 12.2 | Zweckbestimmung Erholungswald | n/a | "E" in circle | n/a | n/a | V |

Note (verbatim): "Die Flächensignaturen können auch als Randsignaturen verwendet werden." (V)

#### Group 13: Natur und Landschaft

| No. | Planzeichen | Colour name | b/w depiction | colour depiction | Sampled RGB | St. |
|---|---|---|---|---|---|---|
| 13.1 | Umgrenzung von Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Natur und Landschaft (§ 5 Abs. 2 Nr. 10, § 9 Abs. 1 Nr. 20) | Grün dunkel | border line with T-shaped ticks pointing inward | green band carrying the T-ticks | #39E554 (57,229,84) | V |
| 13.2 Anpflanzen: Bäume | tree to be planted | Grün dunkel | circle with a small OPEN ring in the centre | green-filled circle with open ring | #2CE34B (44,227,75) | V |
| 13.2 Anpflanzen: Sträucher | shrubs to be planted | Grün dunkel | three-lobed "cloud" outline with small open ring | green-filled cloud with open ring | same | V |
| 13.2 Anpflanzen: Sonstige Bepflanzungen | other planting | Grün dunkel | cloud outline with a rectangle inside | green-filled, rectangle inside | same | V |
| 13.2 Erhaltung: Bäume | tree to be preserved | Grün dunkel | circle with FILLED centre dot | green-filled circle with filled dot | #32E34D | V |
| 13.2 Erhaltung: Sträucher | shrubs to be preserved | Grün dunkel | cloud outline with filled dot | green-filled cloud with filled dot | same | V |
| 13.2 Erhaltung: Sonstige Bepflanzungen | other planting to be preserved | Grün dunkel | cloud with rectangle and filled dot | green-filled | same | V |
| 13.2.1 | Umgrenzung von Flächen zum Anpflanzen von Bäumen, Sträuchern und sonstigen Bepflanzungen (§ 9 Abs. 1 Nr. 25 Buchst. a) | n/a | border line with a row of small OPEN circles along the inside | n/a | n/a | V |
| 13.2.2 | Umgrenzung von Flächen mit Bindungen für Bepflanzungen und für die Erhaltung von Bäumen, Sträuchern und sonstigen Bepflanzungen sowie von Gewässern (§ 9 Abs. 1 Nr. 25 Buchst. b) | n/a | border line with a row of FILLED dots along the inside | n/a | n/a | V |
| 13.3 | Umgrenzung von Schutzgebieten und Schutzobjekten im Sinne des Naturschutzrechts | Grün dunkel | border line with groups of short perpendicular strokes (blocks of 4) | green band with the stroke groups | #48E658 | V |
| 13.3 letters | N = Naturschutzgebiet, NLP = Nationalpark, L = Landschaftsschutzgebiet, NP = Naturpark, ND = Naturdenkmal, LB = Geschützter Landschaftsbestandteil (each in a circle) | n/a | n/a | n/a | n/a | V |

Notes (verbatim): "Im Bebauungsplan sind die Maßnahmen näher zu bestimmen." (13.1); "Festsetzungen für Teile baulicher Anlagen sind im Bebauungsplan näher zu bestimmen." (13.2); "Bei Bedarf sind zur weiteren Unterscheidung der Schutzgebiete und Schutzobjekte Differenzierungen in der Umgrenzungssignatur zulässig." (13.3) (V)

The principle "open centre = new planting (Anpflanzen), filled centre = existing/preserve (Erhaltung)" is the single most reusable PlanZV motif for point vegetation symbols.

#### Group 15: Sonstige Planzeichen (selection)

| No. | Planzeichen | Colour name | Depiction | Sampled RGB | St. |
|---|---|---|---|---|---|
| 15.3 | Umgrenzung von Flächen für Nebenanlagen, Stellplätze, Garagen und Gemeinschaftsanlagen; abbreviations St, GSt, Ga, GGa; Spielplatz pictogram (bucket) | Rot | b/w dashed line; colour: red dashed line | thin line, unreliable | V |
| 15.5 | Mit Geh-, Fahr- und Leitungsrechten zu belastende Flächen | n/a | line with a row of open boxes; "bei schmalen Flächen": double dashed line | n/a | V |
| 15.8 | Umgrenzung der Flächen, die von der Bebauung freizuhalten sind | n/a | border with zigzag inner line | n/a | V |
| 15.11 | Umgrenzung der Flächen, bei deren Bebauung besondere bauliche Vorkehrungen gegen äußere Einwirkungen erforderlich sind / Bergbau | Grau dunkel | n/a | #787B77 (120,123,119) | V |
| 15.13 | Grenze des räumlichen Geltungsbereichs des Bebauungsplans (§ 9 Abs. 7 BauGB) | Grau dunkel | b/w: thick broken black band (long thick dashes with gaps); colour: continuous dark-grey band | #767A76 (118,122,118) | V |
| 15.14 | Abgrenzung unterschiedlicher Nutzung ... (z. B. § 1 Abs. 4, § 16 Abs. 5 BauNVO) | n/a | thin line with filled dots ("Perlschnur") | n/a | V |
| 4.2 | Flächen für Sport- und Spielanlagen | n/a | border of small dots; Sportanlagen = white stadium oval on dark; Spielanlagen = white bucket on dark | n/a | V |

### 1.5 Colour names of the whole Anlage with sampled values (non-normative)

Sampling method: dominant colour bin of the image in the "farbig" column on gesetze-im-internet.de (JPEG scans of the BGBl. Anlagenband 1991; later amendments are separate scans with visibly different colour rendering, e.g. "Braun mittel" ranges from #DDD292 to #B49151 across sub-items). Use only as an indication of hue family.

| Colour name (Anlage) | Used for | Sampled hex (RGB) | St. |
|---|---|---|---|
| Rot mittel | 1.1 Wohnbauflächen incl. 1.1.1–1.1.4 | #F5C2B3–#FAC3B3 (≈250,195,179) | V (sampled) |
| Braun mittel | 1.2 Gemischte Bauflächen incl. 1.2.1–1.2.5 | #DAC583 (218,197,131); range #DDD292 … #B49151 | V (sampled) |
| Grau mittel | 1.3 Gewerbliche Bauflächen | #B3BAB2 (179,186,178) | V (sampled) |
| Orange mittel | 1.4 Sonderbauflächen; 1.5 Beschleunigungsgebiete Windenergie | #FCAE0B (252,174,11); 1.5 scan: #F3BB5C | V (sampled) |
| Rot | 3.4 Baulinie; 14.1/14.2; 15.3 | #EA5C48 (234,92,72) (3.4); #E98A76 (14.1) | V (sampled) |
| Blau | 3.5 Baugrenze | #1995C3 (25,149,195) | V (sampled) |
| Karminrot mittel | 4.1 Flächen für den Gemeinbedarf | #FBB7DE (251,183,222) | V (sampled) |
| Goldocker | 5.1, 6.1, 6.3 | #FEE223–#FEE333 | V (sampled) |
| Violett mittel | 5.2.1 Bahnanlagen | #D18CD3 (209,140,211) | V (sampled) |
| Violett dunkel | 5.2.2, 5.2.3, 5.4 | ≈ #BD5AC2 (189,90,194) | V (sampled) |
| Permanentgrün hell | 6.2 Straßenbegrenzungslinie | #5AE458 (90,228,88) | V (sampled) |
| Gelb hell | 7 Versorgungsanlagen ...; 15.1 | #F7FF5E (247,255,94) | V (sampled) |
| Grün mittel | 9 Grünflächen | #92EB9B (146,235,155) | V (sampled) |
| Blau mittel | 10.1 Wasserflächen | #C4E3EC (196,227,236) | V (sampled) |
| Blau dunkel | 10.2, 10.3 | #3BA4CD–#44ABD4 | V (sampled) |
| Gelbgrün | 12.1 Landwirtschaft | #BCFC9C (188,252,156) | V (sampled) |
| Blaugrün | 12.2 Wald | #15ADAA (21,173,170) | V (sampled) |
| Grün dunkel | 13.1, 13.2, 13.3 | #2CE34B–#39E554 | V (sampled) |
| Grau dunkel | 15.11, 15.13 | #767A76 (118,122,118) | V (sampled) |

### 1.6 Numeric colour values published elsewhere

| Source | What it gives | Binding? | St. | URL |
|---|---|---|---|---|
| PlanZV itself | colour names + printed samples only, no numbers | law (Soll) | V | https://www.gesetze-im-internet.de/planzv_90/anlage.html |
| xPlanBox default WMS styles ("xplansyn/default", SE/SLD), open-source reference implementation for XPlanung visualisation (Freie und Hansestadt Hamburg / lat/lon; DiPlanung) | hex colours per XPlanung class, see 2.6 | de-facto convention, not law; code is AGPL v3 | V | https://gitlab.opencode.de/diplanung/ozgxplanung (tags xplanbox-7.0 and xplanbox-9.3 checked; identical colours) |
| BfN-Schriften 461/2 "Planzeichen für die Landschaftsplanung – Planzeichenkatalog" (Hoheisel, Mengel, Heiland, Mertelmeyer, Meurer, Rittel 2017; DOI 10.19217/skr4612) | RAL/RGB values, line widths for landscape-planning symbols (not PlanZV) | recommendation | S (abstract only; catalogue not opened) | https://www.bfn.de/publikationen/bfn-schriften/bfn-schriften-4612-planzeichen-fuer-die-landschaftsplanung |
| Länder / municipal drafting guides with RGB/CMYK/RAL tables for PlanZV colours | not found in this session | n/a | n.v. | n/a |

---

## 2. XPlanung / XPlanGML

### 2.1 Versions

| Item | Value | St. | Source |
|---|---|---|---|
| Current version | XPlanung 6.1, "offiziell veröffentlicht" 15.04.2025; ca. 80 change requests; GML profile moved to GML 3.2.2 | V | https://xleitstelle.de/node/196 |
| Published versions | 3.0, 4.0.2, 4.1, 5.0.1, 5.1.2, 5.2.1, 5.3, 5.4, 6.0.2, 6.1 (+ Wärmeplan 0.9X) | V | https://xleitstelle.de/xplanung/releases-xplanung |
| 6.1 release folder | Definitions.zip, Enumerationen.zip (04.04.2025), GML_Dictionaries_61_Kuerzel.zip (22.05.2026), ObjektartenkatalogHTML.zip, ObjektartenkatalogXPlanGML_6.1.pdf, Schema.zip (18.07.2025), Struktur_und_Konzepte.pdf, UML-Diagramme.pdf, XPlanGML_6_1_Konformitätsbedingungen.pdf (16.06.2026), XPlanGML_6_1.qea, Änderungen_Datenmodell.pdf | V | https://xleitstelle.de/xplanung/releases-xplanung?fid=2275 |
| Machine-readable schema | namespace `http://www.xplanung.de/xplangml/6/1`; XSDs + GML dictionaries of all enumerations | V | https://registry.gdi-de.org/schemas/de.xleitstelle.xplanung/6.1/ |
| External code lists | register "XPlanung Codelisten" (owner XLeitstelle) | V | https://registry.gdi-de.org/codelist/de.xleitstelle.xplanung |
| HTML object catalogue | 6.0: online; 6.1: the embedded catalogue link was broken on 2026-09-30 (404) | V | https://xleitstelle.de/releases/objektartenkatalog_6_0 ; https://xleitstelle.de/releases/objektartenkatalog_6_1 |
| Newer than 6.1? | none listed on the releases page on 2026-09-30; enum documentation announces removals "in Version 7" | V | releases page; XSD annotations |

### 2.2 Changes 6.0 → 6.1 relevant for open space (from "XPlanGML 6.1 – Änderungen im Datenmodell", all V)

Source: https://xleitstelle.de/filebrowser/download/2285?fid=2285

| Element | Change | CR |
|---|---|---|
| XP_AnpflanzungBindungErhaltungsGegenstand | new code 1300 (Obstbaeume); new code 9999 (SonstGegenstand) | XPLAN-350 |
| XP_HandlungsfeldNatuerlicherKlimaschutz | new enumeration | XPLAN-424 |
| BP_NatuerlicherKlimaschutz, FP_NatuerlicherKlimaschutz | new classes | XPLAN-424 |
| XP_ERFlaechenArt | new enumeration (copy of LP_ERFlaechenArt, which was renamed/moved) | XPLAN-443 |
| BP_SchutzPflegeEntwicklungsFlaeche / -Massnahme | new attributes `nutzungsform`, `eRFlaechenArt`; `istAusgleich` redefined | XPLAN-306/428/443 |
| BP_AnpflanzungBindungErhaltung | new attributes `erlaeuterung`, `stammdurchmesser`, `eRFlaechenArt`; `kronendurchmesser`, `istAusgleich` redefined | XPLAN-306/350/369/443 |
| BP_AusgleichsFlaeche, BP_AusgleichsMassnahme, FP_AusgleichsFlaeche | deprecated ("veraltet", to be dropped in version 7; use SPE classes with istAusgleich = true) | XPLAN-306 |
| XP_Objekt | new attributes `vertikaleLage`, `massstabFaktor`, `skalierung`; new enum XP_VertikaleLage | XPLAN-432/433/448 |
| XP_ZweckbestimmungKennzeichnung 4000 | deprecated (use SO_Bodenschutzrecht); SO_KlassifizNachBodenschutzrecht new code 3000 SchadstoffBelasteterBoden | XPLAN-425 |
| SO_KlassifizWasserwirtschaft | new code 1450 (Hochwasserschutzanlage) | XPLAN-384 |
| SO_Wasserwirtschaft | new attributes `name`, `nummer` | XPLAN-422 |
| LP_GesGeschBiotopTyp | new code 9998 Unbekannt | XPLAN-408/431 |
| LP_RechtsstandSchutzGeb | new codes 9998 Unbekannt, 3100 Fortfallend, 3200 Aufgehoben | XPLAN-431/445 |
| SO_Festpunkt, SO_FestpunktTyp; BP_HoehenFestsetzung; BP_GebaeudeTyp; BP_ImmissionsortLaerm; RP_TextAbschnittObjekt | new | various |

No change entries exist for XP_ZweckbestimmungGruen, XP_ZweckbestimmungLandwirtschaft, XP_ZweckbestimmungWald, XP_SPEMassnahmenTypen, XP_SPEZiele, XP_ABEMassnahmenTypen, SO_KlassifizGewaesser → identical in 6.0 and 6.1 (V, by absence in the change document).

### 2.3 Enumerations (XPlanGML 6.1)

All rows V. Codes and documentation from `XPlanGML_Basisschema.xsd` / `XPlanGML_SonstigePlanwerke.xsd` / `XPlanGML_LPlan_Kernmodell.xsd` (6.1); names from the GML dictionaries `Enumerationen/<Name>.xml` (same registry folder): https://registry.gdi-de.org/schemas/de.xleitstelle.xplanung/6.1/

#### XP_ZweckbestimmungGruen (35 values): used by BP_GruenFlaeche / FP_Gruen via `zweckbestimmung.allgemein`

In 6.x the former "besondere Zweckbestimmung" (5-digit) codes are merged into this one enumeration; the first 2 digits show the parent.

| Code | Name (identifier) | Lesbarer Name | Documentation (XSD) |
|---|---|---|---|
| 1000 | Parkanlage | Parkanlage | Parkanlage; auch: Erholungsgrün, Grünanlage, Naherholung. |
| 10000 | ParkanlageHistorisch | Historische Parkanlage | Historische Parkanlage |
| 10001 | ParkanlageNaturnah | Naturnahe Parkanlage | Naturnahe Parkanlage |
| 10002 | ParkanlageWaldcharakter | Parkanlage mit Waldcharakter | Parkanlage mit Waldcharakter |
| 10003 | NaturnaheUferParkanlage | Naturnahe Ufer-Parkanlage | Ufernahe Parkanlage |
| 1200 | Dauerkleingarten | Dauerkleingarten | Dauerkleingarten; auch: Gartenfläche, Hofgärten, Gartenland. |
| 12000 | ErholungsGaerten | Erholungsgärten | Erholungsgarten |
| 1400 | Sportplatz | Sportplatz | Sportplatz |
| 14000 | Reitsportanlage | Reitsportanlage | Reitsportanlage |
| 14001 | Hundesportanlage | Hundesportanlage | Hundesportanlage |
| 14002 | Wassersportanlage | Wassersportanlage | Wassersportanlage |
| 14003 | Schiessstand | Schießstand | Schießstand |
| 14004 | Golfplatz | Golfplatz | Golfplatz |
| 14005 | Skisport | Skisport | Anlage für Skisport |
| 14006 | Tennisanlage | Tennisanlage | Tennisanlage |
| 1600 | Spielplatz | Spielplatz | Spielplatz |
| 16000 | Bolzplatz | Bolzplatz | Bolzplatz |
| 16001 | Abenteuerspielplatz | Abenteuerspielplatz | Abenteuerspielplatz |
| 1800 | Zeltplatz | Zeltplatz | Zeltplatz |
| 18000 | Campingplatz | Campingplatz | Campingplatz |
| 2000 | Badeplatz | Badeplatz | Badeplatz, auch Schwimmbad, Liegewiese. |
| 2200 | FreizeitErholung | Freizeit und Erholung | Anlage für Freizeit und Erholung. |
| 22000 | Kleintierhaltung | Kleintierhaltung | Anlage für Kleintierhaltung |
| 22001 | Festplatz | Festplatz | Festplatz |
| 2400 | SpezGruenflaeche | Spezielle Grünfläche | Spezielle Grünfläche |
| 24000 | StrassenbegleitGruen | Straßenbegleitgrün | Straßenbegleitgrün |
| 24001 | BoeschungsFlaeche | Böschungsfläche | Böschungsfläche |
| 24003 | Uferschutzstreifen | Uferschutzstreifen | Uferstreifen |
| 24004 | Abschirmgruen | Abschirmgrün | Abschirmgrün |
| 24005 | UmweltbildungsparkSchaugatter | Umweltbildungspark, Schaugatter | Umweltbildungspark, Schaugatter |
| 24006 | RuhenderVerkehr | Ruhender Verkehr | Fläche für den ruhenden Verkehr. |
| 2600 | Friedhof | Friedhof | Friedhof |
| 2700 | Naturerfahrungsraum | Naturerfahrungsraum | Naturerfahrungsräume sollen insbesondere Kindern und Jugendlichen die Möglichkeit geben, in ihrem direkten Umfeld Natur vorzufinden ... |
| 9999 | Sonstiges | Sonstiges | Sonstige Zweckbestimmung, falls keine der aufgeführten Klassifikationen anwendbar ist. |
| 99990 | Gaertnerei | Gärtnerei | Gärtnerei |

(There is no code 24002 in 6.1.)

Related: `nutzungsform` (XP_Nutzungsform): 1000 Privat, 2000 Oeffentlich (V), this is the machine form of the PlanZV duty to mark Grünflächen as "öffentlich" or "privat".

#### Detaillierte Zweckbestimmung Grün: external code lists (attribute `zweckbestimmung.detail`, gml:CodeType)

Register entries, governance level "national-legal", status "Gültig"; code = `<parent>_<n>` (V). Sources: https://registry.gdi-de.org/codelist/de.xleitstelle.xplanung/BP_DetailZweckbestGruenFlaeche and .../FP_DetailZweckbestGruen

| Code | BP_DetailZweckbestGruenFlaeche (37) | FP_DetailZweckbestGruen (37) |
|---|---|---|
| 1000_1 | Grünanlage | Grünanlage |
| 1000_2 | Grünanlage z.T. mit Freizeiteinrichtungen | same |
| 1200_1 | Grabeland | same |
| 1400_0_1 | Reitsport Ferienanlage | same |
| 1400_1_1 / _1_2 / _1_3 | Hundevereinsplatz / Hundeauslaufplatz / Hundeschule | same |
| 1600_1 | Freispielfläche | same |
| 1600_2 | Rodelberg | same |
| 1600_nrw_A / _B / _C | Spielbereich A / B / C | same |
| 2200_2 | Feuerstelle, Grillplatz | same |
| 2200_3 | Fahrradtourismus | same |
| 2200_4 | Wassertourismus | same |
| 2200_5 | Zoo | same |
| 2200_6 | vereinsbezogene Nutzung | same |
| 2400_6_1 | Wohnmobilstellplatz | same |
| 2400_7 | Aufforstung | same |
| 2400_8 | naturnahe Grünfläche, Naturschutz | same |
| 2400_10 | Gehoelzflaeche | Steilufer |
| 2400_11 | Gruenland/Weideland | Strand |
| 2400_12 | Windschutzpflanzungen | Grünverbindung Entwicklung: Grünverbindungen - Planung |
| 2400_13 | n/a | Grünverbindung Sicherung: Grünverbindungen |
| 2400_14 | Lärmschutzanlage | same |
| 2400_15 | Ortsrandeingrünung | same |
| 2400_16 | Eigentümergärten | same |
| 2400_17 | Streuobst-/ Obstbaumwiese | same |
| 2400_18 | Durchgruenung | same |
| 2600_1 | Tierfriedhof | same |
| 9999_1 | Segelfluggelände | same |
| 9999_2 | Bootslager/ Stellplätze für Boote | same |
| 9999_3 | Modellflugplatz | same |
| 9999_4 | Angelsport | same |
| 9999_5 | Gastronomie | same |
| 9999_6 | Grünverbindung | same |
| 9999_7 | Pferdebezogene Anlagen und Nutzungen | same |
| 9999_10 | Eigentümergarten | n/a |

Caution: identical codes 2400_10/_11/_12 mean different things in the BP and the FP list (V).

Other relevant external code lists (V): BP_VegetationsobjektTypen (1 value: 2050_1 Einheimische Gehölze); BP_DetailZweckbestLandwirtschaft (1000_1 Landwirtschaftliche Fläche ökologisch wertvoll; 1000_2 Gewächshausanlagen); BP_DetailZweckbestWaldFlaeche (1000_1 Sukzessionswald; 1800_1 Aufforstung; 9999_1 Begräbniswald, Bestattungswald; 9999_02 Sport-Freizeitbezogene Waldnutzung); SO_DetailZweckbestStrassenverkehr (14004_1 Radschnellweg; 14004_2 Radwandern; 14004_3 Fernradweg; 14008_1 Autohof; 1400_14 Fähre; 1600_0_1 Wohnmobilstellplatz).

#### Gewässer: no "XP_ZweckbestimmungGewaesser" in 6.x

In XPlanGML 6.0/6.1 water bodies are modelled by the plan-type-independent class **SO_Gewaesser** (attribute `artDerFestlegung.allgemein` : SO_KlassifizGewaesser); the schema folder contains no XP_ZweckbestimmungGewaesser (V). The enumeration of that name belongs to the 5.x line (values there not verified this session; recalled: 1000 Hafen, 1100 Wasserflaeche, 1200 Fliessgewaesser, 9999 Sonstiges, **R**).

| SO_KlassifizGewaesser | Name | Lesbarer Name / documentation |
|---|---|---|
| 1000 | Gewaesser | Gewässer, Allgemeines, bestehendes Gewässer |
| 2000 | FliessGewaesser | Fließgewässer, Allgemeines Fließgewässer |
| 20000 | Gewaesser1Ordnung | Gewässer 1. Ordnung |
| 20001 | Gewaesser2Ordnung | Gewässer 2. Ordnung |
| 20002 | Gewaesser3Ordnung | Gewässer 3. Ordnung |
| 3000 | StehendesGewaesser | Stehendes Gewässer |
| 4000 | Hafen | Hafen |
| 40000 | Sportboothafen | Sportboothafen |
| 5000 | Wasserstrasse | Wasserstraße |
| 6000 | Kanal | Kanal |
| 9999 | Sonstiges | Sonstiges bestehendes Gewässer |

SO_DetailKlassifizGewaesser (external code list, 9): 1000_1 Wattflächen; 1000_2 Freizeitnutzung auf Wasserflächen; 1000_3 Löschwasserteich; 4000_1 Bootsliegeplätze; 4000_2 Schiffsanleger, Anleger, Anlegestelle, Landungssteg; 4000_3 Handelshafen / Frachthafen; 4000_4 Yachthafen, Marina; 4000_5 Industriehafen; 9999_1 Schifffahrtsweg (V).

| SO_KlassifizWasserwirtschaft (SO_Wasserwirtschaft; PlanZV 10.2) | Name |
|---|---|
| 1000 | HochwasserRueckhaltebecken |
| 1100 | Ueberschwemmgebiet (Überschwemmungsgefährdetes Gebiet nach § 31c des vor dem 1.10.2010 gültigen WHG) |
| 1200 | Versickerungsflaeche |
| 1300 | Entwaesserungsgraben |
| 1400 | Deich |
| 1450 | Hochwasserschutzanlage (new in 6.1) |
| 1500 | RegenRueckhaltebecken |
| 9999 | Sonstiges |

SO_KlassifizNachWasserrecht: 2000 Ueberschwemmungsgebiet; 20000 FestgesetztesUeberschwemmungsgebiet; 20001 NochNichtFestgesetztesUeberschwemmungsgebiet; 20002 UeberschwemmGefaehrdetesGebiet; 3000 Risikogebiet; 4000 RisikogebietAusserhUeberschwemmgebiet; 5000 Hochwasserentstehungsgebiet; 9999 Sonstiges (V).
SO_KlassifizSchutzgebietWasserrecht: 1000 Wasserschutzgebiet; 10000 QuellGrundwasserSchutzgebiet; 10001 OberflaechengewaesserSchutzgebiet; 2000 Heilquellenschutzgebiet; 9999 Sonstiges. SO_SchutzzonenWasserrecht: 1000 Zone_1; 1100 Zone_2; 1200 Zone_3; 1300 Zone_3a; 1400 Zone_3b; 1500 Zone_4 (V).

#### XP_ZweckbestimmungLandwirtschaft (9)

| Code | Name | Lesbarer Name |
|---|---|---|
| 1000 | LandwirtschaftAllgemein | Landwirtschaft allgemein |
| 1100 | Ackerbau | Ackerbau |
| 1200 | WiesenWeidewirtschaft | Wiesen, Weidewirtschaft |
| 1300 | GartenbaulicheErzeugung | Gartenbauliche Erzeugung |
| 1400 | Obstbau | Obstbau |
| 1500 | Weinbau | Weinbau |
| 1600 | Imkerei | Imkerei |
| 1700 | Binnenfischerei | Binnenfischerei |
| 9999 | Sonstiges | Sonstiges |

#### XP_ZweckbestimmungWald (14), XP_EigentumsartWald, XP_WaldbetretungTyp

| Code | Name | Lesbarer Name |
|---|---|---|
| 1000 | Naturwald | Naturwald |
| 10000 | Waldschutzgebiet | Waldschutzgebiet |
| 1200 | Nutzwald | Nutzwald |
| 1400 | Erholungswald | Erholungswald (= PlanZV 12.2 "E") |
| 1600 | Schutzwald | Schutzwald |
| 16000 | Bodenschutzwald | Bodenschutzwald |
| 16001 | Biotopschutzwald | Biotopschutzwald |
| 16002 | NaturnaherWald | Naturnaher Wald |
| 16003 | SchutzwaldSchaedlicheUmwelteinwirkungen | Schutzwald schädliche Umwelteinwirkungen |
| 16004 | Schonwald | Schonwald |
| 1700 | Bannwald | Bannwald |
| 1800 | FlaecheForstwirtschaft | Fläche Forstwirtschaft |
| 1900 | ImmissionsgeschaedigterWald | Immissionsgeschädigter Wald |
| 9999 | Sonstiges | Sonstiges |

XP_EigentumsartWald: 1000 Öffentlicher Wald allgemein; 1100 Staatswald; 1200 Körperschaftswald; 12000 Kommunalwald; 12001 Stiftungswald; 2000 Privatwald allgemein; 20000 Gemeinschaftswald; 20001 Genossenschaftswald; 3000 Kirchenwald; 9999 Sonstiger Wald. XP_WaldbetretungTyp: 1000 Radfahren; 2000 Reiten; 3000 Fahren; 4000 Hundesport (V).

#### XP_SPEMassnahmenTypen (16): "Aufzählung der Typen von Ausgleichs- und Ersatzmaßnahmen" (the closest thing XPlanung has to a habitat-type list)

| Code | Name | Lesbarer Name | Documentation (abridged) |
|---|---|---|---|
| 1000 | ArtenreicherGehoelzbestand | Artenreicher Gehölzbestand | aus unterschiedlichen, standortgerechten Gehölzarten aufgebaut, mit Strauchanteil |
| 1100 | NaturnaherWald | Naturnaher Wald | standortgemäße Gehölzzusammensetzung unterschiedlicher Altersstufen, Schichtung, Totholzanteil |
| 1200 | ExtensivesGruenland | Extensives Grünland | geringere Beweidungsintensität und Düngung, höhere Artenzahlen |
| 1300 | Feuchtgruenland | Feuchtgrünland | artenreich, auf feuchten bis wechselnassen Standorten |
| 1400 | Obstwiese | Obstwiese | mittel-/hochstämmige Obstbäume auf beweidetem oder gemähtem Grünland |
| 1500 | NaturnaherUferbereich | Naturnaher Uferbereich | Röhrichte, Hochstaudenrieder, Seggen, Ufergehölze |
| 1600 | Roehrichtzone | Röhrichtzone | hochwüchsige Röhrichtbestände im flachen Wasser / auf nassen Böden |
| 1700 | Ackerrandstreifen | Ackerrandstreifen | breite Streifen im Randbereich eines Ackerschlages |
| 1800 | Ackerbrache | Ackerbrache | mindestens eine Vegetationsperiode nicht bewirtschaftet |
| 1900 | Gruenlandbrache | Grünlandbrache | analog |
| 2000 | Sukzessionsflaeche | Sukzessionsfläche | dauerhaft ungenutzte, der natürlichen Entwicklung überlassene Bestände |
| 2100 | Hochstaudenflur | Hochstaudenflur | feuchte bis nasse Standorte |
| 2200 | Trockenrasen | Trockenrasen | zeitweise extreme Trockenheit, Nährstoffarmut |
| 2300 | Heide | Heide | Zwergstrauchgesellschaften (Calluna / Erica) |
| 2400 | Moor | Moor | "Moore, Sümpfe, Röhrichte, Großseggenrieder, seggen- und binsenreiche Nasswiesen, Quellbereiche, Binnenlandsalzstellen" gem. § 30 Abs. 2 Nr. 2 BNatSchG |
| 9999 | Sonstiges | Sonstiges | n/a |

#### XP_SPEZiele (5), XP_ABEMassnahmenTypen (3), XP_AnpflanzungBindungErhaltungsGegenstand (13), XP_ERFlaechenArt (5)

| Enumeration | Code | Name | Lesbarer Name / documentation |
|---|---|---|---|
| XP_SPEZiele | 1000 | SchutzPflege | Schutz und Pflege |
| | 2000 | Entwicklung | Entwicklung |
| | 3000 | Anlage | Anlage (doc: Neu-Anlage) |
| | 4000 | SchutzPflegeEntwicklung | Schutz, Pflege und Entwicklung |
| | 9999 | Sonstiges | Sonstiges Ziel |
| XP_ABEMassnahmenTypen | 1000 | BindungErhaltung | "Bindungen für Bepflanzungen und für die Erhaltung von Bäumen, Sträuchern und sonstigen Bepflanzungen sowie von Gewässern. Dies entspricht dem Planzeichen 13.2.2 der PlanzV 1990." |
| | 2000 | Anpflanzung | "Anpflanzung von Bäumen, Sträuchern oder sonstigen Bepflanzungen. Dies entspricht dem Planzeichen 13.2.1 der PlanzV 1990." |
| | 3000 | AnpflanzungBindungErhaltung | both |
| XP_AnpflanzungBindungErhaltungsGegenstand | 1000 | Baeume | Bäume |
| | 1100 | Kopfbaeume | Kopfbäume |
| | 1200 | Baumreihe | Baumreihe |
| | 1300 | Obstbaeume | Obstbäume (new in 6.1) |
| | 2000 | Straeucher | Sträucher |
| | 2050 | BaeumeUndStraeucher | Bäume und Sträucher |
| | 2100 | Hecke | Hecke |
| | 2200 | Knick | Knick |
| | 3000 | SonstBepflanzung | Sonstige Bepflanzung |
| | 4000 | Gewaesser | Gewässer (nur Erhaltung) |
| | 5000 | Fassadenbegruenung | Fassadenbegrünung |
| | 6000 | Dachbegruenung | Dachbegrünung |
| | 9999 | SonstGegenstand | Sonstiger Gegenstand (new in 6.1) |
| XP_ERFlaechenArt | 1000 | PotenzielleFlaecheKompensation | Potenzielle Fläche für Kompensation (§ 9 Abs. 3 Ziffer 4 lit. c BNatSchG) |
| | 2000 | Flaechenpool | Flächenpool |
| | 3000 | KompensationEinzelflaeche | Kompensation (Einzelfläche) |
| | 4000 | Kompensationsverzeichnis | Kompensationsverzeichnis |
| | 9999 | Sonstiges | Sonstiger Typ |

XP_HandlungsfeldNatuerlicherKlimaschutz (new 6.1): 1000 Schutz intakter Moore und Wiedervernässung; 2000 Naturnaher Wasserhaushalt mit lebendigen Flüssen, Seen und Auen; 3000 Meere und Küsten; 4000 Wildnis und Schutzgebiete; 5000 Waldökosysteme; 6000 Böden als Kohlenstoffspeicher; 7000 Natürlicher Klimaschutz auf Siedlungs- und Verkehrsflächen (V). XP_ZweckbestimmungSpielSportanlage: 1000 Sportanlage; 2000 Spielanlage; 3000 SpielSportanlage; 9999 Sonstiges (V).

#### SO_ZweckbestimmungStrassenverkehr (30): traffic surfaces incl. paths, squares, traffic green

1000 AutobahnUndAehnlich; 1200 Hauptverkehrsstrasse; 1400 SonstigerVerkehrswegAnlage; 14000 VerkehrsberuhigterBereich; 14001 Platz; 140010 UeberfuehrenderVerkehrsweg; 140011 UnterfuehrenderVerkehrsweg; 140012 Wirtschaftsweg; 140013 LandwirtschaftlicherVerkehr; 14002 Fussgaengerbereich; 14003 RadGehweg; 14004 Radweg; 14005 Gehweg; 14006 Wanderweg; 14007 ReitKutschweg; 14008 Rastanlage; 14009 Busbahnhof; 14014 Anschlussflaeche; 14015 Verkehrsgruen; 1600 RuhenderVerkehr; 16000 Parkplatz; 16001 FahrradAbstellplatz; 16002 P_RAnlage; 16003 B_RAnlage; 16004 Parkhaus; 16005 CarSharing; 16006 BikeSharing; 3400 Mischverkehrsflaeche; 3500 Ladestation; 9999 Sonstiges (V).

Others (V): SO_KlassifizGelaendemorphologie 1000 Terassenkante, 1100 Rinne, 1200 EhemMaeander, 9999 SonstigeStruktur; BP_StrassenkoerperHerstellung 1000 Aufschuettung, 2000 Abgrabung, 3000 Stuetzmauer; BP_WegerechtTypen 1000 Gehrecht, 2000 Fahrrecht, 2500 Radfahrrecht, 4000 Leitungsrecht, 9999 Sonstiges; BP_ZweckbestimmungNebenanlagen 1000 Stellplaetze, 2000 Garagen, 3000 Spielplatz, 3100 Carport, 3200 Tiefgarage, 3300 Nebengebaeude, 3400 AbfallSammelanlagen, 3500 EnergieVerteilungsanlagen, 3600 AbfallWertstoffbehaelter, 3700 Fahrradstellplaetze, 9999 Sonstiges; BP_ZweckbestimmungGemeinschaftsanlagen incl. 4200 Gemeinschaftsdachgaerten, 4300 GemeinschaftlichNutzbareDachflaechen.

### 2.4 Feature types for open space (XPlanGML 6.1, all V from the XSDs)

| Class | Definition (XSD documentation) | Key attributes | PlanZV |
|---|---|---|---|
| BP_GruenFlaeche (Flächenschlussobjekt) | Festsetzungen von öffentlichen und privaten Grünflächen (§ 9 Abs. 1 Nr. 15 BauGB) | zweckbestimmung (allgemein: XP_ZweckbestimmungGruen; detail: CodeType; textlicheErgaenzung; aufschrift), nutzungsform, zugunstenVon | 9 |
| FP_Gruen | Darstellung einer Grünfläche nach § 5 Abs. 2 Nr. 5 BauGB | zweckbestimmung, nutzungsform, zugunstenVon | 9 |
| BP_SpielSportanlagenFlaeche / FP_SpielSportanlage | Flächen für Sport- und Spielanlagen (§ 9 Abs. 1 Nr. 5) | zweckbestimmung (XP_ZweckbestimmungSpielSportanlage) | 4.2 |
| BP_LandwirtschaftsFlaeche / FP_Landwirtschaft | § 9 Abs. 1 Nr. 18a / § 5 Abs. 2 Nr. 9a | zweckbestimmung (XP_ZweckbestimmungLandwirtschaft) | 12.1 |
| BP_WaldFlaeche / FP_WaldFlaeche | § 9 Abs. 1 Nr. 18b / § 5 Abs. 2 Nr. 9b | zweckbestimmung (XP_ZweckbestimmungWald), eigentumsart, betreten | 12.2 |
| SO_Gewaesser | Planartübergreifende Klasse zur Abbildung von Gewässern | artDerFestlegung (SO_KlassifizGewaesser + detail), name, nummer | 10.1 |
| SO_Wasserwirtschaft | Flächen für die Wasserwirtschaft, Hochwasserschutzanlagen, Regelung des Wasserabflusses (§ 9 Abs. 1 Nr. 16a/16b, § 5 Abs. 2 Nr. 7) | artDerFestlegung (SO_KlassifizWasserwirtschaft), name, nummer | 10.2 |
| SO_Wasserrecht / SO_SchutzgebietWasserrecht | Festlegung nach WHG / Schutzgebiet | artDerFestlegung, zone, istNatuerlichesUberschwemmungsgebiet | 10.2/10.3 |
| BP_SchutzPflegeEntwicklungsFlaeche / -Massnahme; FP_SchutzPflegeEntwicklung | Flächen/Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Natur und Landschaft (§ 9 Abs. 1 Nr. 20 / § 5 Abs. 2 Nr. 10) | ziel (XP_SPEZiele), massnahme (XP_SPEMassnahmenDaten → XP_SPEMassnahmenTypen), istAusgleich, nutzungsform, eRFlaechenArt, refLandschaftsplan | 13.1 |
| BP_AnpflanzungBindungErhaltung (point/line/area) | § 9 Abs. 1 Nr. 25 | massnahme (XP_ABEMassnahmenTypen), gegenstand, erlaeuterung, kronendurchmesser, stammdurchmesser, pflanztiefe, pflanzenArt, mindesthoehe, anzahl, istAusgleich, eRFlaechenArt | 13.2, 13.2.1, 13.2.2 |
| BP_NatuerlicherKlimaschutz / FP_NatuerlicherKlimaschutz (new 6.1) | "Fläche zur Gewährleistung eines natürlichen Klimaschutzes (§9, Absatz 1, Nr. 15a BauGB)" / "(§5, Absatz 2, Nr. 5a BauGB)" | handlungsfeld, massnahmen | none |
| BP_AufschuettungsFlaeche / BP_AbgrabungsFlaeche; FP_Aufschuettung / FP_Abgrabung | § 9 Abs. 1 Nr. 17 / § 5 Abs. 2 Nr. 8 | aufschuettungsmaterial / abbaugut | 11.1 / 11.2 |
| BP_Strassenkoerper | § 9 Abs. 1 Nr. 26 | typ (BP_StrassenkoerperHerstellung) | 15.9 |
| SO_Strassenverkehr | Verkehrsfläche besonderer Zweckbestimmung (§ 9 Abs. 1 Nr. 11), überörtlicher Verkehr (§ 5 Abs. 2 Nr. 3), Straßenverkehrsrecht | artDerFestlegung (SO_ZweckbestimmungStrassenverkehr), einteilung, nutzungsform, begrenzungslinie | 5.1, 6.1, 6.3 |
| BP_StrassenbegrenzungsLinie | § 9 Abs. 1 Nr. 11 | bautiefe | 6.2 |
| BP_FreiFlaeche | "Umgrenzung der Flächen, die von der Bebauung freizuhalten sind ... Dies entspricht dem Planzeichen PlanZV 15.8 (Satz 1)." | nutzung | 15.8 |
| BP_Wegerecht | § 9 Abs. 1 Nr. 21 | typ, zugunstenVon, breite, istSchmal | 15.5 |
| BP_NebenanlagenFlaeche | § 9 Abs. 1 Nr. 4 | zweckbestimmung | 15.3 |
| BP_KleintierhaltungFlaeche | § 9 Abs. 1 Nr. 19 | n/a | n/a |
| BP_EingriffsBereich | Bereich, in dem ein Eingriff nach dem Naturschutzrecht zugelassen wird | n/a | n/a |
| SO_Gelaendemorphologie | "Das Landschaftsbild prägende Geländestruktur" | artDerFestlegung | n/a |
| SO_Forstrecht; SO_Bodenschutzrecht; SO_Grenze | nachrichtliche Übernahmen | see enumerations | n/a |
| FP_AnpassungKlimawandel | § 5 Abs. 2 Nr. 2c BauGB | massnahme (FP_MassnahmeKlimawandelTypen), detailMassnahme | 7 |

Open point: whether "§ 9 Abs. 1 Nr. 15a / § 5 Abs. 2 Nr. 5a BauGB" quoted by the 6.1 schema are already in force was not checked.

### 2.5 Landschaftsplan model (LP_*, "Landschaftsplan_Kernmodell", XPlanGML 6.1)

The LP model was rebuilt in 6.0 ("neues Datenmodell Landschaftsplanung", https://xleitstelle.de/node/94, S for the statement) and is small and generic: three content classes plus complex data types (all V from `XPlanGML_LPlan_Kernmodell.xsd`).

| Class (FeatureType) | Definition | Key attributes |
|---|---|---|
| LP_Plan | Planwerk mit landschaftsplanerischen gutachterlichen Aussagen, Darstellungen bzw. Festsetzungen | planArt (LP_PlanArt: 1000 Landschaftsprogramm, 2000 Landschaftsrahmenplan, 3000 Landschaftsplan, 4000 Gruenordnungsplan, 9999 Sonstiges), bundesland, rechtsstand, rechtlicheAussenwirkung ... |
| LP_Bereich | Planbereich (Kartenblatt, Teilplan ...) | n/a |
| LP_Objekt (abstract) / LP_Geometrieobjekt (abstract) | Basisklassen; point, line or area geometry | raumkonkretisierung (LP_Raumkonkretisierung: 1000 Scharf, 2000 Suchraum, 3000 Unscharf, 4000 Position, 5000 Raumunkonkret, 9998 Unbekannt), vorschlagIntegrationBLP / RO |
| **LP_ZieleErfordernisseMassnahmen** | Ziele, Erfordernisse und Maßnahmen für Naturschutz und Landschaftspflege gem. Kapitel 2 BNatSchG | zieleErfordernisseMassnahmen (LP_ZEMTyp 1000 Ziel, 2000 Erfordernis, 3000 Massnahme); schutzgut; zielDimNatSchLaPfl; adressat; schutzPflegeEntwicklung; biologischeVielfalt; boden; wasser; klima; luft; landschaftsbild; erholung; freiraeume; foerdermoeglichkeit; nutzungseinschraenkung |
| **LP_BiotopverbundBiotopvernetzung** | Flächen und Elemente für Biotopverbund und Biotopvernetzung | planungsEbene (1000 Biotopverbund, 2000 Biotopvernetzung); typBioVerbund (LP_FlaechenTypBV 1000 Kernflaeche, 2000 Verbindungsfläche, 3000 Verbindungselement; LP_FlaechenTypBVSpeziell 1000 Verbindungsraeume, 2000 Verbundachse, 3000 Wildtierkorridor, 4000 Entwicklungsflaeche, 5000 Entwicklungsmassnahme, 6000 Vernetzungselement, 7000 Trittsteinbiotop, 9999); bioVerbundsystemArt (1000 Allgemein, 2000 OffenlandHalboffenland, 3000 Wald, 4000 Gewaesser); bioVStandortFeuchte (1000 Feucht, 2000 Mittel, 3000 Trocken); rechtlicheSicherung |
| **LP_SchutzBestimmterTeileVonNaturUndLandschaft** | Schutzgebietskategorien gemäß Kapitel 4 BNatSchG | artDerFestlegung (LP_KlassifizierungNaturschutzrecht); rechtsstandSchG; gesetzlGeschBiotop (LP_GesGeschBiotopTyp); detailGesetzlGeschBiotopLR (CodeType); schutzzone |
| **LP_Eingriffsregelung** | Planungsaussagen mit Bezug zur Eingriffsregelung ... (Ausgleichs- und Ersatzmaßnahmen) | eingriffsregelungFlaechenTyp (XP_ERFlaechenArt); umsetzungsstand; massnahmentyp (LP_MassnahmenTyp: 1000 Kompensationsmassnahme, 2000 MassnahmeCEF, 3000 MassnahmeFCS, 4000 MassnahmeKohaerenzsicherung, 9998 Unbekannt) |
| LP_GenerischesObjekt, LP_TextAbschnittObjekt | catch-all / text areas | zweckbestimmung (CodeType) |

Where biotope and vegetation types live: there is **no biotope/vegetation feature class**. Biotope type is carried in the data type **LP_BioVfBiotoptypKomplex** with four attributes (V): `bioVfBiotoptyp_BKompV` (CodeType → code list "Biotoptypen-Katalog der Bundeskompensationsverordnung (Anlage 2 zu § 5 Absatz 1 BKompV)"), `bioVfBiotoptyp_LandesKS` (CodeType → Landes-Kartierschlüssel), `bioVf_FFH_LRT` (CodeType → "FFH-Lebensraumtypen gem. Anhang I der Fauna Flora Habitatrichtlinie"), `bioVfBiotoptyp_Text`. The three registry code lists exist but are EMPTY (0 items) on 2026-09-30 (V: https://registry.gdi-de.org/codelist/de.xleitstelle.xplanung/LP_BioVfBiotoptyp_BKompV etc.). → XPlanung itself names BKompV biotope types, Länder keys and FFH-LRT as the three crosswalk keys for biotopes.

LP enumerations (all V):

| Enumeration | Values |
|---|---|
| LP_SchutzgutArt | 1000 AlleSchutzgueter; 2000 ArtenLebensgemeinschaften; 3000 Biotope; 4000 Boden; 5000 Wasser; 6000 Klima; 7000 Luft; 8000 Landschaftsbild; 9000 ErholungInNaturUndLandschaft; 9998 Unbekannt; 9999 Sonstiges |
| LP_ZielDimensionTyp | 1000 SchutzBiologischeVielfalt; 2000 SchutzNaturhaushalt; 3000 SchutzLandschaftsbildErholungsvorsorge; 9998; 9999 |
| LP_SchutzPflegeEntwicklung | 1100 Schutz; 1200 Pflege; 2000 Entwicklung; 3000 Anlage; 3500 Wiederherstellung; 5100 Vermeidung; 5200 Minderung; 5300 Beseitigung; 9999 Sonstiges |
| LP_KlassifizierungNaturschutzrecht | 1000 Naturschutzgebiet; 1100 Nationalpak [sic] (Nationalpark); 1200 Biosphaerenreservat; 1300 Landschaftsschutzgebiet; 1400 Naturpark; 1500 Naturdenkmal; 1600 GeschuetzterLandschaftsBestandteil; 1700 GesetzlichGeschuetztesBiotop; 1800 Natura2000; 18000 GebietGemeinschaftlicherBedeutung; 18001 EuropaeischesVogelschutzgebiet; 2000 NationalesNaturmonument; 9999 Sonstiges |
| LP_GesGeschBiotopTyp (§ 30 BNatSchG groups) | 1000 GewaesserBiotope; 2000 FeuchtNassBiotope; 3000 TrockenBiotope; 4000 WaldBiotope; 5000 FelsenAlpinBiotope; 6000 KuestenBiotope; 9998 Unbekannt; 9999 Sonstiges |
| LP_SchutzzonenNaturschutzrecht | 1000–1200 Schutzzone_1–3; 2000 Kernzone; 2100 Pflegezone; 2200 Entwicklungszone; 2300 Regenerationszone; 9999 |
| LP_BioVfBestandteil | 1000 Art; 2000 BiotopLebensraum; 4000 LebensstaetteArthabitat; 9999 Sonstiges |
| LP_ErholungFunktionen (43) | 1000 Gruenflaechen; 1100 ParkanlageGruenanlage; 1200 Dauerkleingaerten; 1300 Sportplatz; 1400 Spielplatz; 1500 BadeplatzFreibad; 1600 Liegewiese; 2000 Erholungsinfrastruktur; 2100 Schutzhuette; 2110 Rastplatz; 2120 Informationstafel; 2130 FeuerstelleGrillplatz; 2200 Aussichtsturm; 2210 Aussichtspunkt; 2300 Angelteich; 2400 Modellflugplatz; 2410 Gleitschirmplatz; 2500 WildgehegeSchaugatter; 2600 Parkplatz; 2700 ZeltplatzCampingplatz; 2750 JugendzeltplatzEinzelcamp; 2900 ErholungsInfrastrukturBesBedeutung; 3000 WandernAllgemein; 3100 Wanderweg; 3200 Lehrpfad; 3300 Reitweg; 3400 Radweg; 4000 Wintersport; 4100 Skiabfahrt; 4200 Skilanglaufloipe; 4300 RodelbahnBobbahn; 5000 WassersportSchifffahrt; 5100 Wasserwanderweg; 5200 Schifffahrtsroute; 5300 AnlegestelleMitMotorbooten; 5310 AnlegestelleOhneMotorboote; 6000 Seilbahn; 6100 SesselliftSchlepplift; 6200 Kabinenseilbahn; 7000 Bildungsstaette; 7100 Umweltbildungsstaette; 7200 Museum; 9999 Sonstiges |
| LP_WasserAuspraegung (34) | 1100 Hochwasserschutz; 1200 Ueberschwemmungsgebiet; 1300 Hochwasservorsorge; 1310 Retentionsraum; 1320 Polderflaeche; 1400 Deichrueckverlegung; 1500 Trinkwassergewinnung; 1600 Trinkwasserschutz; 1700 Grundwasserneubildungsgebiet; 2100 LaengsdurchgaengigkeitGewaesser; 2200 MindestwasserfuehrungGewaesser; 2300 Drainage; 2400 Entwaesserungsgraben; 3100 NaturnaeheGewaesser; 3200 NaturnaheUferbereiche; 3300 OekologischeFunktionFliessgewaesser; 3400 OekologischeFunktionQuellbereich; 3500 OekologischeFunktionStillgewaesser; 3600 Gewaesserstruktur; 3700 Gewaesserdynamik; 5100 Gewaesserrandstreifen; 5200 Gewaesserschutzstreifen; 5300 Pufferzone; 5400 Ufergehoelze; 6100 FischaufstiegsAbstiegsanlage; 6200 Wehr; 6300 Verrohrung; 6400 Sohlstufe; 7100 Gewaesserguete; 7200 StoffeintraegeInGrundwasser; 7300 StoffeintraegeInOberflaechengewaesser; 8100 Versickerungsflaeche; 8200 Verlandungsbereiche; 9999 Sonstiges |
| LP_BodenAuspraegung (20) | 1110 Ablagerungen; 1120 Altablagerungsflaeche; 1130 Altlastenverdachtsflaeche; 2110 BodenFilterPufferfunktion; 2120 BodenHoheBodenfruchtbarkeit; 2130 BodenHoherFunktionglobalerKlimaschutz; 2210–2240 Boden kultur-/natur-/geowissenschaftliche Bedeutung, Extremstandort; 3100 ehemMilitaerischGenutzterStandort; 4100/4110/4120 Erosionsgefaehrdet (Wind/Wasser); 5110 Geotop; 5120 SelteneBodenform; 5210 NaturnaherBoden; 6100 BoedenHohesRetentionspotenzial; 6200 EntsiegelungWiederherstBodenfunktion; 9999 |
| LP_KlimaArt | 1000 BioklimatischeFunktion; 2000 Luftleitbahn; 3100 Frischluftbahn; 3200 Frischluftentstehungsgebiet; 4100 Kaltluftbahn; 4200 Kaltluftentstehungsgebiet; 5000 Stadtklima; 6000 THGSenkenKlimaschutzflaechen; 9999 |
| LP_LandschaftsbildArt (22) | 1100 KircheKlosterKapelle ... 2100 Aussichtspunkt; 2200 Aussichtsturm; 3100 landschaftsgerechteEinbindung; 3200 LandschaftsgerechterSiedlungsrand; 4100 Strukturvielfalt; 4200 LandschaftHoheEigenart; 5100 Landschaftsachsen; 5200 Landschaftsraeume; 6100 HistorischeWaldinsel; 6200 Waldraender; 7000 Kulturlandschaft; 7100 HistorischeKulturlandschaft; 7200 Kulturlandschaftselement; 7300 Hohlweg; 8000 Gartendenkmal; 9999 |
| LP_LuftArt | 1000 Geruchsbelastung; 2000 Laermbelastung; 3000 lufthygienischeFktStofflBelastung; 4000 Staubbelastung; 9999 |

### 2.6 De-facto visualisation colours: xPlanBox default styles (V)

Source: `xplan-workspaces/src/main/workspace/styles/xplansyn/default/{bp,fp,so,lp}/*.xml` at tag xplanbox-7.0 and `xplan-webservices/xplan-webservices-workspaces/src/main/workspace/styles/xplansyn/default/...` at tag xplanbox-9.3 (2026-07-03) of https://gitlab.opencode.de/diplanung/ozgxplanung, colours identical in both. File header: "Copyright (C) 2008 - 2023 Freie und Hansestadt Hamburg, developed by lat/lon ..."; licence GNU Affero GPL v3 (relevant if SVG symbols were copied; hex values are facts).

| XPlanung class / rule | Style | PlanZV colour name it implements |
|---|---|---|
| BP_BaugebietsTeilFlaeche / FP_BebauungsFlaeche: Wohnen | fill #CF9377 | Rot mittel |
| … gemischt (Dorf-/Misch-/Kern-/Urbanes Gebiet) | fill #D5A744 | Braun mittel |
| … gewerblich | fill #A6A596 | Grau mittel |
| … Sondergebiet | fill #FE7F26 | Orange mittel |
| BP_GemeinbedarfsFlaeche | fill #E94EA5 (outline variant #FF0070) | Karminrot mittel |
| BP_VerEntsorgung | fill #FFFF1A | Gelb hell |
| **BP_GruenFlaeche** (privat, öffentlich, ohne Nutzungsform) | fill **#7FC643**, stroke #000000 0.2 | Grün mittel |
| FP_Gruen | privat #7FC643; öffentlich / ohne Angabe **#80E41B**; Zweckbestimmung pictograms as SVG point symbols (gruenflpark_sym.svg, gruenfldakleingar_sym.svg, gruenflsportpl_sym.svg, gruenflspielpl_sym.svg, gruenflzeltpl_sym.svg, gruenflbadpl_sym.svg, gruenflfriedh_sym.svg ...) | Grün mittel |
| BP_GewaesserFlaeche (legacy) / **SO_Gewaesser** | fill **#99D9E8**; line: #99D9E8 width 4 | Blau mittel |
| FP_Gewaesser | fill #75C7FF | Blau mittel |
| BP_WasserwirtschaftsFlaeche, SO_Wasserrecht, SO_SchutzgebietWasserrecht | band stroke **#007BCE** width 3 + black 0.2 | Blau dunkel |
| **BP_LandwirtschaftsFlaeche / FP_Landwirtschaft** | fill **#CCE968** | Gelbgrün |
| **BP_WaldFlaeche / FP_WaldFlaeche** | fill **#34AB8F** | Blaugrün |
| SO_Forstrecht | fill #1AA600, dashed outline | n/a |
| BP_StrassenVerkehrsFlaeche | fill **#FFD92F** | Goldocker |
| FP_Strassenverkehr | fill #FDDF1B; ruhender Verkehr #FFEC8B | Goldocker |
| BP_VerkehrsflaecheBesondererZweckbestimmung | bitmap pattern verksflbeszwb_neu.png (striped) | Goldocker stripes |
| BP_StrassenbegrenzungsLinie | #4DAE38 width 0.8 + #000000 width 0.3 | Permanentgrün hell |
| BP_SchutzPflegeEntwicklungsFlaeche / -Massnahme, BP_AusgleichsFlaeche, Schutzgebiete (BP/SO/LP) | band stroke **#4DAE38** width 3 + SVG T-ticks (schutzpflentwfl_rs.svg / naturschutzrecht.svg) + black 0.2 | Grün dunkel |
| FP_SchutzPflegeEntwicklung | band #008000 | Grün dunkel |
| BP_AnpflanzungBindungErhaltung, Bäume | circle fill #4DAE38, black outline; inner mark filled black (Erhaltung) or unfilled (Anpflanzung); Sträucher / Sonstige: SVG symbols anpflanzbinderh*_sym.svg | Grün dunkel |
| BP_Plan (Geltungsbereich) | stroke **#80847A** width 3 (opacity 0.8) | Grau dunkel |
| BP_NebenanlagenFlaeche | #FD341F dashed (2 2) | Rot |
| BP_BauLinie / BP_BauGrenze | #FD341F / #1763AA width 0.8 + black dash-dot | Rot / Blau |
| BP_EingriffsBereich | band #CCD4C7 | n/a |
| LP_ZieleErfordernisseMassnahmen, LP_BiotopverbundBiotopvernetzung, LP_Eingriffsregelung | black outline only (no thematic colours) | n/a |

---

## 3. ALKIS / ATKIS (AAA model, GeoInfoDok 7.1)

### 3.1 Status of the standard

| Item | Value | St. | Source |
|---|---|---|---|
| GeoInfoDok is now modular; each application schema versioned separately | current schemas: AAA-Anwendungsschema (AFIS-ALKIS-ATKIS) **7.1.2**; AAA-Ausgabekatalog 2.0.0; **Landbedeckung 1.0.1**; **Landnutzung 1.0.2**; Geographische Informationen 1.0.0; Geometrische Verbesserung 1.0.0; Bodenrichtwerte 3.0.1; WFS-Erweiterungen 2.0.1 | V | https://www.adv-online.de/de/geoinfodok/aktuelle-anwendungsschemata |
| AdV reference version | "AdV-Referenzversion 7.1" with AAA-AS 7.1.2 current since 1 January 2024 (as summarised from the AdV page by the fetch tool) | V (summary) | https://www.adv-online.de/GeoInfoDok/ |
| AAA-AS 7.1.2 date | Version 7.1.2, Stand 01.11.2022 | V | ALKIS-OK DLKM 7.1.2 title page (Profil Hessen, Stand 02.01.2024): https://hvbg.hessen.de/sites/hvbg.hessen.de/files/2024-01/objektartenkataloge_zur_geolnfodok-bf.pdf |
| NAS schemas | AAA 7.1.2: https://repository.gdi-de.org/schemas/adv/nas/7.1/ ; LB: .../nas-lb/1.0/ ; LN: .../nas-ln/1.0/ | V | listed on the AdV page |
| All enumerations with labels and definitions, machine-readable (405 lists incl. AX_*, LB_*, LN_*) | register "GeoInfoDok (AdV)", owner AdV, control body AAA-Revisionsausschuss | V | https://registry.gdi-de.org/codelist/de.adv-online.gid |
| Catalogue generator (HTML/DOCX/XML/CSV per schema and Modellart) | GeoInfoDok Objektartenkatalog App (form-based download; not used in this session) | V (exists) | https://www.gid-katalog-app.org/ |

### 3.2 Objektartenbereich "Tatsächliche Nutzung" (TN): object types

Kennung + name: ALKIS-OK DLKM 7.1.2 (Profil Hessen) group lists, "vollständig und unabhängig von der gewählten Modellart" (pp. 158, 181, 196, 209), cross-checked against `featureTypeNumber` in the ALKIS-Signaturenkatalog 2.1.0 XML. Nutzungsartkennung (8-digit destatis key) and attributes: NAS `AAA-Fachschema.xsd` 7.1.2. All V.

The abstract superclass is AX_TatsaechlicheNutzung (Kennung 40001) with `datumDerLetztenUeberpruefung` (DLU), `istWeitereNutzung` (IWN; 1000 = Überlagernd) and `ergebnisDerUeberpruefung` (EDU). TN objects cover the surface "lückenlos, überschneidungsfrei und flächendeckend" unless they are overlays (IWN). Erfassungsuntergrenze in ALKIS: ca. 1 000 m² (Dominanzprinzip).

| Kennung | Class | German name | Nutzungsartkennung | Key attributes |
|---|---|---|---|---|
| **41000 Siedlung** | | | 10000000 | |
| 41001 | AX_Wohnbauflaeche | Wohnbaufläche | 11000000 | artDerBebauung, funktion, name, zustand, zweitname |
| 41002 | AX_IndustrieUndGewerbeflaeche | Industrie- und Gewerbefläche | 12000000 | funktion, name, bezeichnung, foerdergut, lagergut, primaerenergie, zustand |
| 41003 | AX_Halde | Halde | 13000000 | lagergut, name, zustand |
| 41004 | AX_Bergbaubetrieb | Bergbaubetrieb | 14000000 | abbaugut, funktion, name, bezeichnung, zustand |
| 41005 | AX_TagebauGrubeSteinbruch | Tagebau, Grube, Steinbruch | 15000000 | abbaugut, funktion, name, bezeichnung, zustand |
| 41006 | AX_FlaecheGemischterNutzung | Fläche gemischter Nutzung | 16000000 | artDerBebauung, funktion, name, zustand |
| 41007 | AX_FlaecheBesondererFunktionalerPraegung | Fläche besonderer funktionaler Prägung | 17000000 | funktion, artDerBebauung, name, zustand |
| 41008 | AX_SportFreizeitUndErholungsflaeche | Sport-, Freizeit- und Erholungsfläche | 18000000 | **funktion (FKT)**, name, zustand, bezeichnung |
| 41009 | AX_Friedhof | Friedhof | 19000000 | funktion, name, zustand |
| 41010 | AX_Siedlungsflaeche | Siedlungsfläche | n/a | artDerBebauung, funktion, name, regionalsprache |
| **42000 Verkehr** | | | 20000000 | |
| 42001 | AX_Strassenverkehr | Straßenverkehr | 21010000 | funktion (AX_Funktion_Strasse), name, zweitname, zustand |
| 42006 | AX_Weg | Weg | 21020000 | funktion, name, bezeichnung |
| 42009 | AX_Platz | Platz | 21030000 | funktion, name, strassenschluessel, zweitname, regionalsprache |
| 42010 | AX_Bahnverkehr | Bahnverkehr | 22000000 | funktion, bahnkategorie, bezeichnung, nummerDerBahnstrecke, zustand |
| 42015 | AX_Flugverkehr | Flugverkehr | 23000000 | funktion, art, name, nutzung, zustand |
| 42016 | AX_Schiffsverkehr | Schiffsverkehr | 24000000 | funktion, name, zustand |
| (42002, 42003, 42005, 42008, 42014) | Straße, Straßenachse, Fahrbahnachse, Fahrwegachse, Bahnstrecke | line/ZUSO objects of the group | n/a | n/a |
| **43000 Vegetation** | | | 30000000 | |
| 43001 | AX_Landwirtschaft | Landwirtschaft | 31000000 | **vegetationsmerkmal (VEG)**, name |
| 43002 | AX_Wald | Wald | 32000000 | vegetationsmerkmal, name, bezeichnung, zustand, nutzung, regionalsprache |
| 43003 | AX_Gehoelz | Gehölz | 33000000 | vegetationsmerkmal, name, funktion |
| 43004 | AX_Heide | Heide | 34000000 | name only |
| 43005 | AX_Moor | Moor | 35000000 | name only |
| 43006 | AX_Sumpf | Sumpf | 36000000 | name only |
| 43007 | AX_UnlandVegetationsloseFlaeche | Unland/Vegetationslose Fläche | 37000000 | **oberflaechenmaterial (OFM)**, name, funktion |
| **44000 Gewässer** | | | 40000000 | |
| 44001 | AX_Fliessgewaesser | Fließgewässer | 41000000 | funktion, name, zustand, hydrologischesMerkmal |
| 44005 | AX_Hafenbecken | Hafenbecken | 42000000 | funktion, name, nutzung, seekennzahl |
| 44006 | AX_StehendesGewaesser | Stehendes Gewässer | 43000000 | funktion, name, seekennzahl, hydrologischesMerkmal, widmung, schifffahrtskategorie, bezeichnung, wasserspiegelhoeheInStehendemGewaesser, nutzung, zustand |
| 44007 | AX_Meer | Meer | 44000000 | funktion, name, bezeichnung, tidemerkmal |
| (44002, 44003, 44004) | Wasserlauf, Kanal, Gewässerachse | line/ZUSO objects | n/a | n/a |

Definitions (verbatim, ALKIS-OK 7.1.2, V): Sport-, Freizeit- und Erholungsfläche "ist eine bebaute oder unbebaute Fläche, die dem Sport, der Freizeitgestaltung oder der Erholung dient."; Friedhof "ist eine Landfläche, die zur Bestattung dient oder gedient hat, sofern die Zuordnung zu Grünanlage nicht zutreffender ist. Waldbestattungsflächen werden der Nutzungsart Wald zugeordnet."; Gehölz "ist eine Fläche, die mit einzelnen Bäumen, Baumgruppen, Büschen, Hecken und Sträuchern bestockt ist."; Heide "ist eine Fläche mit typischen Sträuchern, Gräsern und geringwertigem Baumbestand."; Moor "ist eine unkultivierte Fläche, deren obere Schicht aus vertorften oder zersetzten Pflanzenresten besteht."; Sumpf "ist ein wassergesättigtes, zeitweise unter Wasser stehendes Gelände."; Unland/Vegetationslose Fläche "ist eine Fläche, die nicht dauerhaft landwirtschaftlich genutzt wird, wie z. B. Fels-, Sand- oder Eisflächen, Uferstreifen längs von Gewässern und Sukzessionsflächen."

### 3.3 Coded values (Wertearten)

Codes: NAS 7.1.2 XSD (complete code sets). Labels/definitions: GDI-DE register de.adv-online.gid (same code sets, cross-checked for all lists below). All V. NAK = Nutzungsartkennung where seen in the OK/XSD; "(G)" = Grunddatenbestand, "(LN)" = value qualifying for the automatic derivation of Landnutzung, as printed in the ALKIS-OK Profil Hessen (only seen for the values shown there).

#### AX_Funktion_SportFreizeitUndErholungsflaeche (FKT of 41008; 42 values)

| Code | Bezeichner | NAK | Note |
|---|---|---|---|
| 1200 | Parken | 18980000 | only as overlay (IWN 1000) |
| 4001 | Gebäude- und Freifläche Sport, Freizeit und Erholung | 18710000 | |
| 4100 | Sportanlage | 18010000 | (LN) |
| 4101 | Gebäude- und Freifläche Sport | 18017100 | |
| 4110 | Golf | 18010100 | |
| 4120 | Sportplatz | 18010200 | |
| 4130 | Rennbahn | 18010300 | |
| 4140 | Reitsport | 18010400 | |
| 4150 | Schießanlage | 18010500 | |
| 4160 | Eis-, Rollschuhbahn | 18010600 | |
| 4170 | Tennis | n.v. | |
| 4200 | Freizeitanlage | 18020000 | (LN) |
| 4210 | Zoo | 18020100 | |
| 4211 | Gebäude- und Freifläche Freizeit, Zoologie | n.v. | |
| 4220 | Safaripark, Wildpark | 18020200 | |
| 4230 | Freizeitpark | 18020300 | |
| 4235 | Kletteranlage | n.v. | |
| 4240 | Freilichtbühne | 18020500 | |
| 4250 | Freilichtmuseum | 18020600 | |
| 4260 | Autokino, Freilichtkino | 18020700 | |
| 4270 | Verkehrsübungsplatz, Testgelände, Fahrsicherheit | 18020800 | |
| 4275 | Go-Kart-Bahn | n.v. | |
| 4280 | Hundeübungsplatz | n.v. | |
| 4290 | Modellfluggelände | 18021100 | |
| 4295 | Gelände für Luftsportgeräte | n.v. | |
| 4300 | Erholungsfläche | 18030000 | (LN) |
| 4301 | Gebäude- und Freifläche Erholung | n.v. | |
| 4310 | Wochenend- und Ferienhausfläche | 18030100 | (LN) |
| 4320 | Schwimmen | 18030200 | (LN) |
| 4321 | Gebäude- und Freifläche Erholung, Bad | n.v. | |
| 4330 | Campingplatz | 18030300 | (LN) |
| 4331 | Gebäude- und Freifläche Erholung, Camping | n.v. | |
| **4400** | **Grünanlage**: "eine Anlage mit Bäumen, Sträuchern, Rasenflächen, Blumenrabatten und Wegen. Sie dient der Erholung einschließlich spielerischer Aktivitäten oder erfüllt stadtgestalterische Aufgaben." | 18040000 | (G) (LN) |
| 4410 | Siedlungsgrünfläche, "unbebaute Wiese, Rasenfläche und Parkanlage in Städten und Siedlungen" | n.v. | |
| 4420 | Park, "landschaftsgärtnerisch gestaltete Grünanlage, die der Repräsentation und der Erholung dient" | 18040200 | |
| 4430 | Botanischer Garten | n.v. | |
| 4431 | Gebäude- und Freifläche Grünanlage, Botanik | n.v. | |
| 4440 | Kleingarten (Schrebergarten) | 18040400 | |
| 4450 | Wochenendplatz | 18040500 | |
| 4460 | Garten, "Flächen, die nicht im unmittelbaren Zusammenhang mit Wohnbauflächen stehen und nicht dem Bundeskleingartengesetz unterliegen ..." | 18040600 | |
| 4470 | Spielplatz, Bolzplatz | n.v. | |
| 9999 | Sonstiges | n.v. | |

#### AX_Funktion_Friedhof (41009), AX_Funktion_Platz (42009), AX_Funktion_Strasse (42001), AX_Funktion_Weg (42006)

| List | Values |
|---|---|
| AX_Funktion_Friedhof | 1200 Parken; 9401 Gebäude- und Freifläche Friedhof; 9402 Friedhof (ohne Gebäude); 9403 Parkfriedhof; 9404 Historischer Friedhof |
| AX_Funktion_Platz | 5130 Fußgängerzone; 5310 Parkplatz; 5320 Rastplatz; 5330 Raststätte, Autohof; 5340 Marktplatz; 5350 Festplatz; 5360 Busbahnhof; 5370 Caravan-, Wohnmobilstellplatz |
| AX_Funktion_Strasse | 2311 Gebäude- und Freifläche zu Verkehrsanlagen, Straße; 2312 Begleitfläche Straßenverkehr; 2313 Straßenentwässerungsanlage; 2314 Betriebsfläche Straßenverkehr; 2315 Fahrbahn; 5130 Fußgängerzone (NAK 21010400) |
| AX_Funktion_Weg | 5210 Fahrweg; 5211 Hauptwirtschaftsweg; 5212 Wirtschaftsweg; 5220 Fußweg; 5230 Gang; 5240 Radweg; 5250 Rad- und Fußweg; 5260 Reitweg; 5270 Begleitfläche Weg; 9999 Sonstiges |

#### AX_Vegetationsmerkmal_Landwirtschaft (VEG of 43001; 17 values)

| Code | Bezeichner | NAK | Note |
|---|---|---|---|
| 1010 | Ackerland | 31010000 | |
| 1011 | Streuobstacker | 31010100 | |
| 1012 | Hopfen | 31010200 | |
| 1013 | Spargel | n.v. | |
| 1014 | Hanf | n.v. | |
| 1020 | Grünland, "Grasfläche, die gemäht oder beweidet wird" | 31020000 | |
| 1021 | Streuobstwiese | 31020100 | |
| 1022 | Salzweide | n.v. | |
| 1030 | Gartenbauland | 31030000 | |
| 1031 | Baumschule | 31030100 | |
| 1040 | Rebfläche | 31040000 | |
| 1050 | Obst- und Nussplantage | 31050000 | |
| 1051 | Obst- und Nussbaumplantage | n.v. | |
| 1052 | Obst- und Nussstrauchplantage | n.v. | |
| 1060 | Weihnachtsbaumkultur | 31060000 | (LN) |
| 1100 | Kurzumtriebsplantage | 31100000 | |
| 1200 | Brachland | 31200000 | |

#### Wald, Gehölz, Unland, Gewässer

| List | Values |
|---|---|
| AX_Vegetationsmerkmal_Wald (VEG of 43002) | 1100 Laubholz; 1200 Nadelholz; 1300 Laub- und Nadelholz; 1310 Laubholz mit Nadelbäumen; 1320 Nadelholz mit Laubbäumen |
| AX_Nutzung_Wald (NTZ) | 1000 Forstwirtschaftsfläche (LN); 2000 Unbewirtschaftet; 3000 Waldbestattungsfläche (LN) |
| AX_Zustand_Wald (ZUS) | 6100 Verjüngungs-, Neuanpflanzungsfläche; 7100 Dauerhaft unbestockt |
| AX_Vegetationsmerkmal_Gehoelz (VEG of 43003) | 1400 Latschenkiefer (only value) |
| AX_Funktion_Gehoelz | 1000 Windschutz (only value) |
| AX_Heide, AX_Moor, AX_Sumpf | no coded attribute (name only) |
| AX_Funktion_UnlandVegetationsloseFlaeche (FKT of 43007) | 1000 Vegetationslose Fläche (NAK 37010000); 1100 Gewässerbegleitfläche (37020000); 1110 Bebaute Gewässerbegleitfläche; 1120 Unbebaute Gewässerbegleitfläche; 1200 Sukzessionsfläche (37030000); 1300 Naturnahe Fläche (37040000) |
| AX_Oberflaechenmaterial_UnlandVegetationsloseFlaeche (OFM; only with FKT 1000) | 1010 Fels; 1020 Steine, Schotter; 1030 Geröll; 1040 Sand; 1110 Schnee; 1120 Eis, Firn |
| AX_Funktion_Fliessgewaesser (44001) | 8200 Fluss; 8210 Altwasser; 8220 Altarm; 8230 Flussmündungstrichter; 8300 Kanal; 8400 Graben; 8410 Fleet; 8500 Bach |
| AX_Funktion_StehendesGewaesser (44006) | 8610 See; 8620 Teich; 8630 Stausee; 8631 Speicherbecken; 8640 Baggersee; 9999 Sonstiges |
| AX_HydrologischesMerkmal_Fliessgewaesser / _StehendesGewaesser | 2000 Nicht ständig Wasser führend |
| AX_Oberflaechenmaterial_Strasse (attribute `oberflaechenmaterial` of **AX_Strassenachse** (42003) and **AX_Fahrbahnachse** (42005), V, NAS XSD) | 1220 Beton; 1230 Bitumen, Asphalt; 1240 Pflaster; 1250 Gestein, zerkleinert |
| AX_Oberflaechenmaterial_Flugverkehrsanlage (attribute of AX_Flugverkehrsanlage) | codes 1210, 1220, 1230 (V); labels not fetched, by analogy and by the ATKIS-SK10 texts "Gras, Rasen" / "Beton" / "Bitumen, Asphalt" (S) |
| AX_Befestigung_Fahrwegachse (AX_Fahrwegachse.befestigung); AX_Befestigung_WegPfadSteig | 1000, 2000 (V); WegPfadSteig labels: 1000 Befestigt, 2000 Unbefestigt (V) |

#### 3.3b Complete Nutzungsartkennungen (NAK) per Werteart (V; read from the `AAA:Nutzungsartkennung` tagged values in the NAS 7.1.2 XSD: this supersedes the "n.v." entries in the tables above)

| List | code = NAK |
|---|---|
| AX_Funktion_SportFreizeitUndErholungsflaeche | 1200=18980000; 4001=18710000; 4100=18010000; 4101=18017100; 4110=18010100; 4120=18010200; 4130=18010300; 4140=18010400; 4150=18010500; 4160=18010600; 4170=18010700; 4200=18020000; 4210=18020100; 4211=18020171; 4220=18020200; 4230=18020300; 4235=18020400; 4240=18020500; 4250=18020600; 4260=18020700; 4270=18020800; 4275=18020900; 4280=18021000; 4290=18021100; 4295=18021200; 4300=18030000; 4301=18037100; 4310=18030100; 4320=18030200; 4321=18030271; 4330=18030300; 4331=18030371; **4400=18040000; 4410=18040100; 4420=18040200; 4430=18040300**; 4431=18040371; **4440=18040400; 4450=18040500; 4460=18040600; 4470=18040700**; 9999=18050000 |
| AX_Funktion_Friedhof | 1200=19980000; 9401=19710000; 9402=19010000; 9403=19020000; 9404=19030000 |
| AX_Funktion_Strasse | 2311=21017100; 2312=21010200; 2313=21010201; 2314=21010300; 2315=21010100; 5130=21010400 |
| AX_Funktion_Weg | 5210=21020100; 5211=21020101; 5212=21020102; 5220=21020200; 5230=21020300; 5240=21020400; 5250=21020500; 5260=21020600; 5270=21020700; 9999=21020800 |
| AX_Funktion_Platz | 5130=21030100; 5310=21030200; 5320=21030300; 5330=21030400; 5340=21030500; 5350=21030600; 5360=21030700; 5370=21030800 |
| AX_Vegetationsmerkmal_Landwirtschaft | 1010=31010000; 1011=31010100; 1012=31010200; 1013=31010300; 1014=31010400; 1020=31020000; 1021=31020100; 1022=31020200; 1030=31030000; 1031=31030100; 1040=31040000; 1050=31050000; 1051=31050100; 1052=31050200; 1060=31060000; 1100=31100000; 1200=31200000 |
| AX_Funktion_UnlandVegetationsloseFlaeche | 1000=37010000; 1100=37020000; 1110=37020100; 1120=37020200; 1200=37030000; 1300=37040000 |
| AX_Funktion_Fliessgewaesser | 8200=41010000; 8210=41010100; 8220=41010200; 8230=41010300; 8300=41020000; 8400=41030000; 8410=41030100; 8500=41040000 |
| AX_Funktion_StehendesGewaesser | 8610=43010000; 8620=43020000; 8630=43010100; 8631=43010101; 8640=43010200; 9999=43030000 |

The 8-digit NAK ("wie sie von destatis festgelegt ist", ALKIS-OK) is the most stable single crosswalk key for ALKIS land use: it is unique across object type + Werteart and is the key of the official area statistics (Flächenerhebung nach Art der tatsächlichen Nutzung).

### 3.4 AX_Vegetationsmerkmal (Kennung 54001): "Besondere Vegetationsmerkmale" (point/line/area overlay)

Kennung V (ALKIS-SK 2.1.0 XML `featureTypeNumber` 54001). Attributes (NAS XSD, V): `bewuchs` (BWS), `zustand`, `funktion`, `name`, `bezeichnung`, `breiteDesObjekts`.

| AX_Bewuchs_Vegetationsmerkmal | Bezeichner |
|---|---|
| 1011 | Nadelbaum |
| 1012 | Laubbaum |
| 1020 | Baumbestand |
| 1021 | Baumbestand, Laubholz |
| 1022 | Baumbestand, Nadelholz |
| 1023 | Baumbestand, Laub- und Nadelholz |
| 1100 | Hecke |
| 1101 / 1102 / 1103 | Heckenkante, rechts / Heckenkante, links / Heckenmitte |
| 1210 | Baumreihe, Laubholz |
| 1220 | Baumreihe, Nadelholz |
| 1230 | Baumreihe, Laub- und Nadelholz |
| 1250 | Gehölz |
| 1260 | Gebüsch |
| 1300 | Schneise |
| 1400 | Röhricht, Schilf |
| 1500 | Gras |
| 1510 | Rain |
| 1600 | Zierfläche |
| 1700 | Korbweide |
| 1800 | Reet |
| 1900 | Streuobst |

AX_Zustand_Vegetationsmerkmal: 5000 Nass; 6100 Waldverjüngungs-, Neuanpflanzungsfläche. AX_Funktion_Vegetationsmerkmal: 1000 Windschutz (V).

### 3.5 Bauwerke, Einrichtungen, Relief (selection)

Kennungen: 51000 group list V (ALKIS-OK Profil Hessen p. 222); 53xxx, 55xxx, 61xxx V via ALKIS-SK 2.1.0 XML `featureTypeNumber`; AX_Boeschungsflaeche 61002 = R (not contained in the SK XML or the Hessen profile).

| Kennung | Class | Coded attribute | Values |
|---|---|---|---|
| 51006 | AX_BauwerkOderAnlageFuerSportFreizeitUndErholung | bauwerksfunktion (BWF) | 1410 Spielfeld; 1411 Hartplatz; 1412 Rasenplatz; 1420 Rennbahn, Laufbahn, Geläuf; 1430 Zuschauertribüne; 1431 …, überdacht; 1432 …, nicht überdacht; 1440 Stadion; 1441/1442 Stadion überdacht / nicht überdacht; 1450 Schwimmbecken; 1460 Liegewiese; 1470 Sprungschanze (Anlauf); 1480 Schießanlage; 1490 Gradierwerk; 1510 Wildgehege; 1610 Zoo; 1620 Safaripark, Wildpark; 1630 Freizeitpark; 1640 Freilichtbühne; 1650 Wassersportanlage; 9999 Sonstiges |
| | | sportart | 1010 Ballsport; 1011 Fußball; 1020 Leichtathletik; 1030 Tennis; 1040 Reiten; 1050 Schwimmen; 1060 Ski; 1070 Eissport, Rollschuhlaufen; 1071 Eislauf, Eishockey; 1072 Rollschuhlaufen; 1080 Skating; 1090 Motorrennsport; 1100 Radsport; 1110 Pferderennsport; 1115 Hunderennsport; 1120 Hundesport |
| 51009 | AX_SonstigesBauwerkOderSonstigeEinrichtung | bauwerksfunktion | 1610 Überdachung; 1611 Carport; 1620 Treppe; 1621 Freitreppe; 1622 Rolltreppe; 1630 Treppenunterkante; 1640 Kellereingang (1641 offen, 1642 geschlossen); 1650 Rampe; 1670 Terrasse; **1700 Mauer** (1701 Mauerkante rechts, 1702 links, 1703 Mauermitte); **1720 Stützmauer** (1721/1722/1723); **1740 Zaun**; 1750 Gedenkstätte, Denkmal, Denkstein, Standbild; 1760 Bildstock, Wegekreuz, Gipfelkreuz (1761/1762/1763); 1770 Meilenstein, historischer Grenzstein; 1780 Brunnen; 1781 Brunnen (Trinkwasserversorgung); 1782 Springbrunnen, Zierbrunnen; 1783 Ziehbrunnen; 1790 Spundwand; 1791 Höckerlinie; 9999 Sonstiges |
| 51010 | AX_EinrichtungInOeffentlichenBereichen | art | 1100 Kommunikationseinrichtung … 1350 Bushaltestelle; 1500 Bahnübergang, Schranke; 1510 Tor; 1600 Laterne, Kandelaber (1610–1650); 1700 Säule, Werbefläche; 1910 Fahnenmast; 2100 Straßensinkkasten; 2200 Müllbox; 2300 Kehrichtgrube; 2400 Uhr; 2500 Richtscheinwerfer; 2600 Flutlichtmast; 9999 (35 values in total) |
| 53002 | AX_Strassenverkehrsanlage | art | 1000 Fahrbahn; 1010 Fahrbahnbegrenzungslinie; 1011 …, überdeckt; 2000 Furt; 3000 Autobahnknoten; 3001 Kreuz; 3002 Dreieck; 3003 Anschlussstelle, Anschluss; 4000 Platz; 5330 Raststätte, Autohof; 6000 Busbahnhof; 9999 |
| 53003 | AX_WegPfadSteig | art | 1103 Fußweg; 1105 Karren- und Ziehweg; 1106 Radweg; 1107 Reitweg; 1108 Wattenweg; 1109 (Kletter-)Steig im Gebirge; 1110 Rad- und Fußweg; 1111 Skaterstrecke |
| | | befestigung | 1000 Befestigt; 2000 Unbefestigt |
| 55001 | AX_Gewaessermerkmal | art | 1610 Quelle; 1620 Wasserfall; 1630 Stromschnelle; 1640 Sandbank; 1650 Watt; 1660 Priel; 1700 Bodden, Haff; 9999 |
| 55002 | AX_UntergeordnetesGewaesser | funktion, lageZurErdoberflaeche, hydrologischesMerkmal | (values not extracted) |
| 61001 | AX_BoeschungKliff (ZUSO) | zustand | 2400 Befestigt; 2500 Unbefestigt; plus objekthoehe, name |
| 61002 (R) | AX_Boeschungsflaeche | n/a | no attributes (geometry part of the Böschung) |
| 61003 | AX_DammWallDeich | art | 1910 Hochwasserdeich; 1920 Hauptdeich, Landesschutzdeich; 1930 Überlaufdeich; 1940 Leitdeich; 1950 Polderdeich; 1960 Schlafdeich; 1970 Mitteldeich; 1980 Binnendeich; 1990 Wall (1991/1992/1993); **2000 Knick** (2001/2002/2003); 2010/2011 Graben mit Wall rechts/links; 2012/2013 Graben mit Knick rechts/links |
| | | funktion | 3001 Hochwasserschutz, Sturmflutschutz; 3002 Verkehrsführung; 3003 beides; 3004 Lärmschutz |
| 61005 / 61006 / 61007 | AX_Hoehleneingang / AX_FelsenFelsblockFelsnadel / AX_Duene | n/a | n/a |

### 3.6 What changed with GeoInfoDok 7.1: Landbedeckung / Landnutzung

Verified facts:

1. Two NEW, separate application schemas exist next to the AAA schema: **Landbedeckung (LB) 1.0.1** and **Landnutzung (LN) 1.0.2** (own namespaces `.../adv/lb/1.0`, `.../adv/ln/1.0`; classes derive from TA_SurfaceComponent) (V: NAS-LB/NAS-LN XSD).
2. The AAA-AS 7.1.2 itself KEEPS the combined "Tatsächliche Nutzung" classes (41001–44007). The object catalogue adds per class a line "Landnutzung: Ja" ("Kennzeichnung für das verpflichtende Mapping in die Landnutzung") and marks Wertearten "die sich zur automatisierten Ableitung der Landnutzung qualifizieren" with "(LN)" (V: ALKIS-OK 7.1.2 Teil A, pp. 8–14). AA_Fachdatenverbindung types "Mapping für Landnutzung" (2600) and "Erweitertes Mapping für Landnutzung" (2610) exist in the Hessen profile (V).
3. AX_Siedlungsflaeche (41010) is part of the 41000 group; there is no AX_FlaecheZurZeitUnbestimmbar in the 7.1.2 NAS schema and the 43000 group list ends at 43007 (V). Whether these are changes against 6.0.1 was not compared in this session (R: 43008 existed in 6.0).

**Landbedeckung 1.0.1, 9 classes** (V, `lb.xsd`):

| Class | Attributes and values |
|---|---|
| LB_Hochbau | n/a |
| LB_Tiefbau | n/a |
| LB_Festgestein | n/a |
| LB_Lockermaterial | oberflaechenmaterial: 1000 Geröll, Schotter, Kies; 2000 Sand, Feinkies; 3000 Erdreich; 4000 Ton, Schluff; 5000 künstlich. wassersaettigung: 1000 ganzjährig; 2000 zeitweilig |
| LB_HolzigeVegetation | vegetationsmerkmal: 4000 Bäume; 5000 Gehölz; 6000 Büsche, Sträucher; 7000 Zwergsträucher. blattform: 1000 Laub; 2000 Nadel (0..2). wassersaettigung: 1000/2000. verjuengungsflaeche: boolean |
| LB_KrautigeVegetation | vegetationsmerkmal: 1000 Gras; 2000 Röhricht, Schilf; 3000 Getreide, Staudengewächse, Farne. wassersaettigung: 1000/2000. salzigerStandort: boolean |
| LB_Binnengewaesser | gewaesserart: 1010 Fluss; 1020 Bach; 2000 Altwasser, Altarm; 3010 Kanal; 3020 Graben; 4000 Becken; 5000 See, Teich. fliesseigenschaft: 1000 fließend; 2000 stehend. wasserfuehrung: 1000 ganzjährig; 2000 zeitweilig |
| LB_Meer | meerart: 1010 Watt; 1020 Haff, Bodden; 1030 Priel. tideeinfluss: boolean |
| LB_Eis | eisart: 2010 Gletscher; 2020 Dauerschnee, Firn |

Common attributes of LB_Landbedeckung: artDerErhebung (1000 Übernahme amtlicher Vermessungsdaten; 2000 Gebietstopograph, Terrestrische Außendiensterhebung; 3100 manuelle Interpretation Fernerkundung; 3200 automatische Analyse Fernerkundung; 4000 Übernahme von amtlichen Daten dritter Seite; 5000 Übernahme von nicht-amtlichen Daten), geometrischeGenauigkeit, bodenaufloesung, aktualitaetsstand.

**Landnutzung 1.0.2, 22 classes** (V, `ln.xsd`): LN_Wohnnutzung; LN_IndustrieUndVerarbeitendesGewerbe; LN_GewerblicheDienstleistungen; LN_VersorgungUndEntsorgung; LN_Lagerung; LN_Abbau; LN_OeffentlicheEinrichtungen; LN_KulturUndUnterhaltung; **LN_Sportanlage**; **LN_Freizeitanlage**; **LN_FreiluftUndNaherholung**; **LN_Bestattung**; LN_StrassenUndWegeverkehr; LN_Bahnverkehr; LN_Flugverkehr; LN_Schiffsverkehr; LN_Landwirtschaft; LN_Forstwirtschaft; LN_AquakulturUndFischereiwirtschaft; LN_Wasserwirtschaft; LN_Schutzanlage; **LN_OhneNutzung**. Common: istWeitereNutzung (1000 Überlagernd), ergebnisDerUeberpruefung, mappingannahme.

| LN list | Values |
|---|---|
| LN_Art_FreiluftUndNaherholung | 4400 Grünanlage; 4410 Siedlungsgrünfläche; 4420 Park; 4430 Botanischer Garten; 4440 Kleingarten; 4450 Wochenendplatz; 4470 Spielplatz, Bolzplatz; 4480 Zierfläche |
| LN_Art_Freizeitanlage | 4210 Zoo; 4220 Safaripark, Wildpark; 4230 Freizeitpark; 4240 Freilichtbühne; 4250 Freilichtmuseum; 4260 Autokino, Freilichtkino; 4270 Modellfluggelände; 4310 Festplatz; 4320 Freizeitbad; 4330 Campingplatz; 4340 Kletteranlage; 4350 Gelände für Luftsportgeräte; 4360 Go-Kart-Bahn; 4370 Hundeübungsplatz |
| LN_Sportart_Sportanlage | 1010 Ballsport; 1011 Fußball; 1012 Golf; 1013 Tennis; 1020 Leichtathletik; 1030 Wassersport; 1040 Schwimmen; 1050 Ski; 1060 Motorrennsport; 1070 Eislauf, Eishockey; 1080 Rollschuhlaufen, Skating; 1110 Radsport; 1120 Pferdesport; 1130 Schießen |
| LN_ArtDerBestattungsflaeche_Bestattung | 1000 Friedhof; 2000 Waldbestattungsfläche; 3000 historischer Friedhof; 4000 Parkfriedhof |
| LN_Funktion_StrassenUndWegeverkehr | 5110 Straßen- und Wegeverkehrsfläche; 5111 Fahrbahn; 5112 Begleitfläche Straßen- und Wegeverkehr; 5120 Betriebsfläche Straßen- und Wegeverkehr; 5130 Rastplatz; 5140 Raststätte, Autohof; 5150 Parkplatz; 5160 Marktplatz; 5170 Busbahnhof; 5180 Caravan-, Wohnmobilstellplatz; fussgaengerzone: 5130 Fußgängerzone; artDesParkplatzes: 1000 Öffentlich, 2000 Nutzungsbezogen |
| LN_Bewirtschaftung_Landwirtschaft | 1010 Ackerland; 1011 Streuobstacker; 1012 Hopfen; 1013 Spargel; 1014 Hanf; 1020 Mahd- und Weideland; 1021 Streuobstwiese; 1030 Gartenbauland; 1040 Rebfläche; 1050 Obst- und Nussplantage; 1060 Kurzumtriebsplantage; 1070 Baumschule; 1080 Weihnachtsbaumkultur; 1200 Brachland; 1300 Betriebsfläche Landwirtschaft |
| LN_Art_Forstwirtschaft | 6100 Forstwirtschaftsfläche; 6200 Betriebsfläche Forstwirtschaft |
| LN_Art_Wasserwirtschaft | 7100 Wasserregulierung; 7110 Stauung; 7120 Speicherung; 7130 Niederschlagrückhalt; 7200 Entwässerung |
| LN_Funktion_Schutzanlage | 5510 Hochwasserschutz (Damm, Wall, Deich, Schutzwand, Schutzmauer); 5520 Polder; 5530 Lärmschutz (Wall, Schutzwand); 5540 Windschutz (Hecke, Knick) |

Caution: LN codes are NOT the same as AAA TN codes (e.g. Modellfluggelände 4290 in AAA vs 4270 in LN; Campingplatz 4330 in both; Weihnachtsbaumkultur 1060 in AAA vs 1080 in LN). Crosswalks must be keyed by list name + code.

---

## 4. Official German map colours (numeric)

### 4.1 ALKIS-Signaturenkatalog (AdV AAA-SK 2.1, ALKIS Farbausgabe 2.1.0, Stand 01.10.2024)

Sources (V): overview https://www.adv-online.de/de/geoinfodok/aaa-signaturenkatalog-21-alkis-und-atkis ; HTML https://sg.geodatenzentrum.de/web_public/adv/sk/v2.1/alkis/docAlkisFB/SymbologyCatalog.html ; colour table .../docAlkisFB/html/ColorTable-SYCALFB1.html ; XML https://sg.geodatenzentrum.de/web_public/adv/sk/v2.1/alkis/XML/FB.xml (8.4 MB, 1039 rules; scale range 1:500–1:1000; "GeoInfoDok Version 7.1.2"). The AAA-SK 2.1 "beziehen sich ausschließlich auf die Geobasisdaten ... des AAA-Anwendungsschemas 7.1.2".

Colour table of the ALKIS-SK (complete; RGB and CMYK in percent as published, plus the published web hex):

| ID | Name | RGB % | CMYK % | Web |
|---|---|---|---|---|
| COL00001 | Weiß | 100/100/100 | 0/0/0/0 | #ffffff |
| COL00002 | Grau5 | 70/70/70 | 30/30/30/0 | #b3b3b3 |
| COL00003 | Grau3 | 90/90/90 | 10/10/10/0 | #e6e6e6 |
| COL00004 | Schwarz | 0/0/0 | 0/0/0/100 | #000000 |
| COL00005 | Rot2 | 96/52/50 | 4/48/50/0 | #f58580 |
| COL00006 | Rot | 99/88/88 | 1/12/12/0 | #fde1e1 |
| COL00007 | Grau2 | 96/96/96 | 4/4/4/0 | #f5f5f5 |
| COL00008 | Braun | 95/89/79 | 5/11/21/0 | #f3e3ca |
| COL00009 | Grün2 | 86/90/76 | 14/10/24/0 | #dce6c2 |
| COL00010 | Grün | 95/96/80 | 5/4/20/0 | #f3f5cc |
| COL00011 | Ocker | 100/97/86 | 0/3/14/0 | #fff8dc |
| COL00012 | Blau | 75/91/98 | 25/9/2/0 | #c0e8fa |
| COL00013 | Grün3 | 81/91/85 | 19/9/15/0 | #cfe8d9 |
| COL00014 | Blau5 | 0/41/63 | 100/59/37/0 | #0068a1 |
| COL00015 | Braun4 | 50/36/23 | 50/64/77/0 | #805c3a |
| COL00016 | Grau6 | 60/60/60 | 40/40/40/0 | #999999 |
| COL00017 | Grau | 100/99/94 | 0/1/6/0 | #fffdf0 |
| COL00018 | Grau4 | 80/80/80 | 20/20/20/0 | #cccccc |
| COL00019 | Grün7 | 0/51/19 | 100/49/81/0 | #008230 |
| COL00020 | Braun2 | 84/78/69 | 16/22/31/0 | #d7c7b0 |
| COL00021 | Orange | 100/85/60 | 0/15/40/0 | #ffd999 |
| COL00022 | Gelb | 100/98/64 | 0/2/36/0 | #fffaa3 |
| COL00023 | Grün6 | 32/68/49 | 68/32/51/0 | #51ae7d |
| COL00024 | Blau2 | 56/85/96 | 44/15/4/0 | #8fd9f5 |
| COL00025 | Violett | 86/44/63 | 14/56/37/0 | #dc70a1 |
| COL00026 | Braun3 | 83/58/53 | 17/42/47/0 | #d49487 |
| COL00027 | Grün4 | 57/77/52 | 43/23/48/0 | #91c585 |
| COL00028 | Gelb2 | 100/94/0 | 0/6/100/0 | #fff000 |
| COL00029 | Blau3 | 0/71/92 | 100/29/8/0 | #00b5eb |
| COL00030 | Blau4 | 0/60/100 | 100/40/0/0 | #0099ff |
| COL00031 | Rot3 | 89/4/9 | 11/96/91/0 | #e30a17 |
| COL00032 | Grün5 | 58/77/48 | 42/23/52/0 | #94c57a |
| COL00033 | Ocker2 | 84/70/32 | 16/30/68/0 | #d7b351 |

Area fills of the TN classes, group Siedlung (V, from the rules in FB.xml; "sig" = Signaturnummer):

| Object type / condition | Area signature | Fill colour | Additional symbol |
|---|---|---|---|
| 41001 Wohnbaufläche; 41006 Fläche gemischter Nutzung (default); 41007 Fläche besonderer funktionaler Prägung | sig 1401 | "Rot" COL00006 #fde1e1 | TN boundary line sig 2515 "Grau5" #b3b3b3 |
| 41002 Industrie- und Gewerbefläche; 41003 Halde; 41004 Bergbaubetrieb; 41005 Tagebau, Grube, Steinbruch; 41006 with FKT 3000–3003, 6800–6830, 7600 (land-/forst-/fischereiwirtschaftliche Betriebsflächen) | sig 1403 | "Grau2" COL00007 #f5f5f5 | point symbols 3401–3407 (Tankstelle, Förderanlage, Kraftwerk, Umspannstation, Bergbau ...) |
| 41005 Tagebau ... with Abbaugut 4010 (Torf) | sig 1404 | "Braun" COL00008 #f3e3ca | |
| **41008 Sport-, Freizeit- und Erholungsfläche; 41009 Friedhof** | sig 1405 | **"Grün2" COL00009 #dce6c2** | see below |

Point symbols (area-filling/pattern or single symbol) inside 41008 by FKT (V): Grünanlage / Siedlungsgrünfläche (4400, 4410) sig 3413 in "Grün7" #008230; Park (4420) sig 3415 (Grün7); Garten (4460) sig 3421 (Grün7); Kleingarten (4440) sig 3419; Spielplatz, Bolzplatz (4470) sig 3423; Botanischer Garten (4430, 4431) sig 3417; Zoo (4210, 4211) sig 3410; Safaripark, Wildpark (4220) sig 3411; Campingplatz (4330, 4331) sig 3412; other functions (Sportanlage, Golf, Erholungsfläche, Schwimmen ...) are labelled by text (sig 4140).

#### 4.1b ALKIS-SK: Verkehr, Vegetation, Gewässer, Vegetationsmerkmal, Bauwerke (all V, from the rules in FB.xml)

| Object type / condition | Area signature / fill | Boundary | Symbol inside (point signature, colour) |
|---|---|---|---|
| 42001 Straßenverkehr, 42006 Weg, 42009 Platz, 42010 Bahnverkehr, 42016 Schiffsverkehr (default) | **no fill** (paper white) | sig 2515 "Grau5" #b3b3b3; "im Bau": sig 2516 "Grau4" #cccccc | n/a |
| 42001 FKT 2312 Begleitfläche Straßenverkehr, 2313 Straßenentwässerungsanlage; 42010 FKT 2322 Begleitfläche Bahnverkehr; 42006 FKT 5270 Begleitfläche Weg; 42015 Flugverkehr | sig 1406 "Grün" COL00010 **#f3f5cc** | n/a | Hubschrauberlandeplatz 3438, Segelfluggelände 3439 |
| Fußgängerzone (42001 or 42009 with FKT 5130) | sig 1414 "Grün3" COL00013 #cfe8d9 | n/a | n/a |
| 42009 Parkplatz (5310) / Rastplatz (5320) / Raststätte, Autohof (5330) | no fill | 2515 | 3432 / 3434 / 3436 in "Blau4" #0099ff |
| 42006 Fußweg, Gang (5220, 5230) / Radweg (5240) / Rad- und Fußweg (5250) / Reitweg (5260) | no fill | 2515 | 3424 / 3426 / 3428 / 3430 (Blau4) |
| 43001 Landwirtschaft, VEG 1010–1014 or empty (Ackerland, Streuobstacker, Hopfen, Spargel, Hanf) | sig 1409 "Ocker" COL00011 **#fff8dc** | 2515 | Streuobstacker 3440, Hopfen 3442, Spargel 3444 |
| 43001 VEG 1020–1100 (Grünland, Streuobstwiese, Salzweide, Gartenbauland, Baumschule, Rebfläche, Obst- und Nussplantagen, Weihnachtsbaumkultur, Kurzumtriebsplantage) | sig 1406 "Grün" COL00010 **#f3f5cc** | 2515 | Grünland **3413** (same symbol as Grünanlage); Streuobstwiese 3441; Salzweide 3660; Gartenbauland 3421 (same as Garten); Baumschule 3446; Rebfläche 3448; Obst-/Nussplantage 3450 / 3452 / 3454; Weihnachtsbaumkultur 3661; Kurzumtriebsplantage 3662, all in "Grün7" #008230 |
| 43001 VEG 1200 Brachland | sig 1404 "Braun" COL00008 #f3e3ca | 2515 | n/a |
| 43002 Wald | sig 1414 "Grün3" COL00013 **#cfe8d9** | sig 2517 "Grün7" #008230 | Wald 3456; Laubholz 3458; Nadelholz 3460; Laub- und Nadelholz (1300/1310/1320) 3462 (Grün7) |
| 43003 Gehölz | sig 1414 "Grün3" #cfe8d9 | 2517 Grün7 | Gehölz 3470; Latschenkiefer 3472 |
| 43004 Heide | sig 1404 "Braun" **#f3e3ca** | n/a | 3474 (Grün7) |
| 43005 Moor | sig 1404 "Braun" #f3e3ca | n/a | 3476 (Grün7) |
| 43006 Sumpf | sig 1404 "Braun" #f3e3ca | n/a | 3478 ("Blau5" #0068a1) |
| 43007 Unland, FKT 1000 Vegetationslose Fläche | no fill | n/a | 3480; by OFM: Fels 3481, Steine/Schotter 3482, Geröll 3483 (all "Grau5" #b3b3b3); **Sand 3484 ("Ocker2" #d7b351)**; Schnee / Eis, Firn 3486 (Blau5) with boundary 2518 |
| 43007 FKT 1100/1110/1120 Gewässerbegleitfläche, 1200 Sukzessionsfläche, 1300 Naturnahe Fläche | sig 1406 "Grün" #f3f5cc | n/a | n/a |
| 44001 Fließgewässer, 44005 Hafenbecken, 44006 Stehendes Gewässer, 44007 Meer | sig 1410 "Blau" COL00012 **#c0e8fa** | sig 2518 "Blau5" **#0068a1**; "nicht ständig Wasser führend": sig 2520; Kanal im Bau: 2519 | 3488 / 3490 (Blau5; flow-direction / water symbol) |
| 54001 Vegetationsmerkmal (overlay): Baumbestand Laub-/Nadel-/Mischholz (1021/1022/1023), Gehölz (1250), Gebüsch (1260), Röhricht/Schilf (1400), Gras (1500), Zierfläche (1600), Korbweide (1700), Reet (1800) | sig 1560: **outline only** in "Grün7" #008230, no fill | n/a | 3493 / 3494 / 3495, 3496, 3601, 3603, 3492, 3605, 3607, 3609 (Grün7) |
| 54001 Schneise (1300), Rain (1510) | sig 1561 "Grün" #f3f5cc with Grün7 outline | n/a | Rain: 3492 |
| 54001 Nadelbaum (1011) / Laubbaum (1012), point | n/a | n/a | 3597 / 3599 (Grün7) |
| 54001 Hecke (1100–1103), Gebüsch (line) | n/a | n/a | 3601 repeated along the line (Grün7) |
| 54001 Baumreihe Laubholz (1210) / Nadelholz (1220) / gemischt (1230), line | n/a | n/a | 3493 / 3494 / both, repeated along the line |
| 54001 Zustand 5000 "nass" | sig 1563 outline "Blau5" | n/a | 3478 (Blau5; same as Sumpf) |
| 51006 Spielfeld / Hartplatz / Rasenplatz (1410–1412) | sig 1520 "Grün3" #cfe8d9, outline "Braun4" #805c3a | n/a | n/a |
| 51006 Schwimmbecken (1450) | sig 1526 "Blau" #c0e8fa, outline Blau5 | n/a | n/a |
| 51006 Liegewiese (1460) | sig 1524 outline Braun4, no fill | n/a | n/a |
| 51009 Treppe/Freitreppe, Rampe, Terrasse, Mauer, Stützmauer (area) | sig 1305 "Grau3" #e6e6e6, black outline | n/a | n/a |
| 51009 Mauerkante / Stützmauer (line 1701–1703, 1721–1723) | n/a | line sig 2510 (Grau3) | n/a |
| 51009 Zaun (1740) | n/a | line sig 2002 black with point marks 3580/3581 | n/a |
| 51009 Brunnen (1780) | sig 1525 "Blau" with Blau5 outline / point 3529 | n/a | n/a |
| 61001 Böschung, Kliff | n/a | sig 2531 "Braun4" #805c3a (slope hachures; SK element `SlopeHatchLines`) | n/a |
| 61003 Damm, Wall, Deich / Knick | sig 1551 outline Braun4 | line 2620 Braun4 + 3632 | Knick: additionally hedge symbol 3601 (Grün7) |

Reading of the ALKIS palette (my summary of the verified values): built-up = very light red (#fde1e1) or near-white grey (#f5f5f5); recreation/cemetery = light grey-green (#dce6c2); grassland and "green" agriculture = pale yellow-green (#f3f5cc); arable = pale ochre (#fff8dc); forest/woodland = pale blue-green (#cfe8d9); heath/bog/swamp/fallow = pale brown (#f3e3ca); water = light blue (#c0e8fa) with dark blue outline (#0068a1); all vegetation symbols dark green (#008230). Traffic surfaces stay white. These are very pale tints by design (the Liegenschaftskarte must keep parcel boundaries and text legible).

### 4.2 ATKIS-Signaturenkatalog (SK10 / SK25 …)

Available (V): ATKIS-SK10 2.1.3 (Stand 30.11.2024), SK25 2.1.3, SK50 2.1.3, SK100 2.1.3 as HTML at https://sg.geodatenzentrum.de/web_public/adv/sk/v2.1.3/atkis/docAtkisSK10/SymbologyCatalog.html (…SK25, SK50, SK100) and as XML (SK10: 13.4 MB). Only **SK10 (DTK10, 1:10 000)** was evaluated here; SK25/50/100 not opened (open point).

**Colour table of ATKIS-SK10 2.1.3** (V; https://sg.geodatenzentrum.de/web_public/adv/sk/v2.1.3/atkis/docAtkisSK10/html/ColorTable-SYCAT010.html). The ATKIS-SK defines colours **in CMYK only** (no RGB/hex is published, unlike the ALKIS-SK). The "naive RGB" column is my arithmetic conversion R = 255·(1−C)(1−K) etc., not colour-managed, indicative only.

| ID | Name | C/M/Y/K % | naive RGB (indicative) |
|---|---|---|---|
| COL00002 | Weiß | 0/0/0/0 | #FFFFFF |
| COL00003 | Wattgrau | 25/10/10/0 | #BFE6E6 |
| COL00004 | Parkgrün | 40/0/30/0 | #99FFB3 |
| COL00005 | Wiesengrün | 10/0/20/0 | #E6FFCC |
| COL00006 | Waldgrün | 25/0/50/0 | #BFFF80 |
| COL00007 | Brachbraun | 5/5/20/0 | #F2F2CC |
| COL00008 | Ackerocker | 0/0/10/0 | #FFFFE6 |
| COL00009 | Seeblau | 25/0/0/0 | #BFFFFF |
| COL00010 | Industrieflächengrau | 0/0/0/20 | #CCCCCC |
| COL00011 | Wohnflächenhellrot | 0/20/10/0 | #FFCCE6 |
| COL00018 | Gefahrenrot | 0/60/0/0 | #FF66FF |
| COL00020 | Gebäudegrau | 0/0/0/45 | #8C8C8C |
| COL00021 | Straßengelb | 0/0/100/0 | #FFFF00 |
| COL00022 | Straßenorange | 0/30/100/0 | #FFB300 |
| COL00024 | Gebäuderot | 0/100/100/0 | #FF0000 |
| COL00025 | Grenzviolett | 40/100/0/0 | #9900FF |
| COL00026 | Baumgrün | 100/0/100/0 | #00FF00 |
| COL00027 | Bachblau | 100/0/0/0 | #00FFFF |
| COL00028 | Reliefbraun | 20/60/60/0 | #CC6666 |
| COL00029 | Grundrissbraun | 60/100/100/0 | #660000 |
| COL00030 | Schwarz | 0/0/0/100 | #000000 |
| COL00032 | Schutzgebietegrün | 50/0/50/0 | #80FF80 |
| COL00050 | TK10-braun | 9/88/91/7 | n/a |
| COL00051 | TK10-mittelbraun | 4/35/36/3 | n/a |
| COL00052 | TK10-hellbraun | 0/13/14/0 | n/a |

**Area fills in SK10** (V; symbolizer descriptions from .../html/SymbolizersTable-SYCAT010.html, colour reference from .../mdlsrc/SymbologyCatalog_mdl.html; SNR = Signaturnummer):

| SNR | Object types (description in the SK) | Fill colour |
|---|---|---|
| 20100 | Wohnbaufläche; Fläche gemischter Nutzung (Gebäude- und Freifläche Land- und Forstwirtschaft, Wohnen, Wohnen und Betrieb); Fläche besonderer funktionaler Prägung | Wohnflächenhellrot (0/20/10/0) |
| 20400 | Industrie- und Gewerbefläche; Landwirtschaftliche Betriebsfläche; Halde; Bergbaubetrieb; Deponie; Raffinerie; Werft; Kraftwerk; Umspannstation; Förderanlage; Kläranlage; Fabrikanlage; Ausstellungsgelände; Gärtnerei; Heizwerk; Wasserwerk; Abfallbehandlungsanlage | Industrieflächengrau (0/0/0/20) |
| 22600 | Tagebau, Grube, Steinbruch | Industrieflächengrau |
| 22690 | Torfstich | Brachbraun |
| **21800** | **Sport-, Freizeit- und Erholungsfläche** (general rule of AX_SportFreizeitUndErholungsflaeche; table text: "Sportanlage, Freizeitanlage, Sportplatz") | **Parkgrün (40/0/30/0)** |
| **21700** (+21701 overlay) | **Friedhof**; Freiflächen (Landwirtschaft); Forstwirtschaftliche Betriebsfläche; Stadion; Zuschauertribüne nicht überdacht | **Wiesengrün (10/0/20/0)** |
| 30001 | Straßenverkehr, nicht Funktion Begleitfläche | Industrieflächengrau |
| 30002 | Straßenverkehr in Funktion Begleitfläche Straßenverkehr; Begleitfläche | Wiesengrün |
| 34800 / 34801 | Bahnverkehr, nicht Begleitfläche / Begleitfläche Bahnverkehr | Industrieflächengrau / Wiesengrün |
| 31900 (+31901 contour) | Platz, Fußgängerzone | Parkgrün |
| 32600 (+32601 contour) | Platz: Parkplatz, Rastplatz, Marktplatz, Festplatz, Busbahnhof, Caravan-, Wohnmobilstellplatz | Weiß |
| 35300 | Platz, Raststätte, Autohof | Weiß |
| 33800 | Flughafen; Begleitfläche Flugverkehr; Begleitfläche Schiffsverkehr | Wiesengrün |
| 34400 | Betriebsfläche Flugverkehr / Schiffsverkehr | Industrieflächengrau |
| 34200 / 34300 | Start-/Landebahn, Rollbahn, Vorfeld: Beton, Bitumen/Asphalt / Gras, Rasen | Weiß / Wiesengrün |
| 40100 | Ackerland; Spargel; Hanf; Obst- und Nussbaumplantage; Obst- und Nussstrauchplantage; Weihnachtsbaumkultur; Kurzumtriebsplantage; Streuobstacker | Ackerocker (0/0/10/0) |
| 41500 | Landwirtschaft (Hopfen, Baumschule, Rebfläche) | Ackerocker |
| 40400 | Obst- und Nussplantage | Ackerocker |
| **40200** | **Grünland; Salzweide; Streuobstwiese; Unland: Gewässerbegleitfläche und naturnahe Fläche** (also AX_Vegetationsmerkmal areas such as Gras) | **Wiesengrün** |
| 40300 | Gartenbauland | Parkgrün |
| 41700 | Unland: Sukzessionsfläche; Brachland | Brachbraun (5/5/20/0) |
| **40900** | **Wald** (also Vegetationsmerkmal "Wald, Gehölz, Gebüsch") | **Waldgrün (25/0/50/0)** |
| 41200 | Gehölz | Waldgrün |
| 40500 / 40600 / 40700 | Heide / Moor / Sumpf | Brachbraun (each with its own pattern symbol) |
| 41800 | Unland: Vegetationslose Fläche | Weiß (patterns for Fels, Sand ... are separate symbol signatures) |
| 42100 | Vegetationslose Fläche (Schnee, Eis, Firn) | Weiß |
| 50100 / 51200 | Fließgewässer / nicht ständig Wasser führend, Kanal im Bau | Seeblau (25/0/0/0) |
| 51800 / 52000 | Stehendes Gewässer / nicht ständig Wasser führend | Seeblau |
| 51700, 34420, 51400, 51500 | Meer; Hafenbecken; Priel, Bodden, Haff; Quelle | Seeblau |
| 52100 / 52200 | Watt / Sandbank | Wattgrau / Weiß |
| 27800 | Schwimmbecken | Seeblau |
| 22900 | Klärbecken, Rieselfeld | Brachbraun |
| 23110 / 23310 | Gebäude / öffentliches Gebäude | Gebäudegrau / Gebäuderot |

Line/symbol colours by name (V, colour table): Baumgrün (vegetation symbols), Bachblau (water lines), Reliefbraun (relief), Straßengelb / Straßenorange (road fills), Grenzviolett (boundaries), Schutzgebietegrün (protected-area borders), Grundrissbraun, Gefahrenrot.

### 4.3 basemap.de Web Vektor (AdV Smart Mapping): style `bm_web_col`

Source (V): https://sgx.geodatenzentrum.de/gdz_basemapde_vektor/styles/bm_web_col.json, read 2026-09-30: `"name": "bm_web_col"`, `"basemapde:style-version": "5.0.3"`, 550 layers (62 fill, 269 line, 209 symbol, 7 circle, 3 fill-extrusion), vector source https://sgx.geodatenzentrum.de/gdz_basemapde_vektor/tiles/v2/bm_web_de_3857/bm_web_de_3857.json, attribution "© 2026 basemap.de / BKG | Datenquellen: © GeoBasis-DE". Documentation: https://sgx.geodatenzentrum.de/web_public/gdz/dokumentation/deu/basemap.de_web_vektor.pdf (Stand 03.03.2025; styles "Relief", "Farbe", "Grau", S, from search snippet). Values below are exact strings from the JSON.

| Layer id | source-layer | Filter (`klasse` values) | fill-color | Notes |
|---|---|---|---|---|
| Hintergrund | Hintergrund | n/a | rgb(255,253,238) = #FFFDEE | map background (also used for Ackerland) |
| SiedlungF_SportFreizeitundErholung | Siedlungsflaeche | Autokino, Freilichtkino; Botanischer Garten; Campingplatz; Erholungsfläche; Freilichtmuseum; Freilichtbühne; Freizeitanlage; Freizeitpark; Garten; Gelände für Luftsportgeräte; Go-Kart-Bahn; Golf; **Grünanlage**; Hundeübungsplatz; Kletteranlage; Reitsport; **Kleingarten**; Modellfluggelände; **Park**; Safaripark, Wildpark; Schwimmen; Sportanlage; Sport- Freizeit- und Erholungsfläche; Wochenend- und Ferienhausfläche; Zoo; **Siedlungsgrünfläche**; **Spielplatz, Bolzplatz**; Tennis; Verkehrsübungsplatz, Testgelände, Fahrsicherheit; Wochenendplatz | **rgb(230,247,210) = #E6F7D2** | z 11–22 |
| SiedlungF_Friedhof | Siedlungsflaeche | Friedhof; Parkfriedhof | rgb(223,240,182) = #DFF0B6 | |
| SiedlungF_Siedlung | Siedlungsflaeche | Bildung und Wissenschaft; Wohnbaufläche; Fläche besonderer funktionaler Prägung; Gesundheit, Kur; Kultur; Medien und Kommunikation; Regierung und Verwaltung; Religiöse Einrichtung; Sicherheit und Ordnung; Soziales; Öffentliche Zwecke; Fläche gemischter Nutzung; Gebäude- und Freifläche Land- und Forstwirtschaft; Wohnen; Wohnen und Betrieb | rgb(242,236,249) = #F2ECF9 | z 14–22 |
| SiedlungF_Siedlung_Industrie | Siedlungsflaeche | all settlement + industry classes | stops z9 rgb(238,221,255) → z13 rgb(242,236,249) | z 9–14 |
| SiedlungF_Industrie_und_Gewerbe | Siedlungsflaeche | Industrie und Gewerbe; Handel; Gärtnerei; Kläranlage, Klärwerk; Kraftwerk; Lagerfläche; Landwirtschaftliche Betriebsfläche ...; (52 classes) | rgb(214,210,219) = #D6D2DB | z 14–22 |
| SiedlungF_TagebauGrubeSteinbruch / _Bergbau / _Halde | Siedlungsflaeche | Tagebau, Grube, Steinbruch / Bergbau / Halde | rgb(214,210,219) | |
| SiedlungF_ForstFischerei | Siedlungsflaeche | Fischereiwirtschaftsfläche (4 variants); Forstwirtschaftliche Betriebsfläche | rgb(248,239,197) = #F8EFC5 | |
| VegetationsF_Ackerland_und_Co | Vegetationsflaeche | Ackerland; Streuobstacker; Hopfen; Rebfläche; Obst- und Nussplantage; Obst- und Nussstrauchplantage; Obst- und Nussbaumplantage; Baumschule; Weihnachtsbaumkultur; Kurzumtriebsplantage; Salzweide; Hanf; Spargel; Brachland | rgb(255,253,238) = #FFFDEE | same as background |
| VegetationsF_Gruenland | Vegetationsflaeche | **Grünland; Streuobstwiese; Streuobst; Gras** | **rgb(223,240,182) = #DFF0B6** | |
| VegetationsF_Gartenland | Vegetationsflaeche | Gartenbauland | rgb(201,245,216) = #C9F5D8 | |
| VegetationsF_Heide | Vegetationsflaeche | Heide | rgb(238,221,238) = #EEDDEE | opacity stops z8 0 → z10 1 |
| VegetationsF_Moor_Sumpf | Vegetationsflaeche | Moor; Sumpf | rgb(202,203,134) = #CACB86 | opacity z8 0 → z10 1 |
| VegetationsF_Gehoelz | Vegetationsflaeche | **Gehölz; Bewuchs, Gehölz; Gebüsch** | stops z11 rgb(223,240,182) → z22 **rgb(154,182,109) = #9AB66D** | |
| VegetationsF_Wald | Vegetationsflaeche | **Laubholz; Laub- und Nadelholz; Nadelholz; Wald; Baumbestand, Laub- und Nadelholz; Baumbestand, Laubholz; Baumbestand, Nadelholz** | stops z11 rgb(223,240,182) → z22 rgb(154,182,109) | opacity z6 0.3 → z8 1 |
| VegetationsF_VegetationsloseFlaeche_Fels_Geroell_Stein | Vegetationsflaeche | Vegetationslose Fläche; Fels; Geröll; Steine, Schotter | rgb(238,238,238) = #EEEEEE | |
| VegetationsF_VegetationsloseFlaeche_Sand; ReliefF_Duene; Gewaesser_F_Sandbank | n/a | Sand; Düne; Sandbank | **rgb(255,242,224) = #FFF2E0** | |
| VegetationsF_VegetationsloseFlaeche_Eis | Vegetationsflaeche | Eis, Firn | rgb(177,252,247) = #B1FCF7 | |
| Gewaesser_F_Meer / _Fliessgewaesser / _See_Hafenbecken / _Priel | Gewaesserflaeche | Meer; Fliessgewässer, Kanal, Flussmündungstrichter; See, Hafenbecken, Baggersee, Stausee, Speicherbecken; Priel | **rgb(210,232,250) = #D2E8FA** | |
| Gewaesser_F_Watt | Gewaesserflaeche | Watt | rgb(219,224,240) = #DBE0F0 | |
| Gewaesser_F_Quelle_Wasserfall; BauwerkF_Brunnen | n/a | Quelle; Wasserfall; Brunnen | rgb(170,204,255) = #AACCFF | |
| Gewaesser_L_* (line layers) | Gewaesserlinie | water lines by width class (3 m … 200 m); outlines of water polygons | line-color **rgb(170,204,255) = #AACCFF**; "nicht ständig wasserführend": dashed | |
| Verkehrsflaeche_Fussgaengerzone; Decker_Fussgaengerzone_... | Verkehrsflaeche / Verkehrslinie | Fußgängerzone | **rgb(182,223,210) = #B6DFD2** | |
| Verkehrsflaeche_Platz; IstWeitereNutzung_Flaeche_Platz | Verkehrsflaeche | Festplatz; Parkplatz; Platz; Rastplatz; Raststätte, Autohof; Marktplatz; Busbahnhof; Caravan-, Wohnmobilstellplatz; (funktion = Parken) | rgb(255,255,255) | |
| Verkehrsflaeche_Flugverkehr | Verkehrsflaeche | Flugverkehr etc. | rgb(230,247,210) | runway/apron: rgb(255,255,255) |
| Verkehrsflaeche_Bahnverkehr_Schiffsverkehr | Verkehrsflaeche | Bahnverkehr; Schiffsverkehr | rgb(214,210,219) | |
| Road casings / fills (line layers "Kontur_*", "Decker_*") | Verkehrslinie | n/a | casing rgb(153,153,153); Gemeinde-/Kreisstraße fill rgb(255,255,255); Landes-/Staatsstraße rgb(255,243,105); Bundesstraße rgb(255,203,79); Autobahn rgb(89,143,236); Hauptwirtschaftsweg rgb(230,230,230); Fußwege: rgb(153,153,153) dashed [4,2] | |
| Railways | Verkehrslinie | n/a | Eisenbahn rgb(102,102,102); S-Bahn rgb(51,153,51); U-Bahn rgb(0,0,255); Stadtbahn rgb(241,82,82) | |
| VegetationsL_Baumreihe / _Baumreihe_Fuellung | Vegetationslinie | Baumreihe | dotted line rgb(115,141,0) over rgb(223,240,182) | dash [0,2] (dots) |
| VegetationsL_Hecke | Vegetationslinie | Hecke | dotted line rgb(147,217,101) = #93D965 | |
| VegetationsL_Schneise / VegetationsF_Schneise | n/a | Schneise | dashed rgb(129,183,41) | |
| Symbol_VegetationP_Laubbaum / _Nadelbaum | Vegetationspunkt | Laubbaum / Nadelbaum | sprite icons "Laubbaum", "Nadelbaum" | |
| Gebaeude2D_nicht_oeffentlich / _oeffentlich / _Treibhaus | Gebaeudeflaeche | n/a | rgb(168,168,168) / rgb(232,179,158) / rgb(255,255,255) with outline rgb(138,213,110) | |
| BauwerkF_Schwimmbecken_Fuellung; BauwerkF_Rueckhaltebecken_Fuellung | Bauwerksflaeche | Schwimmbecken; Rückhaltebecken | rgb(210,232,250) | outline rgb(170,204,255) |
| BauwerkF_Stadion_Spielfeld_Schiessanlage | Bauwerksflaeche | Spielfeld; Stadion (überdacht / nicht überdacht); Schießanlage | rgb(248,239,197) = #F8EFC5 | outline rgb(153,153,153) |
| Barriere_Mauer / _Zaun / _Stuetzmauer | Barrierenlinie | Mauer; Zaun; Stützmauer | rgb(180,155,136); rgb(180,155,136) dashed; rgb(153,153,153) | |
| ReliefL_Daemme_Deiche / _Einschnitt | Relieflinie | n/a | rgb(150,111,57) | |
| Grenz-/Schutzgebiets-Layer | Grenze_Flaeche | Nationalpark; Biosphärenreservat; Naturschutzgebiet | rgb(111,193,53), fill-opacity 0.3 | |

---

## 5. BKG LBM-DE

Source for everything in this section (V unless noted): BKG, "Dokumentation Landbedeckungsmodell für Deutschland LBM-DE2021", Stand 30.04.2025, 64 pp., https://sg.geodatenzentrum.de/web_public/gdz/dokumentation/deu/lbm-de2021.pdf (product page: https://gdz.bkg.bund.de/index.php/default/digitales-landbedeckungsmodell-deutschland-stand-2021-lbm-de.html). Pages read: 1–14, 45–46, 54–55.

### 5.1 Product facts

| Item | Value |
|---|---|
| Product | Landbedeckungsmodell für Deutschland, Stand 2021 (LBM-DE2021); vector, polygons, "lückenlos und überlappungsfrei" |
| Reference year / cycle | 2021; updated every 3 years (LBM-DE2012, 2015, 2018, 2021; predecessors DLM-DE2009, DLM-DE 2006 study) |
| Minimum mapping unit | Mindestkartierfläche 1 ha; Mindestkartierbreite 15 m |
| Sources | flächenhafte Objektarten des ATKIS Basis-DLM (Lieferstand 3. Quartal 2021); LBM-DE2018; SPOT 6/7; Sentinel-2; DOPs |
| Format / access | GeoPackage; WMS |
| Purpose | "Hauptanwendungsziel des LBM-DE ist die Ableitung des Datensatzes CORINE Land Cover (CLC) für das Gebiet der Bundesrepublik Deutschland", national CLC contribution for Copernicus, on behalf of UBA |
| Attributes | LB_AKT (Landbedeckungscode), LN_AKT (Landnutzungscode), ZUS_AKT (Zusatzfunktion: F = Friedhof, M = Militär, S = Solar, O = Ortslage, K = künstlich geschaffene Fläche, W = Wald), SIE_AKT (Versiegelungsanteil), VEG_AKT (Vegetationsanteil), METHOD_AKT (31–34), CLC21 (derived CLC code), LBMDE_ID, LAND |
| History of the model | LB/LN separation introduced 2012 (DLM-DE2009 was still in CLC nomenclature); VEG, SIE, ZUS introduced with LBM-DE2015; "Mit der Fortführung des LBM-DE2021 ergaben sich keine weiteren konzeptionellen Veränderungen." |

### 5.2 Landbedeckung (LB): 31 classes in 7 groups (Anlage 1, p. 11)

| Group | Code | Name |
|---|---|---|
| A | B110 | Bebauung |
| A | B121 | Anlagen |
| A | B122 | Versiegelte gebäudelose Flächen |
| A | B242 | Mischflächen (regelmäßige Struktur) |
| B | B211 | Ackerland |
| B | B221 | Weinbau |
| B | B222 | Obst- und Beerenobst |
| B | B224 | Hopfen |
| C | B231 | homogenes Grünland |
| C | B321 | inhomogenes Grünland |
| C | B233 | Grasland mit Bäumen (< 50%) |
| D | B322 | Zwergsträucher (Heide) |
| D | B324 | Büsche, Sträucher |
| D | B310 | Aufforstung |
| D | B311 | Laubbäume |
| D | B312 | Nadelbäume |
| D | B313 | Nadel- und Laubbäume |
| E | B330 | Sand, Steine, Erde |
| E | B332 | Fels |
| E | B334 | Brandfläche |
| E | B335 | Schnee (permanent) und Eis |
| F | B411 | Sumpf |
| F | B412 | Moor |
| F | B413 | Sumpf mit Büschen/Bäumen < 50% |
| F | B414 | Moor mit Büschen/Bäumen < 50% |
| G | B423 | Watt |
| G | B511 | Wasserlauf |
| G | B512 | Wasserfläche |
| G | B521 | Lagune |
| G | B522 | Mündungstrichter |
| G | B523 | Offenes Meer |

Legend colours of the groups in the BKG document (as printed, not sampled): A pink, B yellow, C light green, D dark green, E grey, F violet, G light blue.

### 5.3 Landnutzung (LN): 16 classes (Anlage 1, pp. 45–46)

| Code | Name | Description (abridged from the BKG text) |
|---|---|---|
| N112 | Wohnen | Wohnen als Hauptnutzung (mind. 1 Wohnhaus pro Objekt) |
| N120 | Produktion | industrielle Produktion, Energieproduktion, Wasser-/Abwasserwerke, Ver- und Entsorgung |
| N121 | Öffentlichkeit | Handel & Dienstleistung, öffentliche Einrichtungen |
| N123 | Hafen | Hafenanlagen, Werften, Schleusen |
| N131 | Abbauflächen | Tagebau, Tongrube, Steinbruch, Baggersee |
| N132 | Deponien | Abfallstoffe und Abraum |
| N122 | Straßen- und Bahnverkehr | bebaute und nicht bebaute Flächen (auch Vegetation), die dem Verkehr dienen |
| N124 | Flugverkehr | n/a |
| **N142** | **Sport und Freizeit** | "Bebaute oder unbebaute Flächen, die dem Sport, der Freizeitgestaltung oder der Erholung dienen. Dazu gehören: außerstädtische Parks, Zoos, Friedhöfe & Grünanlagen, Sportanlagen, Kleingärten, Freizeitparks, Campingplätze, Ferienhäuser etc." |
| **N141** | **Städtische Grünfläche** | "Unbebaute Grünflächen im städtischen Bereich. Dazu gehören: innerstädtische Parks, Zoos, Friedhöfe & Grünanlagen" |
| N510 | Wasser | Flächen am Wasser (Wiesen vs. Salzwiesen); Wasserflächen mit Schifffahrtsnutzung |
| N211 | Landwirtschaft (intensiv) | regelmäßig gepflügte Flächen, Weideflächen, Baumschulen |
| N214 | Extensive Nutzung | Grünland, nur einmal pro Jahr gemäht; v. a. in Naturschutzgebieten |
| N311 | Forst | Waldflächen, Aufforstungsflächen, Waldlichtungen |
| N133 | Baustelle | n/a |
| N999 | Nicht relevant | "Nur zulässig in Verbindung mit Landbedeckungsklassen der Gruppen C-G" |

### 5.4 Relation to CLC

- CLC is derived per object from the **combination LB × LN**, "unter Berücksichtigung von Vegetations- und Versiegelungsgrad" (SIE/VEG thresholds) and in some cases ZUS, by the cross table in Anlage 3 (p. 54); the result is stored in attribute CLC21 (V).
- The LB codes are deliberately CLC-like: "B" + a number that for most natural classes equals the CLC code obtained when LN = N999 (e.g. B311 → 311, B312 → 312, B313 → 313, B322 → 322, B324 → 324, B332 → 332, B334 → 334, B335 → 335, B411 → 411, B412 → 412, B423 → 423, B511 → 511, B512 → 512, B521 → 521, B522 → 522, B523 → 523), read from the cross-table image (small print; S-quality reading, re-check against the PDF before hard-coding).
- The LN codes are likewise CLC-like: for most LB classes the columns give N141 → CLC 141 (Städtische Grünflächen), N142 → 142 (Sport- und Freizeitanlagen), N122 → 122, N124 → 124, N123 → 123, N131 → 131, N132 → 132, N133 → 133, N120/N121 → 121; N112 → 111 or 112 depending on SIE (B110 with SIE ≥ 70 → 111; SIE > 15 and < 70 → 112) (same caveat).
- ZUS modifications (p. 55, clearly legible, V): B321 + N121 + ZUS M → 321; B2xx + N121 + SIE ≤ 5 + VEG ≥ 95 + M → 321; B311/B312/B313/B324/B322 + N121 + SIE ≤ 5 + VEG ≥ 95 + M → 311/312/313/324/322; B310 + N121 + SIE ≤ 5 + VEG ≥ 95 + M → 324; Bxxx + N112 + SIE < 15 + ZUS O → 112.
- Anlage 2 of the document contains the CLC nomenclature and the "Farblegende für CORINE Land Cover" (pp. 52–53; not read in this session).
- The BKG warns that in change analyses the following code groups are sensitive to definition changes: N141/N142 (Grün- und Freizeitflächen), N141/B31x/B231 (städtische Grünflächen), B321/B324/B322/B231, B311/B312/B313; in LBM-DE2015 "eine Reduzierung von Landnutzung N141 (städtische Grünfläche) und N122 (Straßenbegleitgrün)" was carried out (V, p. 9).

Relation to the AdV schemas: LBM-DE (BKG product, CLC-oriented, MMU 1 ha) is NOT the same thing as the AdV application schemas "Landbedeckung 1.0.1" / "Landnutzung 1.0.2" of the GeoInfoDok (section 3.6); both split cover from use, but with different class lists and codes.

---

## 6. Open points (not verified or not done in this session)

1. **Numeric PlanZV colours in Länder/municipal drafting guides** (RGB/CMYK/RAL): none found in one search round. Candidates not opened: Länder XPlanung Pflichtenhefte/Leitfäden (e.g. https://lbv.brandenburg.de/sixcms/media.php/9/X-Planung-Pflichtenheft_2025.pdf), municipal CAD/GIS standards, vendor symbol libraries.
2. **BfN-Schriften 461/2 Planzeichenkatalog Landschaftsplanung** (RAL/RGB values) was only identified, not opened (probably covered by another stream).
3. **XP_ZweckbestimmungGewaesser** (XPlanGML 5.x) values are recalled only (R). In 6.x the enumeration does not exist; SO_KlassifizGewaesser replaces it (V).
4. Whether **§ 9 Abs. 1 Nr. 15a / § 5 Abs. 2 Nr. 5a BauGB** ("natürlicher Klimaschutz"), quoted by XPlanGML 6.1, are in force was not checked; PlanZV has no Planzeichen for them.
5. **ATKIS-SK**: only SK10 2.1.3 evaluated; colours exist in CMYK only (the RGB column in 4.2 is my naive conversion); SK25/50/100 not opened; shapes of pattern/point signatures (Heide, Moor, Sumpf, Laub-/Nadelbaum, Grünanlage symbol 3413, Park 3415 ...) were NOT viewed, only signature numbers and colours are documented.
6. **AAA 6.0.1 → 7.1.2 diff** at Werteart level not done (which FKT/VEG values are new is unknown); AX_Boeschungsflaeche Kennung 61002 is R; ATKIS-Basis-DLM-specific modelling (Modellart differences, AX_Ortslage etc.) not evaluated, TN tables come from the ALKIS (DLKM) catalogue, the common NAS 7.1.2 schema and the AdV enumeration register. The "(G)/(LN)" flags were only read for the values printed in the Hessen profile.
7. **AdV statement on the reference version** ("Referenzversion 7.1 since 1 Jan 2024") was read via a summarising fetch; re-read before quoting.
8. **LBM-DE cross table** (Anlage 3) was read from a small image; cell-level mappings in 5.4 must be re-checked against the PDF before hard-coding. CLC colour legend (Anlage 2) not read.
9. The **GeoInfoDok Objektartenkatalog App** (https://www.gid-katalog-app.org/) can produce complete CSV/XML catalogues for AAA 7.1.2, LB 1.0.1 and LN 1.0.2; it requires a form submission + file download, which I did not perform. Recommended as the bulk source for building crosswalk tables.
10. **basemap.de**: only `bm_web_col` (style-version 5.0.3) read; grey/relief styles, sprite icons and the print product basemap.de P10 not inspected.
11. **PlanZV sampled colours** come from JPEG scans on gesetze-im-internet.de; the printed BGBl. Anlagenband was not consulted. xPlanBox SVG symbol files were not inspected (AGPL-licensed).
12. Binding character of XPlanung (IT-Planungsrat decision 2017; obligation dates) was not researched in primary sources in this stream (only a secondary snippet).

## 7. Implications for the element catalog

### 7.1 Where symbology is legally prescribed and where it is free

| Regime | Applies to | What is fixed | Numeric colours | Consequence |
|---|---|---|---|---|
| **PlanZV Anlage** (federal ordinance, "sollen") | only Bauleitpläne (FNP, B-Plan); deviations allowed (§ 2 Abs. 2, 3), breach harmless if legible (Abs. 5) | hue family by name + symbol geometry; b/w and colour variants equally valid; legend required | none | Offer a strict "PlanZV" theme only for planning-type elements. Exact RGB is our choice: document it as "xPlanBox-compatible" (hex from the open reference implementation) or as "sampled from the Anlage". |
| **AdV ALKIS-Signaturenkatalog 2.1.0** | official Liegenschaftskarte of the surveying authorities (AdV standard; not binding for third parties) | full symbol rules per object type/Werteart | yes: RGB %, CMYK %, web hex | An exact "ALKIS" theme is possible (33 colours, signature numbers). Very pale tints. |
| **AdV ATKIS-Signaturenkataloge (SK10 …)** | official DTK products | full rules | CMYK only | "DTK" theme needs a documented CMYK→RGB conversion. |
| **basemap.de Web Vektor** | BKG/AdV web product | open style JSON | yes (rgb strings) | Best ready-made convention reference for web maps; pastel. |
| **XPlanung / AAA / LBM-DE** | data semantics | classes and codes only | n/a | Pure crosswalk targets; no symbology prescribed. |
| Everything else (inventory, ecology, design maps) | n/a | nothing | n/a | House style is free; only conventions apply. |

### 7.2 Hue-family conventions that all four official sources share (verified values)

| Theme | PlanZV (name / sampled) | xPlanBox | ALKIS-SK | ATKIS-SK10 (CMYK) | basemap.de |
|---|---|---|---|---|---|
| Public/private green space, parks, sport/recreation | Grün mittel / #92EB9B | #7FC643, #80E41B | Grün2 #dce6c2 (+ dark-green symbols #008230) | Parkgrün 40/0/30/0 | #E6F7D2 |
| Cemetery | (green + cross pictogram) | n/a | Grün2 #dce6c2 | Wiesengrün 10/0/20/0 | #DFF0B6 |
| Grassland / meadow | (Landwirtschaft) Gelbgrün / #BCFC9C | #CCE968 | Grün #f3f5cc | Wiesengrün 10/0/20/0 | #DFF0B6 |
| Arable land | Gelbgrün | #CCE968 | Ocker #fff8dc | Ackerocker 0/0/10/0 | #FFFDEE |
| Forest / woodland / Gehölz | Blaugrün / #15ADAA | #34AB8F | Grün3 #cfe8d9 | Waldgrün 25/0/50/0 | #DFF0B6 → #9AB66D |
| Heath, bog, swamp, fallow | n/a | n/a | Braun #f3e3ca | Brachbraun 5/5/20/0 | Heide #EEDDEE; Moor/Sumpf #CACB86 |
| Water | Blau mittel / #C4E3EC | #99D9E8 | Blau #c0e8fa, outline #0068a1 | Seeblau 25/0/0/0 | #D2E8FA, lines #AACCFF |
| Sand | n/a | n/a | symbol in Ocker2 #d7b351 | (white + pattern) | #FFF2E0 |
| Rock / gravel / bare | n/a | n/a | symbols in Grau5 #b3b3b3 | white | #EEEEEE |
| Residential | Rot mittel / #F5C2B3 | #CF9377 | Rot #fde1e1 | Wohnflächenhellrot 0/20/10/0 | #F2ECF9 |
| Industrial / commercial | Grau mittel / #B3BAB2 | #A6A596 | Grau2 #f5f5f5 | Industrieflächengrau 0/0/0/20 | #D6D2DB |
| Road surface | Goldocker / #FEE223 | #FFD92F | white | Industrieflächengrau (area); Straßengelb/-orange (lines) | white; casing #999999 |
| Pedestrian zone | (6.3 striped Goldocker) | pattern | Grün3 #cfe8d9 | Parkgrün | #B6DFD2 |
| Nature-conservation overlays | Grün dunkel band / #39E554 | #4DAE38 | n/a | Schutzgebietegrün 50/0/50/0 | rgb(111,193,53) |
| Water-law overlays | Blau dunkel band / #3BA4CD | #007BCE | n/a | n/a | n/a |
| Plan boundary | Grau dunkel band / #767A76 | #80847A | n/a | n/a | n/a |

Take-aways for the mellow house theme: (1) keep green space, grassland and woodland as three distinguishable greens with woodland shifted towards blue-green or darker; (2) water = light blue fill + darker blue outline; (3) heath/bog/fallow = brownish; arable = pale ochre/yellow; (4) the cadastral (ALKIS) and web (basemap.de) palettes are already pastel, so a pastel house palette is conventional in Germany; only the PlanZV theme is saturated; (5) topographic sources leave traffic surfaces white/grey, planning sources colour them yellow-ochre, the theme switch must swap this family.

### 7.3 Reusable symbol motifs (all from the PlanZV Anlage unless noted)

- Area textures (b/w column): fine dot raster = green space; horizontal wavy lines = water; sparse small-dot grid = agriculture; dense large-dot grid = forest.
- Border ("Randsignatur") motifs: T-ticks inward = SPE area (13.1); row of open circles = planting area (13.2.1); row of filled dots = preservation area (13.2.2); groups of short strokes = protected area (13.3); wavy inner line = water management (10.2); looped inner line = water-law area (10.3); outward/inward solid triangles = fill/excavation (11.1/11.2); zigzag = keep free of building (15.8); thick broken grey band = plan boundary (15.13).
- Point symbols: circle = tree, three-lobed cloud = shrub, cloud + rectangle = other planting; **open centre = to be planted, filled centre = to be preserved**; letters in circles for protected-area types (N, NLP, L, NP, ND, LB) and water functions (H, R, Ü, GW, OW); "E" = Erholungswald.
- Purpose pictograms in a frame: dot clumps (park), 2×3 plots with dots (allotments), oval (sports ground), bucket (playground), tent (camp site), waves (bathing), three crosses (cemetery); P / pedestrian / V for traffic areas.
- Slope hachures for Böschung/embankment (PlanZV 15.9; ALKIS-SK sig 2531, `SlopeHatchLines`).
- ALKIS-SK habit: pale area tint + dark-green (#008230) repeating point symbol per vegetation type; overlays (AX_Vegetationsmerkmal) are outline-only with symbols, a good model for "texture on top of tint".

### 7.4 Must-have elements implied by this stream

Beyond the present 16 classes, the following are needed to cover PlanZV group 9–13, XPlanung open-space enumerations and the ALKIS TN/overlay catalogue:

| Group | Elements (German term → crosswalk anchor) |
|---|---|
| Green-space purposes (planning) | Grünfläche öffentlich/privat (PlanZV 9; BP_GruenFlaeche + nutzungsform); Parkanlage (XP 1000); Dauerkleingarten (1200 / ALKIS FKT 4440); Sportplatz (1400 / 4120); Spielplatz, Bolzplatz (1600, 16000 / 4470); Zeltplatz, Campingplatz (1800, 18000 / 4330); Badeplatz, Freibad (2000 / 4320); Friedhof (2600 / 41009); Straßenbegleitgrün / Verkehrsgrün (24000; SO 14015; ALKIS 2312); Böschungsfläche (24001); Uferschutzstreifen (24003); Abschirmgrün (24004); Naturerfahrungsraum (2700); Gärtnerei (99990); Garten (ALKIS 4460); Botanischer Garten (4430); Zierfläche (54001 BWS 1600; LN 4480) |
| Agriculture | Ackerland (VEG 1010); Grünland (1020); Streuobstwiese (1021) / Streuobst (BWS 1900); Gartenbauland (1030); Baumschule (1031); Rebfläche (1040); Obstplantage (1050); Brachland (1200); Kurzumtriebsplantage (1100) |
| Semi-natural | Heide (43004); Moor (43005); Sumpf (43006); Sukzessionsfläche (43007 FKT 1200); Naturnahe Fläche (1300); Gewässerbegleitfläche (1100); Fels (OFM 1010); plus XP_SPEMassnahmenTypen targets: extensives Grünland, Feuchtgrünland, Obstwiese, naturnaher Uferbereich, Röhrichtzone, Ackerrandstreifen, Acker-/Grünlandbrache, Hochstaudenflur, Trockenrasen |
| Woody vegetation (area/line/point) | Wald Laub/Nadel/Misch (VEG 1100/1200/1300); Gehölz (43003; BWS 1250); Gebüsch (1260); Hecke (1100); Knick (61003 art 2000; XP 2200); Baumreihe (1210–1230; XP 1200); Einzelbaum Laub/Nadel (1012/1011); Kopfbaum (XP 1100); Obstbaum (XP 1300); Windschutz (funktion 1000) |
| Water | Fluss, Bach, Graben, Kanal (FKT 8200/8500/8400/8300); See, Teich, Stausee, Baggersee (8610/8620/8630/8640); "nicht ständig Wasser führend" variant (HYD 2000); Quelle (55001 art 1610); Schwimmbecken (51006 BWF 1450); Regen-/Hochwasserrückhaltebecken, Versickerungsfläche (SO_KlassifizWasserwirtschaft 1500/1000/1200) |
| Traffic surfaces | Fahrbahn (2315); Fußweg (5220); Radweg (5240); Rad- und Fußweg (5250); Wirtschaftsweg (5212); Platz; Parkplatz (5310); Marktplatz (5340); Fußgängerzone (5130); Verkehrsberuhigter Bereich (SO 14000); Mischverkehrsfläche (SO 3400); Begleitfläche (2312, 5270) |
| Built context | Wohnbaufläche, Fläche gemischter Nutzung, Industrie-/Gewerbefläche, Fläche besonderer funktionaler Prägung (41001–41007); Gebäude (public / other) |
| Sport/play furniture | Spielfeld, Hartplatz, Rasenplatz (BWF 1410–1412); Laufbahn (1420); Liegewiese (1460); Tribüne |
| Structures (line/point) | Mauer (1700), Stützmauer (1720), Zaun (1740), Treppe (1620), Rampe (1650), Terrasse (1670), Brunnen (1780–1783), Denkmal (1750); Böschung (61001, befestigt/unbefestigt); Damm/Wall/Deich (61003); Laterne, Bushaltestelle etc. (51010) |
| Planning overlays | SPE-Fläche / -Maßnahme (PlanZV 13.1); Anpflanzfläche (13.2.1); Erhaltungsfläche (13.2.2); Ausgleich/Kompensation (istAusgleich, XP_ERFlaechenArt); Schutzgebiete (13.3; LP_KlassifizierungNaturschutzrecht incl. gesetzlich geschütztes Biotop, Natura 2000); Überschwemmungsgebiet, Wasserschutzgebiet (10.2/10.3); Geltungsbereich (15.13); Aufschüttung / Abgrabung (11.1/11.2); Biotopverbund (Kernfläche, Verbindungsfläche, Trittsteinbiotop ...) |
| Building greening | Dachbegrünung, Fassadenbegrünung (XP gegenstand 6000 / 5000; no AAA code) |

Crosswalk of the present 16 classes (anchors verified above; "-" = no code found in the examined catalogues):

| House class | PlanZV | XPlanung 6.1 | ALKIS/ATKIS 7.1.2 (Kennung / attribute = value; NAK) | AdV LB 1.0.1 / LN 1.0.2 | LBM-DE |
|---|---|---|---|---|---|
| Lawn | 9 Grünflächen | XP_ZweckbestimmungGruen 1000 (as purpose) | 41008 FKT 4400 Grünanlage (18040000) / 4410 Siedlungsgrünfläche (18040100); 54001 BWS 1500 Gras, 1600 Zierfläche | LB_KrautigeVegetation VEG 1000 Gras; LN_FreiluftUndNaherholung 4400/4410/4480 | B231 + N141 |
| Meadow | 12.1 | XP_ZweckbestimmungLandwirtschaft 1200; XP_SPE 1200, 1300 | 43001 VEG 1020 Grünland (31020000) | LB_KrautigeVegetation 1000; LN_Landwirtschaft 1020 Mahd- und Weideland | B231 / B321 + N211 / N214 |
| Wildflower meadow | n/a | XP_SPE 1200 ExtensivesGruenland, 2100 Hochstaudenflur, 2200 Trockenrasen | 43007 FKT 1300 Naturnahe Fläche (37040000) (nearest) | LB_KrautigeVegetation 3000 Getreide, Staudengewächse, Farne (nearest) | B321 + N214 |
| Shrub | 13.2 Sträucher | gegenstand 2000, 2100 Hecke, 2200 Knick | 43003 Gehölz (33000000); 54001 BWS 1250, 1260, 1100 | LB_HolzigeVegetation 6000 Büsche, Sträucher / 5000 Gehölz | B324 |
| Woodland | 12.2 | XP_ZweckbestimmungWald; XP_SPE 1000, 1100 | 43002 Wald VEG 1100/1200/1300 (32000000) | LB_HolzigeVegetation 4000 Bäume + blattform; LN_Forstwirtschaft 6100 | B311/B312/B313 (+ N311) |
| Urban trees | 13.2 Bäume (Anpflanzen / Erhaltung) | gegenstand 1000, 1100, 1200, 1300 | 54001 BWS 1011/1012, 1210–1230, 1020–1023, 1900 | LB_HolzigeVegetation 4000 | B233 (Grasland mit Bäumen) (nearest) |
| Reed / wetland | n/a | XP_SPE 1600 Roehrichtzone, 2400 Moor; LP_GesGeschBiotopTyp 2000 | 54001 BWS 1400 Röhricht, Schilf / 1800 Reet; zustand 5000 Nass; 43005 Moor; 43006 Sumpf | LB_KrautigeVegetation 2000 Röhricht, Schilf + wassersaettigung | B411–B414 |
| Water body | 10.1 | SO_KlassifizGewaesser 1000/2000/3000 | 44001, 44006 (+FKT); 55002 | LB_Binnengewaesser (gewaesserart, fliesseigenschaft, wasserfuehrung) | B511 / B512 |
| Soil / bare ground | n/a | n/a | 43007 FKT 1000 (37010000); 43001 VEG 1200 Brachland | LB_Lockermaterial 3000 Erdreich / 4000 Ton, Schluff | B330 |
| Sand | n/a | FP detail 2400_11 Strand | 43007 OFM 1040 Sand; 61007 Düne | LB_Lockermaterial 2000 Sand, Feinkies | B330 |
| Gravel | n/a | n/a | 43007 OFM 1020 Steine, Schotter / 1030 Geröll; Straßenachse OFM 1250 Gestein, zerkleinert | LB_Lockermaterial 1000 Geröll, Schotter, Kies | B330 |
| Paving (light / dark) | 6.1 / 6.3 (as traffic area) | SO_ZweckbestimmungStrassenverkehr 14001 Platz, 14002 Fussgaengerbereich | Straßenachse/Fahrbahnachse OFM 1240 Pflaster; 42009 Platz | LB_Tiefbau | B122 |
| Asphalt | 6.1 | SO_Strassenverkehr | OFM 1230 Bitumen, Asphalt; 42001 FKT 2315 Fahrbahn (21010100) | LB_Tiefbau | B122 |
| Concrete | 6.1 | n/a | OFM 1220 Beton | LB_Tiefbau | B122 |
| Wood decking | n/a | n/a |, (nearest: 51009 BWF 1670 Terrasse) | LB_Tiefbau (nearest) | n/a |

Finding: the official German catalogues describe land use and vegetation in depth but surface MATERIALS only marginally (4 road-surface values on axis objects, LB_Tiefbau without sub-types, LB_Lockermaterial). Light/dark paving, wood decking and "wildflower meadow" have no official code; they remain house elements with a "nearest" crosswalk and must be flagged as such.

### 7.5 Attributes every element should be able to carry

| Attribute | Why (source) |
|---|---|
| `nutzungsform` public / private | PlanZV 9 note; XP_Nutzungsform 1000/2000; LN artDesParkplatzes |
| `status` existing / planned, and for vegetation "Anpflanzen" vs "Erhaltung" | PlanZV 13.2; XP_ABEMassnahmenTypen 1000/2000/3000; XP_SPEZiele |
| `overlay` (istWeitereNutzung) | AAA TN overlay principle; BP Überlagerungsobjekte |
| `leaf_type` Laub / Nadel / gemischt | AX_Vegetationsmerkmal_Wald; BWS; LB blattform |
| `wetness` / `intermittent` | LB wassersaettigung / wasserfuehrung; HYD 2000; zustand 5000 |
| `surface_material`, `paved` (befestigt/unbefestigt) | AX_Oberflaechenmaterial_*; AX_Befestigung_*; AX_Zustand_BoeschungKliff |
| `sealing_pct`, `vegetation_pct` | LBM-DE SIE_AKT / VEG_AKT |
| geometry role: area / line / point / border ("Randsignatur") | PlanZV allows area symbols as border symbols; AAA point/line/area variants |
| tree details: crown diameter, trunk diameter, species, count, min height | BP_AnpflanzungBindungErhaltung attributes |
| compensation flag / type | istAusgleich; XP_ERFlaechenArt; LP_MassnahmenTyp (CEF, FCS ...) |

### 7.6 Crosswalk keys to store per element

`planzv` (Anlage number, e.g. "9", "10.1", "13.2.1" + Zweckbestimmung name); `xplan` (class + enumeration:code, e.g. `BP_GruenFlaeche/XP_ZweckbestimmungGruen:1000`, optional detail code list value, version 6.1); `alkis` (Kennung + attribute = value, e.g. `41008/FKT=4400`, schema 7.1.2); `nak` (8-digit Nutzungsartkennung, e.g. 18040000); `aaa_lb` and `aaa_ln` (class + list:code, schema LB 1.0.1 / LN 1.0.2); `lbmde_lb` (Bxxx), `lbmde_ln` (Nxxx); `clc` (derived); `basemap_klasse` (string value of the basemap.de vector tiles); `alkis_sk` (signature number + colour id) and `atkis_sk10` (signature number) for the official themes; for biotope elements the three XPlanung-LP keys `bkompv`, `land_key`, `ffh_lrt`. Always store the schema/version with the code, because identical numbers mean different things in different lists (AAA vs LN; BP vs FP detail lists).


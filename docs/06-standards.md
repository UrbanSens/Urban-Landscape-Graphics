# 6 · Standards

*Welchen deutschen und europäischen Standards der Stil folgt, wie er das tut und wo er ihnen bewusst nicht folgt.
Die vollständigen Belege stehen im [Standards-Bericht](research/standards-report.md).*

## 6.1 Was „konform“ hier bedeutet

Farben sind fast nie gesetzlich geregelt. Die PlanZV, die einzige gesetzliche Regelung der Planzeichen in
Deutschland, benennt Farben in Worten, gilt nur für Flächennutzungs- und Bebauungspläne und lässt Abweichungen
zu, solange der Plan lesbar bleibt. Festgelegt *sind* dagegen Schlüssel, Symbole mit Bedeutung und Zahlen.

> Eine Verletzung von Vorschriften der Absätze 1 bis 4 ist unbeachtlich, wenn die Darstellung, Festsetzung, Kennzeichnung, nachrichtliche Übernahme oder der Vermerk hinreichend deutlich erkennbar ist.
>
> Quelle: Planzeichenverordnung 1990, § 2 Abs. 5

Die Bibliothek ist deshalb auf fünf Ebenen konform:

| Ebene | Was standardisiert ist | Wie ulg dem Standard folgt |
|---|---|---|
| **Schlüssel** | die Klassen der Schemata für Kataster, Planung, Biotope, Landbedeckung und OSM | 26 Zuordnungstabellen (Crosswalks) übersetzen 3926 Klassen in Elemente, jeweils mit Passgrad und Belegstufe (6.3) |
| **Amtliche Darstellung** | veröffentlichte Farbwerte von ALKIS, basemap.de, BfN, OSM Carto, der PlanZV-Praxis | sechs Themes zeichnen jede Karte in diesen Farben neu (6.2); Crosswalk-Einträge tragen die eigene Farbe eines Schemas, wo sie geprüft wurde |
| **Symbole mit Bedeutung** | Bestand / Planung / Erhalt / Beseitigung; Umgrenzungen in Plänen; Wurzelschutz | Statussymbole für Bäume und Sträucher, PlanZV-Umgrenzungen, Zonen nach DIN 18920 ([Stilleitfaden 2.5](02-style.md#25-symbole)) |
| **Zahlen** | Gewichtungsfaktoren, Abflussbeiwerte, Versiegelungsklassen, EU-Definitionen für urbanes Grün | Element-Attribute mit ihren Quellen, `ulg.indicators()` (6.4) |
| **Lesbarkeit** | WCAG-2.2-Kriterien 1.4.1 und 1.4.11, Farbsehschwäche | `ulg check` in der Testsuite ([Stilleitfaden 2.8](02-style.md#28-lesbarkeit)) |

Die Recherche dazu wurde am 30. September 2026 in sieben Strängen durchgeführt; jeder Wert ist nach der Art seiner
Prüfung gekennzeichnet: **V** in der Primärquelle gelesen, **V\*** über eine Extraktion gelesen oder einem
amtlichen Farbmuster entnommen, **S** aus einer Sekundärquelle, **R** aus dem Gedächtnis angegeben und nicht geprüft.

## 6.2 Themes

| Theme | Konvention | Verwendete Ausgabe | Belegstufe |
|---|---|---|---|
| `mellow` | UrbanSens-Hausstil | diese Bibliothek | keine |
| `planzv` | Farben deutscher Flächennutzungs- und Bebauungspläne | PlanZV 1990 (geändert 2025), Hex-Werte der XPlanung-Referenzimplementierung xPlanBox | Farbangaben in Worten V; Hex-Werte V aus xPlanBox |
| `alkis` | Katasterkarte (Liegenschaftskarte) | ALKIS-Signaturenkatalog 2.1.0 (01.10.2024) | V |
| `basemap` | die Web-Basiskarte des Bundes | basemap.de Web Vektor `bm_web_col` 5.0.3 | V |
| `bfn` | Landschaftspläne | BfN-Skripten 461/2 (2017), Pastellserie | V |
| `osm` | OpenStreetMap | OSM Carto v6.1.0 | V |
| `mono` | Schwarz-Weiß-Zeichnung | nach den Konventionen der ISO 11091 | hauseigene Interpretation |

Die amtlichen Themes schalten die handgezeichnete Kontur ab und verwenden einfarbige Füllungen, wie es die
Originale tun. Elemente ohne eigenen Eintrag übernehmen die Farbe der Kategorie, zu der sie in der jeweiligen
Konvention gehören; der Beleg jeder Farbe steht in der Theme-Datei (siehe [reference/themes.md](reference/themes.md)).

## 6.3 Crosswalks

| Familie | Schemata (Einträge) |
|---|---|
| Deutsche Planung und Kataster | `planzv` (72), `xplanung` (357), `alkis` (292), `alkis_nak` (138), `adv_lbln` (141), `basemap_de` (140), `lbm_de` (116) |
| Biotope, Kompensation, Kosten | `bkompv` (369), `baykompv` (345), `ffh_lrt` (41), `berlin_biotope` (33), `din276` (70) |
| Europa und weltweit | `clc` (64), `urban_atlas` (44), `clcplus` (14), `eunis` (381), `hilucs` (92), `lucas` (111), `esa_worldcover` (11), `lcz` (24) |
| OpenStreetMap und nationale Modelle | `osm` (457), `bgt` (NL, 114), `swiss_av` (CH, 96), `at_dkm` (AT, 126), `uk_metric` (121), `ukhab` (157) |

Jeder Eintrag gibt an, wie genau die Übersetzung ist:

| Passgrad | Bedeutung | Beispiel |
|---|---|---|
| `exact` | gleiches Konzept | CLC 141 *Städtische Grünflächen* → `green_space` |
| `narrower` | das Element ist spezifischer als die Klasse | ALKIS *Pflaster* → `concrete_pavers` |
| `broader` | das Element ist allgemeiner als die Klasse | ALKIS *Salzweide* → `salt_marsh` |
| `nearest` | keine echte Entsprechung; die nächstliegende Darstellung | OSM `landuse=greenery` → `perennials` |
| `none` | keine darstellbare Klasse | OSM `highway=proposed` |

Biotopschemata tragen ihre Bewertung: Die Einträge der BKompV enthalten den Biotopwert (0–24 oder je Altersklasse),
die der BayKompV die Wertpunkte (0–15) und den gesetzlichen Schutz. Die amtlichen Legendenfarben bleiben je
Klasse erhalten (`ulg.official_colors("clc")`), sodass eine Karte, die das CORINE-Rosa für städtische
Grünflächen verwenden muss, dies auch kann. Einzelheiten, Quellen und Lizenzhinweise je Schema:
[reference/crosswalks.md](reference/crosswalks.md).

## 6.4 Kennwerte

| Attribut | Standard | Belegstufe |
|---|---|---|
| `bff`, `bff_1990` | Berliner Biotopflächenfaktor, Broschüre 02/2021 (16 Typen) und die Liste von 1990 | V |
| `runoff_cs`, `runoff_cm` | DIN 1986-100:2016-12, Tabelle 9 | S (kommunale Wiedergabe; die Norm ist kostenpflichtig) |
| `sealing` | Definitionen des Umweltbundesamts | V |
| `bdla_class` | bdla, qualifizierter Freiflächengestaltungsplan (07/2022) | V |
| `belagsklasse` | Berliner Umweltatlas 01.02 (2017) | V |
| `albedo`, `emissivity` | Nachschlagetabellen des Modellsystems PALM 6.0 | V |
| `nrr_urban_green` | Verordnung (EU) 2024/1991, Art. 3 Nr. 20; Klassen 2, 3, 4, 5, 6, 8, 10 des CLC+ Backbone | V |

Werte werden übernommen, nie interpoliert. Wo sich zwei Instrumente widersprechen (ein wassergebundener Weg hat
eine niedrige BFF-Gewichtung, aber einen hohen Abflussbeiwert), bleiben beide erhalten, weil sie unterschiedliche
Fragen beantworten.

## 6.5 Zeichenkonventionen

| Konvention | Quelle | In ulg |
|---|---|---|
| Bestand dünn, Planung dick; geschützt mit einem Rahmen aus Strichpunktlinie; Beseitigung gestrichelt und durchkreuzt | ISO 11091 | Statussymbole für Bäume und Sträucher, Theme `mono` |
| offene Mitte = anpflanzen, gefüllte Mitte = erhalten | PlanZV 13.2 | `tree_planned`, `shrub_planned`, `tree_protected` |
| Umgrenzungen mit nach innen gerichteten T-Strichen, offenen Kreisen, gefüllten Punkten; Grenze des Geltungsbereichs | PlanZV 13.1, 13.2.1, 13.2.2, 15.13 | `compensation_area`, `planting_area`, `preservation_area`, `planning_boundary` |
| Bestand grau, neu rot, Beseitigung gelb; Neubau kreuzschraffiert | Bayerische Bauvorlagenverordnung, Anlage 1 | `signal.*`-Tokens, `status_planned` (rote Kreuzschraffur), `status_removal`, `tree_remove` |
| Beseitigung als dünne gestrichelte Schraffur | ISO 11091 | `status_removal` (gelb, gestrichelte Schraffur) |
| Wurzelbereich = Kronentraufe + 1,50 m (Säulenform + 5,00 m); Gräben ≥ 4 × Stammumfang, mindestens 2,50 m | DIN 18920 (Ausgabe 2014), R SBB | `ulg.root_protection_zone()` |
| braune senkrechte Striche für Brache | BfN 461/2 | `grassland_fallow` |
| Strichstärken | Normenreihe ISO 128 | `settings.json → line_weights` |
| Maßstäbe je Leistungsphase | HOAI Anlage 11 | Grenzen der Detailstufen 1:750 / 1:2500 / 1:10 000 |

## 6.6 Bewusste Abweichungen

Der Hausstil ist frei, wo keine Regel ihn bindet, und sagt das auch:

- **Geschützte Biotope** sind eine grüne Schraffur; der bayerische Biotop-Viewer verwendet Magenta. Verwenden Sie
  das Theme `bfn` oder färben Sie das Overlay um, wenn es auf die örtliche Konvention ankommt.
- **Grenzen** folgen der Praxis der Landschaftspläne, nicht jeder amtlichen Linienform: Die Grundstücksgrenze ist
  eine neutrale durchgezogene Linie (die Bauvorlagenverordnung verwendet eine violette Linie aus langen Strichen),
  Schutzgebietsgrenzen eine grüne Strichpunktlinie (PlanZV 13.3 verwendet Strichgruppen), Überschwemmungsgebiete
  eine Schraffur (PlanZV 10.2 eine wellenförmige Umgrenzung).
- **Rasen, Wiese und Blumenwiese** teilen sich eine Farbfamilie, wie in jedem untersuchten Schema; der Hausstil
  unterscheidet sie durch die Textur, nicht durch den Farbton.
- **Belagsmaterialien** sind eine Unterscheidung des Hausstils: Kein europäisches Schema und nur wenige deutsche
  Schemata kennen sie, daher werden externe Schlüssel auf allgemeine Elemente (`sealed`, `concrete_pavers`)
  abgebildet und nicht auf ein geratenes Material.
- **Klimaklassen** (`klimatop`, `utci`, `pet`) verwenden Hausfarben in der üblichen Farbreihenfolge; einen
  numerischen Farbstandard gibt es noch nicht (VDI 3787 Blatt 12 ist in Vorbereitung).

## 6.7 Aktuell halten

Standards ändern sich: Die PlanZV wurde 2025 geändert, CLC 2024 wird erwartet, DIN 18920 ist 2026 in einer neuen
Ausgabe erschienen. Der Bericht nennt, was zu beobachten ist, und den Stand vom 30. September 2026
([Bericht 5.4](research/standards-report.md#54-what-to-re-check-when-standards-change)). Wenn sich eine Quelle
ändert, aktualisieren Sie die Element-, Theme- oder Crosswalk-Datei, vermerken Sie die Ausgabe in deren Feld
`version` oder `evidence`, führen Sie die Tests aus und erzeugen Sie die Blätter neu ([Erweitern des Stils](08-extending.md)).

**Lizenzen.** Schlüssel und veröffentlichte Farbwerte sind Fakten und werden zitiert, nicht als Grafik übernommen.
Symboldateien des BfN (CC BY-ND / alle Rechte vorbehalten) und von UKHab (lizenzgebunden) werden nicht
mitgeliefert; die Bibliothek zeichnet eigene Symbole nach denselben Konventionen. Wenn Sie eine Karte im Theme
`basemap` veröffentlichen, nennen Sie „© basemap.de / BKG“ ([Bericht 5.3](research/standards-report.md#53-licences)).

---

Weiter: [7 · Für KI-Agenten](07-agents.md)

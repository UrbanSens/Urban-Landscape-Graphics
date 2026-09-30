# WIP notes stream 04 (image-derived facts, to be merged into 04_osm_national_topo_prior_art.md)

## BEV DKM DXF – "Katastralmappe DXF, Schnittstellenbeschreibung – Version 2.6 freigegeben am 16.12.2024"
URL: https://www.bev.gv.at/dam/jcr:3a92eaa4-9e9e-4ce3-af96-c1fa6e722548/BEV_S_KA_Katastralmappe_DXF_V2.5.2.pdf (46 pages) – read pages 1-12, 15-26 as images (V)

Layer table (Kap. 6): Objektart | Layer | Farbe Screen | Farbe Plot
- Mappenblattkennung RL | v–6 | s–7
- Staatsgrenze RG | Farbe–12 | br–8
- Landesgrenze LG | Farbe–11 | br–8
- Vermessungsbezirksgrenze VG | Farbe–21 | br–8
- Bezirksgerichtsgrenze BG | c–42 | br–8
- Politische Gemeindegrenze PG | g–51 | br–8
- Katastralgemeindegrenze KG | v–62 | br–8
- Grundstücksgrenze GG | w–7 | s–7 (polyline; ideelle Grenze Linetype DOT)
- Grundstücksnummer GN | w–7 | s–7
- GNR am Rand RN | v–6 / br–13 | s–7
- GNR mit Pfeil PN | w–7 | s–7
- Gebäudegrenze (Hausgrenze) HG | r–1 | r–1
- Gebäudegrenze (Hausgrenze) HL (aus Luftbildauswertung) | br–9 | br–8
- Nutzungsgrenze NG | gr–3 | gr–3
- Nutzungssymbole NS | gr–3 | gr–3 | insert FIG040-041, FIG048, FIG052-054, FIG056, FIG059-062, FIG072, FIG083-084, FIG087-088, FIG092, FIG095-096
- Verkleinerte Nutzungssymbole VS | gr–3 | gr–3 (Größenfaktor = Maßstab/2)
- Nutzungssymbole am Rand RS | v–6 | gr–3
- Sonstige Linie SG | bl–5 | bl–5 (unterirdisch: Linetype UGROUND strichliert)
- Sonstige Symbole SS | bl–5 | bl–5 ; FIG073, FIG074, FIG077, FIG078: o–30 | o–30
- Sonstige Beschriftung SB | bl–5 | bl–5
- Grenzpunkt GP | w–7 | s–7 ; Staatsgrenzpunkt SP w–7/s–7 ; RGB layer bl–5/br–8
- PP, EP, TP, HP | w–7 | s–7
Abbreviations (Kap. 7): Farbe "Screen" = AutoCAD-Bildschirm, "Plot" = DKM-Auszeichnung; "bl, br, g, gr, r, s, v, w für blau, braun, gelb, grün, rot, schwarz, violett, weiß" (numbers = AutoCAD colour index).
Text: "Das Nutzungssymbol FIG041 (Gebäude) wird rot dargestellt." ; 2012: "Rechtssymbole: Die Farbgebung der Rechtssymbole (FIG073, FIG074, FIG077, FIG78) wurde auf orange gesetzt. Anm.: Für die weiteren Symbole bleibt die Farbe grün bzw. blau." ; "Straßenverkehrsanlagen sind mit dem Nutzungssymbol FIG095 ("V") zu bezeichnen."
Nutzungsgrenzen hierarchisch den Grundstücksgrenzen untergeordnet; Flächenbezeichnung über Referenzpunkt der Nutzungssymbole (= Nutzungsflächen).

Symbols (2003 → 2012 description), layer NS unless noted:
- FIG040: Gärten (Gt) → Dauerkulturanlagen oder Erwerbsgärten
- FIG041: Gebäude (Bauflächenpunkt) → Gebäude
- FIG042 (new 2012): Parkplätze
- FIG048: Landwirtschaftlich genutzte Grundflächen (LN) → Äcker, Wiesen oder Weiden
- FIG052: Baufläche begrünt → Gärten
- FIG053: Weingärten (Wgt) → Weingärten
- FIG054: Alpen → Alpen
- FIG055 (new 2012): Krummholzflächen
- FIG056: Wald (Wld) → Wälder
- FIG057 (new 2012): verbuschte Flächen
- FIG058 (new 2012): Forststraßen
- FIG059: Gewässer fließend (Flusspfeil) → Fließende Gewässer
- FIG060: Gewässer stehend → Stehende Gewässer
- FIG061: Sumpf → Feuchtgebiete
- FIG062: Ödland → Vegetationsarme Flächen
- FIG063 (new 2012): Betriebsflächen
- FIG064 (new 2012): Gewässerrandflächen
- FIG065 (new 2012): Verkehrsrandflächen
- FIG072: Friedhof (SS) → Friedhöfe (NS)
- FIG083: Baufläche befestigt → Gebäudenebenflächen
- FIG084: Abbaufläche → Abbauflächen, Halden und Deponien
- FIG087: Fels und Geröll → Fels- und Geröllflächen
- FIG088: in layer table (FIG087-088) – name not seen on pages read (Gletscher presumably, NOT verified)
- FIG092: Bahnanlage → Schienenverkehrsanlagen
- FIG095: Straßenanlage → Straßenverkehrsanlagen
- FIG096: Erholungsfläche → Freizeitflächen
- SS: FIG038 Bauwerk (Keller) unter fremden Grund; FIG039 Gebäude nicht in DKM abgebildet; FIG071 Tempel, Synagoge; FIG073 Rechtlich nicht Wald; FIG074 Rechtlich Wald; FIG077 Rechtlich Weingarten; FIG078 Rechtlich kein Weingarten
- Deleted 2012: FIG030 Waldweide, FIG044 Streuwiese, FIG045 Brachland, FIG046 Bergmahd, FIG047 Weide, FIG049 Acker, FIG050 Wiese, FIG051 Hutweide, FIG085 Deponie, FIG086 Sonstige (SB), FIG089 Streuobstwiese, FIG090 Flugverkehrsanlage, FIG091 Hafenanlage, FIG094 Technische Ver- und Entsorgungsanlage, FIG097 Lagerplatz, FIG098 Werksgelände

BANU-V § 2 (RIS NOR40117347, BGBl. II Nr. 116/2010, Fassung in Kraft 07.05.2012) – fetched as text (V):
(1) Bauflächen: Z1 Gebäude; Z2 Gebäudenebenflächen ("befestigte Flächen in Verbindung mit Gebäuden (Innenhöfe, Terrassen, kleine Vorplätze usw.)")
(2) Landwirtschaftlich genutzte Grundflächen: Z1 Äcker, Wiesen oder Weiden; Z2 Dauerkulturanlagen oder Erwerbsgärten; Z3 Verbuschte Flächen
(3) Gärten ("Haus-, Zier- und Vorgärten in Verbindung mit Gebäuden, Kleingärten oder Siedlungsflächen mit Bebauungsabsicht")
(4) Weingärten
(5) Alpen
(6) Wald: Z1 Wälder; Z2 Krummholzflächen; Z3 Forststraßen
(7) Gewässer: Z1 Fließende Gewässer; Z2 Stehende Gewässer; Z3 Gewässerrandflächen; Z4 Feuchtgebiete
(8) Sonstige: Z1 Straßenverkehrsanlagen; Z2 Schienenverkehrsanlagen; Z3 Verkehrsrandflächen; Z4 Parkplätze; Z5 Betriebsflächen; Z6 Abbauflächen, Halden, Deponien; Z7 Freizeitflächen ("künstliche Grünflächen für Freizeit- oder Erholungszwecke"); Z8 Friedhöfe; Z9 Fels- und Geröllflächen; Z10 Vegetationsarme Flächen; Z11 Gletscher

## Statutory Biodiversity Metric – User Guide (First published Feb 2024, last updated June 2026), 89 pp
URL: https://assets.publishing.service.gov.uk/media/6a1d98e9c7335e2ca6daadd5/The_Statutory_Biodiversity_Metric_-_User_Guide_-_June_2026.pdf (V; pages 1-6, 26-29, 57-69 read)
- Table 5 distinctiveness: Very high 8; High 6; Medium 4; Low 2; Very low (hedgerow module) 1; Very low (area module) 0 (p.27)
- Table 6 condition: Good 3; Fairly Good 2.5; Moderate 2; Fairly Poor 1.5; Poor 1; Condition Assessment N/A 1; N/A – Other 0 (p.28)
- Table 15 tree size classes (p.62): Small >7.5 cm and ≤30 cm DBH = 0.0041 ha; Medium >30 and ≤60 = 0.0163 ha; Large >60 and ≤90 = 0.0366 ha; Very large >90 cm = 0.0765 ha. "Tree helper values are a representation of canopy biomass, and are based on the root protection area formula, derived from BS 5837:2012."
- Modules: area (ha); hedgerow module (hedgerows and lines of trees, km); watercourse module (km); 'watercourse footprint' area category carries no units.
- Urban (p.59-60): default 70:30 ratio of 'urban – developed land; sealed surface' to 'urban – vegetated garden' for housing areas without detailed plans; created habitats in private gardens only as 'urban – vegetated garden' or 'urban - unvegetated garden'; green roofs on private dwellinghouses only 'other green roof'; green roof area subtracted from building footprint; green walls by vertical area, not contributing to site area.
- Individual trees (p.61): 'urban' or 'rural'; lines, blocks or groups of trees within/around urban land recorded as individual trees; do not use hedgerow-module 'line of trees' in urban environment; non-native ornamental hedges (leylandii) → non-native ornamental hedges in hedgerow module.
- Lakes (p.67): waterbodies <2 ha = ponds; ≥2 ha = lakes.
- Habitats with land-use function (p.57): cropland – arable field margins; lakes – reservoirs; urban – allotments; urban – cemeteries and churchyards; urban – sustainable drainage system; urban – actively worked sand pit quarry or open cast mine.
- Defined mosaics (p.58): urban - open mosaic on previously developed land; grassland - floodplain wetland mosaic and CFGM; urban – vegetated gardens; grassland – traditional orchard; woodland and forest – wood-pasture and parkland.
- Acknowledgements (p.6): "The UK Habitat Classification System is used under licence from UKHab Ltd. No onward licence implied or provided and, where applicable, the same shall be out of scope of the OGL v3.0"
- gov.uk page (last updated 2 June 2026): calc tool v1.0.4 (xlsm/xlsx), SSM tool 1.2.3, condition assessments July 2025.

## Small Sites Metric User Guide (July 2025), 63 pp – Appendix 2 Table A2 "UKHab Translation Table" (pp 58-63) (V)
URL: https://assets.publishing.service.gov.uk/media/686677acdd1a7e01559e6d45/The_Small_Sites_Metric__Statutory_Biodiversity_Metric__-_User_Guide_July_2025.pdf
SSM distinctiveness (Table 6): Medium 4; Low 2; Very low (hedgerow) 1; Very low (area) 0. Condition (Table 7): Good 3; Moderate 2; Poor 1; N/A 1; N/A–Other 0. Strategic significance: High 1.15; Medium 1.10; Low 1.
Landscape term | code | SSM broad habitat – habitat type | distinctiveness
- Saltmarsh | A2.5 | Coastal saltmarsh - Saltmarshes and saline reedbeds | Medium
- Cropland | Arable c1c | Cropland - Cereal crops | Low
- Cropland | c1c7 | Cereal crops other | Low
- Cropland | c1d | Non-cereal crops | Low
- Cropland | c1b | Temporary grass and clover leys | Low
- Cropland margins | c1a7 | Arable field margins cultivated annually | Medium
- Cropland margins | c1a8 | Arable field margins game bird mix | Medium
- Cropland margins | c1a6 | Arable field margins pollen & nectar | Medium
- Cropland margins | c1a | Arable field margins tussocky | Medium
- Cropland margins | c1c5 | Cereal crops winter stubble | Low
- Horticulture | c1f | Cropland - Horticulture | Low
- Orchard | c1e | Cropland - Intensive orchards | Low
- Amenity Grassland or Grassland Seed Mix | g4 | Grassland - Modified grassland | Low
- Amenity Grassland or Grassland Seed Mix | g4 (as printed) | Grassland - Other neutral grassland | Medium
- Bracken | g1c | Grassland - Bracken | Low
- Meadow Grassland or Wildflower Seeding | g1d | Other lowland acid grassland | Medium
- Meadow Grassland or Wildflower Seeding | g3c | Other neutral grassland | Medium
- Meadow Grassland or Wildflower Seeding | g1b | Upland acid grassland | Medium
- Invasive Scrub | h3g | Heathland and shrub - Rhododendron scrub | Low
- Native Scrub | h3a Blackthorn scrub M; h3d Bramble scrub M; h3e Gorse scrub M; h3f Hawthorn scrub M; h3b Hazel scrub M; h3h Mixed scrub M; h3cNE2 Sea buckthorn scrub (other) Low
- Native Hedge | h2NE5 Hedgerow - Native hedgerow M; h2NE2 Species-rich native hedgerow M; h2NE9 Native hedgerow - associated with bank or ditch M
- Native Hedge with Standard Trees | h2NE4 | Native hedgerow with trees | Low (as printed)
- Ornamental Hedge | h2NE3 | Non-native and ornamental hedgerow | Low
- Standard Trees | w1g6NE4 Line of trees - associated with bank or ditch Low; w1g6NE2 Line of trees Low; w1g6NE1 Ecologically valuable line of trees - assoc. bank or ditch Medium; w1g6NE3 Ecologically valuable line of trees Medium
- Intertidal: ART_A1.4 Artificial features of hard structures Low; ART_A1 Artificial hard structures Low; ART_A1_IGGI Artificial hard structures with IGGI Medium; artificial littoral sediments Low; A2.4 Littoral mixed sediments Low; A2.21 Littoral sand Medium
- Reservoirs | 108 | Lakes - Reservoirs | Medium
- Wildlife Pond | r1b | Lakes - Ponds (non-priority habitat) | Medium
- Canal | r1eNE1 | Rivers & Streams - Canals | Medium
- Culvert | rNE1 | Rivers & Streams - Culvert | Low
- Ditch | r1eNE2 | Rivers & Streams - Ditches | Medium
- Ruderals | 17 | Sparsely vegetated land - Ruderal/ephemeral | Low
- Scree | s1d | Sparsely vegetated land - Other inland rock and scree | Medium
- Allotments | 910 | Urban - Allotments | Low
- Bare ground | 510 | Urban - Vacant/derelict land/ bare ground | Low
- Biodiverse Roof | 1113 | Urban – Biodiverse green roof | Medium
- Bioswale | 1191 | Urban - Bioswale | Low
- Cemetery | 800 | Urban - Cemeteries and churchyards | Medium
- Garden | 231 | Urban - Vegetated Garden | Low
- Garden | 232 | Urban - Un-vegetated garden | Very low
- Green Roof | 1111 | Urban - Other green roof | Medium (as printed; other sources say Low – check tool)
- Green Roof - Sedum | 1112 | Urban - Intensive green roof | Low
- Green Wall | 1122 | Urban - Facade-bound green wall | Low
- Green Wall | 1121 | Urban - Ground based green wall | Low
- Impermeable Hardscape | u1b | Urban - Developed land; sealed surface | Very low
- Ornamental Pond | 362 | Lakes - Ornamental Lake or pond | Low
- Ornamental Shrub Planting | 1160 | Urban - Introduced shrub | Low
- Permeable Hardscape | u1c | Urban - Artificial unvegetated, unsealed surface | Very low
- Planters | 1140 | Urban - Ground level planters | Low
- Quarry | 1030 | Urban - Sand pit quarry or open cast mine | Low
- Standard Tree | 1170 | Urban - Urban tree | Low (as printed in SSM)
- SuDS | 1192 | Urban - Rain garden | Low
- SuDS | 1119 | Urban - Sustainable drainage system | Low
- Wall | u1e | Urban - Built linear features | Very low
- Conifer Woodland | w2c | Other coniferous woodland | Low
- Conifer Woodland | w2b | Other Scot's pine woodland | Medium
- Native Broadleaved Woodland | w1g | Other woodland; broadleaved | Medium
- Native Mixed Woodland | w1h | Other woodland; mixed | Medium

## LBP-Musterlegendenkatalog (Bundesnetzagentur; 2. Fassung, Dezember 2021; redaktionell überarbeitet ggü. Sept 2020) (V – pages 1-19 read)
URL: https://www.netzausbau.de/SharedDocs/Downloads/DE/Methodik/Eingriffsregelung/LBP-Musterlegendenkatalog.pdf?__blob=publicationFile
- Maßstab Bestands-/Konflikt-/Maßnahmenpläne 1:1.000 bis 1:5.000; Übersicht 1:5.000–1:25.000.
- "Eine farbige Gestaltung der Pläne wird als Standard vorausgesetzt ... (z. B. blauer Farbton für wasserbezogene Themen)"; Schraffuren: Farbe und Ausrichtung beizubehalten; Punktsymbole maßstabsabhängig skalierbar.
- Luftbild als Grundlage: Flächen mit Transparenz, "Der empfohlene Transparenzwert beträgt 35%".
- Biotop-/Realnutzungsgrenzen: Bestands-/Konfliktplan grau RGB 78/78/78; Maßnahmenplan grün RGB 38/115/0.
- Obergruppen + RGB (4.1): Laubwald "RGB: 0/168/132" as printed (swatch looks light green; sect. 5.3 gives Laubwald hatch 137/205/102 → probable typo); Nadelwald 114/137/68; Mischwald Fläche 137/205/102 + Linie 114/137/68 (vertical stripes); Waldrand/Waldlichtung Fläche 137/205/102 + Linie 163/255/115 (diagonal); Flächenhafter Gehölzbestand 163/255/115; Solitärbaum / Einzelbaum / Neupflanzung-Jungbaum / Einzelstrauch point symbols 163/255/115; Stillgewässer 0/197/255; Fließgewässer (line) 0/197/255; Quellbereich (triangle) 0/197/255; Gehölzfreie Biotope der Sümpfe, Niedermoore und Ufer 205/205/102; Übergangsmoore Fläche 205/205/102 + Punkte 168/112/0; Hochmoore 168/112/0; Fels-, Gesteins- und Offenbodenbiotope 245/162/122; Heiden und Magerrasen 245/122/182; Grünland 220/255/200; Trockene bis feuchte Stauden- und Ruderalfluren 232/190/255; Acker- und Gartenbaubiotope 255/255/220; Siedlungsbiotope: Grünanlagen 158/215/194; Gebäude / Wohn- und Mischbebauung 255/200/200; Verkehrs- und Industrieflächen / Infrastruktur im Außenbereich 225/225/225.
- Schutzgebiete: FFH-Gebiet 0/168/132; Vogelschutzgebiet 122/182/245; Naturschutzgebiet "02300/169" (typo as printed; presumably 0/230/169); Landschaftsschutzgebiet 230/230/0; Nationalpark 255/115/223; Naturpark 85/255/0; Biosphärenreservat 255/115/223; Überschwemmungsgebiet 0/112/255; Wasserschutzgebiet 179/255/255; Gesetzlich geschütztes Biotop 223/115/255; Geschützter Landschaftsbestandteil 137/68/101; Natur-/Kulturdenkmal 255/190/232; Lebensraumtyp 132/0/168.
- Maßnahmen: Neuanlage/Anpflanzung/Entwicklung = diagonal hatch in colour of target biotope (e.g. Grünland 220/255/200; Heiden 245/122/182; Gehölz 163/255/115); Extensivierung/Waldumbau = dot pattern RGB 0/168/132 over base colour; Maßnahmenkennung vorgezogen 255/255/0, bauzeitlich 255/170/0, nach Bauabschluss 115/178/255; Konflikt label 255/255/190; Verlust von Einzelbäumen X 255/0/0; zu schützender Baum: red ring 255/0/0 + fill 163/255/115; Entsiegelung crosshatch 78/78/78; Versiegelung "RGB: 137/68/68" as printed; Flurstücksgrenze 0/0/0.
- Example codes use Drachenfels (Niedersachsen) key.
- "style-Datei ... kann auf Anfrage von der Bundesnetzagentur ... zur Verfügung gestellt werden."

## Hamburg – Kartieranleitung und Biotoptypenschlüssel für die Biotopkartierung in Hamburg, 7. überarbeitete Auflage, Stand März 2025 (V – pp 1-8, 20-22, 46-52, 276-289 read)
URL: https://www.hamburg.de/resource/blob/1036252/de53ab36043c5d658b46aa8d4337c97b/kartieranleitung-biotoptypenschluessel-maerz-2025-data.pdf
- 451 Biotoptypen; key modelled on Niedersachsen (Drachenfels); flächendeckend; merges biotope + land-use type mapping.
- Shapes: Flächenshape >5 m Breite; Linienshape ≤5 m; Punktshape (Einzelbäume, Quellen); digitise ≥1:1.000 (Stillgewässer 1:500); attribute GRUPPE = "1. Buchstabe des Biotoptyps (Feldwerte dienen der Legendenbildung)"; no RGB table found in pages read.
- Wald: Deckung Baumschicht >30 %; BHD classes 1 = 7–<13 cm Stangenholz; 2 = 13–<50; 3 = 50–<70; 4 = ≥70 cm.
- Groups: A Gras-, Stauden- und Ruderalfluren; B Biotopkomplexe der Siedlungsflächen; E Biotopkomplexe der Freizeit-, Erholungs-, Grünanlagen; F Lineare und Fließgewässer; G Grünländer; H Gebüsche und Kleingehölze; K Küstenbiotope; L Biotope landwirtschaftlich genutzter Flächen; M Hoch- und Übergangsmoore; N Biotope der Sümpfe und Niedermoore (gehölzfrei); O Offenbodenbiotope; S Stillgewässer; T Heiden, Borstgrasrasen, Magerrasen; V Biotopkomplexe der Verkehrsflächen; W Wälder; Y Biotope vegetationsarmer Flächen mit Spontanvegetation; Z Vegetationsbestimmte Habitatstrukturen besiedelter Bereiche.
- Z: ZH Gepflanzter Gehölzbestand (ZHF nicht heimisch, ZHN heimisch); ZN Nutzbeet; ZR Rasen (ZRE Raseneinsaat, ZRR Extensivrasen-Einsaat, ZRT Scher- und Trittrasen, ZRW Stadtwiese); ZS Zier-Gebüsch, -Hecke (ZSF nicht heimisch, ZSH Zierstrauchhecke, ZSN heimisch/standortgerecht, ZSR Rankengewächse, Lianen, ZSS Schnitthecke); ZZ Zierbeet, Rabatt.
- Y: YD Dach (YDG Begrüntes Dach, YDK Kiesdach, YDR Reetdach, YDX Sonstiges Dach, YDZ Ziegeldach); YF Befestigte und unbefestigte Flächen (YFB Unbefestigter Rand, Baumscheibe; YFK Kies- oder Schotterdecke; YFP Gepflasterte Fläche, Ziegel, Betonplatten etc.; YFR Pflasterritzen; YFS Stein- und Blockschüttung; YFV Asphalt- oder Betondecke; YFW Unbefestigte, verdichtete Erd- oder Sandfläche; YFZ Sonstige befestigte Fläche); YM Mauer oder Wand (YMF Fachwerk, YMH Holzwand, YMN Natursteinwand/-mauer, YMW Wand im Wasserwechselbereich, YMX Sonstige Wand oder Mauer, YMZ Ziegelwand/-mauer).
- E: EB Freibad; EC Zelt-, Camping- oder Bauwagenplatz; EF Friedhof (EFA Sonstiger gehölzarmer, EFW Waldfriedhof, EFP Parkartiger, EFR Sonstiger gehölzreicher); EG Tierpark, Tiergehege; EH Hausgarten (EHN Naturgarten, EHP Parkartiger Garten mit Großbäumen, EHH Hausgartengebiet heterogen, EHB Bauerngarten traditionell, EHG Gemüsegarten, EHO Obstgarten, EHZ Ziergarten); EK Kleingartenanlage (EKR strukturreich, EKA strukturarm, EKZ Sonstiger Kleingarten, Grabeland); EP Park / Grünanlage / Freizeitpark (EPA Kleinteilige Grünanlage naturnah, EPB Botanischer Garten, EPI Intensiv gepflegte Parkanlage, EPK Kleinteilige Grünanlage naturfern, EPL Alter Landschaftspark, EPN Parkneuanlage, EPW Waldartige Parkanlage, EPZ Sonstiger Park oder Grünanlage); ES Sportplatz (ESB Ball- und Laufsportanlage, ESG Golfplatz, ESS Sonstige großflächige Sportanlage); ET Spielplatz; EX Sonstige Freizeit-, Erholungs- oder Grünanlage.
- H: HE Einzelbaum und Baumgruppe (HEA Baumreihe, Allee; HEE Einzelbaum; HEG Baumgruppe); HF Weidengebüsch der Auen/Ufer; HG Feld-, Stadt- und Kleingehölz (HGF, HGM, HGT, HGX standortfremd, HGZ); HH Ebenerdige Hecke (HHB Baumhecke, HHM Strauch-Baumhecke, HHN Heckenneuanlage, HHS Strauchhecke); HM Mesophiles Gebüsch; HR Ruderal- und sonstiges Gebüsch (HRR Ruderalgebüsch, HRX Standortfremdes Gebüsch, HRZ Naturnahes sonstiges Sukzessionsgebüsch); HS Moor- und Sumpfgebüsch; HT Gebüsch bodensaurer/trocken-magerer Standorte; HU Ufergehölzsaum; HW Knick (Wallhecke).
- A: AH Gras- und Staudenflur trockener bis mittlerer Standorte (AHM, AHP Adlerfarn, AHT); AK Halbruderale Gras- und Staudenflur (AKF, AKM, AKT); AN Neophytenflur (ANF Staudenknöterich, ANS Goldruten, ANZ); AP Ruderalflur (APF feucht, APM mittel, APT trocken).
- G: GF Sonstiges Feucht- und Nassgrünland; GI Artenarmes Grünland (GIA Grünland-Einsaat, Grasacker; GIF; GIM gemäht mittlerer Standorte; GIS auf Sand; GIW beweidet); GM Artenreiches Grünland frischer bis mäßig trockener Standorte (GMG Glatthafer-Wiese FFH 6510; GMM Wiesen-Fuchsschwanz-Wiese; GMT; GMW; GMZ); GN Seggen-, binsen- und hochstaudenreiche Nasswiese; GW Stark veränderte Weidefläche.
- N: NG Seggen-, Binsen- und Simsenrieder; NH Hochstaudenflur feuchter bis nasser Standorte; NP Pioniervegetation (wechsel-)nasser Standorte; NR Röhricht (NRB Bach-/Kleinröhricht, NRE Simsen, NRG Rohrglanzgras, NRR Rohrkolben, NRS Schilf, NRT Schilf Tide-Elbe, NRW Wasserschwaden, NRZ); NU Feuchter Staudensaum.
- O: OA Aufschüttungsfläche (OAG Schotterfläche, Steinhaufen, Blockschüttung; OAS Spülfläche, Sandaufschüttung; OAT; OAX); OB Abgrabungsfläche (OBK Kies- und Sandabbau; OBT; OBX); OK Abbruchkante; OW Nicht oder leicht befestigter Weg (OWL Lehmweg, OWS Sandweg, OWX); OX Sonstige offene Fläche und Rohbodenstandorte.
- S: SE naturnah nährstoffreich (SEG Angelegtes Stillgewässer klein; SER Naturnahes Regenrückhaltebecken; SET Teich; ...); SO nährstoffarm; ST Tümpel; SV Stillgewässervegetation; SX Naturfernes Stillgewässer (SXA Abbaugewässer, SXG Naturfernes Ziergewässer, SXK Klärteich/Absetzbecken, SXL Löschwasserbecken, SXP Fischteich, SXR Rückhaltebecken naturfern, SXT Teich naturfern, SXY Beregnungsbecken, SXZ Sonstiges naturfernes Wasserbecken).
- F: FB Bach; FF Fluss; FG Graben mit Stillgewässercharakter; FH Hafenbecken; FK Kanal; FL Gräben und Wettern mit Fließgewässercharakter; FQ Quellbereich; FS Flussstrand; FV Fließgewässervegetation; FW Flusswatt; FX Fließgewässer, verrohrt.
- L: LA Acker (LAL, LAM, LAS); LB Baumschule; LG Erwerbsgartenbaufläche (LGG unter Glas; LGO im Freiland); LO Obstpflanzung (LOA Obstbaumplantage; LOB Beerenobstplantage; LOW Obstwiese); LW Wildacker; LZ Sonstige.
- V: VB Bahnanlage (VBG Gleisanlage); VK Hafen- und Schleusenanlage; VL Luftverkehrsfläche; VS Straßenverkehrsfläche (VSA Autobahn oder Schnellstraße; VSF Fußgängerfläche und Radwege; VSL Land-/Haupt- oder Durchgangsstraße; VSM Städtischer Platz; VSP Parkplatz; VSS Wohn- oder Nebenstraße; VSW Wirtschaftsweg; VSZ Sonstige).
- B: BB Geschlossene Bebauung (BBA Altstadt, BBG, BBN, BBV); BF Gebäudekomplex der Verkehrsanlagen; BH Hochhausbebauung; BI Industrie-/Gewerbefläche (BIG, BII); BM Dörfliche Bebauung; BN Einzel- und Reihenhausbebauung (BNA, BNE, BNG, BNN, BNO, BNS, BNV); BR Blockrandbebauung; BS Sonstige Bebauung; BV Ver- und Entsorgungsfläche; BZ Zeilenbebauung.
- W: WB Bruch-/Moorwälder; WC Eichen-Hainbuchenwald; WE Erlen-/Eschenwald; WH Hartholz-Auwald; WI Waldlichtungs-/Kahlschlagsflur; WJ Wald-Jungbestand; WM Buchenwald; WN Nadelwald/-forst naturnah; WP Pionierwald/Vorwald; WQ Bodensaurer Eichen-Mischwald; WR Waldrand; WS Sumpfwald; WW Weiden-Auwald; WX Sonstiger Laubforst naturfern; WY Sonstiger Mischwald naturfern; WZ Nadelforst naturfern.
- T: TC Zwergstrauch-Heide; TD Binnendüne; TM Trocken-/Halbtrockenrasen; TN Borstgrasrasen. M: MF, MH, MM, MX.

## Swiss AV – Weisung "Amtliche Vermessung: Darstellung des Planes für das Grundbuch", vom 9. März 2007 (Stand am 1. Februar 2014), swisstopo / Eidg. Vermessungsdirektion, 25 pp (V – pages 1-8, 12-17, 19-21, 24-25 read)
URL: https://www.cadastre-manual.admin.ch/dam/de/sd-web/pysw2JgMIIer/Weisung-GB-de.pdf
- Standard scales on paper: 1:200, 1:250, 1:500, 1:1000, 1:2000, 1:2500, 1:5000 und 1:10000; symbol dimensions defined for reference scale 1:1000; point symbols integrated in font CADASTRA (open-source font based on Bitstream; may be modified if renamed).
- 1.5.6 Farbe: "Die Darstellungsbeschreibung des Planes für das Grundbuch benutzt die schwarze Farbe, die Verwendung von eingefärbten Elementen in den Plänen für das Grundbuch ist optional."
- Uniform legend at www.cadastre.ch/legende (instead of legend on plan).
- Priority layers (top→bottom): Planrahmen; Hoheitsgrenzpunkte; Fixpunkte; Liegenschaften Grenzpunkte; ...; Bodenbedeckung Liniensignaturen; Rohrleitungen; Planabgrenzung; Bodenbedeckung Flächensignaturen BB-Art "Gebäude" (Raster); Einzelobjekte Flächensignaturen; Bodenbedeckung Flächensignaturen übrige BB-Arten (Raster).
- 3.3 Bodenbedeckung boundary line types (0.20 mm at 1:1000): ausgezogen (solid) for: fliessendes, Flugplatz, Gebaeude, stehendes, Strasse_Weg, Trottoir, Verkehrsinsel, Wasserbecken; gestrichelt1 (dashed 1.5/0.5 mm) for: Abbau_Deponie, Acker_Wiese_Weide, Bahn, Fels, Gartenanlage, Geroell_Sand, geschlossener_Wald, Gletscher_Firn, Hoch_Flachmoor, Reben, Schilfguertel, uebrige_befestigte, uebrige_bestockte, uebrige_humusierte, uebrige_Intensivkultur, uebrige_vegetationslose, Wytweide_dicht, Wytweide_offen; projektierte Objekte: gestrichelt.
- 3.4 Einzelobjekte line types (0.20 mm; schmaler_Weg 0.30 mm): Mauer ausgezogen; schmale_bestockte_Flaeche gestrichelt2; schmaler_Weg gestrichelt2; Rinnsal ausgezogen; eingedoltes_oeffentliches_Gewaesser punktiert; unterirdisches_Gebaeude punktiert; Brunnen ausgezogen; wichtige_Treppe ausgezogen; Bahngeleise strichpunktiert2; Uferverbauung ausgezogen; Unterstand gestrichelt2; uebriger_Gebaeudeteil gestrichelt2 ...
- Line style table: Punktiert 0.5/0.5 (0.20 mm); Gestrichelt 2.5/0.7 (0.40); Gestrichelt1 1.5/0.5 (0.20); Gestrichelt2 1.0/0.7; Gestrichelt3 4.0/1.0 (0.40); Strichpunktiert1 6.5/1.0/1.0/1.0/1.0/1.0; Strichpunktiert2 10/1.0/1.8/1.0 (0.20); Planabgrenzung grau 30 % RGB 178,178,178 (10 mm band); Bodenverschiebung grau 60 % RGB 102,102,102 (10 mm).
- 4 Flächensignaturen (b/w): "Alle Raster mit Symbolen werden in grau (ca. 50 %) dargestellt [RGB 130,130,130 / CMYK 0,0,0,50], mit Ausnahme der Punktsignatur (bestockte Flächen)". Gebäude: 30 % Grau Raster (RGB 178,178,178 / CMYK 0,0,0,30); proj. Gebäude ohne Füllung. Unterirdisches Gebäude, Reservoir: 10 % Grau Raster (RGB 225,225,225 / CMYK 0,0,0,11). Reben: symbol (CADASTRA 'b') size 3.0 mm, Abstand 10 mm. Moor: symbol 'D' size 4, Abstand 10. Schilfgürtel: symbol 'c' 3.0, Abstand 10. geschlossener Wald: dot 0.3 mm, Abstand 2 mm. uebrige bestockte: dot 0.3, Abstand 4. Wytweide dicht: dot 0.3, Abstand 8. Wytweide offen: dot 0.3, Abstand 16. Fels: symbol '1' 2.0, Abstand 0. Geröll, Sand: symbol '2' 2.0, Abstand 0. (symbols staggered per row)
- 2.3 point symbols (variable size, at 1:1000): Fliessrichtung H=6 mm (a); Reben (grau 50 %) H=3 (b); Schilfgürtel (grau 50 %) H=3 (c); Moor (grau 50 %) L=4 (D); Wasserbecken, stehendes Gewässer (grau 50 %) L=4 (e); Grotte/Höhleneingang Ø4.5 (f); Einzelner Fels L=4 (g); Mast-Antenne H=4 (h); Quelle H=4 (i); Bildstock/Kruzifix H=4 (j); Denkmal H=4 (k); Fähre H=5 (n); wichtiger Einzelbaum H=4 (o) [cloud-shaped crown outline with centre dot]; Aussichtsturm (p); Bezugspunkt (q).
- 6 Plan für das Grundbuch – Farbig (optional; built on BP-AV colours): "Es werden nur die ... Flächensignaturen der Bodenbedeckungsarten Gebäude, befestigte Flächen, Gewässer und bestockte Flächen sowie die unterirdischen Gebäude des Topics Einzelobjekte dargestellt. Alle übrigen Symbole und Flächen werden nicht farblich dargestellt". Values "(CMYK) / (RGB)":
  - Gebäude: Füllung Rosa (0,25,25,0) / (255,191,191); proj. Gebäude keine Füllung
  - Unterirdisches Gebäude & Reservoir: (0,41,41,0) / (255,150,150) – Punktraster, Hintergrund transparent; proj. keine Füllung
  - Stehendes Gewässer, Fliessendes Gewässer, Wasserbecken: Füllung Blau (30,10,0,0) / (179,230,255)
  - Strasse-Weg: Füllung Grau (0,0,0,25) / (191,191,191)
  - Übrige befestigte, Trottoir, Flugplatz: Füllung Grau (0,0,0,12) / (224,224,224)
  - Geschlossener Wald: Füllung Grün (39,0,39,0) / (156,255,152)
  - Line: Bodenverschiebung (0,29,90,0) / (255,182,25), 10 mm

## Swiss AV – Weisung "Darstellung des Basisplans der amtlichen Vermessung «BP-AV»", Fassung vom 22. April 2009, 18 pp (V – all pages read)
URL: https://www.cadastre-manual.admin.ch/dam/de/sd-web/Zi4MHUCeFgtz/Weisung-BP-AV-de.pdf
- BP-AV: graphic product from DM.01-AV-CH, b/w or colour; "in erster Linie als Planhintergrund in Rasterform vorgesehen, der mit zusätzlicher Thematik überlagert werden kann"; automatic derivation without geometric generalisation.
- Scales 1:2'500, 1:5'000, 1:10'000; reference scale 1:5'000; factors: 1:2'500 → 1.4; 1:5'000 → 1.0; 1:10'000 → 0.7. Own data catalogue per scale.
- All colour values in this Weisung are CMYK only ("Die Werte in Klammern entsprechen den CMYK-Werten").
- Priority table "Situation" (priority; theme; transparency colour version; scales): 15 names; 14 Koordinatenkreuz; 13 Grenzen; 12 EO point/line objects incl. wichtiger_Einzelbaum, Bahngeleise, Bruecke_Passerelle, Mast_Antenne...; 11 BB Flugplatz, Strasse_Weg (all scales), Trottoir (1:2500 only), Verkehrsinsel (1:2500 only); 10 Bahn (BB), Mauer (EO, 1:2500 only), Uferverbauung (1:2500 only); 9 Gebaeude (all), uebrige_befestigte (1:2500 only); 7 EO Bahnsteig, Brunnen, Faehre, Landungssteg, Lawinenverbauung, Reservoir, Rinnsal, schmale_bestockte_Flaeche, Schmaler Weg, Unterstand; 6 Hoehenkurven, Kotenpunkt; 5 BB Abbau_Deponie, Gartenanlage (1:2500+1:5000), Hoch_Flachmoor, Reben, Schilfguertel; 4 BB fliessendes, stehendes, Wasserbecken (1:2500+1:5000); 3 Fels/Geroell raster (from Landeskarte); 2 BB geschlossener_Wald (transparency 65), Gletscher_Firn (65), uebrige_bestockte (50), Wytweide_dicht (65), Wytweide_offen (65); 1 Relief (colour version only). NOT in the BP-AV catalogue at all: Acker_Wiese_Weide fill (white/blank; only boundary line), uebrige_humusierte, uebrige_Intensivkultur, uebrige_vegetationslose.
- 2.1.3 point symbols (colour version, CMYK; size mm at 1:5'000; CADASTRA key): Schilfgürtel Blau (70,60,0,0) 1.8 c; Moor Blau (70,60,0,0) 2.0 d; Grotte Schwarz (0,0,0,100) 1.8 f; Einzelner Fels Schwarz 2.4 g; Mast-Antenne Schwarz 4.3 h; Bildstock Schwarz 2.8 y; Fähre Schwarz 4.3 n; Wichtiger Einzelbaum Grün (100,43,100,0) 2.4 w; Aussichtsturm Schwarz 3.0 x; Ruine Schwarz 2.4 u; Flugplatz Schwarz 4.4 6; Kotenpunkt Braun (20,60,100,0) 0.6; Denkmal Schwarz 3.1 k; Reben Grün (80,34,100,0) 2.0 v; Koordinatenkreuz Schwarz 4.0 s.
- 2.2.4 BB boundary lines (0.20 mm at 1:5'000; Strasse_Weg 0.25 mm): Gebaeude see 2.3.2, Ausgezogen; Strasse_Weg, Verkehrsinsel, Trottoir, Flugplatz: Schwarz (0,0,0,100) Ausgezogen; uebrige_befestigte Schwarz Strichliert1; Gartenanlage Grün (70,40,100,0) Strichliert1; Fliessendes, Wasserbecken, stehendes: Blau (70,60,0,0) Ausgezogen; Gletscher_Firn Blau (98,72,31,0) Strichliert1; Geroell_Sand, Geschlossener_Wald, Wytweide_dicht, Wytweide_offen, Uebrige_bestockte, Moor, Schilfgürtel: Keine (no outline, area signature only); Reben Grün (80,34,100,0) Ausgezogen; Acker_Wiese_Weide Schwarz Strichliert1; Abbau_Deponie Schwarz Strichliert1.
- 2.2.5 EO lines (0.12–0.20 mm; Weg and Rinnsal 0.30): schmale_bestockte_Flaeche Grün (100,43,100,0) Strichliert2 0.15; Brunnen Blau (70,60,0,0) 0.15; Reservoir Blau (70,60,0,0) Punktiert 0.15; Rinnsal Blau (70,60,0,0) Ausgezogen 0.30; Hochspannungsfreileitung Blau (82,46,10,0) Strichpunktiert1 0.20; Mast_Antenne Blau (82,46,10,0); Mauer Schwarz Ausgezogen 0.15; Uferverbauung Schwarz 0.15; Schmaler Weg Schwarz Strichliert1 0.30; Bruecke_Passerelle, Bahnsteig, Bahngeleise Schwarz Ausgezogen 0.20; Skilift Braun (37,80,100,0); Tunnel punktiert 0.20.
- 2.2.6 Liegenschaften Granat (15,50,50,0) 0.20 mm (separate binary raster layer; "Farbwerte sind eine Empfehlung"); Gemeinde-/Kantons-/Landesgrenze Granat (29,100,100,0) 0.40 mm.
- 2.2.10 Höhenkurven Braun (45,73,100,0) 0.15 mm (Zählkurven 0.25), Äquidistanz 10 m (5 m Zwischenkurven if slope < 5 %), Zwischenhöhenkurve punktiert. Koordinatennetz Schwarz 0.12 mm.
- 2.3.2 Gerasterte Flächensignaturen (CMYK):
  - Gebäude b/w: Punktraster Schwarz (0,0,0,100), Abstand 0.5 mm. Gebäude colour 1:2'500 and 1:5'000: Füllung Rosa (0,25,25,0), Kontur Rosa (34,78,100,0); 1:10'000: Füllung und Kontur Rosa (6,72,47,0).
  - Reben: b/w Schwarz / colour Grün (80,34,100,0); symbol v 2.0 mm, Abstand 1.5/3.5, Entfernung 0.75/1.75.
  - Moor: b/w Schwarz / colour blue as 2.1.3; symbol d 2.0, Abstand 9, Entfernung 4.5.
  - Schilfgürtel: b/w Schwarz / colour blue as 2.1.3; symbol c 1.8, Abstand 9, Entfernung 4.5.
  - Geröll, Sand: b/w Schwarz / colour Grau (0,0,0,50); symbol 2, 7.1 mm. (footnote: areas not shown on Landeskarte 1:25'000)
  - Stehendes Gewässer b/w: horizontal line hatch Schwarz 0.12 mm, Abstand 0.8. Colour (Stehendes Gewässer, Wasserbecken, Fliessendes Gewässer): "Farbversion ohne Schraffur", Füllung Blau (30,10,0,0), Transparenz 0 %.
  - Geschlossener Wald, Übrige bestockte: b/w dot raster Schwarz 0.3 mm, Abstand 1.5, Entfernung 0.75; colour: "Farbversion ohne Punktierung", Füllung Grün (60,0,69,0), Transparenz 65 %.
  - Wytweide dicht / offen: b/w dot 0.3, Abstand 4, Entfernung 2; colour Füllung Grün (25,0,45,0), Transparenz 65 %.
  - Bahn, Strasse und Weg: Füllung Weiss (0,0,0,0).
  - Schmale bestockte Fläche: b/w keine Füllung; colour Grün (60,0,69,0), Transparenz 65 %.
  - Gletscher, Firn: b/w keine Füllung; colour Füllung Blau (47,31,25,0), Transparenz 65 %.
  - Abbau, Deponie: Füllung Schwarz (0,0,0,100) random dot raster 0.3 mm, Abstand ~1.
- 2.4 Text: font CADASTRA; Gewässername (Objektname) Blau (100,100,0,0) 2.3 mm kursiv; Flurname 3.0 kursiv Schwarz; Ortsname 4.5 fett Schwarz; Kotenpunkt/Höhenkurven labels Braun (45,73,100,0) 1.8 kursiv.
- 3.1 Relief: "Grautonschummerung mit 2 Meter Maschenweite aus dem DTM-AV bzw. DHM25, mit Beleuchtungsrichtung Nordwest"; "Das Relief darf nicht zu kräftig wirken"; "Farbverlauf von Hellgrau (0,0,0,15) nach Hellgelb (0,0,8,0)".
- Legend: www.cadastre.ch/legende.
- DERIVED by me (naive CMYK→RGB, same formula that reproduces the RGB pairs printed in the Grundbuchplan-Weisung): Wald (60,0,69,0) → (102,255,79) #66FF4F; at 65 % transparency on white ≈ (201,255,193) #C9FFC1. Wytweide (25,0,45,0) → (191,255,140) #BFFF8C; 65 % transp ≈ (233,255,215) #E9FFD7. Gletscher (47,31,25,0) → (135,176,191) #87B0BF; 65 % transp ≈ (213,227,233) #D5E3E9. Wasser (30,10,0,0) → (179,230,255) #B3E6FF [RGB printed in GB-Weisung]. Gebäude (0,25,25,0) → (255,191,191) #FFBFBF [printed]; Kontur (34,78,100,0) → (168,56,0) #A83800; 1:10'000 (6,72,47,0) → (240,71,135) #F04787. Reben (80,34,100,0) → (51,168,0) #33A800. Einzelbaum/schmale bestockte (100,43,100,0) → (0,145,0) #009100. Gartenanlage outline (70,40,100,0) → (77,153,0) #4D9900. Water outline (70,60,0,0) → (77,102,255) #4D66FF. Gletscher outline (98,72,31,0) → (5,71,176) #0547B0. Höhenkurven (45,73,100,0) → (140,69,0) #8C4500. Kotenpunkt (20,60,100,0) → (204,102,0) #CC6600. Liegenschaften (15,50,50,0) → (217,128,128) #D98080. Grenzen (29,100,100,0) → (181,0,0) #B50000. Geröll (0,0,0,50) → (128,128,128). Relief ramp (0,0,0,15) → (217,217,217) to (0,0,8,0) → (255,255,235).

## Swiss AV – Weisung vom 1. August 2024 (Stand am 1. August 2024) "Amtliche Vermessung: Darstellungsmodell für den Basisplan der amtlichen Vermessung gemäss Geodatenmodell DMAV Version 1.0", swisstopo, 23 pp (V – pages 1-7, 11-21 read)
URL: https://www.cadastre-manual.admin.ch/dam/de/sd-web/hjNRml-W3Qoz/240801_Basisplan_DE.pdf
- In force 1 Aug 2024; applies to AV data in DMAV Version 1.0. Colours given as RGB.
- Grundsätze: b/w or colour; Referenzmassstab 1:5'000; permitted scales 1:2'500 and 1:5'000, optionally 1:10'000; factor 1.2 for 1:2'500, 0.7 for 1:10'000; PDF/A; font «Cadastra», Cadastra symbols 15 pt at reference scale.
- "Im Basisplan sind ausschliesslich Daten der amtlichen Vermessung darzustellen. Entsprechend sind keine Höhenlinien/-koten und kein Relief abzubilden. Auch auf die Felszeichnung und Geröllinformationen, die früher aus der Landeskarte 1:25'000 abgeleitet wurden, ist zu verzichten. Als Ersatz für die wegfallende Felszeichnung ist die Bodenbedeckungsart «Fels» dazustellen."
- Priorities (1 = top): 1 Landesgrenzen, 2 Kantonsgrenzen, 3 Bezirksgrenzen, 4 Gemeindegrenzen, 5 Grundstücke, 6 Nomenklatur, 7 Gebäudeadressen, 8 Bodenbedeckung/Einzelobjekte (own order in Table 3: EO point/line objects on top; then Abbau_Deponie, Acker_Wiese_Weide, Bahn, Fels, Flugplatz, Gartenanlage, Gebaeude, Geroell_Sand, Hoch_Flachmoor, Reben, Schilfguertel, Strasse_Weg, Trottoir, uebrige_befestigte, ..., Verkehrsinsel; then further EO; at the bottom fliessendes_Gewaesser, geschlossener_Wald, Gletscher_Firn, stehendes_Gewaesser, uebrige_bestockte, Wasserbecken, Wytweide_dicht, Wytweide_offen).
- Table 3 shown? (1:2'500 / 1:5'000 / 1:10'000): Abbau_Deponie ja; Acker_Wiese_Weide nein; Bahn ja; Fels ja; Flugplatz ja; Gartenanlage nein; Gebaeude ja; Geroell_Sand ja; Hoch_Flachmoor ja; Reben ja; Schilfguertel ja; Strasse_Weg ja; Trottoir ja/nein/nein; uebrige_befestigte ja/nein/nein; uebrige_humusierte nein; uebrige_Intensivkultur nein; uebrige_vegetationslose nein; Verkehrsinsel ja/nein/nein; fliessendes_Gewaesser ja; geschlossener_Wald ja; Gletscher_Firn ja; stehendes_Gewaesser ja; uebrige_bestockte ja; Wasserbecken ja/ja/nein; Wytweide_dicht ja; Wytweide_offen ja. EO: wichtiger_Einzelbaum ja; Mauer nein; Brunnen ja/ja/nein; Bahnsteig ja/ja/nein; schmaler_Weg ja; schmale_bestockte_Flaeche ja; Rinnsal ja; Uferverbauung ja/nein/nein; unterirdisches_Gebaeude nein; wichtige_Treppe nein; Quelle nein; Jauchengrube_Mistlege nein; eingedoltes_oeffentliches_Gewaesser nein; Unterstand ja; Reservoir ja.
  (Note: Table 7 nevertheless lists outline styles for Acker_Wiese_Weide and Gartenanlage – inconsistency in source.)
- DMAV value names seen: fliessendes_Gewaesser, stehendes_Gewaesser (DM.01: fliessendes, stehendes); Hoch_Flachmoor; Reben; EO Jauchengrube_Mistlege.
- Text: black, except Bodenbedeckung (water names) in colour version: blau (0,0,255). Objektname water Italic 6 pt; Flurname Italic 9; Ortsname Bold 9; Gelaendename Regular 9; Lokalisation Italic 7 (1:2'500 only). Halo allowed.
- Table 6 point symbols: wichtiger_Einzelbaum colour grün (0,145,0), Cadastra key o; others black (Grotte f, einzelner_Fels g, Mast_Antenne h, Bildstock j, Faehre n, Denkmal k, Aussichtsturm q).
- Table 7 Bodenbedeckung outlines (RGB; Strichart; mm): Gebaeude braun (161,51,0) ausgezogen 0.20; Strasse_Weg schwarz (0,0,0) ausgezogen 0.25; Trottoir, Verkehrsinsel, Flugplatz schwarz ausgezogen 0.20; uebrige_befestigte schwarz gestrichelt1 0.20; Abbau_Deponie schwarz gestrichelt1 0.20; Gletscher_Firn blau (5,71,176) gestrichelt1 0.20; Geroell_Sand, Fels, geschlossener_Wald, uebrige_bestockte, Wytweide_dicht, Wytweide_offen, Hoch_Flachmoor, Schilfguertel: keine Linie; stehendes_Gewaesser, fliessendes_Gewaesser, Wasserbecken blau (77,102,255) ausgezogen 0.20; Reben grün (51,168,0) ausgezogen 0.20; Acker_Wiese_Weide schwarz gestrichelt1 0.20; Gartenanlage grün (77,153,0) gestrichelt1 0.20. "Die Mitte der Umrandungslinie befindet sich auf dem Objektrand".
- Table 8 EO lines: Reservoir blau (77,102,255) punktiert 0.15; Brunnen blau (77,102,255) 0.15; Rinnsal blau (77,102,255) 0.30; schmaler_Weg schwarz gestrichelt1 0.30; schmale_bestockte_Flaeche grün (0,145,0) gestrichelt2 0.15; Mast_Antenne blau (46,138,230) 0.15; Hochspannungsfreileitung blau (46,138,230) strichpunktiert1 0.20; Skilift braun (161,51,0) 0.20; Bahngeleise schwarz ausgezogen 0.20; Bruecke_Passerelle schwarz 0.20; Uferverbauung schwarz 0.15; Tunnel punktiert 0.20.
- Table 9 Grundstück: rosa (217,128,128), 0.25 mm (Liegenschaft ausgezogen; SDR/Bergwerk gestrichelt1). Table 10 Hoheitsgrenzen rot (181,0,0) 0.40.
- Table 11 Flächensignaturen (b/w | colour RGB):
  - Gebaeude: solid black | rosa (255,191,191)
  - Schilfguertel: Cadastra symbol (c), Abstand horizontal 10.0 mm / vertikal 5.0 mm | blau (77,102,255)
  - Hoch_Flachmoor: Cadastra symbol (d), 10.0 / 5.0 mm | blau (77,102,255)
  - Reben: Cadastra symbol (v), horizontal 1.5 mm / vertikal 1.75 mm | grün (51,168,0)
  - Geroell_Sand: Cadastra symbol (2), Abstand 0.0 | grau (128,128,128)
  - Fels: Cadastra symbol (1), Abstand 0.0 | grau (128,128,128)
  - Abbau_Deponie: Punktraster, Punktgrösse 0.3 mm, Random, Abstand ~1 mm
  - Wasserbecken, stehendes_Gewaesser, fliessendes_Gewaesser: b/w nur Linie | blau (179,230,255)
  - geschlossener_Wald, uebrige_bestockte: b/w Punktraster 0.3 mm Abstand 1.5 mm | grün (156,255,156) Transparenz 50 %
  - schmale_bestockte_Flaeche: b/w nur Linie | grün (156,255,156) Transparenz 50 %
  - Wytweide_dicht, Wytweide_offen: b/w Punktraster 0.3 mm Abstand 4.0 mm | grün (191,255,140) Transparenz 65 %
  - Gletscher_Firn: b/w nur Linie | blau (135,176,191) Transparenz 65 %
  - Bahn, Strasse_Weg: weiss (255,255,255)
  - "Keine resp. 0 % Transparenz bedeutet, dass die Farbe vollständig deckend ist. 100 % Transparenz bedeutet, dass die Farbe vollständig transparent ist."
- DERIVED effective colour on white: Wald (156,255,156)@50 % → ≈(206,255,206) #CEFFCE; Wytweide (191,255,140)@65 % → ≈(233,255,215) #E9FFD7; Gletscher (135,176,191)@65 % → ≈(213,227,233) #D5E3E9.
- Hex: Gebäude #FFBFBF, outline #A13300; water fill #B3E6FF, outline #4D66FF; Reben #33A800; Gartenanlage outline #4D9900; Einzelbaum/schmale bestockte #009100; Geröll/Fels #808080; Wald #9CFF9C; Wytweide #BFFF8C; Gletscher #87B0BF outline #0547B0; Liegenschaft #D98080; Hoheitsgrenzen #B50000; HS-Leitung #2E8AE6.

## DM.01-AV-CH INTERLIS model (V, fetched as text): https://models.geo.admin.ch/V_D/DM.01-AV-CH_LV95_24d_ili1.ili
BBArt = (Gebaeude, befestigt (Strasse_Weg, Trottoir, Verkehrsinsel, Bahn, Flugplatz, Wasserbecken, uebrige_befestigte), humusiert (Acker_Wiese_Weide, Intensivkultur (Reben, uebrige_Intensivkultur), Gartenanlage, Hoch_Flachmoor, uebrige_humusierte), Gewaesser (stehendes, fliessendes, Schilfguertel), bestockt (geschlossener_Wald, Wytweide (Wytweide_dicht, Wytweide_offen), uebrige_bestockte), vegetationslos (Fels, Gletscher_Firn, Geroell_Sand, Abbau_Deponie, uebrige_vegetationslose));
EOArt = (Mauer, unterirdisches_Gebaeude, uebriger_Gebaeudeteil, eingedoltes_oeffentliches_Gewaesser, wichtige_Treppe, Tunnel_Unterfuehrung_Galerie, Bruecke_Passerelle, Bahnsteig, Brunnen, Reservoir, Pfeiler, Unterstand, Silo_Turm_Gasometer, Hochkamin, Denkmal, Mast_Antenne, Aussichtsturm, Uferverbauung, Schwelle, Lawinenverbauung, massiver_Sockel, Ruine_archaeologisches_Objekt, Landungssteg, einzelner_Fels, schmale_bestockte_Flaeche, Rinnsal, schmaler_Weg, Hochspannungsfreileitung, Druckleitung, Bahngeleise, Luftseilbahn, Gondelbahn_Sesselbahn, Materialseilbahn, Skilift, Faehre, Grotte_Hoehleneingang, Achse, wichtiger_Einzelbaum, Bildstock_Kruzifix, Quelle, Bezugspunkt, weitere);

## BEV – "CSV-Datei – Grundstücksdaten, Schnittstellenbeschreibung – Version 1.2 freigegeben am 29.01.2025" (V – all 6 pages read)
URL: https://www.bev.gv.at/dam/jcr:a0e89772-7b55-4889-a029-69d93311811c/BEV_S_KA_Grundstuecksdaten-csv_V1.2.pdf
Fields: KG-NR; GST-NR; G (Grenzkatasterindikator); BA (Benützungsart, Zahl 1); NU (Nutzung, Text 2); TIND; IND; FLAECHE; EMZ; GFN; GFT; KG-EZ; EZ.
"Die Benützungsarten (BA) 1 bis 8 und dazugehörige Nutzungen stellen die tatsächliche Benützungsart/Nutzung des Grundstückes in der Natur dar. Zusätzlich können rechtliche Zusatzinformationen (BA = 9 ...) angegeben werden."
BA/NU table: 1/01 Bauflächen – Gebäude; 1/02 Bauflächen – Gebäudenebenflächen; 2/01 landwirtschaftlich genutzte Grundflächen – Äcker, Wiesen oder Weiden; 2/02 – Dauerkulturanlagen oder Erwerbsgärten; 2/03 – Verbuschte Flächen; 3/01 Gärten – Gärten; 4/01 Weingärten – Weingärten; 5/01 Alpen – Alpen; 6/01 Wald – Wälder; 6/02 Wald – Krummholzflächen; 6/03 Wald – Forststraßen; 7/01 Gewässer – Fließende Gewässer; 7/02 – Stehende Gewässer; 7/03 – Gewässerrandflächen; 7/04 – Feuchtgebiete; 8/01 Sonstige – Straßenverkehrsanlagen; 8/02 – Schienenverkehrsanlagen; 8/03 – Verkehrsrandflächen; 8/04 – Parkplätze; 8/05 – Betriebsflächen; 8/06 – Abbauflächen, Halden und Deponien; 8/07 – Freizeitflächen; 8/08 – Friedhöfe; 8/09 – Fels- und Geröllflächen; 8/10 – Vegetationsarme Flächen; 8/11 – Gletscher; 9/01 Rechtlich Weingarten; 9/02 Rechtlich kein Weingarten; 9/03 Rechtlich Wald; 9/04 Rechtlich nicht Wald.

## BEV – "Katastralmappe SHP, Schnittstellenbeschreibung – Version 2.9 freigegeben am 04.12.2024" (V – pages 4-18 read)
URL: https://www.bev.gv.at/dam/jcr:a6342749-e2c2-4525-9cee-3b7531474599/BEV_S_KA_Katastralmappe_SHP_V2.9.pdf
Layers: *GST (Polygon, Grundstücke); *NFL (Polygon, Nutzungsflächen; attrs KG, NS (Integer 4, Nutzungssymbol Tab. 8), NS_RECHT (Tab. 9)); *VGG (Polylinie, Verwaltungs- und Grundstücksgrenzen; VGG 1 GG, 3 KG, 4 PG, 5 BG, 6 VG, 8 LG, 9 RG); *NSL (Polylinie, Nutzungsgrenzen und Sonstige Linien; NSL 1 Nutzungsgrenze (NG), 2 Hausgrenze (HG), 3 Hausgrenze aus Luftbild (HL), 4 Sonstige Linie (SG); TYP 0 normal, 1 unterirdisch); *GNR (Punkt); *NSY (Punkt, Nutzungs- und Rechtssymbole; NS, NS_RECHT, MST_NS 0 Originalgröße / 1 verkleinert (Faktor ½), ROT_NS); *FPT; *SGG; *SSB (Punkt, Sonstige Symbole und Beschriftung).
Tabelle 8 Nutzungssymbole (NS) – Symbolnummer | glyph | Benützungsart | Nutzung:
40 (circle with V above) | Landwirtschaftlich genutzte Grundflächen | Dauerkulturanlagen oder Erwerbsgärten
41 (dot) | Bauflächen | Gebäude
42 "P" | Sonstige | Parkplätze
48 "LN" | Landwirtschaftlich genutzte Grundflächen | Äcker, Wiesen oder Weiden
52 (stylised tree: oval on stem with foot) | Gärten | Gärten
53 (vine hook) | Weingärten | Weingärten
54 (circle under roof/angle) | Alpen | Alpen
55 (caret "^") | Wald | Krummholzflächen
56 (conifer: two curved strokes meeting at tip, with foot) | Wald | Wälder
57 (small arc/bush) | Landwirtschaftlich genutzte Grundflächen | Verbuschte Flächen
58 "FS" | Wald | Forststraßen
59 (flow arrow, 3 parallel strokes) | Gewässer | Fließende Gewässer
60 (stacked short horizontal strokes) | Gewässer | Stehende Gewässer
61 (horizontal strokes + grass tufts) | Gewässer | Feuchtgebiete
62 (ellipse with slash) | Sonstige | Vegetationsarme Flächen
63 (wheel: circle with cross and X) | Sonstige | Betriebsflächen
64 "GR" | Gewässer | Gewässerrandflächen
65 "VR" | Sonstige | Verkehrsrandflächen
72 (gravestone with cross) | Sonstige | Friedhöfe
83 (small square) | Bauflächen | Gebäudenebenflächen
84 (semicircle with "A") | Sonstige | Abbauflächen, Halden und Deponien
87 (rock zigzag with boulder) | Sonstige | Fels- und Geröllflächen
88 (six-armed star/asterisk) | Sonstige | Gletscher
92 (diamond) | Sonstige | Schienenverkehrsanlagen
95 "V" | Sonstige | Straßenverkehrsanlagen
96 "E" | Sonstige | Freizeitflächen
Tabelle 9 Rechtssymbol NS_RECHT: 73 Rechtlich nicht Wald; 74 Rechtlich Wald; 77 Rechtlich Weingarten; 78 Rechtlich kein Weingarten.
Removed 2012 (NS 2003): 49 Acker "Ac"; 50 Wiese; 51 Hutweide "W"; 85 Deponie "D"; 86 Sonstige "S"; 89 Streuobstwiese; 90 Flugverkehrsanlage; 91 Hafenanlage; 94 Technische Ver- und Entsorgungsanlage "T"; 97 Lagerplatz "LP"; 98 Werksgelände "WG".

## BEV – "Katastralmappe - SHP: Symbolisierung in ArcGIS und QGIS, Beschreibung – Version 1.0 freigegeben am 11.04.2023" (V – 10 pages read)
URL: https://www.bev.gv.at/dam/jcr:be95ead9-0fff-4413-bc14-7eca52ffe6e6/BEV_B_KA_Katastralmappe_SHP_Symbolisierung_V1.0.pdf
- "Grundsätzlich muss beachtet werden, dass der Zeichenschüssel der Vermessungsverordnung nur die zeichnerische Darstellung von Plänen gilt ... Für die Darstellung der digitalen Katastralmappe ist dieser Zeichenschlüssel rechtlich nicht verbindlich."
- BEV provides "Katastralmappe-Symbole_SHP-INFO_V*.zip" with "BEV_DKM_Symbole.ttf" (TrueType font with Nutzungssymbole), "BEV0.mxd" (ArcGIS) and "BEV0.qgz" (QGIS project). No RGB table in the PDF; screenshots show: black parcel lines, green usage symbols/boundaries, red building outlines, blue other lines/labels; Nutzungsflächen layer switched off by default ("Fertige Kataster-Darstellung (ohne Nutzungsflächen)").
- Layer order: 1 SGG, 2 FPT, 3 SSB, 4 NSY, 5 GNR, 6 NSL, 7 VGG, 8 NFL, 9 GST. EPSG 31254/31255/31256 (MGI / Austria GK West/Central/East).

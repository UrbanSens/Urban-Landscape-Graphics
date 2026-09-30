# Urban Landscape Graphics: Dokumentation

<!-- github-only:start -->
*Die Dokumentation liegt auf Deutsch (Standard) und auf Englisch vor. Dies ist die deutsche Fassung; die englische beginnt bei [en/index.md](en/index.md).*

<!-- github-only:end -->
*Der UrbanSens Ecological Vector Style als Bibliothek: ein Katalog aus Farben, Texturen und Symbolen für Karten
urbaner Landschaften, verknüpft mit deutschen und europäischen Standards, dazu Renderer für Python und Exporter
für QGIS, GeoServer, das Web und Design-Tools.*

![Angerpark, das Demoquartier, im Hausstil gezeichnet, Maßstab 1:1500](img/hero-de.png)

## Kapitel

| | Kapitel | Was Sie dort finden |
|---|---|---|
| 1 | [Herkunft](01-origins.md) | woher die Anmutung stammt: Englischer Garten, bayerische Uraufnahme von 1808, Lennés Pläne, PlanZV, OpenStreetMap, Verordnung (EU) 2024/1991 zur Wiederherstellung der Natur (Nature Restoration Regulation, NRR) und das UrbanSens-Briefing |
| 2 | [Der Stilleitfaden](02-style.md) | Prinzipien, Palette, Texturen, Linien, Symbole, Detailstufen, Zeichenreihenfolge, Lesbarkeit, Themes, Richtig und falsch |
| 3 | [Der Katalog](03-catalog.md) | die 173 Elemente, woraus ein Element besteht, die Kennwerte, die sie tragen |
| 4 | [Python](04-python.md) | Installation, Abfragen, Klassifizieren von Daten, Zeichnen von SVG- und Matplotlib-Karten, Legenden, Blätter, OSM-Daten, Standortkennzahlen, die Kommandozeile |
| 5 | [GIS und Web](05-gis-and-web.md) | QGIS-Stile, OGC SLD für GeoServer, MapLibre-Sprites und -Layer, Leaflet, Design-Tokens, Druck |
| 6 | [Standards](06-standards.md) | was „konform“ bedeutet, Themes, die 26 Zuordnungstabellen (Crosswalks), Kennwerte, Zeichenkonventionen, bewusste Abweichungen |
| 7 | [Für KI-Agenten](07-agents.md) | der Skill für Agenten, die Regeln, denen Agenten folgen, JSON-Ausgabe, Beispielanfragen |
| 8 | [Erweitern des Stils](08-extending.md) | Hinzufügen von Elementen, Farben, Motiven, Themes und Crosswalks; Prüfungen, Werkzeuge, Versionen |

## Als HTML

Dieselben Seiten als Website zum Durchblättern, mit Suche sowie Hell- und Dunkelmodus: auf Englisch unter
[urbansens.github.io/Urban-Landscape-Graphics/en/](https://urbansens.github.io/Urban-Landscape-Graphics/en/) und auf Deutsch (Standard) unter
**[urbansens.github.io/Urban-Landscape-Graphics](https://urbansens.github.io/Urban-Landscape-Graphics/)**. Jede Sprache gibt es außerdem als
eine einzige, in sich geschlossene Datei für den E-Mail-Versand und zum Offline-Lesen
([Englisch](https://urbansens.github.io/Urban-Landscape-Graphics/en/ulg-documentation.html),
[Deutsch](https://urbansens.github.io/Urban-Landscape-Graphics/ulg-dokumentation.html)). Alles wird mit
`python tools/build_html.py` erzeugt (in `docs/html/`); GitHub führt den Befehl bei jedem Push aus und veröffentlicht das Ergebnis mit GitHub Pages.

## Referenz

| Seite | Inhalt |
|---|---|
| [Elementliste](reference/element-list.md) | jede Element-ID mit Namen, Aliasen und Beschreibung (erzeugt) |
| [Attribute](reference/attributes.md) | Kennwerte je Element und ihre Quellen (erzeugt) |
| [Crosswalks](reference/crosswalks.md) | die 26 Schemata mit Abdeckung, Quellen und Anmerkungen (erzeugt) |
| [Themes](reference/themes.md) | die sieben Themes mit Quellen und Belegstufen (erzeugt) |
| [API](reference/api.md) | Funktionen, Klassen und die Kommandozeile (erzeugt) |
| [Crosswalk-Format](reference/crosswalk-format.md) | wie eine Crosswalk-Datei geschrieben wird |
| [Standards-Bericht](research/standards-report.md) | die Synthese der Standards-Recherche: Befunde, Konformitätsmatrix, offene Punkte |
| [Recherchestränge](research/streams/) | die sieben ausführlichen Recherchedateien hinter dem Bericht |

## Projekt

| Seite | Inhalt |
|---|---|
| [Lizenz und Nennung](licence-and-credit.md) | die MIT-Lizenz, wie UrbanSens zu nennen ist, das Zeichen auf den Blättern, die Logos, Material von Dritten |
| [Changelog](../CHANGELOG.md) | was sich in jeder Version geändert hat |
| [Mitarbeit an ulg](../AGENTS.md) | Regeln und Befehle für Mitwirkende und Coding-Agenten |

## Lesepfade

- **Ich möchte sofort eine Karte** → [4.1 Installation](04-python.md#41-installation), [4.4 Zeichnen](04-python.md#44-zeichnen),
  [`examples/quickstart.py`](../examples/quickstart.py)
- **Ich arbeite in QGIS** → [5.1 QGIS](05-gis-and-web.md#51-qgis), [`examples/qgis_project.py`](../examples/qgis_project.py)
- **Ich baue eine Web-App** → [5.3 MapLibre](05-gis-and-web.md#53-maplibre-gl), [5.5 Tokens](05-gis-and-web.md#55-design-tokens-und-apps),
  [`examples/web/`](../examples/web/)
- **Ich habe OSM-, ALKIS- oder CORINE-Daten** → [4.5 Klassifizieren](04-python.md#45-externe-daten-klassifizieren),
  [`examples/osm_workflow.py`](../examples/osm_workflow.py)
- **Ich brauche Kennzahlen (BFF, Versiegelung, Abfluss, urbanes Grün)** → [4.7 Standortkennzahlen](04-python.md#47-standortkennzahlen),
  [`examples/indicators.py`](../examples/indicators.py)
- **Ich gestalte den Stil** → [2 · Der Stilleitfaden](02-style.md), [8 · Erweitern des Stils](08-extending.md)
- **Ich bin ein KI-Agent** → [7 · Für KI-Agenten](07-agents.md), `ulg agent`

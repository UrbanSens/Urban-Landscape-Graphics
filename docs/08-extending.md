# 8 · Erweitern des Stils

*Wie der Stilleitfaden wächst: Elemente, Farben, Texturen, Themes und Zuordnungstabellen (Crosswalks) hinzufügen,
sie prüfen und eine neue Version veröffentlichen, die alle Karten, Apps und Agenten übernehmen.*

## 8.1 Wo was liegt

```text
src/ulg/
  data/
    palette.json            Farb-Tokens (family.step)
    settings.json           Strichstärken, LOD-Grenzen, Farbrampen, Klassenpaletten, Attributdokumentation, Mittellinienbreiten
    elements/*.json         der Katalog, eine Datei je Themengruppe, mit der Element-ID als Schlüssel
    themes/*.json           amtliche Konventionen (planzv, alkis, basemap, bfn, osm, mono)
    crosswalks/*.json       26 externe Klassifikationen -> Element-IDs
    agent/                  SKILL.md, AGENTS.md, AGENTS.snippet.md für Coding-Agenten
  catalog.py                Laden, Auflösen der Palette, Themes
  crosswalk.py              resolve / classify / explain
  render/                   Renderer: Geometrie, Texturmotive, Szene, SVG- und Matplotlib-Backends
  export/                   QGIS, SLD, Web (MapLibre), Design-Tokens
  analysis.py               indicators, flatten, Wurzelschutzbereiche
  check.py                  Lesbarkeitsbericht
  legend.py, sheet.py       Legenden und Stilblätter
  brand.py                  die UrbanSens-Namensnennung: Website, Logo, Nennungszeile, das kleine UrbanSens-Zeichen auf den Blättern
tools/                      build_docs.py, build_html.py, build_logo.py, build_reference.py, format_data.py, qgis_render.py
  html/                     Stylesheet, Skript und Schriftart der HTML-Dokumentation
tests/                      pytest-Testsuite
docs/                       die Dokumentation auf Deutsch (Standard); docs/en ist die englische Fassung;
                            docs/reference und docs/html sind erzeugt, docs/img enthält die Abbildungen
examples/                   lauffähige Beispiele und die MapLibre-Seite
LICENSE, CITATION.cff       MIT-Lizenz und die maschinenlesbare Zitierangabe
```

**Zuerst die Daten.** Fast jede Änderung ist eine Änderung an einer JSON-Datei. Python-Code ändert sich nur, wenn der
Stil eine neue Art von Zeichen (ein Motiv oder ein Piktogramm) oder eine neue Fähigkeit braucht.

## 8.2 Ein Element hinzufügen

1. **Prüfen Sie, ob es fehlt.** `ulg find "<deutsche und englische Namen>"`. Viele „neue“ Dinge sind Aliase eines
   vorhandenen Elements. Ergänzen Sie dann stattdessen den Alias.
2. **Wählen Sie Gruppe und Datei.** Vegetation in `10_…`/`20_…`, Bäume in `30_trees.json`, Wasser, Boden, Oberflächen,
   Flächennutzung, Bebauung, Punkte, Linien und Overlays in den jeweiligen Dateien.
3. **Schreiben Sie den Eintrag** nur mit Paletten-Tokens:

```json
"wood_pasture": {
  "group": "vegetation.woody",
  "geometry": ["polygon"],
  "z": 20,
  "label":       {"en": "Wood pasture", "de": "Hutewald / Weide mit Bäumen"},
  "description": {"en": "Grazed grassland with scattered old trees. Very high biodiversity.",
                  "de": "Beweidetes Grünland mit locker stehenden alten Bäumen. Sehr hohe Biodiversität."},
  "fill": "fallow.200",
  "textures": [
    {"motif": "grass_tufts", "ink": "fallow.700", "ink2": "grass.700", "keep": 0.45},
    {"motif": "canopy", "ink": "leaf.800", "tones": ["leaf.400", "leaf.500", "leaf.300"],
     "crown_m": 12.0, "pack": 3.4, "keep": 0.7}
  ],
  "attributes": {"sealing": "unsealed", "bff": 1.0, "runoff_cm": 0.1, "nrr_urban_green": true, "layer": "ground"},
  "aliases": ["Hutewald", "Hutung", "Waldweide", "wood pasture", "wooded pasture"]
}
```

4. **Wählen Sie `z` nach Band** ([Stilleitfaden 2.7](02-style.md#27-zeichenreihenfolge)): 20 für alles, was den Boden
   bedeckt (einschließlich der Komplexe), 30–33 für Wasser und was darauf liegt, 50–66 für Hecken und Bauwerke,
   66–76 für Bäume und Punkte, 84–98 für Overlays.
5. **Attribute nur mit Quelle.** Verwenden Sie die Schlüssel, die in `settings.json → attributes` dokumentiert sind;
   lassen Sie einen Kennwert lieber weg, als ihn zu schätzen. Ein neues Attribut braucht dort einen eigenen Eintrag
   (`meaning`, `source`, `evidence`).
6. **Aliase in beiden Sprachen**, einschließlich der Begriffe aus den Standards, die es benennen
   (ALKIS, BKompV, OSM): Suche und Agenten stützen sich darauf.
7. **Verknüpfen Sie es**: Lassen Sie die Crosswalk-Einträge, die es beschreiben, auf die neue ID zeigen (8.6).
8. **Prüfen und neu erzeugen** (8.8).

## 8.3 Eine Farbe hinzufügen oder ändern

Farben werden nur in `palette.json` festgelegt. Bleiben Sie im Tonwertbereich der Farbfamilie: helle Stufen (100–400)
für Füllungen, dunklere Stufen (500–900) für Zeichen. `ulg check` zeigt, ob eine Änderung zwei Landbedeckungen auf
weniger als ΔE₀₀ 10 Abstand bringt, ohne dass sich ihre Textur unterscheidet. Das gilt auch für simulierte
Farbsehschwächen. Ändert sich ein Token, ändern sich alle Elemente, Theme-Exporte und Blätter, die es verwenden. Das
ist gewollt, vermerken Sie es aber im Changelog.

## 8.4 Ein Texturmotiv hinzufügen

Ein Motiv ist eine Funktion in `src/ulg/render/motifs.py`:

```python
def my_motif(region, p, ctx: Ctx) -> list:
    """What it draws, in one line."""
    x, y, s = G.scatter(region, ctx, p["spacing"], salt=p.get("salt", 31), keep=p["keep"])
    ...
    return [Paths(...), Dots(...)]
```

- `region` ist das Polygon, `p` die Parameter, zusammengeführt aus `DEFAULTS[motif]` (je LOD) und dem Textureintrag
  des Elements; `ctx` enthält den Maßstab (`ctx.u` Meter je Millimeter auf dem Papier), die Detailstufe und den
  Faktor für die handgezeichnete Anmutung.
- Platzieren Sie Zeichen mit den an Bodenkoordinaten verankerten Hilfsfunktionen (`G.scatter`, `_span_lines`, die
  `R`-Streams), nie mit einem Zufallsgenerator ohne festen Seed: So bleiben Muster über benachbarte Polygone hinweg
  fortlaufend, reproduzierbar und beim Zeichnen in Kacheln nahtlos (`ctx.period`).
- Größen werden in Millimetern auf dem Papier angegeben; rechnen Sie mit `ctx.u` um.
- Tragen Sie es in `MOTIFS` ein und legen Sie `DEFAULTS` für LOD 1–3 an. `tests/test_render_engine.py` prüft,
  dass sich Kacheln nahtlos wiederholen.

## 8.5 Ein Piktogramm oder ein Theme hinzufügen

**Piktogramme** sind kleine Vektorgrafiken in `PICTOGRAMS` (`src/ulg/render/scene.py`): eine Liste von Teilen
`(Art, Koordinaten, Füllrolle, Konturrolle, Strichstärke)`, Koordinaten in Einheiten des Symbolradius, Rollen `fill`,
`ink`, `paper`, `accent`, die dem `symbol` des Elements entnommen werden.

**Themes** sind JSON-Dateien in `src/ulg/data/themes/`:

| Schlüssel | Bedeutung |
|---|---|
| `title`, `description`, `source`, `evidence` | was die Konvention ist und woher die Werte stammen |
| `handdrawn` | Konturwackeln für dieses Theme (0 = exakte Linien) |
| `textures` | `"none"` (einfarbige Füllungen; Overlays behalten ihre Schraffuren) oder `"mono"` (jedes Zeichen in der Zeichenfarbe) |
| `background`, `ink`, `paper` | Seitenfarben |
| `default`, `groups`, `elements` | Überschreibungen von Füllung und Kontur, vom Allgemeinen zum Besonderen; jeweils mit einem `evidence`-Vermerk |

Ein neues Theme erscheint automatisch in `ulg.themes()`, in den `--theme`-Optionen der Kommandozeile und in allen
Exportern.

## 8.6 Einen Crosswalk hinzufügen oder erweitern

Eine Datei je Schema in `src/ulg/data/crosswalks/`; das Format steht in
[reference/crosswalk-format.md](reference/crosswalk-format.md). Das Wesentliche:

- Metadaten: `title`, `publisher`, `version`, `source`, `license_note`, `key`, `fields` (Aliase für Spaltennamen),
  optional `hierarchy`, `suffixes`, `fallback_pattern`;
- ein Eintrag je Klasse mit `code` oder `match`, `name`, `element` (oder `null`), `fit` und, nur wenn die eigene
  Legendenfarbe des Schemas verifiziert wurde, `color`;
- der spezifischste Treffer gewinnt, danach die Reihenfolge in der Datei.

`python -m pytest tests/test_crosswalks.py` validiert jede Datei. Ergänzen Sie Stichproben für die Abfragen, auf die
Ihr Projekt angewiesen ist.

## 8.7 Werkzeuge

| Befehl | Aufgabe |
|---|---|
| `python tools/format_data.py` | vereinheitlicht das Layout aller JSON-Datendateien (`--check` meldet nur) |
| `python tools/build_reference.py` | erzeugt `docs/reference/*.md` aus den Daten und Docstrings neu |
| `python tools/build_docs.py [names]` | erzeugt die Bilder in `docs/img/` neu, in beiden Sprachen (Blätter, Texturen, Karten, QGIS-Renderings, die Banner der HTML-Seiten) |
| `python tools/build_logo.py` | zeichnet das Logo, seine Varianten und die Favicons in `docs/img/logo/` aus dem Katalog neu |
| `python tools/build_html.py` | baut `docs/html/`: die deutsche Website (Stammverzeichnis) und die englische Website (`en/`), jeweils mit einer Einzeldatei (Banner, Serifenschrift, nummerierte Abbildungen, Zitate mit Quellenangabe); prüft jeden Link |
| `python -m pytest` | die Testsuite (`-m "not slow"` überspringt die Rasterisierung der Sprites) |
| `ulg check` | der Lesbarkeitsbericht |

## 8.8 Checkliste für jede Änderung

```bash
python tools/format_data.py
```

```bash
ulg check
```

```bash
python -m pytest
```

```bash
python tools/build_reference.py
```

```bash
python tools/build_docs.py sheets
```

```bash
python tools/build_html.py
```

Sehen Sie sich danach die neu erzeugten Blätter an: Der Stil ist visuell, und die Blätter sind sein Prüfexemplar.
Eine Änderung am Text der Dokumentation wird in beiden Sprachen vorgenommen (8.11).

## 8.9 Versionen und der lebende Stilleitfaden

Der Stil wird zusammen mit dem Paket versioniert (`pyproject.toml`, `ulg.__version__` und `palette.json → version`
ändern sich gemeinsam), und jedes Release ist in [`CHANGELOG.md`](../CHANGELOG.md) beschrieben:

| Änderung | Versionsschritt |
|---|---|
| Element-ID entfernt oder umbenannt, oder ihre Bedeutung geändert | Major |
| neue Elemente, Themes, Crosswalks, Motive; sichtbare Farb- oder Texturänderungen | Minor |
| Korrekturen, die das Aussehen bestehender Karten nicht verändern | Patch |

Vorschläge für den Stil funktionieren am besten als Bild: ein Ausschnitt des Blatts oder eine Karte mit dem Problem,
die beteiligten Element-IDs und, bei allem Amtlichen, die Quelle. Apps übernehmen ein Release über
`ulg export tokens` / `ulg export web`, QGIS-Projekte durch erneutes Laden der exportierten QML-Dateien, Agenten über
den installierten Skill, der das installierte Paket liest.

## 8.10 Veröffentlichen

Zwei GitHub-Workflows in `.github/workflows/` laufen bei jedem Push auf `main`:

| Workflow | Aufgabe |
|---|---|
| `ci.yml` (Tests) | installiert das Paket unter Python 3.10, 3.12 und 3.13, prüft das Datenlayout, führt `ulg check` und die Testsuite aus |
| `pages.yml` (Documentation) | baut beide Websites und ihre Einzeldateien mit `python tools/build_html.py --out _site` (der Aufruf schlägt bei einem defekten Link fehl), exportiert und kopiert die MapLibre-Demo und veröffentlicht alles mit GitHub Pages unter <https://urbansens.github.io/Urban-Landscape-Graphics/> (Deutsch) und <https://urbansens.github.io/Urban-Landscape-Graphics/en/> (Englisch) |

Erzeugte Dateien werden nicht committet: `docs/html/`, `examples/output/` und der exportierte Web-Stil in
`examples/web/ulg/` werden von den Workflows oder mit den Befehlen aus 8.7 neu erzeugt. Committet *werden* dagegen die
Bilder in `docs/img/` (Blätter, Karten, Banner, Logos), weil sie das Prüfexemplar des Stils sind.
Erzeugen Sie sie mit `python tools/build_docs.py` und `python tools/build_logo.py` neu, bevor Sie eine Änderung
committen, die das Aussehen des Stils verändert. Das Social-Preview-Bild von GitHub (1280 × 640 px, von Hand unter
Settings > General gesetzt) ist `docs/img/social-preview.png` (Deutsch) oder `social-preview-en.png`, erzeugt mit
`python tools/build_docs.py social`.

## 8.11 Zwei Sprachen

Die Dokumentation liegt auf Deutsch und auf Englisch vor, wobei Deutsch die Standardsprache ist:

| | Deutsch (Standard) | Englisch |
|---|---|---|
| Startseite | `README.md` | `README.en.md` |
| Kapitel | `docs/index.md`, `docs/01-origins.md` ... `docs/08-extending.md`, `docs/licence-and-credit.md` | dieselben Dateinamen in `docs/en/` |
| Abbildungen mit Text | `docs/img/name-de.png` | `docs/img/name.png` |
| Veröffentlicht | Stammverzeichnis der Website | `/en/` |

Die Referenzseiten, die Recherchedateien, die Beispiele, das Changelog und `AGENTS.md` gibt es nur auf Englisch; beide
Websites enthalten sie, und das deutsche Menü kennzeichnet sie mit *EN*. Der deutsche Text verwendet die förmliche
Anrede *Sie* und ist sinngemäß und idiomatisch übersetzt, nicht Wort für Wort. Halten Sie Dateinamen,
Überschriftennummern, Abbildungen und die Anzahl der Codeblöcke in beiden Sprachen identisch; `tests/test_docs_i18n.py`
vergleicht die beiden Verzeichnisbäume. Der Text in den Abbildungen stammt aus `tools/build_docs.py`, das jedes
sprachabhängige Bild zweimal zeichnet. Der Sprachumschalter der Website braucht nichts Zusätzliches: Das Build-Skript
ordnet die Seiten über den Dateinamen einander zu.

Für jeden Text gelten in beiden Sprachen zwei Hausregeln: keine Geviertstriche (stattdessen Komma, Doppelpunkt,
Klammern oder Punkt) und keine Halbgeviertstriche mit Leerzeichen als Ersatz. `tests/test_style_rules.py` prüft das.

---

Zurück zur [Übersicht](index.md)

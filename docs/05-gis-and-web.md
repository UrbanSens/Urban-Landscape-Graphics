# 5 · GIS und Web

*Derselbe Stil in QGIS, GeoServer, MapLibre, Leaflet und Design-Tools, exportiert aus einem einzigen Katalog.*

```bash
ulg export all out/            # alles Folgende; oder: qgis | sld | web | tokens
```

| Ziel | Befehl | Ergebnis |
|---|---|---|
| QGIS | `ulg export qgis out/ --lod auto` | Layerstile für Polygone, Linien und Punkte, eine Stilbibliothek, eine Palette |
| GeoServer, MapServer, QGIS Server, INSPIRE-Darstellungsdienste | `ulg export sld out/` | Dateien im Format OGC SLD 1.0 mit Musterkacheln und Symbolen |
| MapLibre GL, Mapbox GL | `ulg export web out/` | Sprite, Stil-Layer, Musterkacheln, Tokens, Katalog |
| Figma, CSS, Apps | `ulg export tokens out/` | CSS-Variablen, DTCG-Design-Tokens, flaches JSON, Katalog-JSON |

Jeder Export akzeptiert `--theme` (`mellow`, `planzv`, `alkis`, `basemap`, `bfn`, `osm`, `mono`) und
`--lang de` für deutsche Bezeichnungen. Ihre Daten brauchen ein Attribut mit Element-IDs (Standard: `element`);
liegen sie in einem anderen Schema vor, klassifizieren Sie sie zuerst ([4.5](04-python.md#45-externe-daten-klassifizieren)).

## 5.1 QGIS

![Das Demoquartier in QGIS, gestaltet durch das exportierte QML](img/qgis.png)

*Ohne Oberfläche (headless) erzeugtes QGIS-Rendering des Demoquartiers im Maßstab 1:2000 mit den exportierten
Stilen: handgezeichnete Konturen, ein Detailgrad, der dem Kartenmaßstab folgt, Straßen und Gebäude als schlichte
Füllungen.*

![Ein Block im OpenStreetMap-Stil in QGIS](img/qgis-osm.png)

*Das Beispiel im OSM-Stil in QGIS: Teich, Spielplatz und Wiese liegen auf dem Parkrasen, und die Fußwege
(als Linien kartiert) werden als Streifen der Breite `width` gezeichnet.*

**Dateien**

| Datei | Verwendung |
|---|---|
| `ulg_polygons.qml`, `ulg_lines.qml`, `ulg_points.qml` | *Layereigenschaften → Symbolisierung → Stil → Lade Stil…* |
| `ulg_style_library.xml` | *Einstellungen → Stilverwaltung → Element(e) importieren…*: jedes Element als benanntes Symbol, zum manuellen Gestalten |
| `ulg_palette.gpl` | Farbpalette für die Farbwahl |

**Was die Stile leisten**

- **Texturen** sind nahtlose SVG-Musterkacheln, die in die Datei eingebettet sind (`base64:`); das QML braucht
  deshalb weder einen SVG-Suchpfad noch ein Plugin.
- **Handgezeichnete Kontur**: Ein Geometriegenerator wendet `wave_randomized()` in Millimetern auf dem Papier an,
  mit der Objekt-ID als Seed; die Amplitude bleibt unter der halben Strichstärke, sodass der Strich die wahre
  Kante überdeckt. Setzt QGIS 3.24 oder neuer voraus; amtliche Themes verwenden exakte Linien.
- **Detailstufe** (`--lod auto`): Ein regelbasierter Renderer wechselt die Texturen bei 1:750, 1:2500 und
  1:10 000, genau wie der Python-Renderer. Mit einem festen `--lod 2` erhalten Sie einen einfacheren
  kategorisierten Renderer.
- **Bäume** sind SVG-Marker, deren Größe in Karteneinheiten aus `crown_diameter` (oder dem Standardwert des
  Elements) bestimmt wird, sodass die Kronen auf jeder Zoomstufe maßstabsgetreu sind.
- **Straßen und Wege als Mittellinien** (OSM-Highways) werden im Linienstil als Streifen ihrer tatsächlichen
  Breite gezeichnet: Ein Geometriegenerator puffert die Linie entsprechend `width`, `lanes` oder der Klasse
  `highway`.
- **Die Zeichenreihenfolge** folgt den Bändern des Katalogs, danach kommen größere Flächen zuerst
  (`$area DESC`); übereinanderliegende Daten sehen daher so aus wie in Python.

Getestet durch Headless-Rendering mit PyQGIS 3.36 (`tools/qgis_render.py`); das XML entspricht dem, was QGIS
selbst schreibt, und lässt sich ab QGIS 3.28 laden. Ein fertiges Projekt: `python examples/qgis_project.py`.

## 5.2 OGC SLD für GeoServer und INSPIRE

`ulg export sld out/` schreibt `ulg_polygons.sld`, `ulg_lines.sld` und `ulg_points.sld`, eine `Rule` pro
Element, gefiltert nach dem Element-Attribut, mit

- einer einfarbigen Füllung im `PolygonSymbolizer` plus einem `GraphicFill` mit der Musterkachel des Elements
  (`patterns/<id>.svg`),
- von Millimetern in Pixel bei 96 dpi umgerechneten Strichstärken sowie Strichelungen und
  Linieneinfassungen (Casings) für Linien,
- `ExternalGraphic`-Punktsymbolen (`symbols/<id>.svg`) für Piktogramme und Kronen sowie Well-known Marks
  für Punkte.

SLD kann weder die prozedural erzeugte Kontur noch den maßstabsabhängigen Detailgrad ausdrücken; der Stil fällt
deshalb kontrolliert auf eine einfachere Form zurück: einfarbige Füllung, Musterkachel, schlichte Kontur. Diese Form
erwarten auch INSPIRE-Darstellungsdienste. Laden Sie den Ordner mit seinen Unterordnern `patterns/` und `symbols/`
in das Stilverzeichnis von GeoServer hoch.

## 5.3 MapLibre GL

<table>
<tr>
<td width="50%"><img src="img/web-maplibre.jpg" alt="MapLibre, das Demoquartier bei Zoomstufe 17"></td>
<td width="50%"><img src="img/web-maplibre-detail.jpg" alt="MapLibre, Detail bei Zoomstufe 19"></td>
</tr>
<tr>
<td><em>Das Demoquartier in MapLibre GL, Zoomstufe 17.</em></td>
<td><em>Detail bei Zoomstufe 19: Musterkacheln, Teich, Röhrichtgürtel und Bohlenweg.</em></td>
</tr>
</table>

![Der Block im OSM-Stil in MapLibre](img/web-maplibre-osm.jpg)

*Der Block im OpenStreetMap-Stil in MapLibre: gestapelte Flächen in der richtigen Reihenfolge, nach
`diameter_crown` bemessene Bäume, Straßen und Gehwege in Metern aus ihren Mittellinien gezeichnet.*

`ulg export web out/` schreibt unter anderem:

| Datei | Inhalt |
|---|---|
| `ulg-sprite.png/.json`, `ulg-sprite@2x.png/.json` | Musterkacheln `ulg-<id>`, Piktogramme `ulg-icon-<id>`, Kronen `ulg-crown-<id>` |
| `maplibre-layers.json` | Stil-Layer zum Anhängen an die `layers` Ihres Stils |
| `patterns/*.svg`, `patterns.svg` | die Kacheln als SVG-Dateien und als ein `<defs>`-Blatt |
| `ulg.css`, `ulg.tokens.json`, `ulg-colors.json`, `catalog.json` | Tokens und Katalog (5.5) |

**Daten vorbereiten** mit `to_geojson()`: Die Funktion schreibt GeoJSON nach RFC 7946 in WGS 84 und ergänzt
`area_m2`, womit die Layer kleinere Flächen über größeren zeichnen.

```python
from ulg.export.web import to_geojson
to_geojson(gdf, "site.geojson", columns=["element", "crown_diameter"])
```

**Layer einbinden**

```js
const layers = await (await fetch("ulg/maplibre-layers.json")).json();
new maplibregl.Map({
  container: "map",
  style: {
    version: 8,
    sprite: new URL("ulg/ulg-sprite", location.href).href,
    sources: { ulg: { type: "geojson", data: "site.geojson" } },
    layers: [{ id: "paper", type: "background", paint: { "background-color": "#F5F5F1" } }, ...layers]
  }
});
```

| Layer | Zeichnet |
|---|---|
| `ulg-fill`, `ulg-pattern`, `ulg-outline` | einfarbige Füllungen unterhalb von Zoomstufe 15,5, darüber Kacheln mit eigener Füllfarbe, sodass sich Texturen je Objekt stapeln, sowie Konturen. Sortiert nach z, dann nach Fläche |
| `ulg-strips-casing`, `ulg-strips` | Straßen und Wege als Mittellinien, auf jeder Zoomstufe **in Metern** |
| `ulg-lines` | Linienelemente: Hecken, Mauern, Zäune, Grenzen, Gräben |
| `ulg-trees`, `ulg-crowns` | Bäume als Kreise in Metern unterhalb von Zoomstufe 15, darüber als gezeichnete Kronensymbole, skaliert auf ihren tatsächlichen Durchmesser |
| `ulg-points`, `ulg-icons` | Punkte (Sensoren, Poller) und Piktogramme (ab Zoomstufe 17) |

Für Vektorkacheln übergeben Sie `source_layer=` an `maplibre_layers()`. Größen in Metern verwenden den Breitengrad
Ihrer Daten (`latitude=` in `export_web`). Kronengrößen werden aus `crown_diameter`, `diameter_crown`,
`kronendurchmesser` und den übrigen Größenattributen gelesen, die der Python-Renderer kennt. MapLibre überblendet
Füllmuster zwischen den Zoomstufen, daher sind Texturen bei ganzzahligen Zoomstufen am schärfsten.

**Das Beispiel.** `examples/web/` ist eine vollständige Seite. Erzeugen Sie sie und liefern Sie sie aus:

```bash
python examples/web/build.py
```

```bash
python -m http.server 8765 --directory examples/web
```

Öffnen Sie <http://localhost:8765> für das Demoquartier oder <http://localhost:8765/?data=osm> für den Block im
OpenStreetMap-Stil mit gestapelten Flächen und Straßen als Mittellinien. Dieselbe Seite ist live unter
[urbansens.github.io/Urban-Landscape-Graphics/demo/](https://urbansens.github.io/Urban-Landscape-Graphics/demo/)
erreichbar (der Dokumentations-Workflow baut sie bei jedem Push neu).
Die Seite erscheint standardmäßig auf Deutsch; mit `?lang=en` erscheint sie auf Englisch (`/?lang=en&data=osm`).

## 5.4 Leaflet, folium, OpenLayers

APIs im Leaflet-Stil erwarten eine Stilfunktion (Callback) mit einfachen Farben:

```python
folium.GeoJson(gdf.to_crs(4326), style_function=ulg.style_function()).add_to(m)
```

Für Texturen in SVG-basierten Renderern binden Sie `patterns.svg` ein (ein `<pattern id="ulg-<id>">` je
Element) und füllen die Pfade mit `url(#ulg-lawn)`. OpenLayers und deck.gl können die Sprite-PNG-Datei und ihren
JSON-Index als Atlas verwenden.

## 5.5 Design-Tokens und Apps

```bash
ulg export tokens out/
```

| Datei | Format | Für |
|---|---|---|
| `ulg.css` | CSS-Variablen (`--ulg-grass-300`, `--ulg-lawn-fill`, `--ulg-lawn-ink` …) | Web-Apps, die Beispielseite |
| `ulg.tokens.json` | Format der W3C Design Tokens Community Group | Figma (Tokens Studio), Style Dictionary |
| `ulg-colors.json` | flaches `{token: hex}` | jedes Werkzeug |
| `catalog.json` | der vollständige Katalog: Elemente, Namen, Farben, Attribute | Apps, Dashboards, Agenten |

## 5.6 Druck und Illustration

Die SVG-Ausgabe ist in Millimetern im Kartenmaßstab angelegt: Öffnen Sie sie in Inkscape, Illustrator oder Affinity,
und sie ist maßstabsgetreu. Jede Objektgruppe trägt `data-element="<id>"`, sodass sich Layer nach Element
auswählen und neu gestalten lassen. Für PDF:

```bash
inkscape plan.svg --export-type=pdf
```

---

Weiter: [6 · Standards](06-standards.md)

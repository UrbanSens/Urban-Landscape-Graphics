# Lizenz und Nennung

*`ulg` ist freie Software unter der MIT-Lizenz. Im Gegenzug bittet UrbanSens um eines: Sagen Sie, woher der Stil stammt.*

## Lizenz

Die Bibliothek, die Katalogdaten (Elemente, Palette, Themes, Crosswalks), die Werkzeuge und diese Dokumentation sind
unter der **MIT-Lizenz** veröffentlicht. Sie dürfen sie nutzen, verändern und in kommerziellen Produkten ausliefern.
Der Copyright- und Lizenzhinweis muss bei dem Code bleiben, den Sie übernehmen. Die Lizenz gilt für die Software und
ihre Datendateien; auf den Karten und Blättern, die Sie damit zeichnen, verlangt sie keinen Zusatz. Rechtlich
verbindlich ist allein der englische Wortlaut der Lizenz unten; die deutschen Erläuterungen dienen nur dem besseren
Verständnis.

```text
MIT License

Copyright (c) 2026 UrbanSens

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Derselbe Text steht in der Datei `LICENSE` im Repository.

## Bitte nennen Sie UrbanSens

Die Namensnennung ist eine Bitte und keine Bedingung der Lizenz, aber so wird ein kleines Projekt gefunden. Wenn `ulg`
oder der UrbanSens Ecological Vector Style bei einer Karte, einem Plan, einem Bericht, einer Ausschreibung oder einem
Fachartikel geholfen hat, sagen Sie das bitte.
Die Website von UrbanSens: [urbansens.de](https://urbansens.de/).

**In der Bildunterschrift einer Karte, in einer Legende oder im Quellenverzeichnis**

> Map style: UrbanSens Ecological Vector Style (ulg), urbansens.de

**Auf Deutsch**

> Kartenstil: UrbanSens Ecological Vector Style (ulg), urbansens.de

**In einem Literaturverzeichnis** (APA-Stil)

> UrbanSens. (2026). *Urban Landscape Graphics (ulg): the UrbanSens Ecological Vector Style as a library* (Version 0.1.0)
> [Computer software]. https://github.com/UrbanSens/Urban-Landscape-Graphics

**In BibTeX**

```bibtex
@misc{urbansens_ulg_2026,
  author       = {{UrbanSens}},
  title        = {Urban Landscape Graphics ({ulg}): the {UrbanSens} Ecological Vector Style as a library},
  year         = {2026},
  note         = {Version 0.1.0, software},
  howpublished = {\url{https://github.com/UrbanSens/Urban-Landscape-Graphics}}
}
```

<!-- site-only
Die Datei `CITATION.cff` im Repository enthält dieselbe Literaturangabe in maschinenlesbarer Form.
-->
<!-- github-only:start -->
Die Datei [`CITATION.cff`](../CITATION.cff) enthält dieselbe Literaturangabe in maschinenlesbarer Form; GitHub macht
daraus die Schaltfläche **Cite this repository** oben auf der Seite des Repositorys.
<!-- github-only:end -->

In Python liefert `ulg.credit_line()` die Nennungszeile (`ulg.credit_line("de")` die deutsche), damit Skripte oder
Agenten, die eine Karte zeichnen, sie dort einsetzen können, wo die Quellen genannt werden:

```python
import ulg

ulg.credit_line()       # 'Style: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'
ulg.credit_line("de")   # 'Kartenstil: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'
```

## Das Zeichen auf den Blättern

Die Blätter, die die Bibliothek selbst zeichnet, tragen in der unteren rechten Ecke ein kleines UrbanSens-Zeichen (das
Logo mit dem Namen des Stils, der Version und der Website): `ulg.style_sheet()`, `ulg.catalog_sheet()` (das Verzeichnis
aller Elemente) und die Abbildungen dieser Dokumentation. Belassen Sie das Zeichen, wenn Sie die Blätter weitergeben.
`credit=False` (oder `ulg sheet --no-credit`) zeichnet das Blatt ohne das Zeichen. Legenden übernehmen Sie in Ihre
Layouts; deshalb fügt `ulg.legend_svg()` das Zeichen nur mit `credit=True` hinzu.

Ihre Karten erhalten nie einen Stempel: `ulg.render_svg()`, `ulg.plot()` und die exportierten Stile für QGIS, GeoServer,
MapLibre und Design-Tools fügen nichts hinzu.

## Die Logos

Das UrbanSens-Logo (`src/ulg/data/brand/urbansens-logo.png`) und das ulg-Logo (`docs/img/logo/`) sind Grafiken von
UrbanSens. Verwenden Sie sie, um das Projekt zu nennen oder zu zeigen, dass Sie mit dem Stil arbeiten; verwenden Sie sie
nicht so, dass der Eindruck entsteht, UrbanSens stehe hinter Ihrer Arbeit. Die MIT-Lizenz räumt Rechte an der Software
ein, keine Markenrechte.

## Material von Dritten

- **Schriften.** Die Überschriften der HTML-Dokumentation und die Wortmarke des ulg-Logos sind in Rethink Sans gesetzt
  (SIL Open Font License 1.1, `tools/html/fonts/OFL.txt`).
- **Historische Abbildungen** im Kapitel [Herkunft](01-origins.md) sind von Wikimedia Commons verlinkt, nicht kopiert;
  jede hat ihre eigene Lizenz, aufgeführt unter *Bildnachweise* in diesem Kapitel.
- **Standards, amtliche Farben und Schlüssel.** Klassenschlüssel, Farbwerte und Kennwerte externer Schemata (ALKIS,
  basemap.de, BfN, OpenStreetMap Carto, CORINE, PlanZV und andere) werden mit ihrer Quelle in den
  [Referenzseiten](reference/themes.md) und im [Standards-Bericht](research/standards-report.md) zitiert. Die Schemata und
  ihre Namen gehören ihren Herausgebern.
- **OpenStreetMap.** `ulg` enthält keine OpenStreetMap-Daten; die Beispiele verwenden einen erfundenen Beispielblock.
  Karten, die Sie aus OpenStreetMap-Daten zeichnen, brauchen die eigene Namensnennung von OpenStreetMap:
  © OpenStreetMap contributors.

---

Zurück zur [Übersicht](index.md)

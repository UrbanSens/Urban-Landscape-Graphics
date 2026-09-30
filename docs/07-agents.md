# 7 · Für KI-Agenten

*Wie Coding-Agenten (Claude Code und andere) die Bibliothek nutzen, damit jede Karte, die sie für
UrbanSens erstellen, richtig aussieht, ohne dass jemand Farben von Hand prüfen muss.*

Ein Agent, der den Auftrag „Erstellen Sie eine Karte des Standorts mit den Wiesen und den neuen Bäumen“
erhält, erfindet sonst ein Grün und ein Baumsymbol. Mit installiertem `ulg` kann er stattdessen alles
nachschlagen. Die Bibliothek bringt eigene Anweisungen für Agenten mit, dazu einen Befehl, der sie in
jedes Projekt installiert.

## 7.1 Die Anleitung in ein Projekt installieren

```bash
ulg agent install --dir path/to/project
```

Dabei entstehen

- `.claude/skills/urban-landscape-graphics/SKILL.md`: ein [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview),
  den Claude Code lädt, wenn eine Aufgabe Karten, Pläne, Biotope, Landbedeckung, Legenden oder
  Kennzahlen betrifft (nutzen Sie `--agents` für den agentenübergreifenden Ort `.agents/skills/`
  oder beide Optionen);
- ein kurzer Abschnitt zwischen `<!-- ulg:start -->` und `<!-- ulg:end -->` in der `AGENTS.md` des Projekts
  (angelegt, falls sie fehlt, nie doppelt eingetragen), die zu Beginn jeder Sitzung von Agenten gelesen wird.

```bash
ulg agent
```

gibt die vollständige Anleitung aus (derselbe Text wie `src/ulg/data/agent/AGENTS.md`).

## 7.2 Die Regeln, denen Agenten folgen

1. **Nachschlagen, nie erfinden.** Farben, Texturen und Symbole stammen aus dem Katalog:
   `ulg find "Blumenwiese" --json`, `ulg show wildflower_meadow --json`, `ulg.element(id)`.
2. **Mit Zuordnungstabellen (Crosswalks) klassifizieren.** `ulg.classify(gdf, "osm")`, `ulg.resolve("alkis", objart=..., funktion=...)`.
   `ulg schemes` listet die 26 Schemata auf. Nicht zugeordnete Objekte werden zu `unknown`; sie werden
   gemeldet, nicht verborgen.
3. **Metrische Daten.** In Metern rendern und messen (in Bayern EPSG:25832).
4. **Maßstab, nicht Detailstufe.** `scale=` übergeben; die Detailstufe ergibt sich daraus.
5. **Themes für amtliche Darstellungen.** `theme="planzv"`, `"alkis"`, `"basemap"`, `"bfn"`, `"osm"`, `"mono"`;
   den Hausstil nie von Hand umfärben.
6. **Kennwerte haben Quellen.** Fehlende Werte bleiben fehlend; `coverage` gibt an, wie viel bekannt war.
7. **Überlagerte Daten.** OSM- und Skizzendaten überlappen sich; das Zeichnen kommt damit zurecht, das Messen
   braucht `ulg.flatten()`.
8. **UrbanSens nennen.** `ulg` steht unter der MIT-Lizenz und bittet um Namensnennung. Wenn ein Agent eine Karte
   liefert oder beschreibt, schlägt er `ulg.credit_line()` für die Bildunterschrift oder den Quellennachweis vor.
   Die Blätter, die die Bibliothek zeichnet, behalten ihr kleines UrbanSens-Zeichen (`credit=False` nur auf
   Wunsch); Agenten setzen nie Logos auf die eigenen Karten der Nutzenden.

## 7.3 Maschinenlesbare Antworten

Jeder Befehl antwortet mit `--json` in JSON und nennt mit `--lang de` die Namen auf Deutsch:

```bash
ulg find Schotterrasen --json -n 1
```

```json
[{"id": "gravel_turf", "label": {"en": "Gravel turf", "de": "Schotterrasen"}, "group": "surface.permeable",
  "geometry": ["polygon"], "fill": "#CDD4C8", "outline": "#AAB6A2", "ink": "#9A9A98",
  "motifs": ["pebbles", "grass_ticks"]}]
```

```bash
ulg resolve osm leisure=pitch surface=artificial_turf --json
```

```json
{"scheme": "osm", "query": {"leisure": "pitch", "surface": "artificial_turf"}, "element": "artificial_turf",
 "fill": "#BFCBB8", "outline": "#9DAD93", "ink": "#7C907F", "official_color": "#88E0BE",
 "name": "leisure=pitch + surface=artificial_turf", "note": null}
```

`ulg show <id> --json` ergänzt Beschreibung, Texturen, Symbol, Attribute und Aliase.

Der gesamte Katalog als eine Datei für Werkzeuge in anderen Programmiersprachen: `ulg export tokens out/` → `catalog.json`.

## 7.4 Beispielanfragen und was der Agent tut

| Anfrage | Vorgehen des Agenten |
|---|---|
| „Zeichnen Sie den Lageplan aus `bestand.gpkg` im Maßstab 1:500“ | liest die Datei, prüft die Elementspalte (oder klassifiziert mit dem passenden Schema), `ulg render bestand.gpkg --scale 500 --png` |
| „Erstellen Sie eine OSM-Basiskarte von Schwabing in unserem Stil“ | holt OSM-Objekte mit osmnx, `ulg.classify(osm, "osm")`, `ulg.render_svg(osm, scale=5000)`; meldet die Tags, die zu `unknown` werden |
| „Wie grün ist der Innenhof? Wir brauchen den BFF“ | `ulg.indicators(gdf)` → `bff`, `bff_coverage`, der unversiegelte Anteil; nennt die Berliner Liste von 2021 als Quelle |
| „Zeigen Sie die zu fällenden Bäume und die Wurzelschutzbereiche“ | `tree_remove` für die Bäume, `ulg.root_protection_zone(trees)` für die Bereiche, Legende auf Deutsch |
| „Geben Sie mir die QGIS-Stile“ | `ulg export qgis styles/ --lod auto` und erklärt, wie die QML-Dateien geladen werden |
| „Welche Farbe verwendet CORINE für Parks?“ | `ulg resolve clc 141` → Element `green_space`, amtliche Legendenfarbe `#FFA6FF` |

## 7.5 Mitarbeit an der Bibliothek selbst

Agenten, die die Bibliothek ändern, folgen der eigenen [`AGENTS.md`](../AGENTS.md) des Repositorys:
zuerst die Daten, nur Palette-Token, eine Quelle für jeden Wert, `ulg check` und die Tests müssen
bestehen, und die Referenzseiten und Bilder werden nach Datenänderungen neu erzeugt
([Erweitern des Stils](08-extending.md)).

---

Weiter: [8 · Erweitern des Stils](08-extending.md)

# 7 · For AI agents

*How coding agents – Claude Code and others – use the library, so that every map they make for
UrbanSens looks right without anyone checking colours by hand.*

An agent asked to "make a map of the site with the meadows and the new trees" will otherwise invent a
green and a tree symbol. With `ulg` installed it can look everything up instead. The library ships
its own instructions for agents and a command to install them into any project.

## 7.1 Install the guide into a project

```bash
ulg agent install --dir path/to/project
```

This writes

- `.claude/skills/urban-landscape-graphics/SKILL.md` – an [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
  that Claude Code loads when a task involves maps, plans, habitats, land cover, legends or
  indicators (use `--agents` for the cross-agent `.agents/skills/` location, or both flags);
- a short section between `<!-- ulg:start -->` and `<!-- ulg:end -->` in the project's `AGENTS.md`
  (created if missing, never duplicated), which agents read at the start of every session.

```bash
ulg agent
```

prints the full guide (the same text as `src/ulg/data/agent/AGENTS.md`).

## 7.2 The rules agents follow

1. **Look up, never invent.** Colours, textures and symbols come from the catalog:
   `ulg find "Blumenwiese" --json`, `ulg show wildflower_meadow --json`, `ulg.element(id)`.
2. **Classify with crosswalks.** `ulg.classify(gdf, "osm")`, `ulg.resolve("alkis", objart=..., funktion=...)`.
   `ulg schemes` lists the 26 schemes. Unmatched features become `unknown` – report them, do not hide
   them.
3. **Metric data.** Render and measure in metres (EPSG:25832 in Bavaria).
4. **Scale, not detail.** Pass `scale=`; the level of detail follows.
5. **Themes for official looks.** `theme="planzv"`, `"alkis"`, `"basemap"`, `"bfn"`, `"osm"`, `"mono"`;
   never recolour the house style by hand.
6. **Coefficients have sources.** Missing values stay missing; `coverage` says how much was known.
7. **Stacked data.** OSM and sketch data overlap; drawing handles it, measuring needs `ulg.flatten()`.

## 7.3 Machine-readable answers

Every command answers in JSON with `--json`, and names in German with `--lang de`:

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

`ulg show <id> --json` adds the description, textures, symbol, attributes and aliases.

The whole catalog as one file for tools in other languages: `ulg export tokens out/` → `catalog.json`.

## 7.4 Example requests and what the agent does

| Request | Agent actions |
|---|---|
| "Draw the site plan from `bestand.gpkg` at 1:500" | reads the file, checks the element column (or classifies with the right scheme), `ulg render bestand.gpkg --scale 500 --png` |
| "Make an OSM basemap of Schwabing in our style" | fetches OSM features with osmnx, `ulg.classify(osm, "osm")`, `ulg.render_svg(osm, scale=5000)`; reports the `unknown` tags |
| "How green is the courtyard? We need the BFF" | `ulg.indicators(gdf)` → `bff`, `bff_coverage`, the unsealed share; names the Berlin 2021 list as source |
| "Show the trees to be felled and the root zones" | `tree_remove` for the trees, `ulg.root_protection_zone(trees)` for the zones, legend in German |
| "Give me the QGIS styles" | `ulg export qgis styles/ --lod auto` and explains how to load the QML files |
| "Which colour does CORINE use for parks?" | `ulg resolve clc 141` → element `green_space`, official legend colour `#FFA6FF` |

## 7.5 Working on the library itself

Agents that change the library follow the repository's own [`AGENTS.md`](../AGENTS.md): data first,
palette tokens only, sources for every value, `ulg check` and the tests must pass, and the reference
pages and images are regenerated after data changes ([Extending](08-extending.md)).

---

Next: [8 · Extending the style](08-extending.md)

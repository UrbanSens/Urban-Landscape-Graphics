# Crosswalk file format

A crosswalk tells the library how data classified in an external scheme (CORINE, ALKIS, OSM tags, BKompV …) is drawn: which catalog element each class becomes. One scheme = one JSON file in `src/ulg/data/crosswalks/<scheme>.json`. The file name (without `.json`) is the scheme id used in `ulg.resolve("<scheme>", …)`.

## Top level

```json
{
  "title": "CORINE Land Cover, level 3",
  "publisher": "European Environment Agency (Copernicus Land Monitoring Service)",
  "version": "CLC nomenclature as used for CLC 2018 and CLC 2024",
  "source": "https://land.copernicus.eu/...",
  "license_note": "Codes and names are facts; colours are the official legend colours.",
  "key": "code",
  "fields": {"code": ["code_18", "clc_code", "code_12"]},
  "note": "Short remarks on how to use the scheme, known pitfalls.",
  "entries": [ ... ]
}
```

| Field | Required | Meaning |
|---|---|---|
| `title`, `publisher`, `version`, `source` | yes | What the scheme is, which edition, the primary URL used. |
| `key` | yes | Canonical name of the attribute that holds the class code, used when someone calls `resolve(scheme, "141")` or `classify(gdf, scheme, column=...)`. |
| `fields` | no | Maps canonical attribute names to the column names found in real data files (case-insensitive). Example for ALKIS: `{"objart": ["objektart", "objart", "kennung"], "funktion": ["fkt"], "vegetationsmerkmal": ["veg"]}`. |
| `hierarchy` | no | `"prefix"` or `"dotted"`. When a code has no entry, broader codes are tried: with `prefix` by dropping the last character (`G214` → `G21` → `G2` → `G`; `E2.64` → `E2.6` → `E2` → `E`), with `dotted` by dropping the last dotted segment (`34.07a.01` → `34.07a` → `34`). Add group-level entries so every code resolves at least to its group. |
| `suffixes` | no | Code endings that qualify a class without changing it, stripped when the full code has no entry. BKompV age classes: `["J", "M", "A", "MA"]` makes `41.03.03J` resolve as `41.03.03`. |
| `fallback_pattern` | no | Regular expression a code must match to take part in the hierarchy fallback. BayKompV uses `^[A-Z][0-9]` so that bare biotope-mapping codes such as `GU651E` do not fall back to the unrelated BNT group `G`. |
| `license_note`, `note` | no | Free text. |

## Entries

Each entry says: data that looks like *this* is drawn as *that* element.

```json
{"code": "141", "name": "Green urban areas", "name_de": "Städtische Grünflächen",
 "element": "green_space", "fit": "exact", "color": "#FFA6FF", "evidence": "V"}

{"match": {"objart": "41008", "funktion": "4400"}, "name": "Grünanlage",
 "element": "green_space", "fit": "exact", "nak": "18040000", "color": "#DCE6C2", "evidence": "V"}

{"match": {"natural": "wetland", "wetland": "reedbed"}, "element": "reed", "fit": "exact"}
```

| Field | Required | Meaning |
|---|---|---|
| `code` | one of `code` / `match` | The class code (string). Equivalent to `"match": {"<key>": "<code>"}`. |
| `match` | one of `code` / `match` | Several attribute conditions that must all hold. Keys use the canonical names; values are strings; `"*"` means "any non-empty value". |
| `name` | yes | Official class name in the scheme's language. `name_de` / `name_en` optional. |
| `element` | yes | Element id from `docs/reference/element-list.md`, or `null` for classes that are not drawn (with `fit: "none"`). |
| `fit` | yes | `exact` – same concept · `narrower` – the element is more specific than the class · `broader` – the element is more general than the class · `nearest` – no real equivalent, closest drawing · `none` – not drawable (element `null`). |
| `color` | no | The scheme's **own official legend colour** for the class, `#RRGGBB` upper case. Only when the research marks it as verified (V), or V\* with the reason stated in the file's `license_note` (EUNIS legend swatches). Never an invented or house colour. |
| `evidence` | no | `V`, `V*`, `S` or `R` as in the research files, for the mapping row. |
| `note` | no | Short remark (e.g. "use attribute age_class to pick the value"). |
| any other | no | Scheme-specific facts, e.g. `value` (biotope value points), `nak` (ALKIS Nutzungsartkennung), `nrr_urban_green` (true/false), `level`, `parent`. |

## Matching rules

1. Attribute names and values are compared case-insensitively; numbers and strings match (`4400` = `"4400"`).
2. The most specific entry wins: an entry with two conditions beats one with a single condition when both match.
3. Among equally specific entries, the **first in the file** wins. Put specific or preferred rows first.
4. A plain code without an entry is tried without its `suffixes`, then through the `hierarchy` (only if it matches `fallback_pattern`, when one is given). Numeric prefix codes also try zero-padded parents (`18049999` → … → `18040000`).
5. Records that still match nothing become the `unknown` element (configurable with `default=`), so gaps stay visible on the map.

## Validation

`python -m pytest tests/test_crosswalks.py` checks every file: element ids exist, `fit` values are valid, colours are `#RRGGBB`, no two entries have the same match.

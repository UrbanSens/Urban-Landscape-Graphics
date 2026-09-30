"""Crosswalks: from the codes of official classifications (and OSM tags) to catalog elements.

Each scheme is a JSON file in ``ulg/data/crosswalks``. An entry says: data that
looks like *this* is drawn as *that* element. Matching is by attributes; the most
specific entry wins, so ``natural=wetland + wetland=reedbed`` beats
``natural=wetland``. Among equally specific entries the first one in the file wins.

    >>> import ulg
    >>> ulg.resolve("osm", landuse="grass")
    'lawn'
    >>> ulg.resolve("clc", "141")
    'green_space'

File format (see ``docs/reference/crosswalk-format.md``)::

    {
      "title": "...", "publisher": "...", "version": "...", "source": "https://...",
      "key": "code",                               # attribute used for plain-code lookups
      "fields": {"code": ["code_18", "clc"]},      # column names in user data -> canonical keys
      "entries": [
        {"code": "141", "name": "Green urban areas", "element": "green_space",
         "fit": "exact", "color": "#FFA6FF"},
        {"match": {"landuse": "grass"}, "element": "lawn", "fit": "exact"}
      ]
    }

``fit`` grades the semantic match: ``exact`` (same concept), ``narrower`` (the
element is more specific than the class), ``broader`` (the element is more
general), ``nearest`` (no real equivalent; closest drawing), ``none`` (not a
drawable class, ``element`` is null).
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from .catalog import Catalog, CatalogError, load

FITS = ("exact", "narrower", "broader", "nearest", "none")


def _s(v: Any) -> str:
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip().lower()


def _entry_match(entry: dict, key: str) -> dict[str, str]:
    m = {str(k).lower(): _s(v) for k, v in (entry.get("match") or {}).items()}
    if "code" in entry:
        m.setdefault(key, _s(entry["code"]))
    return m


def _blank(v: Any) -> bool:
    if v is None:
        return True
    if isinstance(v, float) and v != v:  # NaN from pandas
        return True
    return str(v).strip() == ""


class Scheme:
    """One external classification with its mapping to elements."""

    def __init__(self, name: str, data: dict):
        self.name = name
        self.title = data.get("title", name)
        self.publisher = data.get("publisher", "")
        self.version = data.get("version", "")
        self.source = data.get("source", "")
        self.note = data.get("note", "")
        self.key = str(data.get("key", "code")).lower()
        self.hierarchy = data.get("hierarchy")  # None | "dotted" | "prefix"
        # optional: code endings to strip before falling back (age classes "41.03.03J" -> "41.03.03")
        self.suffixes = sorted((_s(x) for x in data.get("suffixes", [])), key=len, reverse=True)
        # optional: only codes matching this regex take part in the hierarchy fallback
        pattern = data.get("fallback_pattern")
        self._fallback = re.compile(pattern, re.IGNORECASE) if pattern else None
        self.entries: list[dict] = data.get("entries", [])
        self.data = data
        aliases: dict[str, str] = {}
        for canonical, names in (data.get("fields") or {}).items():
            for n in [canonical, *names]:
                aliases[str(n).lower()] = str(canonical).lower()
        aliases.setdefault("code", self.key)
        self._aliases = aliases
        rules = []
        for n, e in enumerate(self.entries):
            m = _entry_match(e, self.key)
            if m:
                rules.append((len(m), n, m, e))
        self._rules = sorted(rules, key=lambda t: (-t[0], t[1]))
        self._by_code = {}
        for e in self.entries:
            if "code" in e and _s(e["code"]) not in self._by_code:
                self._by_code[_s(e["code"])] = e

    def info(self) -> dict:
        return {"scheme": self.name, "title": self.title, "publisher": self.publisher, "version": self.version,
                "source": self.source, "entries": len(self.entries), "key": self.key,
                "fields": sorted(set(self._aliases.values())), "note": self.note}

    def normalise(self, query: Mapping[str, Any]) -> dict[str, str]:
        """Lower-case keys, apply field aliases, drop empty values."""
        q: dict[str, str] = {}
        for k, v in query.items():
            if _blank(v):
                continue
            k = str(k).lower()
            q[self._aliases.get(k, k)] = _s(v)
        return q

    def lookup(self, query: Mapping[str, Any]) -> dict | None:
        """The most specific entry whose conditions are all met by ``query``."""
        q = self.normalise(query)
        if not q:
            return None
        if len(q) == 1 and self.key in q:
            hit = self._by_code.get(q[self.key])
            if hit is not None and not hit.get("match"):
                return hit
        for _, _, match, entry in self._rules:
            if all(q.get(k) == v or (v == "*" and k in q) for k, v in match.items()):
                return entry
        if self.key in q:
            return self._fallback_lookup(q[self.key])
        return None

    def _fallback_lookup(self, code: str) -> dict | None:
        """Suffix stripping, then broader codes of a hierarchical scheme."""
        candidates = [code] + [code[:-len(x)] for x in self.suffixes if x and code.endswith(x) and len(code) > len(x)]
        for c in candidates[1:]:
            hit = self._by_code.get(c)
            if hit is not None and not hit.get("match"):
                return hit
        if not self.hierarchy:
            return None
        for c in candidates:
            if self._fallback is not None and not self._fallback.match(c):
                continue
            for parent in self._parents(c):
                hit = self._by_code.get(parent)
                if hit is not None:
                    return hit
        return None

    def _parents(self, code: str):
        """Broader codes of a hierarchical code, most specific first ("e2.64" -> "e2.6", "e2", "e").

        Numeric keys also try the zero-padded form of each prefix, because some schemes
        write their groups at full length ("18049999" -> ... "1804", "18040000").
        """
        if self.hierarchy == "dotted":
            parts = code.split(".")
            for n in range(len(parts) - 1, 0, -1):
                yield ".".join(parts[:n])
        else:
            c = code.rstrip(".")
            while len(c) > 1:
                c = c[:-1].rstrip(".")
                yield c
                if code.isdigit() and len(c) < len(code):
                    padded = c.ljust(len(code), "0")
                    if padded != code:
                        yield padded

    def official_color(self, code: Any) -> str | None:
        """The colour the publisher's own legend uses for a class, if it defines one."""
        e = self._by_code.get(_s(code))
        return e.get("color") if e else None

    def colors(self) -> dict[str, str]:
        return {str(e["code"]): e["color"] for e in self.entries if "code" in e and e.get("color")}


def schemes(catalog: Catalog | None = None) -> dict[str, Scheme]:
    catalog = catalog or load()
    cache = getattr(catalog, "_schemes", None)
    if cache is None:
        cache = {name: Scheme(name, data) for name, data in catalog.crosswalks.items()}
        catalog._schemes = cache  # type: ignore[attr-defined]
    return cache


def scheme(name: str, catalog: Catalog | None = None) -> Scheme:
    all_ = schemes(catalog)
    try:
        return all_[name.lower()]
    except KeyError:
        raise CatalogError(f"unknown scheme {name!r}; available: {', '.join(sorted(all_))}") from None


def resolve(scheme_name: str, code: Any = None, *, catalog: Catalog | None = None, default: str | None = None,
            **attrs: Any) -> str | None:
    """Element id for a class of an external scheme.

    ``resolve("clc", 141)``, ``resolve("alkis", objart=43001, vegetationsmerkmal=1020)``,
    ``resolve("osm", natural="wetland", wetland="reedbed")``.
    """
    sch = scheme(scheme_name, catalog)
    query = dict(attrs)
    if code is not None:
        query[sch.key] = code
    entry = sch.lookup(query)
    return entry["element"] if entry and entry.get("element") else default


def explain(scheme_name: str, code: Any = None, *, catalog: Catalog | None = None, **attrs: Any) -> dict | None:
    """The full crosswalk entry that ``resolve`` would use (name, fit, official colour, notes)."""
    sch = scheme(scheme_name, catalog)
    query = dict(attrs)
    if code is not None:
        query[sch.key] = code
    return sch.lookup(query)


def classify(records: Any, scheme_name: str, column: str | None = None, *, catalog: Catalog | None = None,
             default: str | None = "unknown") -> list[str | None]:
    """Element ids for many records at once.

    ``records`` may be a (Geo)DataFrame, a list of dicts (e.g. OSM tags or GeoJSON
    properties) or a list of plain codes. With ``column`` only that column is
    used, as the scheme's code; otherwise every attribute of a record takes part
    in matching, with the scheme's field aliases applied (``Objektart`` -> ``objart``).
    """
    sch = scheme(scheme_name, catalog)
    cache: dict[tuple, str | None] = {}

    def one(query: Mapping[str, Any]) -> str | None:
        q = sch.normalise(query)
        k = tuple(sorted(q.items()))
        if k not in cache:
            entry = sch.lookup(q)
            cache[k] = entry["element"] if entry and entry.get("element") else default
        return cache[k]

    if hasattr(records, "to_dict") and hasattr(records, "columns"):
        if column is not None:
            return [one({sch.key: v}) for v in records[column].tolist()]
        geom = getattr(getattr(records, "geometry", None), "name", None)
        cols = [c for c in records.columns if c != geom]
        return [one(r) for r in records[cols].to_dict("records")]
    out = []
    for r in records:
        if isinstance(r, Mapping):
            out.append(one({sch.key: r[column]} if column is not None else r))
        else:
            out.append(one({sch.key: r}))
    return out


def codes_for(element: str, catalog: Catalog | None = None) -> dict[str, list[dict]]:
    """All external classes that map onto an element, per scheme (the reverse lookup)."""
    out: dict[str, list[dict]] = {}
    for name, sch in schemes(catalog).items():
        hits = [e for e in sch.entries if e.get("element") == element]
        if hits:
            out[name] = hits
    return out


def official_colors(scheme_name: str, catalog: Catalog | None = None) -> dict[str, str]:
    """``code -> hex`` of a scheme's official legend, for maps that must use the prescribed colours."""
    return scheme(scheme_name, catalog).colors()


def coverage(catalog: Catalog | None = None) -> dict[str, dict]:
    """How well each scheme is covered: entries per fit grade, and elements reached."""
    out = {}
    for name, sch in schemes(catalog).items():
        fits: dict[str, int] = {}
        for e in sch.entries:
            fits[e.get("fit", "exact")] = fits.get(e.get("fit", "exact"), 0) + 1
        out[name] = {"entries": len(sch.entries), "fits": fits,
                     "elements": len({e.get("element") for e in sch.entries if e.get("element")})}
    return out


def validate(catalog: Catalog | None = None) -> list[str]:
    """Problems in the crosswalk files: unknown elements, bad colours, duplicate keys, missing fields."""
    import re

    catalog = catalog or load()
    problems = []
    hexre = re.compile(r"^#[0-9A-Fa-f]{6}$")
    for name, sch in schemes(catalog).items():
        seen: dict[tuple, int] = {}
        for n, e in enumerate(sch.entries):
            where = f"{name}[{n}]"
            el = e.get("element")
            if el is not None and el not in catalog:
                problems.append(f"{where}: unknown element {el!r}")
            fit = e.get("fit", "exact")
            if fit not in FITS:
                problems.append(f"{where}: fit {fit!r} not in {FITS}")
            if el is None and fit != "none":
                problems.append(f"{where}: element is null but fit is {fit!r} (use 'none')")
            if "code" not in e and not e.get("match"):
                problems.append(f"{where}: needs 'code' or 'match'")
            col = e.get("color")
            if col is not None and not hexre.match(str(col)):
                problems.append(f"{where}: colour {col!r} is not #RRGGBB")
            key = tuple(sorted(_entry_match(e, sch.key).items()))
            if key in seen:
                problems.append(f"{where}: same match as entry {seen[key]}")
            else:
                seen[key] = n
    return problems

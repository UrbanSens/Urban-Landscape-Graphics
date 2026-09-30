"""The catalog: palette, elements and crosswalks, loaded from the JSON files in ``ulg/data``.

The JSON files are the single source of truth. Python, the exporters, the
command line and AI agents all read the same data, so a colour or a code is
defined in exactly one place.
"""

from __future__ import annotations

import difflib
import json
import re
import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from importlib import resources
from typing import Any, Iterable, Iterator

from . import colormath as C

COLOR_KEYS = ("ink", "ink2", "fill", "stem", "center", "branch", "color", "casing", "halo",
              "ring", "cross_out", "pit", "pit_ink", "frame_color", "centre_fill", "stem_fill", "accent")
COLOR_LIST_KEYS = ("accents", "tones")
GEOMETRIES = ("polygon", "line", "point")


class CatalogError(KeyError):
    """Unknown element, colour token or scheme."""

    def __str__(self) -> str:  # KeyError would show the repr
        return str(self.args[0]) if self.args else ""


# --------------------------------------------------------------------------- palette

class Palette:
    """Named colours, addressed as ``family.step`` (for example ``grass.300``)."""

    def __init__(self, data: dict):
        self.name = data.get("name", "")
        self.theme = data.get("theme", "")
        self.families: dict[str, dict[str, str]] = data["colors"]

    def __contains__(self, ref: str) -> bool:
        try:
            self.resolve(ref)
        except CatalogError:
            return False
        return True

    def resolve(self, ref: str | None) -> str | None:
        """Token or literal colour -> ``#RRGGBB``. ``None`` and ``"none"`` stay ``None``."""
        if ref is None or ref == "none":
            return None
        if ref.startswith("#"):
            return C.to_hex(ref)
        fam, _, step = ref.partition(".")
        try:
            return self.families[fam][step]
        except KeyError:
            raise CatalogError(f"unknown colour token {ref!r}") from None

    def flat(self) -> dict[str, str]:
        return {f"{fam}.{step}": hexv for fam, steps in self.families.items() for step, hexv in steps.items()}


# --------------------------------------------------------------------------- elements

@dataclass(frozen=True)
class Element:
    """One thing that can be drawn on a map, with its style and its standard codes."""

    id: str
    group: str
    geometry: tuple[str, ...]
    label: dict[str, str]
    description: dict[str, str]
    z: int
    fill: str | None
    outline: str | None
    fill_opacity: float
    outline_width: float | None
    outline_dash: tuple | None
    textures: tuple[dict, ...]
    wash: bool
    line: dict | None
    symbol: dict | None
    border: dict | None
    attributes: dict[str, Any]
    codes: dict[str, tuple[str, ...]]
    aliases: tuple[str, ...]
    raw: dict = field(repr=False, compare=False, default_factory=dict)

    def name(self, lang: str = "en") -> str:
        return self.label.get(lang) or self.label.get("en") or self.id

    @property
    def ink(self) -> str | None:
        """The colour of the main texture mark (or the outline if there is no texture)."""
        for t in self.textures:
            if t.get("ink"):
                return t["ink"]
        return self.outline

    def to_dict(self) -> dict:
        """Plain, fully resolved description for JSON output and agents."""
        return {
            "id": self.id,
            "group": self.group,
            "geometry": list(self.geometry),
            "label": dict(self.label),
            "description": dict(self.description),
            "fill": self.fill,
            "fill_opacity": self.fill_opacity,
            "outline": self.outline,
            "outline_width": self.outline_width,
            "outline_dash": list(self.outline_dash) if self.outline_dash else None,
            "ink": self.ink,
            "textures": [dict(t) for t in self.textures],
            "line": self.line,
            "symbol": self.symbol,
            "border": self.border,
            "z": self.z,
            "attributes": dict(self.attributes),
            "codes": {k: list(v) for k, v in self.codes.items()},
            "aliases": list(self.aliases),
        }


def _resolve_spec(spec: dict, palette: Palette) -> dict:
    out = {}
    for k, v in spec.items():
        if k in COLOR_KEYS and isinstance(v, str):
            out[k] = palette.resolve(v)
        elif k in COLOR_LIST_KEYS:
            out[k] = [palette.resolve(c) for c in v]
        elif isinstance(v, dict):
            out[k] = _resolve_spec(v, palette)
        else:
            out[k] = v
    return out


def _norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower().replace("ß", "ss"))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


class Catalog:
    """All elements of one theme plus the crosswalks from external classifications."""

    def __init__(self, palette: Palette, elements: dict[str, dict], crosswalks: dict[str, dict],
                 settings: dict | None = None, theme: dict | None = None):
        self.palette = palette
        self.settings = settings or {}
        self.crosswalks = crosswalks
        self.theme = theme or {"name": "mellow", "title": "UrbanSens mellow (house style)", "handdrawn": 1.0,
                               "background": "paper.base"}
        self._elements: dict[str, Element] = {}
        codes = self._codes_by_element(crosswalks)
        for eid, raw in elements.items():
            self._elements[eid] = self._build(eid, raw, codes.get(eid, {}))
        self._index: dict[str, str] | None = None

    # -- construction ------------------------------------------------------
    def _build(self, eid: str, raw: dict, codes: dict[str, list[str]]) -> Element:
        p = self.palette
        fill = p.resolve(raw.get("fill"))
        outline = raw.get("outline", "auto")
        if outline == "auto":
            outline = C.darken(fill, self.settings.get("outline_darken", 0.10)) if fill else None
        else:
            outline = p.resolve(outline)
        return Element(
            id=eid,
            group=raw.get("group", "other"),
            geometry=tuple(raw.get("geometry", ["polygon"])),
            label=raw.get("label", {"en": eid}),
            description=raw.get("description", {}),
            z=int(raw.get("z", 50)),
            fill=fill,
            outline=outline,
            fill_opacity=float(raw.get("fill_opacity", 1.0)),
            outline_width=raw.get("outline_width"),
            outline_dash=tuple(raw["outline_dash"]) if raw.get("outline_dash") else None,
            textures=tuple(_resolve_spec(t, p) for t in raw.get("textures", [])),
            wash=bool(raw.get("wash", False)),
            line=_resolve_spec(raw["line"], p) if raw.get("line") else None,
            symbol=_resolve_spec(raw["symbol"], p) if raw.get("symbol") else None,
            border=_resolve_spec(raw["border"], p) if raw.get("border") else None,
            attributes=raw.get("attributes", {}),
            codes={k: tuple(v) for k, v in codes.items()},
            aliases=tuple(raw.get("aliases", [])),
            raw=raw,
        )

    @staticmethod
    def _codes_by_element(crosswalks: dict[str, dict]) -> dict[str, dict[str, list[str]]]:
        out: dict[str, dict[str, list[str]]] = {}
        for scheme, cw in crosswalks.items():
            for entry in cw.get("entries", []):
                el = entry.get("element")
                if el:
                    code = entry.get("code")
                    if code is None:
                        code = "+".join(f"{k}={v}" for k, v in (entry.get("match") or {}).items())
                    out.setdefault(el, {}).setdefault(scheme, []).append(str(code))
        return out

    # -- access ------------------------------------------------------------
    def __getitem__(self, eid: str) -> Element:
        try:
            return self._elements[eid]
        except KeyError:
            hint = difflib.get_close_matches(eid, self._elements, n=3)
            msg = f"unknown element {eid!r}" + (f" (did you mean {', '.join(hint)}?)" if hint else "")
            raise CatalogError(msg) from None

    def __contains__(self, eid: str) -> bool:
        return eid in self._elements

    def __iter__(self) -> Iterator[Element]:
        return iter(self._elements.values())

    def __len__(self) -> int:
        return len(self._elements)

    def get(self, eid: str, default: Element | None = None) -> Element | None:
        return self._elements.get(eid, default)

    def ids(self) -> list[str]:
        return list(self._elements)

    def groups(self) -> dict[str, list[Element]]:
        out: dict[str, list[Element]] = {}
        for el in self:
            out.setdefault(el.group, []).append(el)
        return out

    # -- search ------------------------------------------------------------
    def _search_index(self) -> dict[str, str]:
        if self._index is None:
            idx: dict[str, str] = {}
            for el in self:
                names = [el.id, el.id.replace("_", " "), *el.label.values(), *el.aliases]
                for nme in names:
                    idx.setdefault(_norm(nme), el.id)
            self._index = idx
        return self._index

    def find(self, text: str, n: int = 5) -> list[Element]:
        """Elements whose id, label (any language) or alias matches ``text``, best first."""
        idx = self._search_index()
        q = _norm(text)
        if not q:
            return []
        hits: list[str] = []
        if q in idx:
            hits.append(idx[q])
        for key, eid in idx.items():
            if eid not in hits and (q in key.split() or key.startswith(q) or (len(q) >= 4 and q in key)):
                hits.append(eid)
        for key in difflib.get_close_matches(q, idx, n=n * 2, cutoff=0.72):
            if idx[key] not in hits:
                hits.append(idx[key])
        return [self._elements[e] for e in hits[:n]]


# --------------------------------------------------------------------------- themes

_OVERLAY_GROUPS = ("planning", "analysis")


def _theme_override(eid: str, raw: dict, th: dict) -> dict:
    o = dict(th.get("default", {}))
    group = raw.get("group", "")
    for prefix in sorted(th.get("groups", {}), key=len):
        if group == prefix or group.startswith(prefix + "."):
            o.update(th["groups"][prefix])
    o.update(th.get("elements", {}).get(eid, {}))
    return o


def _recolour(spec: dict, colour: str, paper: str | None = None) -> dict:
    """Every colour in a texture / line / symbol spec becomes ``colour`` (fills of marks become ``paper``)."""
    out = {}
    for k, v in spec.items():
        if k in ("tones",):
            out[k] = [paper or colour]
        elif k == "accents":
            out[k] = [colour]
        elif k in ("fill", "centre_fill", "stem_fill", "pit") and paper is not None:
            out[k] = paper
        elif k in COLOR_KEYS and isinstance(v, str):
            out[k] = colour
        elif isinstance(v, dict):
            out[k] = _recolour(v, colour, paper)
        else:
            out[k] = v
    return out


def apply_theme(elements: dict[str, dict], th: dict) -> dict[str, dict]:
    """Raw element dicts with a theme's colours applied (see ``ulg/data/themes``)."""
    import copy

    mode = th.get("textures", "none")
    ink, paper = th.get("ink", "#222222"), th.get("paper", "#FFFFFF")
    out: dict[str, dict] = {}
    for eid, raw in elements.items():
        o = _theme_override(eid, raw, th)
        new = copy.deepcopy(raw)
        new["wash"] = False
        explicit = th.get("elements", {}).get(eid, {})
        if raw.get("fill") is not None or "fill" in explicit:
            if "fill" in o:
                new["fill"] = o["fill"]
        if "outline" in o and (raw.get("outline", "auto") is not None or "outline" in explicit):
            new["outline"] = o["outline"]
        if "outline_width" in o:
            new["outline_width"] = o["outline_width"]
        line_col = o.get("outline") or ink
        overlay = raw.get("group", "").split(".")[0] in _OVERLAY_GROUPS
        if mode == "mono":
            new["textures"] = [_recolour(t, ink, paper) for t in raw.get("textures", [])]
            for t in new["textures"]:
                if t.get("motif") == "canopy":  # crowns are told apart by tone in colour; in ink they need a line
                    t.setdefault("lod", {}).setdefault("1", {}).update({"width": 0.12, "opacity": 1.0})
        elif overlay:
            new["textures"] = [_recolour(t, line_col) for t in raw.get("textures", [])]
        else:
            new["textures"] = o.get("textures", [])
        if raw.get("line"):
            ln = copy.deepcopy(raw["line"])
            if mode == "mono":
                ln = _recolour(ln, ink, paper)
                if ln.get("casing"):
                    ln["color"] = paper if raw["line"].get("color") else None
            else:
                band = bool(ln.get("casing"))
                if ln.get("color"):
                    ln["color"] = (o.get("fill") or line_col) if band else line_col
                if band:
                    ln["casing"] = line_col
                if ln.get("marks"):
                    ln["marks"] = dict(ln["marks"])
                    m = ln["marks"]
                    if m.get("kind") == "crowns":
                        m.update({"tones": [o.get("fill") or paper], "ink": line_col, "branch": line_col, "star": False})
                    else:
                        m["color"] = line_col
            new["line"] = ln
        if raw.get("symbol"):
            sym = copy.deepcopy(raw["symbol"])
            status = {k: sym.get(k) for k in ("frame_color", "cross_out") if sym.get(k)}
            if mode == "mono":
                sym = _recolour(sym, ink, paper)
            elif sym.get("kind") == "crown":
                sym["tones"] = [o.get("fill") or paper]
                sym["ink"] = sym["branch"] = line_col
                if sym.get("centre", "star") == "star":
                    sym["centre"] = "dot"
                sym["star"] = False
                sym["depth"] = min(sym.get("depth", 0.05), 0.02)
                sym.update(status)
            else:
                if o.get("fill"):
                    sym["color"] = o["fill"]
                sym["ink"] = line_col
            new["symbol"] = sym
        if raw.get("border"):
            new["border"] = {**raw["border"], "color": ink if mode == "mono" else line_col}
        out[eid] = new
    return out


def themes() -> dict[str, str]:
    """Available themes: ``name -> title``."""
    out = {"mellow": "UrbanSens mellow (house style)"}
    root = resources.files("ulg").joinpath("data", "themes")
    for node in sorted(root.iterdir(), key=lambda n: n.name):
        if node.name.endswith(".json"):
            out[node.name[:-5]] = json.loads(node.read_text(encoding="utf-8")).get("title", node.name[:-5])
    return out


# --------------------------------------------------------------------------- loading

def _read_json(*parts: str) -> dict:
    node = resources.files("ulg").joinpath("data", *parts)
    return json.loads(node.read_text(encoding="utf-8"))


def _read_dir(name: str) -> Iterable[tuple[str, dict]]:
    root = resources.files("ulg").joinpath("data", name)
    for node in sorted(root.iterdir(), key=lambda n: n.name):
        if node.name.endswith(".json"):
            yield node.name[:-5], json.loads(node.read_text(encoding="utf-8"))


@lru_cache(maxsize=8)
def load(theme: str = "mellow") -> Catalog:
    """Load the built-in catalog, optionally in another theme (``ulg.themes()`` lists them).

    Cached; the result must be treated as read-only.
    """
    palette_data = _read_json("palette.json")
    settings = _read_json("settings.json") if resources.files("ulg").joinpath("data", "settings.json").is_file() else {}
    elements: dict[str, dict] = {}
    for fname, data in _read_dir("elements"):
        for eid, raw in data.get("elements", {}).items():
            if eid in elements:
                raise CatalogError(f"element {eid!r} is defined twice (second time in elements/{fname}.json)")
            elements[eid] = raw
    crosswalks = {fname: data for fname, data in _read_dir("crosswalks")}
    meta = None
    if theme != "mellow":
        node = resources.files("ulg").joinpath("data", "themes", f"{theme}.json")
        if not node.is_file():
            raise CatalogError(f"unknown theme {theme!r}; available: {', '.join(themes())}")
        th = json.loads(node.read_text(encoding="utf-8"))
        elements = apply_theme(elements, th)
        meta = {k: v for k, v in th.items() if k not in ("default", "groups", "elements")}
        meta["name"] = theme
    return Catalog(Palette(palette_data), elements, crosswalks, settings, meta)

"""Legibility report for the catalog.

A pastel palette keeps a map calm but puts many fills close together. This module
measures how close, also under simulated colour-vision deficiencies, and checks
that every pair of land-cover elements that is hard to tell apart by colour is
separated by its texture or outline instead (WCAG 2.2 SC 1.4.1: colour must not
be the only means of conveying information; technique G111 "colour and pattern").

Threshold: CIEDE2000 below 10 counts as "close" (Brychtová & Çöltekin 2016
recommend at least 10 for reliable discrimination of qualitative map colours).
"""

from __future__ import annotations

from itertools import combinations

from . import colormath as C
from .catalog import Catalog, Element, load

DELTA_E_MIN = 10.0

#: groups that are not land cover: they are separated by line style, hatch or position
OVERLAY_GROUPS = ("context", "analysis", "planning", "boundary", "relief", "other")

#: texture parameters that change what a texture looks like
_SHAPE_KEYS = ("spacing", "size", "crown_m", "unit_m", "course_m", "cell_m", "row_m", "band_m", "angle", "cross",
               "spiky", "offset", "keep", "dots", "arms", "kinds", "dash", "length", "height", "blades", "fill_ratio",
               "stagger", "pack")


def _shape(t: dict) -> tuple:
    keys = tuple((k, str(t[k])) for k in _SHAPE_KEYS if k in t)
    lods = tuple((lod, _shape(spec)) for lod, spec in sorted((t.get("lod") or {}).items()))
    return keys + lods


def _signature(el: Element) -> tuple:
    """What an element looks like apart from its fill: texture geometry, outline style and outline lightness."""
    tex = tuple(sorted((t.get("motif"),) + _shape(t) for t in el.textures))
    line = round(C.to_oklab(el.outline)[0], 1) if el.outline else None
    return tex, bool(el.outline_dash), round(el.outline_width or 0.18, 2), bool(el.border), line


def land_cover(catalog: Catalog | None = None) -> list[Element]:
    """Polygon elements that tile the ground and can meet each other on a map."""
    catalog = catalog or load()
    return [el for el in catalog if el.fill and "polygon" in el.geometry
            and el.group.split(".")[0] not in OVERLAY_GROUPS and el.attributes.get("layer") != "overlay"]


def _family(el: Element) -> str | None:
    return el.attributes.get("family")


def close_pairs(catalog: Catalog | None = None, threshold: float = DELTA_E_MIN, cvd: str | None = None) -> list[dict]:
    """Pairs of land-cover elements whose fills are closer than ``threshold`` (CIEDE2000)."""
    out = []
    for a, b in combinations(land_cover(catalog), 2):
        fa, fb = (a.fill, b.fill) if cvd is None else (C.simulate_cvd(a.fill, cvd), C.simulate_cvd(b.fill, cvd))
        de = C.delta_e_2000(fa, fb)
        if de < threshold:
            same_family = _family(a) is not None and _family(a) == _family(b)
            out.append({"a": a.id, "b": b.id, "delta_e": round(de, 1),
                        "texture_differs": _signature(a) != _signature(b), "same_family": same_family})
    return sorted(out, key=lambda d: d["delta_e"])


def mark_contrast(catalog: Catalog | None = None) -> list[dict]:
    """WCAG contrast of each texture mark against its fill (marks below about 1.15 start to vanish in print)."""
    catalog = catalog or load()
    out = []
    for el in catalog:
        if el.fill and el.ink and el.textures:
            out.append({"element": el.id, "fill": el.fill, "ink": el.ink,
                        "contrast": round(C.contrast_ratio(el.fill, el.ink), 2)})
    return sorted(out, key=lambda d: d["contrast"])


def report(catalog: Catalog | None = None) -> dict:
    catalog = catalog or load()
    normal = close_pairs(catalog)
    bad = [p for p in normal if not p["texture_differs"] and not p["same_family"]]
    cvd = {}
    for kind in C.CVD_KINDS:
        pairs = close_pairs(catalog, cvd=kind)
        cvd[kind] = {"close_pairs": len(pairs),
                     "without_texture_difference": [p for p in pairs if not p["texture_differs"] and not p["same_family"]]}
    res = {
        "threshold_delta_e_2000": DELTA_E_MIN,
        "land_cover_elements": len(land_cover(catalog)),
        "close_pairs": len(normal),
        "close_pairs_without_texture_difference": bad,
        "cvd": cvd,
        "weakest_marks": mark_contrast(catalog)[:10],
    }
    res["ok"] = not bad and not any(v["without_texture_difference"] for v in cvd.values())
    return res


def format_report(rep: dict) -> str:
    lines = [f"{rep['land_cover_elements']} land-cover elements; pairs closer than dE00 "
             f"{rep['threshold_delta_e_2000']:g}: {rep['close_pairs']} (these rely on texture, which is intended)"]
    bad = rep["close_pairs_without_texture_difference"]
    lines.append(f"pairs that differ neither in colour nor in texture or outline: {len(bad)}")
    for p in bad:
        lines.append(f"  !! {p['a']:26s} {p['b']:26s} dE00 {p['delta_e']}")
    for kind, v in rep["cvd"].items():
        lines.append(f"{kind}: {v['close_pairs']} close pairs, {len(v['without_texture_difference'])} without texture difference")
        for p in v["without_texture_difference"]:
            lines.append(f"  !! {p['a']:26s} {p['b']:26s} dE00 {p['delta_e']}")
    lines.append("weakest texture marks (WCAG contrast to fill):")
    for m in rep["weakest_marks"][:6]:
        lines.append(f"  {m['element']:26s} {m['contrast']}")
    lines.append("OK" if rep["ok"] else "NOT OK")
    return "\n".join(lines)

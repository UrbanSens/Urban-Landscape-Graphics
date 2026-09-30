"""Command line interface: ``ulg <command>``.

Every query command takes ``--json`` so scripts and AI agents get machine-readable
answers instead of tables.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .catalog import CatalogError, Element, load


def _emit(obj, as_json: bool, text: str) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False) if as_json else text)


def _row(el: Element, lang: str) -> str:
    other = el.name("de" if lang == "en" else "en")
    return f"{el.id:30s} {el.fill or '-':8s} {el.group:22s} {el.name(lang)}" + (f"  /  {other}" if other != el.name(lang) else "")


def _brief(el: Element) -> dict:
    return {"id": el.id, "label": el.label, "group": el.group, "geometry": list(el.geometry), "fill": el.fill,
            "outline": el.outline, "ink": el.ink,
            "motifs": [t.get("motif") for t in el.textures]}


# --------------------------------------------------------------------------- commands

def cmd_list(a) -> int:
    cat = load()
    els = [el for el in cat if (not a.group or el.group.startswith(a.group))
           and (not a.geometry or a.geometry in el.geometry)]
    _emit([_brief(el) for el in els], a.json, "\n".join(_row(el, a.lang) for el in els) + f"\n{len(els)} elements")
    return 0


def cmd_show(a) -> int:
    from .crosswalk import codes_for

    cat = load()
    el = cat[a.id]
    data = el.to_dict()
    data["schemes"] = {k: [{kk: vv for kk, vv in e.items() if kk != "element"} for e in v]
                       for k, v in codes_for(el.id, cat).items()}
    if a.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0
    lines = [f"{el.id}  -  {el.name('en')} / {el.name('de')}", f"  group     {el.group}   geometry {', '.join(el.geometry)}   z {el.z}",
             f"  fill      {el.fill}" + (f"  (opacity {el.fill_opacity:g})" if el.fill_opacity < 1 else ""),
             f"  outline   {el.outline}", f"  ink       {el.ink}"]
    for t in el.textures:
        lines.append(f"  texture   {t.get('motif')}  " + ", ".join(f"{k}={v}" for k, v in t.items() if k not in ('motif', 'lod')))
    if el.description.get(a.lang):
        lines.append(f"  note      {el.description[a.lang]}")
    for k, v in el.attributes.items():
        lines.append(f"  {k:9s} {v}")
    for scheme, entries in data["schemes"].items():
        codes = ", ".join(str(e.get("code") or "+".join(f"{k}={v}" for k, v in (e.get("match") or {}).items())) for e in entries)
        lines.append(f"  {scheme:9s} {codes}")
    print("\n".join(lines))
    return 0


def cmd_find(a) -> int:
    hits = load().find(" ".join(a.text), n=a.n)
    _emit([_brief(el) for el in hits], a.json, "\n".join(_row(el, a.lang) for el in hits) or "no match")
    return 0 if hits else 1


def cmd_schemes(a) -> int:
    from .crosswalk import schemes

    info = [s.info() for s in schemes().values()]
    _emit(info, a.json, "\n".join(f"{i['scheme']:14s} {i['entries']:4d}  {i['title']}  ({i['version']})" for i in info))
    return 0


def cmd_resolve(a) -> int:
    from .crosswalk import scheme

    query = {}
    for item in a.query:
        if "=" in item:
            k, v = item.split("=", 1)
            query[k] = v
        else:
            query["code"] = item
    entry = scheme(a.scheme).lookup(query)
    cat = load()
    if not entry or not entry.get("element"):
        _emit({"scheme": a.scheme, "query": query, "element": None}, a.json, "no mapping")
        return 1
    el = cat[entry["element"]]
    out = {"scheme": a.scheme, "query": query, "element": el.id, "fill": el.fill, "outline": el.outline,
           "ink": el.ink, "official_color": entry.get("color"), "name": entry.get("name"), "note": entry.get("note")}
    _emit(out, a.json, f"{el.id}  fill {el.fill}  ({el.name(a.lang)})"
          + (f"   official legend colour {entry['color']}" if entry.get("color") else ""))
    return 0


def cmd_render(a) -> int:
    import geopandas as gpd

    from .crosswalk import classify
    from .render.api import render_svg
    from .render.svg import rasterize

    gdf = gpd.read_file(a.input, layer=a.layer) if a.layer else gpd.read_file(a.input)
    by = a.by
    if a.scheme:
        gdf = gdf.copy()
        gdf["element"] = classify(gdf, a.scheme, a.by if a.by != "element" else None)
        by = "element"
    svg = render_svg(gdf, by, scale=a.scale, width=a.width, lod=a.lod, seed=a.seed, handdrawn=a.handdrawn,
                     path=a.output, theme=a.theme)
    print(f"{a.output}: {svg.width:.0f} x {svg.height:.0f} mm, 1:{svg.scale:.0f}, LOD {svg.lod}")
    if a.png:
        print(rasterize(a.output, dpi=a.dpi))
    return 0


def cmd_sheet(a) -> int:
    from .render.svg import rasterize
    from .sheet import catalog_sheet, style_sheet

    fn = catalog_sheet if a.catalog else style_sheet
    fn(a.output, lang=a.lang, catalog=load(a.theme), credit=not a.no_credit)
    print(a.output)
    if a.png:
        print(rasterize(a.output, dpi=a.dpi))
    return 0


def cmd_export(a) -> int:
    from .export import qgis, sld, tokens, web

    d = Path(a.directory)
    done: list[Path] = []
    cat = load(a.theme)
    if a.target in ("qgis", "all"):
        done += qgis.export_qgis(d / "qgis" if a.target == "all" else d, lod=a.lod if a.lod == "auto" else int(a.lod),
                                 lang=a.lang, catalog=cat)
    if a.target in ("web", "all"):
        done += web.export_web(d / "web" if a.target == "all" else d, lod=2 if a.lod == "auto" else int(a.lod),
                               catalog=cat)
    if a.target in ("sld", "all"):
        done += sld.export_sld(d / "sld" if a.target == "all" else d, lang=a.lang, catalog=cat)
    if a.target == "tokens":
        d.mkdir(parents=True, exist_ok=True)
        tokens.css(d / "ulg.css", catalog=cat)
        tokens.dtcg(d / "ulg.tokens.json", catalog=cat)
        tokens.tokens_json(d / "ulg-colors.json", catalog=cat)
        tokens.catalog_json(d / "catalog.json", catalog=cat)
        done += [d / "ulg.css", d / "ulg.tokens.json", d / "ulg-colors.json", d / "catalog.json"]
    print(f"{len(done)} files written to {d}")
    return 0


def cmd_check(a) -> int:
    from .check import format_report, report

    rep = report()
    _emit(rep, a.json, format_report(rep))
    return 0 if rep["ok"] else 1


def cmd_themes(a) -> int:
    from .catalog import themes

    info = []
    for name, title in themes().items():
        meta = load(name).theme
        info.append({"theme": name, "title": title, "description": meta.get("description", ""),
                     "source": meta.get("source", "")})
    _emit(info, a.json, "\n".join(f"{i['theme']:9s} {i['title']}" for i in info))
    return 0


def cmd_indicators(a) -> int:
    import geopandas as gpd

    from .analysis import flatten, indicators
    from .crosswalk import classify

    gdf = gpd.read_file(a.input, layer=a.layer) if a.layer else gpd.read_file(a.input)
    by = a.by
    if a.scheme:
        gdf = gdf.copy()
        gdf["element"] = classify(gdf, a.scheme, a.by if a.by != "element" else None)
        by = "element"
    if a.flatten:
        gdf = flatten(gdf, by)
    res = indicators(gdf, by, plot_area=a.plot_area)
    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    rows = [(k, v) for k, v in res.items() if k != "by_element_m2"]
    print("\n".join(f"{k:26s} {v}" for k, v in rows))
    print("area by element (m2):")
    for k, v in list(res.get("by_element_m2", {}).items())[:15]:
        print(f"  {k:26s} {v:12.1f}")
    return 0


def cmd_categories(a) -> int:
    from . import categories

    cats = categories(a.name)
    _emit(cats, a.json, "\n".join(
        f"{c['id']:18s} {c['color']}  {c.get('min', ''):>6} .. {c.get('max', ''):<6} {c['label'][a.lang]}" for c in cats))
    return 0


def cmd_agent(a) -> int:
    from importlib import resources

    guide = resources.files("ulg").joinpath("data", "agent", "AGENTS.md").read_text(encoding="utf-8")
    if a.action == "guide":
        print(guide)
        return 0
    root = Path(a.dir).resolve()
    skill = resources.files("ulg").joinpath("data", "agent", "SKILL.md").read_text(encoding="utf-8")
    targets = []
    if a.claude or not a.agents:
        targets.append(root / ".claude" / "skills" / "urban-landscape-graphics" / "SKILL.md")
    if a.agents:
        targets.append(root / ".agents" / "skills" / "urban-landscape-graphics" / "SKILL.md")
    for t in targets:
        t.parent.mkdir(parents=True, exist_ok=True)
        t.write_text(skill, encoding="utf-8")
        print(f"wrote {t}")
    snippet = resources.files("ulg").joinpath("data", "agent", "AGENTS.snippet.md").read_text(encoding="utf-8")
    agents_md = root / "AGENTS.md"
    marker = "<!-- ulg:start -->"
    text = agents_md.read_text(encoding="utf-8") if agents_md.exists() else ""
    if marker not in text:
        agents_md.write_text((text.rstrip() + "\n\n" if text else "") + snippet, encoding="utf-8")
        print(f"added the ulg section to {agents_md}")
    else:
        print(f"{agents_md} already has the ulg section")
    return 0


# --------------------------------------------------------------------------- parser

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ulg", description="Urban Landscape Graphics - UrbanSens Ecological Vector Style")
    p.add_argument("--version", action="version", version=f"ulg {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    def add(name, fn, help_):
        sp = sub.add_parser(name, help=help_)
        sp.set_defaults(fn=fn)
        sp.add_argument("--json", action="store_true", help="machine-readable output")
        sp.add_argument("--lang", default="en", choices=["en", "de"])
        return sp

    sp = add("list", cmd_list, "list catalog elements")
    sp.add_argument("--group", help="only groups starting with this (e.g. vegetation, surface)")
    sp.add_argument("--geometry", choices=["polygon", "line", "point"])

    sp = add("show", cmd_show, "everything about one element: colours, textures, standard codes")
    sp.add_argument("id")

    sp = add("find", cmd_find, "search elements by English or German name, alias or id")
    sp.add_argument("text", nargs="+")
    sp.add_argument("-n", type=int, default=5)

    add("schemes", cmd_schemes, "list the classification schemes with a crosswalk")

    sp = add("resolve", cmd_resolve, "element for a class of a scheme, e.g. `ulg resolve osm landuse=grass`")
    sp.add_argument("scheme")
    sp.add_argument("query", nargs="+", help="a code, or key=value pairs")

    add("themes", cmd_themes, "list the colour themes (house style and official conventions)")

    sp = add("categories", cmd_categories, "class palettes for analysis maps: klimatop, utci, pet")
    sp.add_argument("name", choices=["klimatop", "utci", "pet"])

    sp = add("indicators", cmd_indicators, "sealing, BFF, runoff, albedo, green-space and canopy shares of a site")
    sp.add_argument("input")
    sp.add_argument("--layer")
    sp.add_argument("--by", default="element")
    sp.add_argument("--scheme", help="classify with a crosswalk first (osm, alkis, clc, ...)")
    sp.add_argument("--plot-area", type=float, dest="plot_area", help="plot area in m2 (default: mapped ground cover)")
    sp.add_argument("--flatten", action="store_true",
                    help="resolve overlapping areas first (needed for OpenStreetMap and other stacked data)")

    sp = add("render", cmd_render, "draw a vector file (GeoPackage, GeoJSON, Shapefile ...) to SVG")
    sp.add_argument("input")
    sp.add_argument("-o", "--output", default="map.svg")
    sp.add_argument("--layer")
    sp.add_argument("--by", default="element", help="attribute with the element id (or the scheme's code)")
    sp.add_argument("--scheme", help="classify with a crosswalk first (osm, alkis, clc, ...)")
    sp.add_argument("--scale", type=float, help="scale denominator, e.g. 500")
    sp.add_argument("--width", type=float, help="page width in mm (if no scale is given)")
    sp.add_argument("--lod", type=int, choices=[0, 1, 2, 3])
    sp.add_argument("--seed", type=int, default=0)
    sp.add_argument("--handdrawn", type=float, default=None, help="0 exact ... 1 house style ... 2 sketchy")
    sp.add_argument("--theme", default="mellow", help="mellow, planzv, alkis, basemap, bfn, osm, mono")
    sp.add_argument("--png", action="store_true")
    sp.add_argument("--dpi", type=int, default=200)

    sp = add("sheet", cmd_sheet, "generate the style sheet (or the full catalog sheet) as SVG")
    sp.add_argument("-o", "--output", default="ulg-style-sheet.svg")
    sp.add_argument("--catalog", action="store_true", help="all elements instead of the overview")
    sp.add_argument("--no-credit", action="store_true", help="leave the small UrbanSens mark off the sheet")
    sp.add_argument("--theme", default="mellow")
    sp.add_argument("--png", action="store_true")
    sp.add_argument("--dpi", type=int, default=150)

    sp = add("export", cmd_export, "write style files for other platforms")
    sp.add_argument("target", choices=["qgis", "web", "sld", "tokens", "all"])
    sp.add_argument("directory")
    sp.add_argument("--lod", default="2", choices=["0", "1", "2", "3", "auto"])
    sp.add_argument("--theme", default="mellow")

    add("check", cmd_check, "legibility report: colour distances, colour-vision deficiencies, mark contrast")
    sp = add("agent", cmd_agent, "guide for AI coding agents; `ulg agent install` adds the skill to a project")
    sp.add_argument("action", nargs="?", default="guide", choices=["guide", "install"])
    sp.add_argument("--dir", default=".", help="project folder for `install`")
    sp.add_argument("--claude", action="store_true", help="install into .claude/skills (default)")
    sp.add_argument("--agents", action="store_true", help="install into .agents/skills (cross-agent convention)")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except CatalogError as exc:
        print(f"ulg: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

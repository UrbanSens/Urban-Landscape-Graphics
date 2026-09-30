"""Legends: textured swatches for SVG pages, proxy handles for Matplotlib."""

from __future__ import annotations

from typing import Iterable

from .catalog import Catalog, Element, load
from .render import rand as R
from .render.geom import Ctx
from .render.samples import swatch_features
from .render.scene import PICTOGRAMS, Options, build
from .render.svg import Svg

LOD_SCALE = {0: 20000.0, 1: 5000.0, 2: 1500.0, 3: 400.0}


def _pick(catalog: Catalog, elements: Iterable[str | Element] | None) -> list[Element]:
    if elements is None:
        return list(catalog)
    return [e if isinstance(e, Element) else catalog[e] for e in elements]


def used_elements(features, catalog: Catalog | None = None) -> list[Element]:
    """Elements that occur in a feature list, in drawing order, for an automatic legend."""
    catalog = catalog or load()
    seen: dict[str, Element] = {}
    for f in features:
        eid = f.element if hasattr(f, "element") else f[1]
        if eid in catalog and eid not in seen:
            seen[eid] = catalog[eid]
    return sorted(seen.values(), key=lambda e: (e.group, e.z, e.id))


def _swatch_kind(el: Element) -> str:
    if "polygon" in el.geometry and (el.fill or el.textures or el.border or el.outline) and (
            "line" not in el.geometry or el.fill or el.textures):
        return "polygon"
    return "line" if "line" in el.geometry else "point"


def _pictogram_scale(el: Element, w: float, h: float) -> float:
    """Enlargement that makes a pictogram span a little under half of the swatch box."""
    spec = el.symbol or {}
    if spec.get("kind") == "crown":
        return 1.0
    parts = PICTOGRAMS.get(spec.get("kind", "dot"))
    extent = max((abs(c).max() for _, c, *_ in parts), default=1.0) if parts else 1.0
    span = 0.46 * min(w, h)
    return min(max(span / (2.0 * spec.get("r", 0.6) * max(extent, 1.0)), 1.4), 12.0)


def draw_swatch(svg: Svg, el: Element, x: float, y: float, w: float, h: float, *, lod: int = 2,
                scale: float | None = None, shape: str = "auto", catalog: Catalog | None = None,
                seed: int = 0, symbol_scale: float | None = None) -> None:
    """Draw one element sample into the box (x, y, w, h) of a page.

    Pictograms are enlarged to read at the size of the box (or by ``symbol_scale``);
    crowns and lines keep their map size (line samples are drawn at 1:1500 so tree
    rows and hedges show several crowns).
    """
    catalog = catalog or load()
    kind = _swatch_kind(el)
    if scale is None:
        scale = LOD_SCALE[lod] if kind == "polygon" else (LOD_SCALE[2] if kind == "line" else LOD_SCALE[max(lod, 2)])
    u = scale / 1000.0
    feats = swatch_features(el, w, h, u, shape, seed=R.stable_seed(el.id) % 997)
    if kind != "point":
        symbol_scale = 1.0
    elif symbol_scale is None:
        symbol_scale = _pictogram_scale(el, w, h)
    opts = Options(seed=seed, min_texture_area=0.0, symbol_scale=symbol_scale)
    ctx_lod = lod if kind == "polygon" else max(lod, 2)
    items = build(feats, catalog, Ctx(u=u, lod=ctx_lod), opts)
    svg.frame(items, (-w * u / 2, -h * u / 2, w * u / 2, h * u / 2), u, x=x, y=y, clip=False)


def draw_legend(svg: Svg, elements: Iterable[str | Element] | None, x: float, y: float, *, lang: str = "en",
                title: str | None = None, columns: int = 1, col_width: float = 52.0, swatch: tuple = (9.0, 5.6),
                row: float = 7.4, size: float = 2.5, lod: int = 2, catalog: Catalog | None = None,
                ink: str = "#293941") -> float:
    """Draw a legend block at (x, y); returns the y below it."""
    catalog = catalog or load()
    els = _pick(catalog, elements)
    if title:
        svg.text(x, y + size, title.upper(), size=size * 0.95, fill=ink, weight="600", spacing=0.25)
        y += size * 2.6
    per_col = -(-len(els) // columns)
    for k, el in enumerate(els):
        c, r = divmod(k, per_col)
        sx, sy = x + c * col_width, y + r * row
        draw_swatch(svg, el, sx, sy, swatch[0], swatch[1], lod=lod, shape="rect", catalog=catalog)
        svg.text(sx + swatch[0] + 2.6, sy + swatch[1] / 2 + size * 0.36, el.name(lang), size=size, fill=ink)
    return y + per_col * row


def legend_svg(elements: Iterable[str | Element] | None = None, *, lang: str = "en", title: str | None = None,
               columns: int = 1, lod: int = 2, catalog: Catalog | None = None, background: str | None = None,
               col_width: float = 52.0, credit: bool = False) -> Svg:
    """A stand-alone legend as SVG.

    Legends go into your layouts, so they carry nothing extra by default; ``credit=True`` adds the small UrbanSens
    mark below the legend (see :mod:`ulg.brand`).
    """
    catalog = catalog or load()
    els = _pick(catalog, elements)
    per_col = -(-len(els) // columns)
    h = per_col * 7.4 + (9.0 if title else 2.0) + 2
    width = columns * col_width + 4
    svg = Svg(width, h + (11.0 if credit else 0.0), background=background)
    draw_legend(svg, els, 2, 2, lang=lang, title=title, columns=columns, col_width=col_width, lod=lod,
                catalog=catalog)
    if credit:
        from .brand import draw_credit

        draw_credit(svg, width - 2, h + 9.5, height=7.5, lang=lang, text=width >= 90, ink=catalog.palette.resolve("ink.400"))
    return svg


def legend_handles(elements: Iterable[str | Element] | None = None, *, lang: str = "en",
                   catalog: Catalog | None = None) -> list:
    """Proxy artists for ``ax.legend(handles=...)`` (flat colours; Matplotlib legends cannot hold textures)."""
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch

    catalog = catalog or load()
    out = []
    for el in _pick(catalog, elements):
        label = el.name(lang)
        if "polygon" in el.geometry and el.fill:
            out.append(Patch(facecolor=el.fill, edgecolor=el.outline or "none", linewidth=0.6, label=label))
        elif "line" in el.geometry:
            spec = el.line or {}
            col = spec.get("color") or el.outline or el.fill or "#505B61"
            out.append(Line2D([], [], color=col, linewidth=max(0.8, spec.get("width", 0.3) * 2.83), label=label,
                              linestyle=(0, tuple(spec["dash"])) if spec.get("dash") else "-"))
        else:
            spec = el.symbol or {}
            col = (spec.get("tones") or [spec.get("color") or el.fill or "#505B61"])[0]
            out.append(Line2D([], [], marker="o", linestyle="none", markersize=7, markerfacecolor=col,
                              markeredgecolor=spec.get("ink") or "#505B61", markeredgewidth=0.6, label=label))
    return out

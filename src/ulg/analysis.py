"""Indicators from classified maps: sealing, biotope area factor, runoff, albedo, green space, canopy.

The same element ids that style a map carry standard coefficients (see
``ulg/data/settings.json`` -> ``attributes`` for sources and editions). This
module sums them over a site:

    >>> import ulg
    >>> ulg.indicators(gdf)["bff"]          # Berlin Biotopflächenfaktor of the plot
    >>> ulg.root_protection_zone(trees)     # DIN 18920 root zones as polygons

Coefficients are never interpolated: surfaces without a value are reported as
"coverage" below 1 instead of being guessed.
"""

from __future__ import annotations

import math
from typing import Any

from shapely import make_valid, union_all
from shapely.errors import GEOSException
from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry

from .catalog import Catalog, load
from .render.scene import (GIRTH_FIELDS, SIZE_FIELDS, STEM_FIELDS, STRIP_Z, Feature, _number, area_only,
                           as_features, centreline_area)

CANOPY_POINTS = ("tree", "tree_conifer", "tree_fruit", "tree_street", "tree_veteran", "tree_protected")


def _metric(data: Any) -> Any:
    if hasattr(data, "crs") and data.crs is not None and getattr(data.crs, "is_geographic", False):
        return data.to_crs(data.estimate_utm_crs())
    return data


def _features(data: Any, by: str, catalog: Catalog) -> list[Feature]:
    return as_features(_metric(data), by)


def flatten(data: Any, by: str = "element", *, catalog: Catalog | None = None):
    """Resolve overlaps the way the map draws them, so that ground cover tiles the site.

    OpenStreetMap and many sketch datasets stack areas (a park polygon under grass, a
    pond and paths). Area statistics need a planar partition instead. ``flatten`` cuts
    every ground feature by the ground features drawn above it (catalog z-order; at
    equal z the later feature is on top), turns centre lines of roads and paths into
    areas at their width, and passes points, roofs and overlays through unchanged.

        >>> ulg.indicators(ulg.flatten(osm_gdf))

    Returns a GeoDataFrame (in a metric CRS) for a GeoDataFrame, otherwise a list of Features.
    """
    from shapely import STRtree
    from shapely.geometry import GeometryCollection, MultiPolygon

    catalog = catalog or load()
    data = _metric(data)
    feats = as_features(data, by)
    ground, rest = [], []
    for n, f in enumerate(feats):
        el = catalog.get(f.element)
        g = f.geometry
        if el is None or g is None or g.is_empty:
            rest.append((n, f))
            continue
        t = g.geom_type
        z = el.z
        if t in ("LineString", "MultiLineString", "LinearRing") and area_only(el):
            g = centreline_area(g, f.props, el, catalog)
            t, z = g.geom_type, max(el.z, STRIP_Z)
        if t in ("Polygon", "MultiPolygon") and el.attributes.get("layer", "ground") == "ground":
            g = make_valid(g)
            ground.append((z, g.area, n, g, f))
        else:
            rest.append((n, f))
    ground.sort(key=lambda r: (-r[0], r[1], -r[2]))  # the reverse of the drawing order: top first
    geoms = [r[3] for r in ground]
    tree = STRtree(geoms) if geoms else None
    out: list[tuple[int, Feature]] = []
    for i, (_, _, n, g, f) in enumerate(ground):
        above = [geoms[j] for j in tree.query(g) if j < i]
        part = g.difference(_union(above)) if above else g
        polys = [p for p in getattr(part, "geoms", [part]) if p.geom_type in ("Polygon", "MultiPolygon") and not p.is_empty]
        if not polys:
            continue
        part = polys[0] if len(polys) == 1 else _union(polys)
        if isinstance(part, GeometryCollection):
            part = MultiPolygon([p for p in part.geoms if p.geom_type == "Polygon"])
        out.append((n, Feature(part, f.element, f.props)))
    out += rest
    out.sort(key=lambda r: r[0])
    result = [f for _, f in out]
    if hasattr(data, "columns") and hasattr(data, "geometry"):
        import geopandas as gpd

        rows = [dict(f.props, **{by: f.element}) for f in result]
        return gpd.GeoDataFrame(rows, geometry=[f.geometry for f in result], crs=data.crs)
    return result


def _union(geoms: list) -> BaseGeometry:
    """Union that survives the slightly invalid polygons real data contains."""
    valid = [make_valid(g) for g in geoms if g is not None and not g.is_empty]
    try:
        return union_all(valid)
    except GEOSException:
        return union_all([g.buffer(0) for g in valid])


def _crown_disc(f: Feature, default_m: float) -> BaseGeometry | None:
    lower = {str(k).lower(): v for k, v in f.props.items()}
    d = _number(lower, SIZE_FIELDS)
    if not d == d or d <= 0:
        d = default_m
    geoms = getattr(f.geometry, "geoms", [f.geometry])
    return _union([Point(g.x, g.y).buffer(d / 2.0, 24) for g in geoms])


def indicators(data: Any, by: str = "element", *, plot_area: float | None = None, catalog: Catalog | None = None,
               trees: bool = True) -> dict:
    """Area-weighted indicators of a classified site plan.

    ``data``        GeoDataFrame / GeoJSON / (geometry, element) pairs in a metric CRS.
    ``plot_area``   area of the plot in m² (default: the summed ground cover).
    ``trees``       count point trees as canopy using their crown diameter.

    Returns shares in 0–1 and coverage values that say for how much of the area a
    coefficient was known. ``bff`` follows the Berlin rule: ground factors plus the
    credits of roof greening, divided by the plot area.
    """
    catalog = catalog or load()
    feats = _features(data, by, catalog)
    ground, roofs, canopy, green = [], [], [], []
    by_element: dict[str, float] = {}
    for f in feats:
        el = catalog.get(f.element)
        if el is None:
            continue
        a = el.attributes
        t = f.geometry.geom_type
        if t in ("Point", "MultiPoint"):
            if trees and el.id in CANOPY_POINTS:
                disc = _crown_disc(f, float((el.symbol or {}).get("crown_m", 6.0)))
                if disc is not None:
                    canopy.append(disc)
            continue
        if t not in ("Polygon", "MultiPolygon"):
            continue
        area = f.geometry.area
        layer = a.get("layer", "ground")
        if layer == "overlay":
            if a.get("canopy"):
                canopy.append(f.geometry)
            continue
        by_element[el.id] = by_element.get(el.id, 0.0) + area
        (roofs if layer == "roof" else ground).append((f.geometry, el, area))
        if layer == "ground" and a.get("canopy"):
            canopy.append(f.geometry)
        if layer == "ground" and a.get("nrr_urban_green"):
            green.append(f.geometry)

    ground_area = sum(ar for _, _, ar in ground)
    plot = float(plot_area) if plot_area else ground_area
    out: dict[str, Any] = {"plot_area_m2": round(plot, 2), "ground_area_m2": round(ground_area, 2),
                           "roof_area_m2": round(sum(ar for _, _, ar in roofs), 2)}
    if ground_area <= 0:
        return out | {"note": "no polygon ground cover found"}

    # sealing shares (UBA wording)
    shares = {"sealed": 0.0, "partly": 0.0, "unsealed": 0.0, "built": 0.0, None: 0.0}
    for _, el, ar in ground:
        shares[el.attributes.get("sealing") if el.attributes.get("sealing") in shares else None] += ar
    out.update({f"{k}_share": round(v / ground_area, 4) for k, v in shares.items() if k})
    out["sealing_unknown_share"] = round(shares[None] / ground_area, 4)

    # roofs lying on buildings replace the building's own surface for runoff and albedo
    roof_union = _union([g for g, _, _ in roofs]) if roofs else None

    def surface_items():
        for g, el, ar in ground:
            if roof_union is not None and el.attributes.get("sealing") == "built":
                ar = max(ar - make_valid(g).intersection(roof_union).area, 0.0)
            yield el, ar
        for _, el, ar in roofs:
            yield el, ar

    def weighted(key: str, items):
        num = den = 0.0
        for el, ar in items:
            v = el.attributes.get(key)
            if v is not None:
                num += v * ar
                den += ar
        return num, den

    # Berlin BFF: ground factors + roof credits, over the plot area
    num_g, den_g = weighted("bff", [(el, ar) for _, el, ar in ground])
    num_r, _ = weighted("bff", [(el, ar) for _, el, ar in roofs])
    out["bff"] = round((num_g + num_r) / plot, 4)
    out["bff_coverage"] = round(den_g / ground_area, 4)

    total_surface = sum(ar for _, ar in surface_items())
    for key in ("runoff_cm", "runoff_cs", "albedo"):
        num, den = weighted(key, list(surface_items()))
        out[key] = round(num / den, 4) if den else None
        out[f"{key}_coverage"] = round(den / total_surface, 4) if total_surface else 0.0

    # NRR: urban green space and tree canopy, seen from above
    top = _union(green + canopy) if (green or canopy) else None
    site = _union([g for g, _, _ in ground])
    out["nrr_green_share"] = round(top.intersection(site).area / site.area, 4) if top is not None else 0.0
    cover = _union(canopy) if canopy else None
    out["canopy_share"] = round(cover.intersection(site).area / site.area, 4) if cover is not None else 0.0
    out["by_element_m2"] = {k: round(v, 2) for k, v in sorted(by_element.items(), key=lambda kv: -kv[1])}
    return out


def root_protection_zone(data: Any, *, crown_field: str | None = None, columnar_field: str | None = None,
                         default_crown_m: float = 6.0, extra_m: float = 1.5, columnar_extra_m: float = 5.0):
    """Root protection zones after DIN 18920 / R SBB: crown drip line + 1.50 m (columnar trees + 5.00 m).

    Points are treated as crowns with the diameter from ``crown_field`` (or the usual
    field names); polygons as crown outlines. Returns a GeoDataFrame for a
    GeoDataFrame input, otherwise a list of polygons. Also adds the minimum distance
    for excavations, 4 x stem circumference but at least 2.50 m (DIN 18920:2014-07, 4.10;
    the wording of the 2026-06 edition was not verified), when a girth or stem diameter
    is known. The girth is used as recorded: German tree surveys measure it at 1.00 m,
    OpenStreetMap's ``circumference`` at 1.30 m.
    """
    fields = (crown_field.lower(),) + SIZE_FIELDS if crown_field else SIZE_FIELDS
    records = data.to_dict("records") if hasattr(data, "to_dict") and hasattr(data, "columns") else None
    geoms = list(data.geometry.values) if records is not None else [g for g, *_ in data]
    props = records if records is not None else [next((r for r in rest if isinstance(r, dict)), {}) for _, *rest in data]
    zones, trench = [], []
    for g, pr in zip(geoms, props):
        lower = {str(k).lower(): v for k, v in pr.items()}
        columnar = bool(columnar_field and lower.get(columnar_field.lower()))
        add = columnar_extra_m if columnar else extra_m
        if g.geom_type in ("Point", "MultiPoint"):
            d = _number(lower, fields)
            d = d if d == d and d > 0 else default_crown_m
            zones.append(g.buffer(d / 2.0 + add, 32))
        else:
            zones.append(g.buffer(add, 16))
        girth = _number(lower, GIRTH_FIELDS)
        if girth != girth:
            stem = _number(lower, STEM_FIELDS)
            girth = stem * 100.0 * math.pi if stem == stem else float("nan")
        trench.append(max(4 * girth / 100.0, 2.5) if girth == girth else None)
    if records is not None:
        import geopandas as gpd

        out = gpd.GeoDataFrame(data.drop(columns=data.geometry.name).copy(), geometry=zones, crs=data.crs)
        out["element"] = "root_protection_zone"
        out["min_trench_distance_m"] = trench
        return out
    return zones

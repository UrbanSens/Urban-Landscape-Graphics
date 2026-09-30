"""Integrity of the element catalog, the palette and the themes."""

import re

import pytest

import ulg
from ulg import check
from ulg.catalog import themes

CAT = ulg.load()
HEX = re.compile(r"^#[0-9A-F]{6}$")
GEOMETRIES = {"polygon", "line", "point"}
LAYERS = {"ground", "roof", "overlay"}
SEALING = {"sealed", "partly", "unsealed", "built"}


def test_catalog_size_and_unique_ids():
    ids = CAT.ids()
    assert len(ids) == len(set(ids)) >= 150


@pytest.mark.parametrize("el", list(CAT), ids=lambda e: e.id)
def test_element_is_complete(el):
    assert re.match(r"^[a-z][a-z0-9_]*$", el.id)
    assert el.label.get("en") and el.label.get("de"), "needs English and German names"
    assert set(el.geometry) <= GEOMETRIES and el.geometry
    for c in (el.fill, el.outline, el.ink):
        assert c is None or HEX.match(c), c
    if "point" in el.geometry and el.geometry[0] == "point":
        assert el.symbol, "point elements need a symbol"
    a = el.attributes
    assert a.get("layer", "ground") in LAYERS
    assert a.get("sealing") in SEALING | {None}
    for k in ("bff", "bff_1990", "runoff_cs", "runoff_cm", "albedo", "emissivity"):
        if k in a:
            assert 0.0 <= a[k] <= 1.0, (k, a[k])
    if "runoff_cs" in a:
        assert a["runoff_cs"] >= a.get("runoff_cm", 0), "peak coefficient is never below the mean"


def test_every_element_has_a_description():
    missing = [el.id for el in CAT if not el.description.get("en") or not el.description.get("de")]
    assert not missing, missing


def test_palette_values_are_hex():
    for token, value in CAT.palette.flat().items():
        assert HEX.match(value), (token, value)


def test_search_finds_german_and_english_names():
    assert ulg.find("Rasengitter")[0].id == "grass_pavers"
    assert ulg.find("wildflower meadow")[0].id == "wildflower_meadow"
    assert ulg.find("Streuobstwiese")[0].id == "orchard_meadow"
    with pytest.raises(ulg.CatalogError, match="did you mean"):
        ulg.element("lawns")


def test_legibility_report_is_clean():
    rep = check.report(CAT)
    assert rep["ok"], check.format_report(rep)


@pytest.mark.parametrize("name", sorted(themes()))
def test_themes_load_and_resolve(name):
    cat = ulg.load(name)
    assert len(cat) == len(CAT)
    assert cat.theme.get("title")
    for el in cat:
        for c in (el.fill, el.outline):
            assert c is None or HEX.match(c), (name, el.id, c)
    if name != "mellow":
        assert cat.theme.get("source"), "official themes must cite their source"


def test_official_theme_values():
    assert ulg.load("alkis")["woodland"].fill == "#CFE8D9"
    assert ulg.load("planzv")["water"].fill == "#99D9E8"
    assert ulg.load("basemap")["cemetery"].fill == "#DFF0B6"
    assert ulg.load("osm")["green_space"].fill == "#C8FACC"
    assert ulg.load("mono")["meadow"].textures, "the drawing theme keeps the textures"
    assert not ulg.load("alkis")["meadow"].textures, "official themes are flat"


def test_categories_and_ramps():
    assert ulg.category_of("utci", 26.0)["id"] == "moderate_heat"
    assert ulg.category_of("utci", 25.9)["id"] == "no_stress"
    assert ulg.category_of("pet", 41.0)["id"] == "extreme_heat"
    assert len(ulg.categories("klimatop")) == 11
    assert len(ulg.ramp("heat", 9)) == 9

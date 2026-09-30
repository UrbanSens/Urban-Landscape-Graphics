"""Exporters write complete, well-formed files."""

import json
import xml.dom.minidom as minidom

import pytest

import ulg
from ulg.export import qgis, sld, tokens, web


def test_qgis_files(tmp_path):
    files = qgis.export_qgis(tmp_path, lod=2)
    names = {f.name for f in files}
    assert {"ulg_polygons.qml", "ulg_lines.qml", "ulg_points.qml", "ulg_style_library.xml", "ulg_palette.gpl"} <= names
    for f in files:
        if f.suffix in (".qml", ".xml"):
            doc = minidom.parse(str(f))
            assert doc.documentElement.tagName in ("qgis", "qgis_style")
    poly = (tmp_path / "ulg_polygons.qml").read_text()
    assert 'class="SVGFill"' in poly and "base64:" in poly and "wave_randomized" in poly
    assert (tmp_path / "ulg_palette.gpl").read_text().startswith("GIMP Palette")


def test_qgis_rule_based_lod(tmp_path):
    f = qgis.layer_style(tmp_path / "auto.qml", "polygon", lod="auto")
    xml = f.read_text()
    assert 'type="RuleRenderer"' in xml and "scalemaxdenom" in xml


def test_sld_files(tmp_path):
    files = sld.export_sld(tmp_path)
    for f in files:
        minidom.parse(str(f))
    assert list((tmp_path / "patterns").glob("*.svg"))
    assert list((tmp_path / "symbols").glob("*.svg"))


def test_tokens(tmp_path):
    css = tokens.css(tmp_path / "ulg.css")
    assert "--ulg-lawn-fill" in css and "--ulg-grass-300" in css
    d = tokens.dtcg(tmp_path / "ulg.tokens.json")
    assert d["element"]["lawn"]["fill"]["$value"].startswith("{palette.")
    cat = tokens.catalog_json(tmp_path / "catalog.json")
    assert len(cat["elements"]) == len(ulg.load())


def test_maplibre_layers_reference_sprite_names():
    layers = web.maplibre_layers()
    ids = [l["id"] for l in layers]
    assert "ulg-fill" in ids and "ulg-pattern" in ids and "ulg-trees" in ids
    json.dumps(layers)


@pytest.mark.slow
def test_web_export_with_sprite(tmp_path):
    files = web.export_web(tmp_path)
    idx = json.loads((tmp_path / "ulg-sprite@2x.json").read_text())
    assert any(k.startswith("ulg-icon-") for k in idx)
    assert all(v["pixelRatio"] == 2 for v in idx.values())
    minidom.parse(str(tmp_path / "patterns.svg"))


def test_qgis_lines_style_draws_centre_lines_as_strips(tmp_path):
    from ulg.export.qgis import layer_style

    qml = layer_style(tmp_path / "lines.qml", "line").read_text()
    assert "value=\"road\"" in qml and "buffer($geometry" in qml
    assert "CASE attribute(" not in qml          # QGIS only knows the searched CASE WHEN ... form


def test_maplibre_line_layer_skips_centre_line_strips():
    from ulg.export.web import maplibre_layers

    layers = {l["id"]: l for l in maplibre_layers()}
    listed = layers["ulg-lines"]["filter"][2][2][1]
    assert "hedge" in listed and "road" not in listed          # roads are drawn by the strip layers
    assert "road" in layers["ulg-strips"]["filter"][2][2][1]


def test_maplibre_crowns_read_osm_diameter_and_fall_back_to_default():
    import json

    from ulg.export.web import maplibre_layers

    crowns = next(l for l in maplibre_layers() if l["id"] == "ulg-crowns")
    text = json.dumps(crowns["layout"]["icon-size"])
    assert '"has", "diameter_crown"' in text and '"has", "crown_diameter"' in text

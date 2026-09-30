"""The UrbanSens credit: the logo, the credit line and the small mark on the library's own sheets."""

import struct
import xml.dom.minidom as minidom

import pytest
from shapely.geometry import box

import ulg
from ulg import brand
from ulg.render.svg import Svg, rasterize


def test_credit_line_names_the_style_the_version_and_the_website():
    assert ulg.credit_line() == f"Style: UrbanSens Ecological Vector Style (ulg {ulg.__version__}) · urbansens.de"
    assert ulg.credit_line("de", version=False) == "Kartenstil: UrbanSens Ecological Vector Style (ulg) · urbansens.de"
    assert brand.WEBSITE == "https://urbansens.de/"


def test_logo_ships_with_the_package():
    data = brand.logo_png()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    w, h = brand.logo_size()
    assert (w, h) == struct.unpack(">II", data[16:24]) and w > h > 100
    assert brand.logo_data_uri().startswith("data:image/png;base64,")


def test_draw_credit_adds_the_logo_a_text_and_a_valid_namespace():
    page = Svg(100, 50)
    x0, y0, x1, y1 = brand.draw_credit(page, 98, 48, height=9.0)
    xml = page.tostring()
    minidom.parseString(xml)                                   # well-formed, xlink prefix declared
    assert 'xmlns:xlink="http://www.w3.org/1999/xlink"' in xml and "<image " in xml and "urbansens.de" in xml
    assert x1 == pytest.approx(98) and y1 == pytest.approx(48) and y0 == pytest.approx(39) and x0 < 98 - 9


def test_draw_credit_variants():
    small = Svg(100, 50)
    brand.draw_credit(small, 98, 48, height=5.0)               # too small to read text: the logo alone
    assert "<image " in small.tostring() and "urbansens.de" not in small.tostring()
    left = Svg(100, 50)
    assert brand.draw_credit(left, 2, 48, height=9.0, align="left")[0] == pytest.approx(2)
    plated = Svg(100, 50)
    box_ = brand.draw_credit(plated, 98, 48, height=9.0, text=False, plate="#F5F5F1")
    assert "<rect" in plated.tostring() and box_[2] > 98       # the plate reaches beyond the logo


def test_pages_without_pictures_do_not_declare_xlink():
    page = Svg(10, 10)
    page.rect(0, 0, 5, 5, fill="#ffffff")
    assert "xmlns:xlink" not in page.tostring()


def test_style_sheet_carries_the_credit_and_can_do_without():
    with_credit = ulg.style_sheet().tostring()
    assert "<image " in with_credit and "urbansens.de" in with_credit and "generated from the catalog" in with_credit
    without = ulg.style_sheet(credit=False).tostring()
    assert "<image " not in without and "urbansens.de" not in without and "generated from the catalog" in without
    assert "aus dem Katalog erzeugt" in ulg.style_sheet(lang="de").tostring()


def test_catalog_sheet_gets_a_footer_for_the_credit():
    a, b = ulg.catalog_sheet(groups=["trees"]), ulg.catalog_sheet(groups=["trees"], credit=False)
    assert "<image " in a.tostring() and "<image " not in b.tostring()
    assert a.height > b.height


def test_legends_are_not_stamped_unless_asked():
    assert "<image " not in ulg.legend_svg(["lawn", "tree"]).tostring()
    stamped = ulg.legend_svg(["lawn", "tree"], credit=True)
    assert "<image " in stamped.tostring() and stamped.height > ulg.legend_svg(["lawn", "tree"]).height


def test_maps_are_never_stamped():
    svg = ulg.render_svg([(box(0, 0, 50, 30), "lawn")], scale=500).tostring()
    assert "<image " not in svg and "urbansens.de" not in svg


def test_sheet_command_can_leave_the_credit_off(tmp_path):
    from ulg import cli

    parser = cli.build_parser()
    assert parser.parse_args(["sheet", "--no-credit"]).no_credit is True
    assert parser.parse_args(["sheet"]).no_credit is False
    target = tmp_path / "s.svg"
    assert cli.main(["sheet", "--catalog", "-o", str(target), "--no-credit"]) == 0
    assert "<image " not in target.read_text(encoding="utf-8")


def test_the_credit_survives_rasterising(tmp_path):
    pil = pytest.importorskip("PIL.Image")
    page = Svg(60, 30, background="#ffffff")
    brand.draw_credit(page, 58, 28, height=14.0, text=False)
    src = page.save(tmp_path / "c.svg")
    try:
        png = rasterize(src, tmp_path / "c.png", dpi=100)
    except RuntimeError:
        pytest.skip("no SVG rasteriser installed")
    im = pil.open(png).convert("L")
    w, h = im.size
    logo_region = im.crop((w // 2, h // 3, w, h))
    assert logo_region.getextrema()[0] < 190                   # the logo is there, not a white box


def test_german_catalog_sheet_has_german_group_headings_and_counts():
    from ulg.sheet import GROUPS_DE, group_title

    cat = ulg.load()
    assert set(cat.groups()) <= set(GROUPS_DE), "every catalog group needs a German heading in ulg.sheet.GROUPS_DE"
    assert group_title("surface.paved", "en") == "surface · paved" and group_title("surface.paved", "de") == "Oberflächen · gepflastert"
    text = ulg.catalog_sheet(groups=["trees"], lang="de").tostring()
    assert "BÄUME" in text and "Elemente · ulg" in text and "elements" not in text

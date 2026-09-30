"""The HTML documentation builds from the Markdown in both languages, and every link in it works."""

import importlib.util
import re
import sys
from pathlib import Path

import pytest

pytest.importorskip("markdown_it")
pytestmark = pytest.mark.slow

ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    spec = importlib.util.spec_from_file_location("build_html", ROOT / "tools" / "build_html.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["build_html"] = module  # dataclasses look their module up here
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    module = load_builder()
    out = tmp_path_factory.mktemp("docs") / "html"
    builder = module.Builder(out)
    problems = builder.build()
    return module, builder, out, problems


def read(out: Path, name: str) -> str:
    return (out / name).read_text(encoding="utf-8")


def test_no_broken_links_anchors_or_duplicate_ids(built):
    *_, problems = built
    assert not problems, "\n".join(problems[:30])


def repo_markdown():
    files = [ROOT / "README.md", ROOT / "README.en.md", ROOT / "CHANGELOG.md", ROOT / "AGENTS.md"]
    return files + [f for f in (ROOT / "docs").rglob("*.md") if ROOT / "docs" / "html" not in f.parents]


def test_every_markdown_page_is_published_in_both_languages(built):
    module, builder, out, _ = built
    sources = {p.src.resolve() for p in builder.pages}
    for md in repo_markdown():
        assert md.resolve() in sources, f"{md.relative_to(ROOT)} has no page"
    for page in builder.pages:
        assert (out / page.out).is_file(), page.out
    german, english = builder.trees["de"], builder.trees["en"]
    assert {p.key for p in german} == {p.key for p in english}     # the two trees have the same pages
    assert all(p.out.startswith("en/") for p in english) and not any(p.out.startswith("en/") for p in german)


def test_german_is_the_default_and_english_lives_under_en(built):
    _, _, out, _ = built
    assert read(out, "index.html").startswith('<!doctype html>\n<html lang="de"')
    assert read(out, "en/index.html").startswith('<!doctype html>\n<html lang="en"')
    assert (out / "ulg-dokumentation.html").is_file() and (out / "en" / "ulg-documentation.html").is_file()


def test_the_language_switch_pairs_the_pages(built):
    _, _, out, _ = built
    de, en = read(out, "02-style.html"), read(out, "en/02-style.html")
    assert re.search(r'<a href="en/02-style\.html" hreflang="en" lang="en"', de)
    assert re.search(r'<a href="\.\./02-style\.html" hreflang="de" lang="de"', en)
    assert 'hreflang="x-default" href="https://urbansens.github.io/Urban-Landscape-Graphics/02-style.html"' in de.replace(
        '<link rel="alternate" ', "") or 'rel="alternate" hreflang="x-default"' in de
    assert '<span class="on"' in de and 'rel="canonical" href="https://urbansens.github.io/Urban-Landscape-Graphics/en/02-style.html"' in en


def test_site_pages_have_banner_navigation_and_next_band(built):
    _, _, out, _ = built
    for name, nxt in (("01-origins.html", "02-style.html"), ("en/01-origins.html", "02-style.html")):
        text = read(out, name)
        assert 'class="sidebar"' in text and 'class="next-band"' in text and 'class="site-footer"' in text
        assert "Next: [" not in text and ">Next: <" not in text and "Weiter: [" not in text   # the pager line became the next band
        assert f'href="{nxt}"' in text
    assert read(out, "assets/style.css").count("--ulg-grass-300") >= 1   # palette tokens


def test_title_moves_into_the_banner(built):
    _, _, out, _ = built
    de = read(out, "01-origins.html")
    hero, article = de.split('<main id="content">')
    assert '<h1 id="1--herkunft">Herkunft</h1>' in hero and "Leitfaden · Kapitel 1 von 8" in hero
    assert "<h1" not in article                                   # one h1 per page, in the banner
    assert "background-image:url('img/banners/origins.jpg')" in hero
    en = read(out, "en/01-origins.html")
    hero_en, article_en = en.split('<main id="content">')
    assert '<h1 id="1--origins">Origins</h1>' in hero_en and "Guide · Chapter 1 of 8" in hero_en
    assert "<h1" not in article_en and "background-image:url('../img/banners/origins.jpg')" in hero_en
    assert (out / "img" / "banners" / "origins.jpg").is_file()
    for name, root in (("index.html", "assets/"), ("en/index.html", "../assets/")):
        home = read(out, name)
        assert 'class="hero home"' in home and "hero-cta" in home and f"{root}logo/ulg-mark.svg" in home


def test_quotations_carry_their_source(built):
    _, _, out, _ = built
    for name in ("01-origins.html", "en/01-origins.html"):
        text = read(out, name).replace("\u00a0", " ")          # the German text uses no-break spaces after § and Abs.
        assert '<blockquote class="quote">' in text and '<p class="cite">' in text
        assert "Planzeichenverordnung 1990, § 2 Abs. 3" in text
    assert "Source:" not in read(out, "01-origins.html").split('<main id="content">')[1].replace("Source: end of", "")


def test_brand_assets_are_bundled(built):
    _, _, out, _ = built
    css = read(out, "assets/style.css")
    assert "data:font/woff2;base64," in css and "{{RETHINK_SANS}}" not in css     # the font needs no download
    for name in ("ulg-mark.svg", "ulg-mark-small.svg", "ulg-favicon.svg", "favicon.ico", "apple-touch-icon.png"):
        assert (out / "assets" / "logo" / name).is_file(), name
    assert chr(0x2014) not in css                                   # the quotation rule is drawn, not typed


def test_big_figures_are_served_as_webp(built):
    _, _, out, _ = built
    assert (out / "img" / "hero.webp").is_file() and not (out / "img" / "hero.png").exists()
    assert (out / "img" / "hero-de.webp").is_file() and (out / "img" / "hero-de.webp").stat().st_size < 1_000_000


@pytest.mark.parametrize("name, prefix", [("ulg-dokumentation.html", ""), ("en/ulg-documentation.html", "en/")])
def test_single_file_is_self_contained(built, name, prefix):
    _, _, out, _ = built
    text = read(out, name)
    assert 'id="04-python"' in text and re.search(r'id="04-python--41-[a-z-]+"', text)
    local_images = re.findall(r'<img[^>]+src="(?!data:|https?:)([^"]+)"', text)
    assert not local_images, local_images[:5]                    # every figure is embedded
    assert "url('img/" not in text and "assets/logo" not in text   # banners and logos are embedded as well
    assert (out / name).stat().st_size < 15_000_000


def test_search_index_per_language(built):
    _, _, out, _ = built
    de, en = read(out, "assets/search-index.de.js"), read(out, "assets/search-index.en.js")
    assert de.startswith("window.ULG_INDEX=") and en.startswith("window.ULG_INDEX=")
    assert "render_svg" in de and "flatten" in de and "render_svg" in en
    assert "Wiederherstellung" in de and "Nature Restoration" in en


def test_github_style_heading_ids(built):
    module, *_ = built
    assert module.slugify("4.1 Install") == "41-install"
    assert module.slugify("5.4 What to re-check when standards change") == "54-what-to-re-check-when-standards-change"
    assert module.slugify("2.7 Drawing order") == "27-drawing-order"
    assert module.slugify("2.7 Zeichenreihenfolge") == "27-zeichenreihenfolge"      # umlauts and ß stay in German anchors
    assert module.slugify("3.2 Größe und Höhe (Bäume)") == "32-größe-und-höhe-bäume"

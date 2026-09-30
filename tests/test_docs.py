"""The HTML documentation builds from the Markdown, and every link in it works."""

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


def test_no_broken_links_anchors_or_duplicate_ids(built):
    *_, problems = built
    assert not problems, "\n".join(problems[:30])


def repo_markdown():
    files = [ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "AGENTS.md"]
    return files + [f for f in (ROOT / "docs").rglob("*.md") if ROOT / "docs" / "html" not in f.parents]


def test_every_markdown_page_is_published(built):
    _, builder, out, _ = built
    sources = {p.src.resolve() for p in builder.pages}
    for md in repo_markdown():
        assert md.resolve() in sources, f"{md.relative_to(ROOT)} has no page"
    for page in builder.pages:
        assert (out / page.out).is_file(), page.out


def test_site_pages_have_banner_navigation_and_next_band(built):
    _, _, out, _ = built
    text = (out / "01-origins.html").read_text(encoding="utf-8")
    assert 'class="sidebar"' in text and 'class="next-band"' in text and 'class="site-footer"' in text
    assert "Next: [" not in text and ">Next: <" not in text      # the Markdown 'Next:' line became the next band
    assert 'href="02-style.html"' in text
    assert (out / "assets" / "style.css").read_text().count("--ulg-grass-300") >= 1   # palette tokens


def test_title_moves_into_the_banner(built):
    _, _, out, _ = built
    text = (out / "01-origins.html").read_text(encoding="utf-8")
    hero, article = text.split('<main id="content">')
    assert '<h1 id="1--origins">Origins</h1>' in hero and "Guide · Chapter 1 of 8" in hero
    assert "<h1" not in article                                   # one h1 per page, in the banner
    assert "background-image:url('img/banners/origins.jpg')" in hero
    assert (out / "img" / "banners" / "origins.jpg").is_file()
    home = (out / "index.html").read_text(encoding="utf-8")
    assert 'class="hero home"' in home and "hero-cta" in home and "assets/logo/ulg-mark.svg" in home


def test_quotations_carry_their_source(built):
    _, _, out, _ = built
    text = (out / "01-origins.html").read_text(encoding="utf-8")
    assert '<blockquote class="quote">' in text and '<p class="cite">' in text
    assert "Planzeichenverordnung 1990, § 2 Abs. 3" in text


def test_brand_assets_are_bundled(built):
    _, _, out, _ = built
    css = (out / "assets" / "style.css").read_text(encoding="utf-8")
    assert "data:font/woff2;base64," in css and "{{RETHINK_SANS}}" not in css     # the font needs no download
    for name in ("ulg-mark.svg", "ulg-mark-small.svg", "ulg-favicon.svg", "favicon.ico", "apple-touch-icon.png"):
        assert (out / "assets" / "logo" / name).is_file(), name


def test_big_figures_are_served_as_webp(built):
    _, _, out, _ = built
    assert (out / "img" / "hero.webp").is_file() and not (out / "img" / "hero.png").exists()
    assert (out / "img" / "hero.webp").stat().st_size < 1_000_000


def test_single_file_is_self_contained(built):
    _, _, out, _ = built
    text = (out / "ulg-documentation.html").read_text(encoding="utf-8")
    assert re.search(r'id="04-python"', text) and 'id="04-python--41-install"' in text
    local_images = re.findall(r'<img[^>]+src="(?!data:|https?:)([^"]+)"', text)
    assert not local_images, local_images[:5]                    # every figure is embedded
    assert "url('img/" not in text and "assets/logo" not in text   # banners and logos are embedded as well
    assert (out / "ulg-documentation.html").stat().st_size < 15_000_000


def test_search_index_finds_the_guide(built):
    _, _, out, _ = built
    index = (out / "assets" / "search-index.js").read_text(encoding="utf-8")
    assert index.startswith("window.ULG_INDEX=") and "render_svg" in index and "flatten" in index


def test_github_style_heading_ids(built):
    module, *_ = built
    assert module.slugify("4.1 Install") == "41-install"
    assert module.slugify("5.4 What to re-check when standards change") == "54-what-to-re-check-when-standards-change"
    assert module.slugify("2.7 Drawing order") == "27-drawing-order"

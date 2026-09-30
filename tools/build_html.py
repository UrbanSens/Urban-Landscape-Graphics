"""Build the documentation as HTML.

    python tools/build_html.py               # site + single file in docs/html/
    python tools/build_html.py --site-only   # only the multi-page site
    python tools/build_html.py --single-only # only docs/html/ulg-documentation.html
    python tools/build_html.py --out DIR     # another output folder

Two forms of the same content, both generated from the Markdown in the repository:

* a **site** (``docs/html/index.html``): one page per chapter with sidebar navigation, search that works
  from ``file://``, light and dark mode, zoomable figures, copy buttons on code, previous/next links;
* a **single file** (``docs/html/ulg-documentation.html``): the guide, reference, standards report and
  examples in one page with the figures embedded (WebP), to send by e-mail or read offline.

The look comes from the library itself: colours are the palette tokens, the logo (``tools/build_logo.py``) is
drawn with catalog elements, the banners are crops of the demo map (``tools/build_docs.py banners``). The layout is
editorial: a banner with the title, a narrow serif column, bold sans headings, numbered figure captions and
quotations with their source; headings are set in Rethink Sans (SIL OFL, bundled in ``tools/html/fonts``).
Historical photographs are linked from Wikimedia Commons (they need a connection).

Needs ``markdown-it-py`` with its ``linkify`` extra; ``pygments`` (code highlighting) and ``pillow`` (WebP for
the figures) are optional:  pip install 'markdown-it-py[linkify]' pygments pillow      (or: pip install -e ".[docs]")
"""

from __future__ import annotations

import argparse
import ast
import base64
import functools
import html
import io
import mimetypes
import os
import re
import shutil
import struct
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

try:
    from markdown_it import MarkdownIt
except ImportError:  # pragma: no cover
    raise SystemExit("tools/build_html.py needs markdown-it-py:  pip install 'markdown-it-py[linkify]' pygments pillow")
try:
    import pygments
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import get_lexer_by_name
except ImportError:  # pragma: no cover - highlighting is optional
    pygments = None
try:
    from PIL import Image
except ImportError:  # pragma: no cover - only needed to shrink the single file
    Image = None

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "html"
ASSETS = Path(__file__).resolve().parent / "html"
sys.path.insert(0, str(ROOT / "src"))

SINGLE_NAME = "ulg-documentation.html"
MARKER = ".ulg-html-docs"
GROUPS = ["Home", "Guide", "Reference", "Research", "Project", "More"]
#: banner image (docs/img/banners/<name>.jpg) of a page: by key, else by group
BANNER_BY_KEY = {"home": "home", "contents": "home", "01-origins": "origins", "02-style": "style", "03-catalog": "catalog",
                 "04-python": "python", "05-gis-and-web": "gis", "06-standards": "standards", "07-agents": "agents",
                 "08-extending": "extending"}
BANNER_BY_GROUP = {"Home": "home", "Guide": "style", "Reference": "catalog", "Research": "research",
                   "Project": "project", "More": "project"}
TOP_LINKS = [("Guide", "01-origins"), ("Reference", "ref-element-list"), ("Research", "report"), ("Project", "examples")]
WEBP_OVER = 120_000        # PNG figures above this size (bytes) are served as WebP
WEBP_QUALITY = 86
LOGO_FILES = ["ulg-mark.svg", "ulg-mark-small.svg", "ulg-favicon.svg", "favicon.ico", "apple-touch-icon.png"]
BRAND_FILES = ["urbansens-logo.png"]          # docs/img/brand: the UrbanSens logo, as supplied
REPO_URL = "https://github.com/UrbanSens/Urban-Landscape-Graphics"
SITE_URL = "https://urbansens.github.io/Urban-Landscape-Graphics/"     # where .github/workflows/pages.yml publishes the site
#: The stripes of the UrbanSens logo from left to right: the mean colour of 48 columns of its skyline
#: (docs/img/brand/urbansens-logo.png). They draw the thin line on top of the pages and above the footer.
UB_STRIPES = ["#acc7d4", "#87adc4", "#acc7d5", "#8fa9b9", "#74a4c3", "#b6cbd8", "#a1b6c6", "#90aebe", "#7a99ac", "#94bbd1",
              "#a3c2d6", "#78a8c6", "#e8d4cc", "#e2bcac", "#e7b4a4", "#e79683", "#e7c0b0", "#e78e7b", "#df7269", "#e49683",
              "#dc746a", "#e18978", "#b1575b", "#b4575b", "#be5a5d", "#af565a", "#e18172", "#df7269", "#e6a08c", "#df7269",
              "#e78e7b", "#e7b8a7", "#e7917e", "#e7c8bd", "#e7c0b0", "#e6c1b2", "#80acc9", "#96bbd2", "#91b9d0", "#90aec1",
              "#a5becb", "#85a6bd", "#acc6d4", "#7aa8c5", "#8bb2c9", "#adc7d5", "#85aec6", "#abc5d2"]
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)

THEME_BOOT = ('<script>try{var q=/[?&]theme=(light|dark)\\b/.exec(location.search),'
              't=q?q[1]:localStorage.getItem("ulg-theme");'
              'if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>')
MENU_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
            '<path d="M4 7h16M4 12h16M4 17h16"/></svg>')
THEME_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 1 0 16z" '
             'fill="currentColor"/></svg>')

STREAM_LABELS = {
    "01": "Planning law and cadastre", "02": "Biotopes and landscape planning", "03": "European classifications",
    "04": "OSM and national models", "05": "Open-space typologies", "06": "Coefficients and drawing standards",
    "07": "Rendering and interoperability",
}
SOURCE_LANG = {".py": "python", ".html": "html", ".js": "js", ".css": "css", ".json": "json", ".sh": "bash",
               ".md": "markdown", ".toml": "toml", ".txt": "text"}


# --------------------------------------------------------------------------- pages

@dataclass
class Page:
    key: str
    out: str                          # path of the html file relative to the site root
    group: str
    src: Path                         # source file; for synthetic pages the path they pretend to have
    label: str = ""
    number: str = ""
    text: str | None = None           # markdown; None reads src
    parent: str | None = None         # key of the page this one is nested under in the navigation
    raw_html: bool = False            # hand-written page: raw HTML passes through
    wide: bool = False
    single: bool = True               # part of the single-file version
    full_text: bool = True            # full text in the search index (else headings only)
    title: str = ""
    desc: str = ""
    body: str = ""
    hero_title: str = ""              # html of the h1, shown in the banner
    h1_id: str = ""
    lede: str = ""                    # html of the italic line under the h1 (Home: the first paragraph)
    read_min: int = 0
    headings: list = field(default_factory=list)   # (level, id, text)
    sections: list = field(default_factory=list)   # (level, id, title, text)

    @property
    def rel(self) -> str:
        try:
            return self.src.relative_to(ROOT).as_posix()
        except ValueError:
            return self.src.as_posix()


def collect_pages() -> list[Page]:
    pages: list[Page] = []

    def add(**kw) -> Page:
        p = Page(**kw)
        pages.append(p)
        return p

    add(key="home", out="index.html", group="Home", src=ROOT / "README.md", label="Overview", raw_html=True)
    add(key="contents", out="contents.html", group="Home", src=DOCS / "index.md", label="Contents", raw_html=True,
        single=False)
    for f in sorted(DOCS.glob("[0-9][0-9]-*.md")):
        add(key=f.stem, out=f"{f.stem}.html", group="Guide", src=f, number=str(int(f.name[:2])), raw_html=True)
    for stem, label in (("element-list", "Element list"), ("attributes", "Attributes"), ("crosswalks", "Crosswalks"),
                        ("themes", "Themes"), ("crosswalk-format", "Crosswalk format"), ("api", "API")):
        add(key=f"ref-{stem}", out=f"reference/{stem}.html", group="Reference", src=DOCS / "reference" / f"{stem}.md",
            label=label, wide=stem != "crosswalk-format", raw_html=stem == "crosswalk-format")
    add(key="report", out="research/standards-report.html", group="Research",
        src=DOCS / "research" / "standards-report.md", label="Standards report", wide=True)
    streams = DOCS / "research" / "streams"
    add(key="streams", out="research/streams/index.html", group="Research", src=streams / "README.md",
        label="Research streams", single=False, text="")
    for f in sorted(streams.glob("[0-9][0-9]_*.md")):
        n = f.name[:2]
        add(key=f"stream-{n}", out=f"research/streams/{f.stem}.html", group="Research", src=f, number=n,
            label=STREAM_LABELS.get(n, f.stem), parent="streams", single=False, full_text=False)
    for f in sorted((streams / "notes").glob("*.md")):
        n = f.name[:2]
        add(key=f"notes-{n}", out=f"research/streams/notes/{f.stem}.html", group="Research", src=f,
            label=f"Working notes {n}", parent="streams", single=False, full_text=False)

    ex = ROOT / "examples"
    add(key="examples", out="examples/index.html", group="Project", src=ex / "README.md", label="Examples",
        raw_html=True)
    for name in ("quickstart.py", "osm_workflow.py", "indicators.py", "qgis_project.py", "themes.py"):
        add(key=f"src-{name}", out=f"examples/{name}.html", group="Project", src=ex / name, label=name,
            parent="examples")
    add(key="src-web", out="examples/web/index.html", group="Project", src=ex / "web" / "README.md",
        label="web/", parent="examples", text="")
    add(key="src-web-build", out="examples/web/build.py.html", group="Project", src=ex / "web" / "build.py",
        label="web/build.py", parent="examples")
    add(key="src-web-index", out="examples/web/index.html.html", group="Project", src=ex / "web" / "index.html",
        label="web/index.html", parent="examples")
    add(key="src-data", out="examples/data/make_osm_sample.py.html", group="Project",
        src=ex / "data" / "make_osm_sample.py", label="data/make_osm_sample.py", parent="examples")
    add(key="changelog", out="changelog.html", group="Project", src=ROOT / "CHANGELOG.md", label="Changelog",
        raw_html=True)
    add(key="contributing", out="contributing.html", group="Project", src=ROOT / "AGENTS.md", label="Working on ulg",
        raw_html=True)

    known = {p.src.resolve() for p in pages}
    for f in sorted(DOCS.rglob("*.md")):
        if f.resolve() not in known and OUT not in f.parents:
            key = "more-" + re.sub(r"[^a-z0-9]+", "-", f.relative_to(DOCS).with_suffix("").as_posix().lower())
            add(key=key, out=f.relative_to(DOCS).with_suffix(".html").as_posix(), group="More", src=f,
                label=f.stem)
    return pages


# --------------------------------------------------------------------------- markdown

def make_parser(raw_html: bool) -> MarkdownIt:
    md = MarkdownIt("gfm-like", {"html": raw_html, "linkify": True, "typographer": False})
    if getattr(md, "linkify", None) is not None:  # link only what has a scheme: README.md or run.py are no domains
        md.linkify.set({"fuzzy_link": False, "fuzzy_email": False, "fuzzy_ip": False})
    else:  # linkify-it-py is not installed: plain URLs stay plain text
        md.options["linkify"] = False
    md.options["highlight"] = highlight
    return md


def highlight(code: str, lang: str, attrs) -> str:
    lang = (lang or "").strip().lower()
    body = None
    if pygments is not None and lang and lang != "text":
        try:
            body = pygments.highlight(code, get_lexer_by_name(lang), HtmlFormatter(nowrap=True))
        except Exception:  # unknown language
            body = None
    cls = f' class="language-{html.escape(lang)}"' if lang else ""
    return f'<pre class="hl"><code{cls}>{body if body is not None else html.escape(code)}</code></pre>'


def slugify(text: str) -> str:
    """GitHub's heading anchors: lower case, punctuation removed, spaces become hyphens."""
    return re.sub(r"[^\w\- ]", "", text.strip().lower()).replace(" ", "-")


def inline_text(tok) -> str:
    out = []
    for c in tok.children or []:
        if c.type in ("text", "code_inline"):
            out.append(c.content)
        elif c.type in ("softbreak", "hardbreak"):
            out.append(" ")
        elif c.type == "image":
            out.append(c.content)
    return "".join(out)


def strip_pager(text: str) -> str:
    """The closing 'Next: ...' line of a chapter: the pages get real previous/next buttons instead."""
    return re.sub(r"\n---[ \t]*\n+(?:Next:|Back to)[^\n]*\n*\Z", "\n", text)


def longest_run(text: str, ch: str = "`") -> int:
    return max((len(m) for m in re.findall(re.escape(ch) + "+", text)), default=0)


def plain(fragment: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def rel_url(target: str, source: str) -> str:
    """URL of site path ``target`` as seen from the page at site path ``source``."""
    return Path(os.path.relpath(target, os.path.dirname(source) or ".")).as_posix()


# --------------------------------------------------------------------------- the builder

@dataclass
class Target:
    kind: str                    # external | anchor | page | out | asset | missing
    url: str
    page: Page | None = None
    path: Path | None = None
    frag: str = ""


class Builder:
    def __init__(self, out: Path = OUT):
        self.out = out
        self.pages = collect_pages()
        self.by_key = {p.key: p for p in self.pages}
        assert len(self.by_key) == len(self.pages), "duplicate page keys"
        self.by_path: dict[Path, Page] = {p.src.resolve(): p for p in self.pages}
        ex = ROOT / "examples"
        self.by_path[ex.resolve()] = self.by_key["examples"]
        self.by_path[(ex / "web").resolve()] = self.by_key["src-web"]
        self.by_path[(DOCS / "research" / "streams").resolve()] = self.by_key["streams"]
        self.dir_alias = {(DOCS / "research" / "streams" / "notes").resolve(): (self.by_key["streams"], "working-notes")}
        self.assets: dict[Path, str] = {}
        self.problems: list[str] = []
        self._sizes: dict[Path, tuple[int, int] | None] = {}
        self._uris: dict[Path, str] = {}
        self._md = {True: make_parser(True), False: make_parser(False)}
        self.version = self._version()

    # ---- conversion -------------------------------------------------------------------------------

    @staticmethod
    def _version() -> str:
        import ulg
        return ulg.__version__

    def synthetic_text(self, p: Page) -> str:
        """Markdown of the pages that have no file of their own (indexes) or show a source file."""
        if p.key == "streams":
            rows = ["# Research streams", "",
                    "*Seven detailed research files written on 2026-09-30, the evidence behind the "
                    "[standards report](../standards-report.md). Every value is marked by how it was verified.*", "",
                    "| Stream | Title |", "|---|---|"]
            for q in self.pages:
                if q.parent == "streams" and q.key.startswith("stream-"):
                    title = q.src.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
                    rows.append(f"| [{q.number} · {q.label}]({q.src.name}) | {title.replace('|', '/')} |")
            rows += ["", "## Working notes", "",
                     "Page-image transcriptions and scratch tables behind streams 02 and 04.", ""]
            rows += [f"- [{q.label}](notes/{q.src.name})" for q in self.pages if q.key.startswith("notes-")]
            return "\n".join(rows) + "\n"
        if p.key == "src-web":
            return ("# examples/web\n\n*A complete MapLibre page: the demo quarter and an OpenStreetMap-style block, "
                    "drawn with the exported web style.*\n\n"
                    "| File | What it does |\n|---|---|\n"
                    "| [build.py](build.py) | writes the two GeoJSON files and runs `export_web` |\n"
                    "| [index.html](index.html) | the page; `?data=osm` switches to the OSM block |\n\n"
                    "Build and serve it from the repository root:\n\n"
                    "```bash\npython examples/web/build.py\n```\n\n"
                    "```bash\npython -m http.server 8765 --directory examples/web\n```\n\n"
                    "Then open <http://localhost:8765>.\n")
        if p.src.suffix != ".md":
            code = p.src.read_text(encoding="utf-8")
            lede = ""
            if p.src.suffix == ".py":
                doc = ast.get_docstring(ast.parse(code)) or ""
                lede = f"*{doc.split(chr(10) * 2)[0].replace(chr(10), ' ')}*\n\n" if doc else ""
            fence = "`" * max(3, longest_run(code) + 1)
            lang = SOURCE_LANG.get(p.src.suffix, "text")
            return f"# {p.rel}\n\n{lede}{fence}{lang}\n{code.rstrip()}\n{fence}\n"
        return p.src.read_text(encoding="utf-8")

    def convert(self, p: Page) -> None:
        text = p.text if p.text else self.synthetic_text(p)
        text = strip_pager(text)
        # The README serves GitHub and this site: what is between github-only markers is dropped here, and the
        # text of an HTML comment that starts with "site-only" is shown here (GitHub hides comments).
        text = re.sub(r"<!-- github-only:start -->.*?<!-- github-only:end -->[ \t]*\n?", "", text, flags=re.S)
        text = re.sub(r"<!-- site-only[ \t]*\n(.*?)-->[ \t]*\n?", r"\1", text, flags=re.S)
        if p.key == "home" and not re.search(r"^# ", text, flags=re.M):        # the README's title is its logo
            text = "# Urban Landscape Graphics\n\n" + text
        if not p.raw_html:
            text = re.sub(r"\A\s*<!--.*?-->\s*", "", text, flags=re.S)
        md = self._md[p.raw_html]
        env: dict = {}
        tokens = md.parse(text, env)
        seen: dict[str, int] = {}
        sections: list[list] = []
        for i, t in enumerate(tokens):
            if t.type == "heading_open":
                title = inline_text(tokens[i + 1])
                base = slugify(title) or "section"
                n = seen.get(base, 0)
                seen[base] = n + 1
                hid = base if n == 0 else f"{base}-{n}"
                t.attrSet("id", hid)
                p.headings.append((int(t.tag[1]), hid, title))
                if int(t.tag[1]) <= 3:
                    sections.append([int(t.tag[1]), hid, title, []])
            elif sections and t.type == "inline" and tokens[i - 1].type != "heading_open":
                sections[-1][3].append(inline_text(t))
            elif sections and t.type in ("fence", "code_block"):
                sections[-1][3].append(t.content)
            elif sections and t.type == "html_block":
                sections[-1][3].append(plain(t.content))
        p.sections = [(lv, hid, title, re.sub(r"\s+", " ", " ".join(parts)).strip()) for lv, hid, title, parts in sections]
        p.title = next((h[2] for h in p.headings if h[0] == 1), p.src.stem)
        if not p.label:
            p.label = re.sub(r"^\d+ · ", "", p.title)
        body = md.renderer.render(tokens, md.options, env)
        p.desc = next((t[:220] for t in (plain(m) for m in re.findall(r"<p>(.*?)</p>", body, re.S)) if len(t) >= 40), "")
        p.body = self.polish(body)
        self.extract_hero(p)

    @staticmethod
    def extract_hero(p: Page) -> None:
        """The h1 and the line under it move into the banner; the article starts with the first paragraph."""
        if p.key == "home":                                      # the logo above the README's title is in the banner already
            p.body = re.sub(r'\A\s*<p align="center">\s*<img\b[^>]*>\s*</p>\s*', "", p.body)
        m = re.match(r'\s*<h1(?: id="([^"]*)")?[^>]*>(.*?)</h1>\s*(?:<p class="lede">(.*?)</p>)?', p.body, re.S)
        if not m:
            return
        p.h1_id, title, p.lede = m.group(1) or "", m.group(2), m.group(3) or ""
        p.body = p.body[m.end():]
        if p.key == "home":                                      # the README's first paragraph is the subtitle
            title = re.sub(r"\s*\(<code>ulg</code>\)\s*$", "", title)
            lead = re.match(r"\s*<p>(.*?)</p>", p.body, re.S)
            if lead and not p.lede:
                p.lede, p.body = lead.group(1), p.body[lead.end():]
        p.hero_title = re.sub(r"^\s*\d+ · ", "", title)         # the chapter number goes to the eyebrow
        words = len(re.findall(r"\w+", plain(p.body)))
        p.read_min = max(1, round(words / 230)) if p.group in ("Home", "Guide") else 0

    @staticmethod
    def polish(h: str) -> str:
        """Link-independent clean-up of the rendered Markdown."""
        def table(m):
            block = m.group(0)
            if "<thead" in block:  # a data table; tables without a header row lay out figures
                return f'<div class="table-wrap">{block}</div>'
            layout = block.replace("<table>", '<table class="layout">', 1)
            return f'<div class="figs">{layout}</div>'

        def code(m):
            lang = re.search(r'language-([\w+#-]+)', m.group(0))
            label = lang.group(1) if lang and lang.group(1) != "text" else ""
            return f'<div class="codeblock" data-lang="{label}">{m.group(0)}</div>'

        def quote(m):
            inner = m.group(1)
            cite = re.search(r"<p>\s*(?:—|–|&mdash;|&ndash;)\s*(.*?)</p>\s*\Z", inner, re.S)
            if not cite:
                return m.group(0)
            return f'<blockquote class="quote">{inner[:cite.start()]}<p class="cite">{cite.group(1)}</p>\n</blockquote>'

        h = re.sub(r"<table>.*?</table>", table, h, flags=re.S)
        h = re.sub(r"<blockquote>(.*?)</blockquote>", quote, h, flags=re.S)
        h = re.sub(r"<pre\b.*?</pre>", code, h, flags=re.S)
        h = re.sub(r'<h([2-4]) id="([^"]+)">(.*?)</h\1>',
                   lambda m: f'<h{m[1]} id="{m[2]}">{m[3]}<a class="anchor" href="#{m[2]}" '
                             f'aria-label="Link to this section">#</a></h{m[1]}>', h, flags=re.S)
        h = re.sub(r"(<h1[^>]*>.*?</h1>\s*)<p><em>(.*?)</em></p>", r'\1<p class="lede">\2</p>', h, count=1, flags=re.S)
        return h

    # ---- links and files ------------------------------------------------------------------------

    def resolve(self, url: str, p: Page) -> Target:
        if not url or EXTERNAL.match(url):
            return Target("external", url)
        if url.startswith("#"):
            return Target("anchor", url, p, frag=unquote(url[1:]))
        path, _, frag = url.partition("#")
        target = (p.src.parent / unquote(path)).resolve()
        frag = unquote(frag)
        if target in self.dir_alias:
            page, anchor = self.dir_alias[target]
            return Target("page", url, page, frag=anchor)
        if target in self.by_path:
            return Target("page", url, self.by_path[target], frag=frag)
        if self.out.resolve() in target.parents:
            return Target("out", url, path=target, frag=frag)
        if target.is_file():
            return Target("asset", url, path=target, frag=frag)
        return Target("missing", url)

    def asset_path(self, path: Path) -> str:
        path = path.resolve()
        if path not in self.assets:
            try:
                rel = path.relative_to(DOCS.resolve()).as_posix()
            except ValueError:
                rel = "files/" + path.relative_to(ROOT.resolve()).as_posix()
            if rel.endswith(".png") and Image is not None and path.stat().st_size > WEBP_OVER:
                rel = rel[:-4] + ".webp"                     # big figures are served as WebP
            self.assets[path] = rel
        return self.assets[path]

    def size_of(self, path: Path) -> tuple[int, int] | None:
        if path not in self._sizes:
            size = None
            try:
                if Image is not None:
                    with Image.open(path) as im:
                        size = im.size
                elif path.suffix.lower() == ".png":
                    size = struct.unpack(">II", path.read_bytes()[16:24])
            except Exception:
                size = None
            self._sizes[path] = size
        return self._sizes[path]

    def data_uri(self, path: Path) -> str:
        if path not in self._uris:
            raw = path.read_bytes()
            mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            if path.suffix.lower() == ".png" and len(raw) > 100_000 and Image is not None:
                with Image.open(io.BytesIO(raw)) as im:
                    im = im if im.mode in ("RGB", "RGBA") else im.convert("RGBA")
                    buf = io.BytesIO()
                    im.save(buf, "WEBP", quality=WEBP_QUALITY, method=6)
                if buf.tell() < len(raw) * 0.8:
                    raw, mime = buf.getvalue(), "image/webp"
            self._uris[path] = f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"
        return self._uris[path]

    def url_for(self, t: Target, p: Page, mode: str, is_img: bool) -> str:
        if t.kind in ("external", "missing"):
            return t.url
        if t.kind == "anchor":
            return "#" + (f"{p.key}--{t.frag}" if mode == "single" and t.frag else t.frag)
        frag = f"#{t.frag}" if t.frag else ""
        if t.kind == "page":
            q = t.page
            if t.frag and t.frag not in {h[1] for h in q.headings}:
                self.problems.append(f"{p.rel}: {t.url}: no heading '{t.frag}' in {q.rel}")
            if mode == "single" and q.single:
                return "#" + q.key + (f"--{t.frag}" if t.frag else "")
            return (rel_url(q.out, p.out) if mode == "site" else q.out) + frag
        if t.kind == "out":
            name = t.path.relative_to(self.out.resolve()).as_posix()
            return (rel_url(name, p.out) if mode == "site" else name) + frag
        out_path = self.asset_path(t.path)
        if mode == "single" and is_img:
            return self.data_uri(t.path)
        return (rel_url(out_path, p.out) if mode == "site" else out_path) + frag

    def relabel(self, h: str, p: Page) -> str:
        """A link whose text is just the file name of another page shows that page's title instead."""
        def repl(m):
            href, label = html.unescape(m.group(1)), html.unescape(m.group(2)).strip()
            t = self.resolve(href, p)
            if t.kind == "page" and not t.frag and label == href.partition("#")[0]:
                return f'<a href="{m.group(1)}">{html.escape(t.page.label)}</a>'
            return m.group(0)
        return re.sub(r'<a href="([^"]+)">(?:<code>)?([^<]*\.md)(?:</code>)?</a>', repl, h)

    def rewrite(self, h: str, p: Page, mode: str) -> str:
        """Point every link and image at its place in the output; wrap figures."""
        h = self.relabel(h, p)
        def attrs(m):
            name, rest = m.group(1), m.group(2)
            local: Path | None = None
            outside = False

            def one(am):
                nonlocal local, outside
                key, val = am.group(1), html.unescape(am.group(2))
                t = self.resolve(val, p)
                if t.kind == "missing":
                    self.problems.append(f"{p.rel}: {val}: file not found")
                if name == "img" and key == "src" and t.kind == "asset":
                    local = t.path
                if mode == "single" and t.kind == "page" and not t.page.single:
                    outside = True
                return f'{key}="{html.escape(self.url_for(t, p, mode, name == "img" and key == "src"), quote=True)}"'

            rest = re.sub(r'\b(href|src)="([^"]*)"', one, rest)
            if outside and " class=" not in rest:  # a page of the multi-page version, next to this file
                rest += ' class="outside" title="Only in the multi-page version (docs/html/), not in this file"'
            if name == "img":
                extra = ' loading="lazy" decoding="async"'
                if local is not None:
                    size = self.size_of(local)
                    if size:
                        extra += f' data-nw="{size[0]}"'
                        if " width=" not in rest:
                            extra += f' width="{size[0]}" height="{size[1]}"'
                elif re.search(r'src="https?://', rest):
                    extra += ' referrerpolicy="no-referrer"'
                rest = rest.rstrip("/ ") + extra
            return f"<{name}{rest}>"

        h = re.sub(r"<(a|img)\b([^>]*)>", attrs, h, flags=re.S)

        def figure(m):
            img, cap = m.group(1), m.group(3)
            nw = re.search(r'data-nw="(\d+)"', img)
            wide = bool(nw) and int(nw.group(1)) >= 1300 and " width=\"" not in img.split("data-nw")[0]
            cls = ' class="wide"' if wide else ""
            return f"<figure{cls}>{img}" + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>"

        return re.sub(r"<p(?: [^>]*)?>\s*(<img\b[^>]*>)\s*</p>(\s*<p><em>(.*?)</em></p>)?", figure, h, flags=re.S)

    def render_body(self, p: Page, mode: str) -> str:
        h = self.rewrite(p.body, p, mode)
        if mode == "single":
            h = re.sub(r'(<h[1-6] id=")([^"]+)"', lambda m: f'{m[1]}{p.key}--{m[2]}"', h)
        else:  # the first picture is above the fold: load it at once instead of lazily
            h = h.replace(' loading="lazy"', ' loading="eager" fetchpriority="high"', 1)
        return h

    # ---- navigation ---------------------------------------------------------------------------

    def included(self, mode: str) -> list[Page]:
        return [p for p in self.pages if mode == "site" or p.single]

    def href(self, p: Page, cur: Page | None, mode: str) -> str:
        return rel_url(p.out, cur.out) if mode == "site" and cur is not None else f"#{p.key}"

    def nav_html(self, cur: Page | None, mode: str, with_single_link: bool = True) -> str:
        pages = self.included(mode)
        out = []

        def item(p: Page) -> str:
            here = cur is p
            kids = [c for c in pages if c.parent == p.key]
            family = here or (cur is not None and cur.parent == p.key)
            cls = ' class="current"' if here else ""
            num = f'<span class="num">{html.escape(p.number)}</span>' if p.number else ""
            s = (f'<li{cls} data-page="{p.key}"><a href="{self.href(p, cur, mode)}"'
                 f'{" aria-current=page" if here else ""}>{num}<span>{html.escape(p.label)}</span></a>')
            subs = [h for h in p.headings if h[0] == 2]
            if subs and (here or mode == "single"):
                links = "".join(
                    f'<li><a href="#{(p.key + "--") if mode == "single" else ""}{hid}">{html.escape(title)}</a></li>'
                    for _, hid, title in subs)
                s += f'<ul class="toc">{links}</ul>'
            if kids and (family or mode == "single"):
                s += "<ul>" + "".join(item(k) for k in kids) + "</ul>"
            return s + "</li>"

        for group in GROUPS:
            top = [p for p in pages if p.group == group and p.parent is None]
            if top:
                out.append(f'<h2>{html.escape(group)}</h2><ul>{"".join(item(p) for p in top)}</ul>')
        if mode == "site" and with_single_link and cur is not None:
            out.append(f'<p class="also">Also as <a href="{rel_url(SINGLE_NAME, cur.out)}">one file</a> with the '
                       "figures embedded, for e-mail and offline reading.</p>")
        if mode == "single":
            out.append(f'<p class="also">Version {self.version}. The same content as a '
                       '<a href="index.html">multi-page site</a>.</p>')
        return "".join(out)

    def neighbours(self, p: Page) -> tuple[Page | None, Page | None]:
        if p.parent:
            seq = [self.by_key[p.parent]] + [q for q in self.pages if q.parent == p.parent]
        else:
            seq = [q for q in self.pages if q.parent is None]
        i = seq.index(p)
        return (seq[i - 1] if i else None, seq[i + 1] if i + 1 < len(seq) else None)

    # ---- html ---------------------------------------------------------------------------------

    @staticmethod
    def article_class(p: Page) -> str:
        return ' class="wide"' if p.wide else ""

    def logo_url(self, name: str, root: str, mode: str, folder: str = "logo") -> str:
        path = DOCS / "img" / folder / name
        if not path.exists():
            raise SystemExit(f"{path} is missing" + ("; run  python tools/build_logo.py" if folder == "logo" else ""))
        return self.data_uri(path) if mode == "single" else f"{root}assets/{folder}/{name}"

    @staticmethod
    def banner_name(p: Page) -> str:
        return BANNER_BY_KEY.get(p.key) or BANNER_BY_GROUP.get(p.group, "project")

    def banner_url(self, q: Page, at: Page | None, mode: str) -> str:
        """The banner of page ``q`` as seen from page ``at`` (empty when the image does not exist)."""
        path = DOCS / "img" / "banners" / f"{self.banner_name(q)}.jpg"
        if not path.exists():
            return ""
        if mode == "single" or at is None:
            return self.data_uri(path)
        return rel_url(self.asset_path(path), at.out)

    def eyebrow_text(self, p: Page) -> str:
        if p.group == "Home":
            return "UrbanSens · Ecological Vector Style"
        if p.group == "Guide" and p.number:
            return f"Guide · Chapter {p.number} of {sum(1 for q in self.pages if q.group == 'Guide')}"
        if p.key.startswith("notes-"):
            return "Research · Working notes"
        if p.key.startswith("stream-"):
            return f"Research · Stream {p.number}"
        if p.key.startswith("src-"):
            return "Project · Example"
        return p.group

    def hero_html(self, p: Page, root: str, mode: str) -> str:
        """The banner: a drawing that fades into the paper, eyebrow, title, a short rule and the subtitle."""
        home = p.key == "home"
        banner = self.banner_url(p, p, mode) if (mode == "site" or home) else ""
        cls = "hero" + (" home" if home else "") + (" page-head" if mode == "single" else "")
        art = f'<div class="hero-art" style="background-image:url(\'{banner}\')"></div>' if banner else ""
        h1_id = ""
        if p.h1_id:
            h1_id = f' id="{p.key}--{p.h1_id}"' if mode == "single" else f' id="{p.h1_id}"'
        parts = []
        if home:
            parts.append(f'<img class="hero-mark" src="{self.logo_url("ulg-mark.svg", root, mode)}" alt="ulg">')
        parts.append(f'<p class="eyebrow">{html.escape(self.eyebrow_text(p))}</p>')
        parts.append(f"<h1{h1_id}>{p.hero_title}</h1>")
        parts.append('<span class="hero-rule"></span>')
        if p.lede:
            parts.append(f'<p class="hero-lede">{self.rewrite(p.lede, p, mode)}</p>')
        meta = f"Version {self.version} · a project by UrbanSens" if home else (f"{p.read_min} min read" if p.read_min else "")
        if meta:
            parts.append(f'<p class="hero-meta">{meta}</p>')
        if home:
            def go(key: str) -> str:
                return rel_url(self.by_key[key].out, p.out) if mode == "site" else f"#{key}"
            parts.append(f'<p class="hero-cta"><a class="btn" href="{go("01-origins")}">Start with the history</a>'
                         f'<a class="btn ghost" href="{go("04-python")}">Use it in Python</a></p>')
        return f'<section class="{cls}">{art}<div class="hero-in">{"".join(parts)}</div></section>\n'

    def topnav_html(self, p: Page | None, mode: str) -> str:
        links = []
        for label, key in TOP_LINKS:
            q = self.by_key[key]
            if mode == "single" and not q.single:
                continue
            href = rel_url(q.out, p.out) if mode == "site" and p is not None else f"#{key}"
            here = ' class="here"' if p is not None and p.group == q.group else ""
            links.append(f'<a href="{href}"{here}>{label}</a>')
        links.append(f'<a href="{REPO_URL}" rel="noopener">GitHub</a>')
        return '<nav class="topnav" aria-label="Sections">' + "".join(links) + "</nav>"

    def head(self, title: str, desc: str, root: str, css: str, single: bool, page: str = "") -> str:
        style = f"<style>{css}</style>" if single else f'<link rel="stylesheet" href="{root}assets/style.css">'
        mode = "single" if single else "site"
        social = ""
        if not single:          # link previews (chat, social media): absolute URLs, the picture made by build_docs.py social
            d = html.escape(desc, quote=True)
            page = "" if page == "index.html" else page          # the start page lives at the site's root
            social = (f'<link rel="canonical" href="{SITE_URL}{page}">\n'
                      '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Urban Landscape Graphics">\n'
                      f'<meta property="og:title" content="{html.escape(title, quote=True)}">\n'
                      f'<meta property="og:description" content="{d}">\n<meta property="og:url" content="{SITE_URL}{page}">\n'
                      f'<meta property="og:image" content="{SITE_URL}assets/social-preview.png">\n'
                      '<meta name="twitter:card" content="summary_large_image">\n')
        icons = f'<link rel="icon" type="image/svg+xml" href="{self.logo_url("ulg-favicon.svg", root, mode)}">\n'
        if not single:
            icons += (f'<link rel="alternate icon" href="{root}assets/logo/favicon.ico">\n'
                      f'<link rel="apple-touch-icon" href="{root}assets/logo/apple-touch-icon.png">\n')
        return (f'<!doctype html>\n<html lang="en" data-root="{root}">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                f"<title>{html.escape(title)}</title>\n"
                f'<meta name="description" content="{html.escape(desc, quote=True)}">\n'
                '<meta name="color-scheme" content="light">\n<meta name="theme-color" content="#F5F5F1">\n'
                f'{social}{icons}{THEME_BOOT}\n{style}\n</head>\n')

    def topbar(self, p: Page | None, root: str, mode: str) -> str:
        mark = self.logo_url("ulg-mark-small.svg", root, mode)
        home = "#home" if mode == "single" else f"{root}index.html"
        return (
            '<a class="skip" href="#content">Skip to content</a>\n<div class="progress" aria-hidden="true"><span></span></div>\n'
            '<header class="topbar">'
            f'<button id="menu" class="icon-btn" type="button" aria-label="Menu" aria-expanded="false">{MENU_SVG}</button>'
            f'<a class="brand" href="{home}"><img src="{mark}" alt="" height="26">'
            f'<span class="name">Urban Landscape Graphics</span><small>{self.version}</small></a>'
            + self.topnav_html(p, mode) +
            '<div class="search"><input id="q" type="search" placeholder="Search the documentation  ( / )" '
            'autocomplete="off" spellcheck="false" aria-label="Search"><div id="results" hidden></div></div>'
            f'<button id="theme" class="icon-btn" type="button" aria-label="Switch between light and dark" '
            f'title="Light / dark">{THEME_SVG}</button></header>\n')

    BRIEF = ("A clean, consistent and scalable visual language to represent nature, surfaces and biodiversity in a "
             "professional, architectural style – using simple vector patterns and symbols.")

    def statement_band(self, p: Page, root: str, mode: str) -> str:
        """The brief that started the style, signed with the UrbanSens logo (home page only)."""
        if p.key != "home":
            return ""
        go = rel_url(self.by_key["02-style"].out, p.out) if mode == "site" else "#02-style"
        logo = self.logo_url("urbansens-logo.png", root, mode, "brand")
        return ('<section class="band"><div class="band-in"><div>'
                f'<p class="band-quote">{html.escape(self.BRIEF)}</p>'
                '<p class="band-cite">UrbanSens · reference sheet of the Ecological Vector Style</p>'
                f'<a class="btn" href="{go}">Read the style guide</a></div>'
                f'<img class="ub-logo" src="{logo}" alt="UrbanSens – Let\'s be part of the change." width="389" height="321">'
                '</div></section>\n')

    def next_band(self, p: Page) -> str:
        prev, nxt = self.neighbours(p)
        if not (prev or nxt):
            return ""

        def card(q: Page, cls: str, label: str) -> str:
            num = f"{q.number} · " if q.number and q.group == "Guide" else ""
            banner = self.banner_url(q, p, "site")
            art = f'<div class="card-art" style="background-image:url(\'{banner}\')"></div>' if banner else ""
            return (f'<a class="card {cls}" href="{rel_url(q.out, p.out)}">{art}<div class="card-text"><small>{label}</small>'
                    f"<b>{html.escape(num + q.label)}</b></div></a>")

        cards = (card(prev, "prev", "Previous") if prev else "") + (card(nxt, "next", "Next") if nxt else "")
        return f'<section class="next-band" aria-label="Previous and next page"><h2>Continue reading</h2><div class="next-cards">{cards}</div></section>\n'

    def footer_html(self, p: Page | None, root: str, mode: str, note: str) -> str:
        pages = self.included(mode)

        def link(q: Page) -> str:
            href = rel_url(q.out, p.out) if mode == "site" and p is not None else f"#{q.key}"
            num = f"{q.number} · " if q.number and q.group == "Guide" else ""
            return f'<li><a href="{href}">{html.escape(num + q.label)}</a></li>'

        cols = "".join(
            f'<div class="foot-col"><h3>{group}</h3><ul>{"".join(link(q) for q in pages if q.group == group and q.parent is None)}</ul></div>'
            for group in ("Guide", "Reference", "Research", "Project"))
        mark = self.logo_url("ulg-mark-small.svg", root, mode)
        ub = self.logo_url("urbansens-logo.png", root, mode, "brand")
        return (f'<footer class="site-footer"><div class="foot-grid"><div class="foot-brand"><img src="{mark}" alt="">'
                '<p class="name">Urban Landscape Graphics</p>'
                "<p>The UrbanSens Ecological Vector Style as a library: colours, textures and symbols for urban landscape "
                f'maps, tied to German and European standards.</p><p>Version {self.version} · <a href="{REPO_URL}" '
                f'rel="noopener">Source on GitHub</a></p></div>{cols}</div>'
                f'<div class="foot-by"><img class="ub-logo" src="{ub}" alt="UrbanSens – Let\'s be part of the change." '
                'width="389" height="321"><p><strong>A project by UrbanSens.</strong> The style began as a single reference '
                "sheet for UrbanSens maps; this library turns it into data, code and documentation.</p></div>"
                f'<p class="foot-note">{note} Headings are set in Rethink Sans (SIL Open Font License), the text in your '
                "system's serif.</p></footer>\n")

    def page_html(self, p: Page) -> str:
        root = "../" * p.out.count("/")
        body = self.render_body(p, "site")
        page_title = p.title if p.group == "Home" else f"{p.title} · Urban Landscape Graphics"
        note = f"Generated from <code>{html.escape(p.rel)}</code> by <code>tools/build_html.py</code>."
        return (
            self.head(page_title, p.desc, root, "", False, p.out) + "<body>\n" + self.topbar(p, root, "site")
            + self.hero_html(p, root, "site")
            + '<div class="layout">\n<nav class="sidebar" aria-label="Documentation">'
            + self.nav_html(p, "site") + '</nav>\n<div class="backdrop"></div>\n'
            + f'<main id="content"><article{self.article_class(p)}>' + body + "</article></main>\n</div>\n"
            + self.statement_band(p, root, "site") + self.next_band(p) + self.footer_html(p, root, "site", note)
            + f'<script defer src="{root}assets/search-index.js"></script>\n'
              f'<script defer src="{root}assets/site.js"></script>\n</body>\n</html>\n')

    def single_html(self, css: str, js: str) -> str:
        pages = self.included("single")
        sections = []
        for p in pages:
            sections.append(f'<section class="page" id="{p.key}">{self.hero_html(p, "", "single")}'
                            f'<article{self.article_class(p)}>{self.render_body(p, "single")}</article></section>')
        title = f"Urban Landscape Graphics {self.version} — documentation"
        note = "Generated by <code>tools/build_html.py</code> from the Markdown in the repository."
        return (
            self.head(title, "The UrbanSens Ecological Vector Style as a library: guide, reference and standards.", "",
                      css, True)
            + "<body data-single>\n" + self.topbar(None, "", "single")
            + '<div class="layout">\n<nav class="sidebar" aria-label="Documentation">' + self.nav_html(None, "single")
            + '</nav>\n<div class="backdrop"></div>\n<main id="content">' + "\n".join(sections)
            + "</main>\n</div>\n" + self.footer_html(None, "", "single", note)
            + f"<script>{self.search_js('single')}</script>\n<script>{js}</script>\n</body>\n</html>\n")

    # ---- search -------------------------------------------------------------------------------

    def search_rows(self, mode: str) -> list[list[str]]:
        rows = []
        for p in self.included(mode):
            display = f"{p.group} — {p.number + ' ' if p.number else ''}{p.label}"
            cap = 1100 if p.full_text else 0
            for level, hid, title, text in p.sections:
                if mode == "site":
                    url = p.out if level == 1 else f"{p.out}#{hid}"
                else:
                    url = f"#{p.key}" if level == 1 else f"#{p.key}--{hid}"
                rows.append([url, display, title, text[:cap]])
        return rows

    def search_js(self, mode: str) -> str:
        import json
        return "window.ULG_INDEX=" + json.dumps(self.search_rows(mode), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";"

    # ---- output -------------------------------------------------------------------------------

    def prepare(self) -> None:
        for p in self.pages:
            self.convert(p)

    def write_assets(self) -> None:
        for src, rel in self.assets.items():
            dest = self.out / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.suffix == ".webp" and src.suffix.lower() == ".png":
                with Image.open(src) as im:
                    im = im if im.mode in ("RGB", "RGBA") else im.convert("RGBA")
                    im.save(dest, "WEBP", quality=WEBP_QUALITY, method=6)
            else:
                shutil.copyfile(src, dest)

    def css(self) -> str:
        font = base64.b64encode((ASSETS / "fonts" / "RethinkSans.woff2").read_bytes()).decode("ascii")
        text = (ASSETS / "style.css").read_text(encoding="utf-8").replace("{{RETHINK_SANS}}", f"data:font/woff2;base64,{font}")
        return palette_css() + "\n" + text

    def build(self, site: bool = True, single: bool = True) -> list[str]:
        if self.out.exists():
            if not (self.out / MARKER).exists() and any(self.out.iterdir()):
                raise SystemExit(f"{self.out} exists and is not a generated documentation folder; choose --out")
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        (self.out / MARKER).write_text("Generated by tools/build_html.py; safe to delete and rebuild.\n")
        self.prepare()
        if site:
            (self.out / "assets").mkdir()
            (self.out / "assets" / "style.css").write_text(self.css(), encoding="utf-8")
            shutil.copyfile(ASSETS / "site.js", self.out / "assets" / "site.js")
            (self.out / "assets" / "logo").mkdir()
            for name in LOGO_FILES:
                shutil.copyfile(DOCS / "img" / "logo" / name, self.out / "assets" / "logo" / name)
            (self.out / "assets" / "brand").mkdir()
            for name in BRAND_FILES:
                shutil.copyfile(DOCS / "img" / "brand" / name, self.out / "assets" / "brand" / name)
            shutil.copyfile(DOCS / "img" / "social-preview.png", self.out / "assets" / "social-preview.png")
            (self.out / "assets" / "search-index.js").write_text(self.search_js("site"), encoding="utf-8")
            for p in self.pages:
                dest = self.out / p.out
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(self.page_html(p), encoding="utf-8")
        if single:
            text = self.single_html(self.css(), (ASSETS / "site.js").read_text(encoding="utf-8"))
            (self.out / SINGLE_NAME).write_text(text, encoding="utf-8")
        self.write_assets()
        self.problems += check_output(self.out)
        return self.problems


# --------------------------------------------------------------------------- shared assets

@functools.lru_cache(maxsize=1)
def palette_css() -> str:
    import ulg
    lines = ["/* palette tokens of the library, as `ulg export tokens` writes them */", ":root {"]
    for fam, steps in ulg.load().palette.families.items():
        lines += [f"  --ulg-{fam}-{step}: {hexc};" for step, hexc in steps.items()]
    n = len(UB_STRIPES)        # hard colour stops: one stripe per sampled column
    stops = ", ".join(f"{c} 0 {(i + 1) * 100 / n:.3f}%" for i, c in enumerate(UB_STRIPES))
    lines.append(f"  --ub-stripes: linear-gradient(90deg, {stops});")
    return "\n".join(lines + ["}"])


# --------------------------------------------------------------------------- output check

class _Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.append(d["id"])
        if tag in ("a", "link") and d.get("href"):
            self.links.append(d["href"])
        if tag in ("img", "script", "source") and d.get("src"):
            self.links.append(d["src"])
        for m in re.finditer(r"url\(['\"]?([^'\")]+)", d.get("style") or ""):
            self.links.append(m.group(1))


def check_output(out: Path) -> list[str]:
    """Broken links, missing files and duplicate ids in the generated html."""
    problems: list[str] = []
    scans: dict[Path, _Scan] = {}

    def scan(path: Path) -> _Scan:
        if path not in scans:
            s = _Scan()
            s.feed(path.read_text(encoding="utf-8"))
            scans[path] = s
        return scans[path]

    for page in sorted(out.rglob("*.html")):
        s = scan(page)
        name = page.relative_to(out).as_posix()
        dupes = {i for i in s.ids if s.ids.count(i) > 1}
        problems += [f"{name}: duplicate id '{i}'" for i in sorted(dupes)]
        for link in s.links:
            if EXTERNAL.match(link) or link.startswith("data:"):
                continue
            path, _, frag = link.partition("#")
            target = (page.parent / unquote(path)).resolve() if path else page
            if not target.exists():
                problems.append(f"{name}: broken link {link}")
            elif frag and target.suffix == ".html" and unquote(frag) not in scan(target).ids:
                problems.append(f"{name}: no anchor in {link}")
    return problems


# --------------------------------------------------------------------------- command line

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(OUT), help=f"output folder (default: {OUT.relative_to(ROOT)})")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--site-only", action="store_true", help="only the multi-page site")
    group.add_argument("--single-only", action="store_true", help=f"only {SINGLE_NAME}")
    args = ap.parse_args(argv)
    builder = Builder(Path(args.out).resolve())
    problems = builder.build(site=not args.single_only, single=not args.site_only)
    out = builder.out
    pages = len(builder.pages) if not args.single_only else 0
    print(f"{out}: {pages} pages" + (f", {SINGLE_NAME} ({(out / SINGLE_NAME).stat().st_size / 1e6:.1f} MB)"
                                       if not args.site_only else ""))
    for problem in problems:
        print("  problem:", problem)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

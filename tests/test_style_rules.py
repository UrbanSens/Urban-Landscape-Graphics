"""House rules for everything we publish: no em dashes, and no spaced en dashes or spaced hyphens in their place."""

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EM, EN = chr(0x2014), chr(0x2013)          # written as code points so that this file itself stays clean
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache", "node_modules", "html", "output",
             ".venv", "venv", "build", "dist"}
TEXT_SUFFIXES = {".py", ".md", ".json", ".js", ".css", ".html", ".toml", ".yml", ".yaml", ".cff", ".txt", ".sh"}
MAX_BYTES = 3_000_000

#: files whose wording is that of an official source or a generated copy of it: only the em dash rule applies
OFFICIAL = ("docs/research/", "docs/reference/", "src/ulg/data/crosswalks/")
SPACED_EN = re.compile(rf"(?:(?<=\s){EN}(?=\s)|^{EN}(?=\s)|(?<=\s){EN}$)", re.M)
SPACED_HYPHEN = re.compile(r"(?<=[^\W\d_]) - (?=[^\W\d_])")          # word - word (letters on both sides)


def text_files():
    for folder, dirs, files in os.walk(ROOT):
        rel = Path(folder).relative_to(ROOT).as_posix()
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.endswith(".egg-info")]
        if rel == "examples/web/ulg":                      # the exported web style is generated
            dirs[:] = []
            continue
        for name in files:
            path = Path(folder, name)
            if (path.suffix.lower() in TEXT_SUFFIXES or name == "LICENSE") and path.stat().st_size <= MAX_BYTES:
                yield path


def lines_of(path: Path):
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return []


def test_no_em_dash_anywhere_in_the_repository():
    found = [f"{p.relative_to(ROOT)}:{n}" for p in text_files() for n, line in enumerate(lines_of(p), 1) if EM in line]
    assert not found, "em dash (write a comma, colon, parentheses or a full stop):\n" + "\n".join(found[:30])


def test_no_spaced_en_dash_in_our_own_text():
    found = []
    for p in text_files():
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(OFFICIAL) and rel != "docs/reference/crosswalk-format.md":
            continue
        text = "\n".join(lines_of(p))
        found += [f"{rel}: {text[:m.start()].count(chr(10)) + 1}" for m in SPACED_EN.finditer(text)]
    assert not found, "spaced en dash used as a dash:\n" + "\n".join(found[:30])


def prose_lines(path: Path):
    """Lines of a Markdown file outside fenced code blocks, with inline code removed."""
    fence = None
    for n, line in enumerate(lines_of(path), 1):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence is None and m:
            fence = m.group(1)[0] * 3
            continue
        if fence is not None:
            if line.strip().startswith(fence):
                fence = None
            continue
        yield n, re.sub(r"`[^`]*`", "", line)


def test_documentation_prose_has_no_spaced_hyphen_dashes():
    files = [ROOT / "README.md", ROOT / "README.en.md", ROOT / "CHANGELOG.md", ROOT / "AGENTS.md",
             *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "docs" / "en").glob("*.md"))]
    found = [f"{p.relative_to(ROOT)}:{n}: {line.strip()[:70]}" for p in files for n, line in prose_lines(p)
             if SPACED_HYPHEN.search(line) and not line.lstrip().startswith("|")]
    assert not found, "a spaced hyphen is not a dash either:\n" + "\n".join(found[:30])


def test_the_rule_is_written_down_where_contributors_look():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "No em dashes" in agents and "tests/test_style_rules.py" in agents

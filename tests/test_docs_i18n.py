"""The German and the English documentation say the same thing in the same places."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IMG = DOCS / "img"
ENGLISH = sorted((DOCS / "en").glob("*.md"))
PAIRS = [(ROOT / "README.en.md", ROOT / "README.md")] + [(p, DOCS / p.name) for p in ENGLISH]
IDS = [de.name for _, de in PAIRS]


def split(text: str):
    """(prose lines, code blocks) of a Markdown text; a code block is (info string, number of lines)."""
    prose, code, fence, info, n = [], [], None, "", 0
    for line in text.splitlines():
        m = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence is None and m:
            fence, info, n = m.group(1)[0] * 3, m.group(2).strip(), 0
        elif fence is not None:
            if line.strip().startswith(fence) and not line.strip().strip(fence[0]):
                code.append((info, n))
                fence = None
            else:
                n += 1
        else:
            prose.append(line)
    return prose, code


def headings(prose):
    out = []
    for line in prose:
        m = re.match(r"^(#{1,6})\s+(\d+(?:\.\d+)*)?", line)
        if m:
            out.append((len(m.group(1)), m.group(2) or ""))
    return out


def table_rows(prose):
    rows, run = [], 0
    for line in prose:
        if line.lstrip().startswith("|"):
            run += 1
        elif run:
            rows.append(run)
            run = 0
    return rows + ([run] if run else [])


def figures(text: str):
    """File names (below docs/img) of the images a Markdown text uses, in order."""
    refs = re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", text) + re.findall(r'<img[^>]+src="([^"]+)"', text)
    return [r.split("img/", 1)[1] for r in refs if "img/" in r and not r.startswith("http")]


def de_name(name: str) -> str:
    stem, dot, ext = name.rpartition(".")
    return f"{stem}-de.{ext}"


def test_every_english_page_has_a_german_twin():
    assert ENGLISH, "docs/en is empty"
    for en, de in PAIRS:
        assert de.is_file(), f"{de.relative_to(ROOT)} is missing (twin of {en.relative_to(ROOT)})"


@pytest.mark.parametrize("en, de", PAIRS, ids=IDS)
def test_same_headings_code_blocks_and_tables(en, de):
    pe, ce = split(en.read_text(encoding="utf-8"))
    pd, cd = split(de.read_text(encoding="utf-8"))
    assert headings(pe) == headings(pd), "headings (level and number) differ"
    assert ce == cd, "fenced code blocks differ (count, language or length)"
    assert table_rows(pe) == table_rows(pd), "tables differ in their number of rows"


@pytest.mark.parametrize("en, de", PAIRS, ids=IDS)
def test_figures_with_text_exist_per_language(en, de):
    fe, fd = figures(en.read_text(encoding="utf-8")), figures(de.read_text(encoding="utf-8"))
    assert len(fe) == len(fd), "number of figures differs"
    for a, b in zip(fe, fd):
        assert (IMG / a).is_file(), f"docs/img/{a} is missing"
        expected = de_name(a) if (IMG / de_name(a)).is_file() else a
        assert b == expected, f"the German page must show {expected}, not {b}"


@pytest.mark.parametrize("en, de", PAIRS, ids=IDS)
def test_quotation_sources_are_labelled_in_each_language(en, de):
    te, td = en.read_text(encoding="utf-8"), de.read_text(encoding="utf-8")
    assert len(re.findall(r"^> Source:", te, re.M)) == len(re.findall(r"^> Quelle:", td, re.M))
    assert not re.search(r"^> Source:", td, re.M)


@pytest.mark.parametrize("en, de", PAIRS, ids=IDS)
def test_german_pages_are_really_translated(en, de):
    pe, _ = split(en.read_text(encoding="utf-8"))
    pd, _ = split(de.read_text(encoding="utf-8"))
    same = [a for a, b in zip(pe, pd) if a == b and len(a.strip()) > 25 and not a.lstrip().startswith(("|", "<", "!["))]
    assert len(same) <= 15, f"{len(same)} prose lines are still English, e.g. {same[:2]}"
    words = re.findall(r"[a-zäöüß]+", " ".join(pd).lower())
    german = sum(w in {"der", "die", "das", "und", "ist", "nicht", "mit", "für", "von", "sie", "werden", "wird"} for w in words)
    english = sum(w in {"the", "and", "is", "not", "with", "for", "of", "you", "are", "will"} for w in words)
    assert german > 3 * english, f"German function words {german}, English {english}"


def test_the_two_trees_point_at_each_other():
    assert "en/index.md" in (DOCS / "index.md").read_text(encoding="utf-8")
    assert "../index.md" in (DOCS / "en" / "index.md").read_text(encoding="utf-8")
    assert "README.en.md" in (ROOT / "README.md").read_text(encoding="utf-8")
    assert "README.md" in (ROOT / "README.en.md").read_text(encoding="utf-8")


def test_the_licence_text_stays_english_in_both_languages():
    mit = "Permission is hereby granted, free of charge, to any person obtaining a copy"
    for page in (DOCS / "licence-and-credit.md", DOCS / "en" / "licence-and-credit.md"):
        assert mit in " ".join(page.read_text(encoding="utf-8").replace(">", " ").split()), page.name

"""Licence, citation file and package metadata agree with each other."""

import json
import re
from pathlib import Path

import ulg

ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_licence_is_mit_and_names_the_copyright_holder():
    text = read("LICENSE")
    assert text.startswith("MIT License") and "Copyright (c) 2026 UrbanSens" in text
    assert "Permission is hereby granted, free of charge" in text and 'THE SOFTWARE IS PROVIDED "AS IS"' in text


def test_pyproject_names_the_licence_the_website_and_the_packaged_logo():
    toml = read("pyproject.toml")
    assert re.search(r'^license = "MIT"', toml, re.M) and 'license-files = ["LICENSE"]' in toml
    assert 'UrbanSens = "https://urbansens.de/"' in toml
    assert "data/brand/*.png" in toml and (ROOT / "src" / "ulg" / "data" / "brand" / "urbansens-logo.png").is_file()


def test_every_file_states_the_same_version():
    toml_version = re.search(r'^version = "([^"]+)"', read("pyproject.toml"), re.M).group(1)
    cff_version = re.search(r'^version: "([^"]+)"', read("CITATION.cff"), re.M).group(1)
    palette_version = json.loads(read("src/ulg/data/palette.json"))["version"]
    assert toml_version == cff_version == palette_version == ulg.__version__
    assert f"## {ulg.__version__} (" in read("CHANGELOG.md")


def test_citation_file_has_what_github_needs():
    cff = read("CITATION.cff")
    for needle in ("cff-version: 1.2.0", "type: software", "title:", "authors:", "repository-code:", "license: MIT",
                   "date-released:", "https://urbansens.de/"):
        assert needle in cff, needle
    assert re.search(r'^date-released: "\d{4}-\d{2}-\d{2}"', cff, re.M)


def test_the_licence_pages_of_the_docs_quote_the_licence_text():
    body = " ".join(read("LICENSE").split()).split("Copyright (c) 2026 UrbanSens", 1)[1].strip()
    for name in ("docs/en/licence-and-credit.md", "docs/licence-and-credit.md"):     # the wording is binding in English only
        page = " ".join(read(name).replace(">", " ").split())
        assert body in page, f"{name} must contain the text of LICENSE"


def test_the_credit_request_is_in_every_place_people_read():
    for name in ("README.md", "README.en.md", "docs/licence-and-credit.md", "docs/en/licence-and-credit.md"):
        text = read(name)
        assert "urbansens.de" in text and "UrbanSens Ecological Vector Style (ulg)" in text, name

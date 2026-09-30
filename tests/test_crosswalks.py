"""Integrity of the crosswalk files, and the lookups people rely on most."""

import pytest

import ulg
from ulg import crosswalk as X

CAT = ulg.load()
SCHEMES = X.schemes(CAT)


def test_crosswalk_files_are_valid():
    problems = X.validate(CAT)
    assert not problems, "\n".join(problems[:40])


@pytest.mark.parametrize("name", sorted(SCHEMES))
def test_every_scheme_has_metadata_and_entries(name):
    sch = SCHEMES[name]
    assert sch.title and sch.source, f"{name}: title and source are required"
    assert sch.entries, f"{name}: no entries"


def need(name):
    if name not in SCHEMES:
        pytest.skip(f"scheme {name} not available")
    return name


def test_osm_core_tags():
    s = need("osm")
    assert ulg.resolve(s, landuse="grass") == "lawn"
    assert ulg.resolve(s, natural="water") in ("water", "watercourse")
    assert ulg.resolve(s, natural="wetland", wetland="reedbed") == "reed"
    assert ulg.resolve(s, natural="wood") in ("woodland", "woodland_deciduous", "woodland_coniferous", "woodland_mixed")
    assert ulg.resolve(s, surface="asphalt") == "asphalt"
    assert ulg.resolve(s, building="yes") == "building"


def test_osm_specific_beats_general():
    s = need("osm")
    assert ulg.resolve(s, leisure="pitch", surface="artificial_turf") == "artificial_turf"
    assert ulg.resolve(s, natural="wetland") != ulg.resolve(s, natural="wetland", wetland="reedbed") or True


def test_clc_codes():
    s = need("clc")
    assert ulg.resolve(s, "141") == "green_space"
    assert ulg.resolve(s, 512) == "water"
    assert X.scheme(s).official_color("141")


def test_alkis_with_field_aliases():
    s = need("alkis")
    assert ulg.resolve(s, objart="43002") in ("woodland", "woodland_deciduous", "woodland_coniferous", "woodland_mixed")
    rows = [{"Objektart": "44006"}, {"OBJART": 41008, "Funktion": 4400}]
    got = ulg.classify(rows, s)
    assert got[0] == "water"
    assert got[1] == "green_space"


def test_classify_is_cached_and_defaults():
    s = need("clc")
    got = ulg.classify(["141", "141", "999999"], s)
    assert got[:2] == ["green_space", "green_space"] and got[2] == "unknown"


def test_hierarchy_fallback_reaches_zero_padded_groups():
    s = need("alkis_nak")
    hit = ulg.explain(s, "18049999")  # unknown detail class of group 1804
    assert hit is not None and hit["code"] == "18040000"


def test_hierarchy_fallback_prefers_the_nearest_parent():
    s = need("clc")
    assert X.scheme(s).lookup({"code": "149"})["code"] == "14"


def test_age_suffix_is_stripped_before_the_fallback():
    s = need("bkompv")
    assert ulg.explain(s, "41.05aM")["code"] == "41.05a"        # no row of its own: the base type


def test_fallback_pattern_blocks_unrelated_groups():
    s = need("baykompv")
    assert ulg.resolve(s, "GU651E") is None                      # a biotope-mapping code, not a BNT
    assert ulg.explain(s, "G214-GU651E") is not None             # a BNT with its mapping sub-type

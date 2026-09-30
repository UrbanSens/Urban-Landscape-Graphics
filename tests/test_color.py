import pytest

from ulg import colormath as C

# Sharma, Wu & Dalal (2005), "The CIEDE2000 color-difference formula", test data
SHARMA = [
    ((50.0, 2.6772, -79.7751), (50.0, 0.0, -82.7485), 2.0425),
    ((50.0, 3.1571, -77.2803), (50.0, 0.0, -82.7485), 2.8615),
    ((50.0, -1.3802, -84.2814), (50.0, 0.0, -82.7485), 1.0000),
    ((50.0, 2.5, 0.0), (73.0, 25.0, -18.0), 27.1492),
    ((60.2574, -34.0099, 36.2677), (60.4626, -34.1751, 39.4387), 1.2644),
    ((2.0776, 0.0795, -1.1350), (0.9033, -0.0636, -0.5514), 0.9082),
]


@pytest.mark.parametrize("a,b,want", SHARMA)
def test_ciede2000_matches_published_pairs(a, b, want):
    assert C._de2000(a, b) == pytest.approx(want, abs=1e-4)


def test_parse_and_hex_roundtrip():
    assert C.to_hex("#cdd2a9") == "#CDD2A9"
    assert C.to_hex("#abc") == "#AABBCC"
    assert C.to_hex("rgb(205, 210, 169)") == "#CDD2A9"
    assert C.to_hex((205, 210, 169)) == "#CDD2A9"
    with pytest.raises(ValueError):
        C.parse("grass")


def test_oklab_roundtrip_and_white():
    L, a, b = C.to_oklab("#FFFFFF")
    assert L == pytest.approx(1.0, abs=1e-6) and abs(a) < 1e-6 and abs(b) < 1e-6
    for hexc in ("#CDD2A9", "#607B8B", "#F4A658", "#112D36"):
        assert C.from_oklab(*C.to_oklab(hexc)) == hexc


def test_wcag_contrast():
    assert C.contrast_ratio("#000000", "#FFFFFF") == pytest.approx(21.0)
    assert C.contrast_ratio("#777777", "#777777") == pytest.approx(1.0)


def test_darken_lighten_keep_hue():
    base = "#CDD2A9"
    h0 = C.to_oklch(base)[2]
    for out in (C.darken(base, 0.1), C.lighten(base, 0.05)):
        assert abs(C.to_oklch(out)[2] - h0) < 2.5
    assert C.to_oklch(C.darken(base, 0.1))[0] < C.to_oklch(base)[0] < C.to_oklch(C.lighten(base, 0.05))[0]


def test_ensure_contrast_reaches_target():
    out = C.ensure_contrast("#B1B78D", "#CDD2A9", 3.0)
    assert C.contrast_ratio(out, "#CDD2A9") >= 3.0
    assert C.ensure_contrast("#000000", "#FFFFFF", 3.0) == "#000000"


def test_cvd_keeps_greys_and_shifts_colours():
    for kind in C.CVD_KINDS:
        assert C.delta_e_ok(C.simulate_cvd("#808080", kind), "#808080") < 0.5
    assert C.delta_e_ok(C.simulate_cvd("#D0786A", "deuteranopia"), "#D0786A") > 5

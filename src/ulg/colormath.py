"""Colour maths for the style system.

Everything works on sRGB hex strings at the edges and OKLab/OKLCH inside, so
tints and shades stay in the same mellow tonal family as the base colour.
Also provides the checks used by the legibility report: WCAG contrast,
CIEDE2000 and colour-vision-deficiency simulation (Machado et al. 2009).
"""

from __future__ import annotations

import math
from typing import Iterable, Sequence

RGB = tuple[float, float, float]

__all__ = [
    "parse", "to_hex", "to_rgb255", "to_oklab", "from_oklab", "to_oklch", "from_oklch",
    "mix", "shade", "darken", "lighten", "with_chroma", "contrast_ratio",
    "relative_luminance", "ensure_contrast", "ramp", "delta_e_ok", "delta_e_2000", "simulate_cvd", "CVD_KINDS",
]


# --------------------------------------------------------------------------- parsing

def parse(c: str | Sequence[float]) -> RGB:
    """Return sRGB floats in 0..1 for ``#RGB``, ``#RRGGBB``, ``rgb(r,g,b)`` or a 3-sequence."""
    if isinstance(c, str):
        s = c.strip()
        if s.startswith("#"):
            s = s[1:]
            if len(s) == 3:
                s = "".join(ch * 2 for ch in s)
            if len(s) not in (6, 8):
                raise ValueError(f"not a hex colour: {c!r}")
            return (int(s[0:2], 16) / 255, int(s[2:4], 16) / 255, int(s[4:6], 16) / 255)
        if s.lower().startswith("rgb"):
            nums = s[s.index("(") + 1 : s.rindex(")")].replace(",", " ").split()
            r, g, b = (float(n) for n in nums[:3])
            return (r / 255, g / 255, b / 255)
        raise ValueError(f"cannot parse colour: {c!r}")
    r, g, b = (float(v) for v in c[:3])
    if max(r, g, b) > 1.0:
        return (r / 255, g / 255, b / 255)
    return (r, g, b)


def _clip01(v: float) -> float:
    return 0.0 if v < 0 else 1.0 if v > 1 else v


def to_hex(rgb: str | Sequence[float]) -> str:
    r, g, b = parse(rgb)
    return "#{:02X}{:02X}{:02X}".format(
        round(_clip01(r) * 255), round(_clip01(g) * 255), round(_clip01(b) * 255)
    )


def to_rgb255(c: str | Sequence[float]) -> tuple[int, int, int]:
    r, g, b = parse(c)
    return (round(_clip01(r) * 255), round(_clip01(g) * 255), round(_clip01(b) * 255))


# --------------------------------------------------------------------------- spaces

def _to_linear(v: float) -> float:
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def _to_gamma(v: float) -> float:
    return 12.92 * v if v <= 0.0031308 else 1.055 * (v ** (1 / 2.4)) - 0.055


def _cbrt(v: float) -> float:
    return math.copysign(abs(v) ** (1 / 3), v)


def to_oklab(c: str | Sequence[float]) -> tuple[float, float, float]:
    r, g, b = (_to_linear(v) for v in parse(c))
    l = _cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b)
    m = _cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b)
    s = _cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b)
    return (
        0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
        1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
        0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
    )


def _oklab_to_linear(L: float, a: float, b: float) -> RGB:
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def from_oklab(L: float, a: float, b: float) -> str:
    """OKLab -> hex. Out-of-gamut colours are pulled in by reducing chroma."""
    L = _clip01(L)
    for _ in range(24):
        lin = _oklab_to_linear(L, a, b)
        if all(-1e-4 <= v <= 1 + 1e-4 for v in lin):
            break
        a *= 0.93
        b *= 0.93
    return to_hex(tuple(_to_gamma(_clip01(v)) for v in lin))


def to_oklch(c: str | Sequence[float]) -> tuple[float, float, float]:
    L, a, b = to_oklab(c)
    return (L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360)


def from_oklch(L: float, C: float, h: float) -> str:
    return from_oklab(L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h)))


# --------------------------------------------------------------------------- operations

def mix(c1: str, c2: str, t: float = 0.5) -> str:
    """Blend two colours in OKLab (t=0 -> c1, t=1 -> c2)."""
    a, b = to_oklab(c1), to_oklab(c2)
    return from_oklab(*(a[i] + (b[i] - a[i]) * t for i in range(3)))


def shade(c: str, dl: float = 0.0, dc: float = 0.0) -> str:
    """Shift OKLCH lightness by ``dl`` and chroma by ``dc`` keeping the hue."""
    L, C, h = to_oklch(c)
    return from_oklch(L + dl, max(0.0, C + dc), h)


def darken(c: str, amount: float = 0.08) -> str:
    """Darker tone of the same hue; chroma rises slightly like a second wash of ink."""
    return shade(c, -amount, amount * 0.12)


def lighten(c: str, amount: float = 0.06) -> str:
    return shade(c, amount, -amount * 0.10)


def with_chroma(c: str, factor: float) -> str:
    L, C, h = to_oklch(c)
    return from_oklch(L, C * factor, h)


# --------------------------------------------------------------------------- legibility

def relative_luminance(c: str) -> float:
    r, g, b = (_to_linear(v) for v in parse(c))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(c1: str, c2: str) -> float:
    """WCAG 2.x contrast ratio (1..21)."""
    l1, l2 = relative_luminance(c1), relative_luminance(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def ensure_contrast(c: str, against: str, ratio: float = 3.0) -> str:
    """Darken (or lighten) ``c`` just enough to reach a WCAG contrast ``ratio`` against ``against``."""
    if contrast_ratio(c, against) >= ratio:
        return to_hex(c)
    L, C_, h = to_oklch(c)
    step = -0.01 if relative_luminance(against) > 0.18 else 0.01
    for _ in range(100):
        L += step
        if not 0.0 <= L <= 1.0:
            break
        out = from_oklch(L, C_, h)
        if contrast_ratio(out, against) >= ratio:
            return out
    return from_oklch(min(max(L, 0.0), 1.0), C_, h)


def delta_e_ok(c1: str, c2: str) -> float:
    """Euclidean distance in OKLab x100 (about 2 is a just-noticeable difference)."""
    a, b = to_oklab(c1), to_oklab(c2)
    return 100 * math.dist(a, b)


def _to_cielab(c: str) -> tuple[float, float, float]:
    r, g, b = (_to_linear(v) for v in parse(c))
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t: float) -> float:
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116

    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e_2000(c1: str, c2: str) -> float:
    """CIEDE2000 colour difference (D65), the metric used in map-legibility research."""
    return _de2000(_to_cielab(c1), _to_cielab(c2))


def _de2000(lab1: Sequence[float], lab2: Sequence[float]) -> float:
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm**7 / (Cm**7 + 25**7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if C1p else 0.0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if C2p else 0.0
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    elif abs(h2p - h1p) <= 180:
        dhp = h2p - h1p
    elif h2p - h1p > 180:
        dhp = h2p - h1p - 360
    else:
        dhp = h2p - h1p + 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lpm = (L1 + L2) / 2
    Cpm = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hpm = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hpm = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hpm = (h1p + h2p + 360) / 2
    else:
        hpm = (h1p + h2p - 360) / 2
    T = (
        1
        - 0.17 * math.cos(math.radians(hpm - 30))
        + 0.24 * math.cos(math.radians(2 * hpm))
        + 0.32 * math.cos(math.radians(3 * hpm + 6))
        - 0.20 * math.cos(math.radians(4 * hpm - 63))
    )
    d_theta = 30 * math.exp(-(((hpm - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cpm**7 / (Cpm**7 + 25**7))
    Sl = 1 + 0.015 * (Lpm - 50) ** 2 / math.sqrt(20 + (Lpm - 50) ** 2)
    Sc = 1 + 0.045 * Cpm
    Sh = 1 + 0.015 * Cpm * T
    Rt = -math.sin(math.radians(2 * d_theta)) * Rc
    return math.sqrt(
        (dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh)
    )


# Machado, Oliveira & Fernandes (2009), severity 1.0, applied in linear RGB.
_CVD = {
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}
CVD_KINDS = tuple(_CVD)


def simulate_cvd(c: str, kind: str = "deuteranopia") -> str:
    """Colour as seen with a colour-vision deficiency (dichromacy simulation)."""
    m = _CVD[kind]
    lin = [_to_linear(v) for v in parse(c)]
    out = [sum(m[i][k] * lin[k] for k in range(3)) for i in range(3)]
    return to_hex(tuple(_to_gamma(_clip01(v)) for v in out))


def ramp(colors: Iterable[str], n: int) -> list[str]:
    """Interpolate ``n`` evenly spaced colours through the given stops (OKLab)."""
    stops = list(colors)
    if n <= 1 or len(stops) == 1:
        return stops[:1] * max(n, 1)
    out = []
    for i in range(n):
        t = i / (n - 1) * (len(stops) - 1)
        k = min(int(t), len(stops) - 2)
        out.append(mix(stops[k], stops[k + 1], t - k))
    return out

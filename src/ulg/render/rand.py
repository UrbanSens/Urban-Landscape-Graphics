"""Stateless, world-anchored randomness.

Textures are not drawn with a sequential random generator. Every random value is
a hash of an integer lattice position plus a seed, so

* the same place on the ground always gets the same marks (stable when the map
  is panned, re-rendered or split into tiles),
* neighbouring polygons of one class share one continuous texture, and
* a lattice can be made periodic, which is what makes seamless pattern tiles.
"""

from __future__ import annotations

import zlib

import numpy as np

_U = np.uint64
_P1, _P2, _P3, _P4 = (
    _U(0x9E3779B97F4A7C15),
    _U(0xC2B2AE3D27D4EB4F),
    _U(0x165667B19E3779F9),
    _U(0x27D4EB2F165667C5),
)
_M1, _M2 = _U(0xBF58476D1CE4E5B9), _U(0x94D049BB133111EB)
_S30, _S27, _S31, _S11 = _U(30), _U(27), _U(31), _U(11)
_INV53 = 1.0 / 9007199254740992.0


def stable_seed(*parts: object) -> int:
    """Deterministic 32-bit seed from any printable parts (independent of PYTHONHASHSEED)."""
    return zlib.crc32("|".join(str(p) for p in parts).encode("utf-8")) & 0xFFFFFFFF


def _as_u64(v) -> np.ndarray:
    return np.atleast_1d(np.asarray(v, dtype=np.int64)).astype(np.uint64)


def _mix(h: np.ndarray) -> np.ndarray:
    with np.errstate(over="ignore"):
        h = (h ^ (h >> _S30)) * _M1
        h = (h ^ (h >> _S27)) * _M2
        return h ^ (h >> _S31)


def cell_hash(i, j, seed: int = 0, salt: int = 0) -> np.ndarray:
    """64-bit hash of integer lattice coordinates."""
    i64, j64 = _as_u64(i), _as_u64(j)
    with np.errstate(over="ignore"):
        h = i64 * _P1 + j64 * _P2 + _as_u64(seed) * _P3 + _as_u64(salt) * _P4
    return _mix(h)


def rand(i, j, seed: int = 0, salt: int = 0) -> np.ndarray:
    """Uniform floats in [0, 1) for lattice coordinates."""
    return (cell_hash(i, j, seed, salt) >> _S11).astype(np.float64) * _INV53


def rand_pm(i, j, seed: int = 0, salt: int = 0) -> np.ndarray:
    """Uniform floats in [-1, 1)."""
    return rand(i, j, seed, salt) * 2.0 - 1.0


def _smooth(t: np.ndarray) -> np.ndarray:
    return t * t * (3.0 - 2.0 * t)


def noise2(x, y, cell: float, seed: int = 0, salt: int = 0, period=None) -> np.ndarray:
    """Smooth 2-D value noise in [-1, 1] with features about ``cell`` wide."""
    x = np.asarray(x, dtype=np.float64) / cell
    y = np.asarray(y, dtype=np.float64) / cell
    i0 = np.floor(x)
    j0 = np.floor(y)
    fx = _smooth(x - i0)
    fy = _smooth(y - j0)
    i0 = i0.astype(np.int64)
    j0 = j0.astype(np.int64)
    i1, j1 = i0 + 1, j0 + 1
    if period is not None:
        px, py = int(period[0]), int(period[1])
        i0, i1, j0, j1 = i0 % px, i1 % px, j0 % py, j1 % py
    v00 = rand_pm(i0, j0, seed, salt)
    v10 = rand_pm(i1, j0, seed, salt)
    v01 = rand_pm(i0, j1, seed, salt)
    v11 = rand_pm(i1, j1, seed, salt)
    return (v00 * (1 - fx) + v10 * fx) * (1 - fy) + (v01 * (1 - fx) + v11 * fx) * fy


class Stream:
    """Tiny helper: successive independent random arrays for one set of lattice points."""

    def __init__(self, i, j, seed: int, salt: int = 0):
        self.i, self.j, self.seed, self.salt = i, j, seed, salt * 1000 + 17

    def take(self, idx) -> "Stream":
        """The same stream for a subset or reordering of the points."""
        out = Stream(self.i[idx], self.j[idx], self.seed)
        out.salt = self.salt
        return out

    def next(self) -> np.ndarray:
        self.salt += 1
        return rand(self.i, self.j, self.seed, self.salt)

    def pm(self) -> np.ndarray:
        return self.next() * 2.0 - 1.0

    def between(self, lo: float, hi: float) -> np.ndarray:
        return lo + (hi - lo) * self.next()

    def choice(self, n: int) -> np.ndarray:
        return np.minimum((self.next() * n).astype(np.int64), n - 1)

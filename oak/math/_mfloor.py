from __future__ import annotations

from math import floor
from typing import SupportsFloat, SupportsIndex, TypeVar


_T = TypeVar("_T")


def mfloor(
    n: SupportsFloat[_T],
    m: SupportsFloat | SupportsIndex,
) -> _T:
    """
    floor(n) to the previous multiple m

    >>> mfloor(21, 5)
    20

    >>> mfloor(21.5, 2.5)
    20.0

    >>> mfloor(21.5, 1)
    21

    :param n: value
    :param m: multiple
    :return: the floor of n to the next multiple m
    """
    if m == 1:
        return floor(n)

    _m = float(m) if isinstance(m, float) else int(m)
    return _m * floor(float(n) / float(m))


__all__ = "mfloor"

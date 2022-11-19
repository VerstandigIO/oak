from __future__ import annotations

from typing import SupportsFloat, SupportsIndex, SupportsRound, TypeVar


_T = TypeVar("_T")


def mround(
    n: SupportsRound[_T],
    m: SupportsFloat | SupportsIndex,
) -> _T:
    """
    round(n) to the nearest multiple m

    >>> mround(21, 5)
    20

    >>> mround(25.5, 2.5)
    25.0

    >>> mround(21.5, 1)
    22

    :param n: value
    :param m: multiple
    :return: n rounded to the nearest multiple m
    """
    if m == 1:
        return round(n)

    _m = float(m) if isinstance(m, float) else int(m)
    return _m * round(round(n) / float(m))


__all__ = "mround"

from __future__ import annotations

from math import ceil
from typing import SupportsFloat, SupportsIndex, TypeVar

_T = TypeVar("_T")


def mceil(
    n: SupportsFloat[_T],
    m: SupportsFloat | SupportsIndex,
) -> _T:
    """
    ceil(n) to the next multiple m

    >>> mceil(21, 5)
    25

    >>> mceil(21.5, 2.5)
    22.5

    >>> mceil(21.5, 1)
    22

    :param n: value
    :param m: multiple
    :return: the ceiling of n to the next multiple m
    """
    if m == 1:
        return ceil(n)

    _m = float(m) if isinstance(m, float) else int(m)
    return _m * ceil(float(n) / float(m))


__all__ = "mceil"

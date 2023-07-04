from __future__ import annotations

from collections.abc import Iterable, Sequence
from itertools import groupby
from operator import attrgetter
from typing import TypeVar

_T = TypeVar("_T")


def group_by(
    items: Iterable[_T],
    *key: str,
) -> Iterable[Sequence[_T]]:
    items = sorted(items, key=attrgetter(*key))
    return iter(list(grouping) for _, grouping in groupby(items, key=attrgetter(*key)))


__all__ = "group_by"

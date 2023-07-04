from typing import TypeVar

from oak.collections.abc import Iterable, Iterator
from oak.collections.mixins import Searchable

_T_co = TypeVar("_T_co", covariant=True)


class MyCollection(Searchable, Iterable):
    def __init__(self, items):
        self._items = items

    def __getitem__(self, i: int) -> _T_co:
        return self._items.__getitem__(i)

    def __len__(self) -> int:
        return self._items.__len__()

    def __iter__(self) -> Iterator[_T_co]:
        return self._items.__iter__()


def test_search_all():
    items = MyCollection(list(range(100)))
    results = list(items.search_all(lambda i: i % 3 == 0, lambda i: i % 5 == 0))

    assert len(results) == 7
    assert results == [0, 15, 30, 45, 60, 75, 90]


def test_search_any():
    items = MyCollection(list(range(100)))
    results = list(items.search_any(lambda i: i % 5 == 0, lambda i: i % 8 == 0))

    assert len(results) == 30
    assert results == [
        0,
        5,
        8,
        10,
        15,
        16,
        20,
        24,
        25,
        30,
        32,
        35,
        40,
        45,
        48,
        50,
        55,
        56,
        60,
        64,
        65,
        70,
        72,
        75,
        80,
        85,
        88,
        90,
        95,
        96,
    ]

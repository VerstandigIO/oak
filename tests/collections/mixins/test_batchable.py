from typing import TypeVar

from oak.collections.abc import Sequence
from oak.collections.mixins import Batchable

_T_co = TypeVar("_T_co", covariant=True)


class MyCollection(Batchable, Sequence):
    def __init__(self, items):
        self._items = items

    def __getitem__(self, i: int) -> _T_co:
        return self._items.__getitem__(i)

    def __len__(self) -> int:
        return self._items.__len__()


def test_batchable():
    items = MyCollection(list(range(9)))
    results = list(items.batch(2))

    assert len(results) == 5
    assert results[0] == [0, 1]
    assert results[1] == [2, 3]
    assert results[2] == [4, 5]
    assert results[3] == [6, 7]
    assert results[4] == [8]

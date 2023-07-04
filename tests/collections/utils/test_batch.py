from typing import TypeVar

from pytest import raises

from oak.collections.abc import Iterator, Sequence
from oak.collections.utils import batch

_T_co = TypeVar("_T_co", covariant=True)


class NonSequence(Iterator):
    def __init__(self, items):
        self._items = items

    def __next__(self) -> _T_co:
        return self._items.__next__()


class SequenceTest(Sequence):
    def __init__(self, items):
        self._items = items

    def __getitem__(self, i: int) -> _T_co:
        return self._items.__getitem__(i)

    def __len__(self) -> int:
        return self._items.__len__()


def test_batch_non_sequence():
    with raises(TypeError):
        items = NonSequence([1, 2, 3, 4, 5])
        list(batch(items, 2))


def test_batch_sequence():
    items = SequenceTest([1, 2, 3, 4, 5])
    batches = list(batch(items, 2))

    assert len(batches) == 3
    assert batches[0] == [1, 2]
    assert batches[1] == [3, 4]
    assert batches[2] == [5]


def test_batch_list():
    items = [1, 2, 3, 4, 5]
    batches = list(batch(items, 2))

    assert len(batches) == 3
    assert batches[0] == [1, 2]
    assert batches[1] == [3, 4]
    assert batches[2] == [5]

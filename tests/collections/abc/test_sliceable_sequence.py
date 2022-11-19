from typing import TypeVar

from _pytest.python_api import raises

from oak.collections.abc import SliceableSequence

_T_co = TypeVar("_T_co", covariant=True)


def test_get_index():
    collection = SliceableSequence(list(range(9)))

    for i in range(len(collection)):
        assert collection[i] == i


def test_get_slice():
    sequence = list(range(9))
    collection = SliceableSequence(sequence)
    collection_slice = collection[1:4]

    assert isinstance(collection_slice, SliceableSequence)

    for i in sequence[1:4]:
        assert collection[i] == i


def test_length():
    collection = SliceableSequence(list(range(9)))
    assert len(collection) == 9


def test_setitem():
    collection = SliceableSequence(list(range(9)))

    with raises(AttributeError):
        collection[0] = 2


def test_repr():
    collection = SliceableSequence(list(range(9)))
    assert (
        repr(collection) == "<SliceableSequence(sequence=(0, 1, 2, 3, 4, 5, 6, 7, 8))>"
    )

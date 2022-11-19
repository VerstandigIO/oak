from __future__ import annotations

from typing import TypeVar

from pytest import raises

from oak.collections.utils import search_all, search_any

_T_co = TypeVar("_T_co", covariant=True)


class NonIterable:
    __slot__ = "__items"

    def __init__(self, items):
        self._items = items


def test_search_all_non_iterable():
    with raises(TypeError):
        items = NonIterable([1, 2, 3, 4, 5])
        list(search_all(items, lambda i: i == 2))


def test_search_all_single_expr():
    items = [1, 2, 3, 4, 5]
    results = list(search_all(items, lambda i: i == 2))

    assert len(results) == 1
    assert results[0] == 2


def test_search_all_multiple_exprs():
    items = range(100)
    results = list(search_all(items, lambda i: i % 3 == 0, lambda i: i % 5 == 0))

    assert len(results) == 7
    assert results == [0, 15, 30, 45, 60, 75, 90]


def test_search_any_non_iterable():
    with raises(TypeError):
        items = NonIterable([1, 2, 3, 4, 5])
        list(search_any(items, lambda i: i == 2))


def test_search_any_single_expr():
    items = [1, 2, 3, 4, 5]
    results = list(search_any(items, lambda i: i == 2))

    assert len(results) == 1
    assert results[0] == 2


def test_search_any_multiple_exprs():
    items = range(100)
    results = list(search_any(items, lambda i: i % 5 == 0, lambda i: i % 8 == 0))

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

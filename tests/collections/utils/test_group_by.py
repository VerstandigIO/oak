from __future__ import annotations

from typing import Any

from oak.collections.utils import group_by


class MyObject:
    __slots__ = (
        "_a",
        "_b",
        "_c",
    )

    def __init__(
        self,
        a: Any,
        b: Any = None,
        c: Any = None,
    ):
        self._a = a
        self._b = b
        self._c = c

    def __repr__(self) -> str:
        return f"MyObject(a={self.a}, b={self.b}, c={self.c})"

    @property
    def a(self) -> Any:
        return self._a

    @property
    def b(self) -> Any:
        return self._b

    @property
    def c(self) -> Any:
        return self._c


def test_single_key():
    items = [
        MyObject(a=1, b=2),
        MyObject(a=2, b=1),
        MyObject(a=1, b=3),
    ]

    results = list(group_by(items, "a"))

    assert len(results) == 2
    assert len(results[0]) == 2
    assert len(results[1]) == 1

    for item in results[0]:
        assert item.a == 1
        assert item.b in [2, 3]

    for item in results[1]:
        assert item.a == 2
        assert item.b in [1]


def test_multiple_keys():
    items = [
        MyObject(a=1, b=2, c=4),
        MyObject(a=2, b=1, c=5),
        MyObject(a=1, b=3, c=4),
    ]

    results = list(group_by(items, "a", "c"))

    assert len(results) == 2
    assert len(results[0]) == 2
    assert len(results[1]) == 1

    for item in results[0]:
        assert item.a == 1
        assert item.b in [2, 3]
        assert item.c == 4

    for item in results[1]:
        assert item.a == 2
        assert item.b in [1]
        assert item.c == 5


def test_multiple_keys_unique():
    items = [
        MyObject(a=1, b=2, c="a"),
        MyObject(a=2, b=1, c="c"),
        MyObject(a=1, b=3, c="b"),
    ]

    results = list(group_by(items, "a", "c"))

    assert len(results) == 3
    assert len(results[0]) == 1
    assert len(results[1]) == 1
    assert len(results[2]) == 1

    for i, expected in enumerate([(1, 2, "a"), (1, 3, "b"), (2, 1, "c")]):
        assert results[i][0].a == expected[0]
        assert results[i][0].b == expected[1]
        assert results[i][0].c == expected[2]

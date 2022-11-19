from __future__ import annotations

from pytest import mark

from oak.math import mfloor


@mark.parametrize(
    "n,m,expected",
    [
        (1, 10, 0),
        (123, 10, 120),
        (12345, 100, 12300),
        (1.5, 10, 0),
        (123.5, 10, 120),
        (12345.5, 100, 12300),
        (1.5, 2.5, 0),
        (12.7, 5.25, 10.5),
        (123.9, 7.15, 121.55),
        (1234.9, 7, 1232),
        (1.5, 1, 1),
        (1.25, 1, 1),
    ],
)
def test_mfloor(
    n: int,
    m: int,
    expected: int,
):
    result = round(mfloor(n, m), ndigits=2)
    assert result == expected

    d = round(result / m, ndigits=2)
    assert d == int(d)

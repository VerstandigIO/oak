from __future__ import annotations

from pytest import mark

from oak.math import mceil


@mark.parametrize(
    "n,m,expected",
    [
        (1, 10, 10),
        (123, 10, 130),
        (12345, 100, 12400),
        (1.5, 10, 10),
        (123.5, 10, 130),
        (12345.5, 100, 12400),
        (1.5, 2.5, 2.5),
        (12.7, 5.25, 15.75),
        (123.9, 7.15, 128.7),
        (1234.9, 7, 1239),
        (1.5, 1, 2),
        (1.25, 1, 2),
    ],
)
def test_mceil(
    n: int,
    m: int,
    expected: int,
):
    result = round(mceil(n, m), ndigits=2)
    assert result == expected

    d = round(result / m, ndigits=2)
    assert d == int(d)

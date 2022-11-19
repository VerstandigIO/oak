import sys
from itertools import compress
from typing import TypeVar

if sys.version_info.minor >= 9:
    from collections.abc import Callable, Iterable
else:
    from typing import Callable, Iterable


_T_co = TypeVar("_T_co", covariant=True)


def search_all(
    iterable: Iterable[_T_co],
    *expr: Callable[[_T_co], bool],
) -> Iterable[_T_co]:
    return _search(iterable, expr, matcher=all)


def search_any(
    iterable: Iterable[_T_co],
    *expr: Callable[[_T_co], bool],
) -> Iterable[_T_co]:
    return _search(iterable, expr, matcher=any)


def _search(
    iterable: Iterable[_T_co],
    exprs: Iterable[Callable[[_T_co], bool]],
    *,
    matcher: Callable[[Iterable[_T_co]], bool] = all,
) -> Iterable[_T_co]:
    return compress(
        iterable, map(lambda item: matcher([expr(item) for expr in exprs]), iterable)
    )


__all__ = (
    "search_all",
    "search_any",
)

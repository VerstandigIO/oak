import sys

from abc import ABC
from typing import Callable, TypeVar

from ..utils import search_all, search_any

if sys.version_info.minor >= 9:
    from collections.abc import Iterable
else:
    from typing import Iterable


_T_co = TypeVar("_T_co", covariant=True)
_T_Searchable = TypeVar("_T_Searchable", bound="Searchable")


class Searchable(ABC, Iterable):
    def search_all(
        self,
        *expr: Callable[[_T_co], bool],
    ) -> Iterable[_T_co]:
        return search_all(self, *expr)

    def search_any(
        self,
        *expr: Callable[[_T_co], bool],
    ) -> Iterable[_T_co]:
        return search_any(self, *expr)


__all__ = "Searchable"

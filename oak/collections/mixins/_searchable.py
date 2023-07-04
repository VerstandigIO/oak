from abc import ABC
from typing import Callable, TypeVar

from ..abc import Iterable
from ..utils import search_all, search_any

_T_co = TypeVar("_T_co", covariant=True)
_T_Searchable = TypeVar("_T_Searchable", bound="Searchable")


class Searchable(ABC, Iterable):
    def search_all(
        self,
        *expr: Callable[[_T_co], bool],
    ) -> Iterable[_T_Searchable]:
        return search_all(self, *expr)

    def search_any(
        self,
        *expr: Callable[[_T_co], bool],
    ) -> Iterable[_T_Searchable]:
        return search_any(self, *expr)


__all__ = "Searchable"

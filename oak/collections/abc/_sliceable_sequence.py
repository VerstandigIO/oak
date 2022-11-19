from __future__ import annotations

from abc import ABC
from collections.abc import Sequence
from typing import TypeVar


_T_co = TypeVar("_T_co", covariant=True)
_T_SliceableSequence = TypeVar("_T_SliceableSequence", bound="SliceableSequence")


class SliceableSequence(ABC, Sequence):
    def __init__(
        self,
        sequence: Sequence[_T_co],
    ):
        self.__sequence = tuple(sequence)

    def __repr__(self) -> str:
        return f"<{str(self.__class__.__name__)}(sequence={tuple(self)})>"

    def __len__(
        self,
    ) -> int:
        return len(self.__sequence)

    def __getitem__(
        self: _T_SliceableSequence,
        key: int | slice,
    ) -> _T_co | _T_SliceableSequence[_T_co]:
        if isinstance(key, slice):
            return self.__class__(self.__sequence[key])

        return self.__sequence[key]

    def __setitem__(self, key, value):
        raise AttributeError("SliceableSequence cannot be modified")


__all__ = "SliceableSequence"

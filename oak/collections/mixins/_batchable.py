import sys
from abc import ABC
from typing import TypeVar

if sys.version_info.minor >= 9:
    from collections.abc import Generator, Sequence
else:
    from typing import Generator, Sequence

from ..utils import batch


_T_co = TypeVar("_T_co", covariant=True)


class Batchable(ABC, Sequence):
    def batch(
        self,
        size: int,
    ) -> Generator[Sequence[_T_co], None, None]:
        return batch(self, size=size)


__all__ = "Batchable"

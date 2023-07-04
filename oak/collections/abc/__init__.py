import sys

if sys.version_info.minor >= 9:
    from collections.abc import (
        Callable,
        Collection,
        Generator,
        Iterable,
        Iterator,
        Sequence,
    )
else:
    from typing import Callable, Collection, Generator, Iterable, Iterator, Sequence

from ._sliceable_sequence import SliceableSequence

__all__ = (
    "Callable",
    "Collection",
    "Generator",
    "Iterable",
    "Iterator",
    "Sequence",
    "SliceableSequence",
)

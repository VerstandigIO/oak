import sys
from typing import TypeVar

if sys.version_info.minor >= 9:
    from collections.abc import Generator, Sequence
else:
    from typing import Generator, Sequence


_T_co = TypeVar("_T_co", covariant=True)


def batch(
    items: Sequence[_T_co],
    size: int,
) -> Generator[Sequence[_T_co], None, None]:
    length = len(items)

    for index in range(0, length, size):
        yield items[index : min(index + size, length)]

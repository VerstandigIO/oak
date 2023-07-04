from typing import TypeVar

from ..abc import Generator, Sequence

_T_co = TypeVar("_T_co", covariant=True)


def batch(
    items: Sequence[_T_co],
    size: int,
) -> Generator[Sequence[_T_co], None, None]:
    length = len(items)

    for index in range(0, length, size):
        yield items[index : min(index + size, length)]

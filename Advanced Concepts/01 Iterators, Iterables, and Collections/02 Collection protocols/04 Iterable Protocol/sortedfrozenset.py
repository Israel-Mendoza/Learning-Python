from __future__ import annotations
from typing import Any


"""
The Iterable protocol requires the collection to 
implement the __iter__ (or __getitem__) method. 
"""


class SortedFrozenSet:
    def __init__(self, items: Any = None) -> None:
        """
        The SortedFrozenSet class is a container that stores elements in a sorted order.
        Initializing the self._items with a list version of the passed items.
        """
        self._items: list[Any] = sorted(set(items) if items is not None else set())

    def __contains__(self, item: Any) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter[Any]:  # type: ignore
        return iter(self._items)

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

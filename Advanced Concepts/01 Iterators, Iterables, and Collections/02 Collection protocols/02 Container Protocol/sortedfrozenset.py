from __future__ import annotations
from typing import Any, Iterator


"""
The Container protocol requires the collection to implement the __contains__ method. 

"""


class SortedFrozenSet:
    def __init__(self, items: Any = None) -> None:
        """
        The SortedFrozenSet class is a container that stores elements in a sorted order.
        Initializing the self._items with a list version of the passed items.
        """
        self._items: list[Any] = list(items) if items is not None else list()

    def __contains__(self, item: Any) -> bool:
        return item in self._items

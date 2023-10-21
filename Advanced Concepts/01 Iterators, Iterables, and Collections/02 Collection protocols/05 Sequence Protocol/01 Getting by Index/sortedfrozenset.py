from __future__ import annotations
from typing import Any


"""
The Sequence Protocol required the collection to:
1. Be able to retrieve an item with an index.
    item: Any = my_set[0]
2. Optionally retrieve items by slicing.
    itemset: set[Any] = my_set[0:2]
3. Produce a reverse iterator.
    reversed_iter: iter[Any] = reversed(my_set)
4. Locate an item by value and return its index:
    index: int = my_set.index(item)
5. Count how many items exist in the collection:
    num: int = my_set.count(item)


Starting with the first requirement. 
We must implement de __getitem__ method to retrieve an item with an index.

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

from __future__ import annotations
from typing import Any
from collections.abc import Sequence
from itertools import chain


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

Implementing the "+" and "*" operands by overriding the 
__add__ and __mul__ methods.

"""


class SortedFrozenSet(Sequence):
    def __init__(self, items: Any = None) -> None:
        """
        The SortedFrozenSet class is a container that stores elements in a sorted order.
        Initializing the self._items with a list version of the passed items.
        """
        self._items: tuple[Any] = tuple(
            sorted(set(items) if items is not None else set())
        )

    def __contains__(self, item: Any) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter[Any]:  # type: ignore
        return iter(self._items)

    def __getitem__(self, index: int | slice) -> Any:
        result = self._items[index]
        return result if isinstance(index, int) else SortedFrozenSet(result)

    def __repr__(self) -> str:
        return "{type}({arg})".format(
            type=type(self).__name__,
            arg=(
                "[{}]".format(", ".join(map(repr, self._items))) if self._items else ""
            ),
        )

    def __eq__(self, other: SortedFrozenSet | list[Any]) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items

    def __hash__(self) -> int:
        return hash((type(self), self._items))

    def __add__(self, other: SortedFrozenSet) -> SortedFrozenSet:
        if not isinstance(other, type(self)):
            return NotImplemented
        result: SortedFrozenSet = SortedFrozenSet(chain(self._items + other._items))
        return result

    def __mul__(self, other: int) -> SortedFrozenSet:
        if other <= 0:
            return SortedFrozenSet()
        return SortedFrozenSet(self._items)

    def __rmul__(self, other: int) -> SortedFrozenSet:
        return self * other

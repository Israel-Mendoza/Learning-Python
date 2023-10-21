from __future__ import annotations
from typing import Any, Sequence


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

Reversing with the implementation of __reversed__.
If this method is not implemented, the reversed() 
built-in function will use the implementation of 
__getitem__ and __len__ to reverse the collection.

In this example, we won't do any work here (other
than creating the test method) since we have al-
ready implemented the __getitem__ and __len__ 
methods.

"""


class SortedFrozenSet:
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


a = SortedFrozenSet()

print(repr(a))

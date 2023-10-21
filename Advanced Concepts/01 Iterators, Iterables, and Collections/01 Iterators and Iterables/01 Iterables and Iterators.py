from __future__ import annotations
from typing import Any


class MyIterable:
    def __init__(self: MyIterable, a_list: list[Any]) -> None:
        self._sequence: list[Any] = a_list
        self._index: int = 0

    def __next__(self: MyIterable) -> Any:
        # If the index is greater than or equal to the length of the list, raise an error
        if self._index >= len(self._sequence):
            raise StopIteration("The list got exhausted!")
        # Storing the next item in a temporary variable
        result: Any = self._sequence[self._index]
        # Incrementing the index by one
        self._index += 1
        return result

    def __iter__(self: MyIterable) -> MyIterable:
        # Complying with the iterable protocol.
        return self


# Create a list of integers
my_list: list[int] = [1, 2, 3, 4, 5]

# Create an instance of MyIterable
iterator: MyIterable = MyIterable(my_list)

# The for loop will call the __iter__ method and then the __next__ method until the list gets exhausted.
for item in iterator:
    print(item, end=" ")
# 1 2 3 4 5
print()

try:
    item: int = next(iterator)
    print(item)
except StopIteration as e:
    print(f"Error raised at this point: '{e}'")
# Error raised at this point: 'The list got exhausted!'

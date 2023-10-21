from __future__ import annotations
from typing import Any, Sequence


class LevelOrderIterator:
    def __init__(self, sequence: Sequence) -> None:
        if not LevelOrderIterator._is_perfect_length(sequence):
            raise ValueError(
                f"Sequence is not perfect (length={len(sequence)}). Length must be 2^h - 1"
            )
        self._sequence: Sequence = sequence
        self._index: int = 0

    def __iter__(self) -> LevelOrderIterator:
        return self

    def __next__(self) -> Any:
        if self._index >= len(self._sequence):
            raise StopIteration
        result: Any = self._sequence[self._index]
        self._index += 1
        return result

    @staticmethod
    def _is_perfect_length(sequence: Sequence) -> bool:
        """
        True if the length of the sequence has 2^h - 1
        The sequence must not be empty.
        """
        length: int = len(sequence)
        return ((length + 1) & length == 0) and length != 0


# Testing the _is_perfect_length function.
perfect_trees: dict[int, bool] = {}
# Populating the dictionary with the results of the
# _is_perfect_length function, when it's passed a se-
# quence of the size if the "i" variable
for i in range(1, 128):
    perfect_trees[i] = LevelOrderIterator._is_perfect_length([1] * i)

# Printing the results
for num, value in perfect_trees.items():
    if value:
        print(f"{num} is perfect")
# 1 is perfect
# 3 is perfect
# 7 is perfect
# 15 is perfect
# 31 is perfect
# 63 is perfect
# 127 is perfect


# Testing the LevelOrderIterator class
non_perfect_tree: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perfect_tree: list[str] = ["*", "-", "+", "a", "b", "c", "d"]

print(len(non_perfect_tree))
print(len(perfect_trees))

try:
    level_order_iter = LevelOrderIterator(non_perfect_tree)
except ValueError as err:
    print(err)
# Output:
# Sequence is not perfect (length=10). Length must be 2^h - 1

level_order_iter = LevelOrderIterator(perfect_tree)


final_exp: str = " ".join(level_order_iter)
print(final_exp)
# * - + a b c d

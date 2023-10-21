from __future__ import annotations
from typing import Any, Sequence


class PreOrderIterator:
    def __init__(self, sequence: Sequence) -> None:
        if not PreOrderIterator._is_perfect_length(sequence):
            raise ValueError(
                f"Sequence is not perfect (length={len(sequence)}). Length must be 2^h - 1"
            )
        self._sequence: Sequence = sequence
        self._index: int = 0
        # Creating a stack using a list, since Python doesn't have one.
        self._stack: list[int] = [0]

    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> Any:
        if len(self._stack) == 0:
            raise StopIteration
        index: int = self._stack.pop()
        result: Any = self._sequence[index]

        # Pre-order: Push right child first, so left
        # child is popped and processed first. LIFO.
        right_child_index: int = PreOrderIterator._right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index: int = PreOrderIterator._left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result

    @staticmethod
    def _is_perfect_length(sequence: Sequence) -> bool:
        """
        True if the length of the sequence has 2^h - 1
        The sequence must not be empty.
        """
        length: int = len(sequence)
        return ((length + 1) & length == 0) and length != 0

    @staticmethod
    def _left_child(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def _right_child(index: int) -> int:
        return 2 * index + 2


initial_exp: list[str] = "* + - a b c d a1 a2 b1 b2 c1 c2 d1 d2".split()
iterator: PreOrderIterator = PreOrderIterator(initial_exp)

final_exp: str = "  ".join(iterator)

print(final_exp)
# *  +  a  a1  a2  b  b1  b2  -  c  c1  c2  d  d1  d2

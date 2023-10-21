from __future__ import annotations
from typing import Any, Sequence


class InOrderIterator:
    def __init__(self, sequence: Sequence) -> None:
        if not InOrderIterator._is_perfect_length(sequence):
            raise ValueError(
                f"Sequence is not perfect (length={len(sequence)}). Length must be 2^h - 1"
            )
        self._sequence: Sequence = sequence
        self._index: int = 0
        # Creating a stack using a list, since Python doesn't have one.
        self._stack: list[int] = []
        self._index: int = 0

    def __iter__(self) -> InOrderIterator:
        return self

    def __next__(self) -> Any:
        if (len(self._stack) == 0) and (self._index >= len(self._sequence)):
            raise StopIteration

        # Push left children to the stack, when possible.
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = InOrderIterator._left_child(self._index)

        # Pop from the stack and process, before moving to the right child.
        index: int = self._stack.pop()
        result = self._sequence[index]
        self._index = InOrderIterator._right_child(index)
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
iterator: InOrderIterator = InOrderIterator(initial_exp)

final_exp: str = "  ".join(iterator)

print(final_exp)
# a1  a  a2  +  b1  b  b2  *  c1  c  c2  -  d1  d  d2

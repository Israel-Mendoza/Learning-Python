import unittest
from sortedfrozenset import SortedFrozenSet
from typing import Iterator


class TestConstruction(unittest.TestCase):
    def test_construct_empty(self):
        s: SortedFrozenSet = SortedFrozenSet([])

    def test_construct_from_non_empty(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3])

    def test_construct_from_an_iterator(self) -> None:
        items = [1, 2, 3]
        iterator: Iterator[int] = iter(items)
        s: SortedFrozenSet = SortedFrozenSet(iterator)

    def test_construct_no_args(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet()


if __name__ == "__main__":
    unittest.main()

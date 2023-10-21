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


class TestContainerProtocol(unittest.TestCase):
    def setUp(self) -> None:
        self.s = SortedFrozenSet([1, 2, 3])

    def test_positive_contained(self) -> None:
        self.assertTrue(1 in self.s)

    def test_negative_contained(self) -> None:
        self.assertFalse(10 in self.s)

    def test_positive_not_contained(self) -> None:
        self.assertTrue(10 not in self.s)

    def test_negative_not_contained(self) -> None:
        self.assertFalse(1 not in self.s)


if __name__ == "__main__":
    unittest.main()

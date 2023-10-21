import unittest
from collections.abc import Container, Sized, Iterable, Sequence, Hashable
from sortedfrozenset import SortedFrozenSet
from typing import Iterator
import collections


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

    def test_container_protocol(self) -> None:
        self.assertTrue(isinstance(self.s, Container))


class TestSizedProtocol(unittest.TestCase):
    def test_empty_with_default(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet()
        self.assertEqual(len(s), 0)

    def test_empty(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([])
        self.assertEqual(len(s), 0)

    def test_one(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1])
        self.assertEqual(len(s), 1)

    def test_ten(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3, 1, 2, 3])
        self.assertEqual(len(s), 3)

    def test_container_protocol(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet()
        self.assertTrue(isinstance(s, Sized))


class TestIterableProtocol(unittest.TestCase):
    def setUp(self) -> None:
        self.s = SortedFrozenSet([3, 4, 1, 2])

    def test_iter(self) -> None:
        iterator: Iterator[int] = iter(self.s)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 4)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_for_loop(self) -> None:
        index: int = 0
        expected: list[int] = [1, 2, 3, 4]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

    def test_iterable_protocol(self) -> None:
        self.assertTrue(isinstance(self.s, Iterable))


class TestSequenceProtocol(unittest.TestCase):
    def setUp(self) -> None:
        self.s = SortedFrozenSet([3, 4, 1, 2, 5])
        # [1, 2, 3, 4, 5]

    def test_index_zero(self) -> None:
        self.assertEqual(self.s[0], 1)

    def test_index_four(self) -> None:
        self.assertEqual(self.s[4], 5)

    def test_index_one_beyond_the_end(self) -> None:
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self) -> None:
        self.assertEqual(self.s[-1], 5)

    def test_index_minus_five(self) -> None:
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_the_beginning(self) -> None:
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self) -> None:
        self.assertEqual(self.s[:3], SortedFrozenSet([1, 2, 3]))

    def test_slice_to_end(self) -> None:
        self.assertEqual(self.s[3:], SortedFrozenSet([4, 5]))

    def test_slice_empty(self) -> None:
        self.assertEqual(self.s[10:], SortedFrozenSet())

    def test_slice_arbitrary(self) -> None:
        self.assertEqual(self.s[2:4], SortedFrozenSet([3, 4]))

    def test_slice_step(self) -> None:
        self.assertEqual(self.s[::2], SortedFrozenSet([1, 3, 5]))

    def test_slice_full(self) -> None:
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3])
        r: SortedFrozenSet = reversed(s)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 2)
        self.assertEqual(next(r), 1)
        with self.assertRaises(StopIteration):
            next(r)

    def test_index_positive(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s.index(8), 3)

    def test_index_negative(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        with self.assertRaises(ValueError):
            s.index(10)

    def test_count_zero(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s.count(0), 0)

    def test_count_one(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s.count(5), 1)

    def test_add_disjoint(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        t: SortedFrozenSet = SortedFrozenSet([4, 3, 2, 1])
        self.assertEqual(s + t, SortedFrozenSet([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_add_equal(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s + s, s)

    def test_add_intersecting(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        t: SortedFrozenSet = SortedFrozenSet([5, 4, 3, 2, 1])
        self.assertEqual(s + t, SortedFrozenSet([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_add_type_error_left(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        with self.assertRaises(TypeError):
            s + "abc"

    def test_add_type_error_right(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        with self.assertRaises(TypeError):
            "abc" + s

    def test_repetition_zero_right(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s * 0, SortedFrozenSet())

    def test_repetition_negative_right(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s * -1, SortedFrozenSet())

    def test_repetition_nonzero_right(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s * 100, s)

    def test_repetition_zero_left(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(0 * s, SortedFrozenSet())

    def test_repetition_negative_left(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(-1 * s, SortedFrozenSet())

    def test_repetition_nonzero_left(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([9, 8, 7, 6, 5])
        self.assertEqual(s * 100, s)

    def test_sequence_protocol(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3])
        self.assertTrue(isinstance(s, Sequence))


class TestReprProtocol(unittest.TestCase):
    def test_repr_empty(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet()
        self.assertEqual(repr(s), "SortedFrozenSet()")

    def test_repr_one(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1])
        self.assertEqual(repr(s), "SortedFrozenSet([1])")

    def test_repr_multiple(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3])
        self.assertEqual(repr(s), "SortedFrozenSet([1, 2, 3])")


class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self) -> None:
        self.assertTrue(SortedFrozenSet([1, 2, 3]) == SortedFrozenSet([1, 2, 3]))

    def test_negative_equal(self) -> None:
        self.assertFalse(SortedFrozenSet([1, 2, 3]) == SortedFrozenSet([1, 2, 4]))

    def test_positive_not_equal(self) -> None:
        self.assertTrue(SortedFrozenSet([1, 2, 3]) != SortedFrozenSet([1, 2, 4]))

    def test_negative_not_equal(self) -> None:
        self.assertFalse(SortedFrozenSet([1, 2, 3]) != SortedFrozenSet([1, 2, 3]))

    def test_type_mismatch(self) -> None:
        self.assertFalse(SortedFrozenSet([1, 2, 3]) == [1, 2, 3])

    def test_identical(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3])
        self.assertTrue(s == s)


class TestHashableProtocol(unittest.TestCase):
    def test_equal_sets_have_same_hash_code(self) -> None:
        self.assertEqual(
            hash(SortedFrozenSet([1, 2, 3])),
            hash(SortedFrozenSet([1, 2, 3])),
        )

    def test_hashable_protocol(self) -> None:
        s: SortedFrozenSet = SortedFrozenSet([1, 2, 3])
        self.assertTrue(isinstance(s, Hashable))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations
from fractions import Fraction
from typing import Iterator


"""
When passing an object to the iter() function, Python will check if the object has a __iter__() method.
If it does, then Python will call that method and return the result.
If it does not, then Python will check if the object has a __getitem__() method.
If it does, then Python will create the iterator for us, using the __getitem__() method.
"""


class RationalRange:
    def __init__(self: RationalRange, start: int, end: int, number_of_steps: int):
        if not isinstance(number_of_steps, int):
            raise ValueError(f"Steps must be an int value ({number_of_steps} is not).")
        if number_of_steps < 1:
            raise ValueError(f"Steps must be 1 or more ({number_of_steps} is not).")
        self._start: int = start
        self._end: int = end
        self._number_of_steps: int = number_of_steps
        self._step: Fraction = Fraction(end - start, number_of_steps)

    def __getitem__(self: RationalRange, index: int) -> Fraction:
        if index < 0 or index > self._number_of_steps:
            raise IndexError(f"Index {index} out of range).")
        result: Fraction = self._start + (self._step * index)
        return result


my_range: RationalRange = RationalRange(1, 10, 4)

iterator: Iterator[Fraction] = iter(my_range)

result: Fraction = next(iterator)
print(result)
# 1

result: Fraction = next(iterator)
print(result)
# 13/4

result: Fraction = next(iterator)
print(result)
# 11/2

result: Fraction = next(iterator)
print(result)
# 31/4

result: Fraction = next(iterator)
print(result)
# 10


result: Fraction = next(iterator)
# Output:
# Traceback (most recent call last):
#   File "../06 Alternative Iterable Protocol.py", line 51, in <module>
#     result: Fraction = next(iterator)
#                        ^^^^^^^^^^^^^^
# StopIteration

from collections.abc import Sequence
from random import randint


"""Creating a simple 'sequence' object by implementing the __next__ method"""


class SquareNumbers:
    def __init__(self, limit: int) -> None:
        self.index: int = 0
        self._limit: int = limit

    def __len__(self) -> int:
        return self._limit

    def __next__(self) -> int:
        if self.index >= self._limit:
            raise StopIteration
        result: int = self.index ** 2
        self.index += 1
        return result


# Instantiating our SquareNumbers class
sq = SquareNumbers(10)


# "Iterating" through sq
while True:
    try:
        print(next(sq))
    except StopIteration:
        print("Iteration is over!")
        break
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# Iteration is over!

# "Iterating" through sq again
while True:
    try:
        print(next(sq))
    except StopIteration:
        print("Iteration is over!")
        break
# Iteration is over!


# Resetting our sequence
sq = SquareNumbers(10)

# Trying to use a for loop to iterate over it
try:
    for num in sq:  # TypeError: 'SquareNumbers' object is not iterable
        print(num)
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: 'SquareNumbers' object is not iterable  // __next__ is not enough for an interable


"""Another example"""


class RandomNumberSequence:
    def __init__(self, seq_length: int, *, lower_limit: int = 0, upper_limit: int = 0) -> None:
        self._index: int = 0
        self._length: int = seq_length
        self.lower_limit: int = lower_limit
        self.upper_limit: int = upper_limit

    def __len__(self) -> int:
        return self._length

    def __next__(self) -> int:
        if self._index >= self._length:
            raise StopIteration
        result: int = randint(self.lower_limit, self.upper_limit)
        self._index += 1
        return result


# Instantiating our RandomNumberSequence class
ten_random_numbers = RandomNumberSequence(10, lower_limit=-100, upper_limit=100)


# "Iterating" through the ten_random_numbers object
while True:
    try:
        print(next(ten_random_numbers))
    except StopIteration:
        print("Iteration is over!")
        break
# -40
# 90
# -90
# 69
# -36
# 25
# -91
# 13
# -34
# -23
# Iteration is over!


# "Iterating" through the ten_random_numbers object again
while True:
    try:
        print(next(ten_random_numbers))
    except StopIteration:
        print("Iteration is over!")
        break
# Iteration is over!


# Resetting our sequence
ten_random_numbers = RandomNumberSequence(10, lower_limit=-100, upper_limit=100)

# Trying to use a for loop to iterate over it
try:
    for num in ten_random_numbers:
        print(num)
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: 'RandomNumberSequence' object is not iterable  // __next__ is not enough for an interable

"""Creating a class decorator that fills in ordering methods"""

from math import sqrt
from typing import Type


def complete_ordering(cls: Type) -> Type:
    """
    Class decorator that fills in missing ordering methods,
    provided __eq__ and __lt__ are implemented.
    """
    if "__eq__" in dir(cls) and "__lt__" in dir(cls):
        cls.__ne__ = lambda self, other: not self == other
        cls.__gt__ = lambda self, other: not self < other
        cls.__ge__ = lambda self, other: self == other or self > other
        cls.__le__ = lambda self, other: self == other or self < other
    else:
        raise AttributeError("Both __eq__ or __lt__ must be implemented.")
    # Return patched class for reassigment
    return cls


@complete_ordering
class Point:
    """A class to represent a two-dimension point"""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: "Point") -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other: "Point") -> bool:
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


"""Creating Point instances"""

p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(0, 0)

"""Testing ordering methods"""

print(p1 == p2) # True
print(p1 != p2) # False
print(p1 < p3)  # False
print(p1 > p3)  # True
print(p1 >= p2) # True
print(p1 <= p2) # True

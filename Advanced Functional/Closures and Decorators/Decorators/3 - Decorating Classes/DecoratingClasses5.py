"""Using the functools.total_ordering class decorator"""


from functools import total_ordering
from math import sqrt


@total_ordering
class Point:
    """A class to represent a two-dimension point"""

    def __init__(self, x: float, y: float) -> None:
        """Initializes the Point coordenates"""
        self.x = x
        self.y = y

    def __abs__(self) -> float:
        """
        The absolute value of a Point 
        is its distance to the origin
        """
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

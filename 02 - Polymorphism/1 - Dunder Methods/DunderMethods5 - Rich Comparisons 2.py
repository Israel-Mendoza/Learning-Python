from __future__ import annotations
from typing import Any
from functools import total_ordering

"""total_ordering is a class decorator that will fill the missing ordering methods."""


@total_ordering
class Vector:
    def __init__(self: Vector, x: int | float, y: int | float) -> None:
        self._x: int | float = x
        self._y: int | float = y

    @property
    def x(self) ->int | float:
        """X value of the vector"""
        return self._x

    @x.setter
    def x(self: Vector, value: Any) -> None:
        if isinstance(value, float) or isinstance(value, int):
            self._x: int | float = value
        else:
            raise ValueError("X value of vector must be a valid number...")

    @property
    def y(self: Vector) -> int | float:
        """Y value of the vector"""
        return self._y

    @y.setter
    def y(self: Vector, value: Any) -> None:
        if isinstance(value, float) or isinstance(value, int):
            self._y = value
        else:
            raise ValueError("Y value of vector must be a valid number...")

    def __eq__(self: Vector, other: Any) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == self.y
        else:
            return NotImplemented

    def __lt__(self: Vector, other: Any) -> bool:
        if isinstance(other, Vector):
            return self.x < other.x and self.y < other.y
        else:
            return NotImplemented


v1 = Vector(10, 20)
v2 = Vector(10, 20)
v3 = Vector(20, 30)

print(f"{v1 is v2 = }")
# v1 is v2 = False
print(f"{v1 == v2 = }")
# v1 == v2 = True
print(f"{v1 > v3 = }")
# v1 > v3 = False

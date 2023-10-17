from __future__ import annotations

"""Using Rich Comparations"""


from typing import Any


class Vector:
    def __init__(self: Vector, x: int | float, y: int | float) -> None:
        self._x: int | float = x
        self._y: int | float = y

    @property
    def x(self: Vector) -> int | float:
        """X value of the vector"""
        return self._x

    @x.setter
    def x(self: Vector, value: Any) -> None:
        if isinstance(value, float) or isinstance(value, int):
            self._x = value
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
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self: Vector, other: Any) -> bool:
        if isinstance(other, Vector):
            return self.x < other.x and self.y < other.y
        else:
            return NotImplemented

    def __le__(self: Vector, other: Any) -> bool:
        if isinstance(other, Vector):
            return self.x <= other.x and self.y <= other.y
        else:
            return NotImplemented

    def __repr__(self: Vector) -> str:
        return f"Vector({self.x}, {self.y})"


v1: Vector = Vector(10, 20)
v2: Vector = Vector(10, 20)
v3: Vector = Vector(20, 30)

print(f"{hex(id(v1)).upper() = }")
# hex(id(v1)).upper() = '0X7F7C50F255B0'
print(f"{hex(id(v2)).upper() = }\n")
# hex(id(v2)).upper() = '0X7F7C50F25310'

print(f"{v1 is v2 = }")
# v1 is v2 = False
print(f"{v1 == v2 = }")
# v1 == v2 = True
print(f"{v1 > v3 = }")
# v1 > v3 = False

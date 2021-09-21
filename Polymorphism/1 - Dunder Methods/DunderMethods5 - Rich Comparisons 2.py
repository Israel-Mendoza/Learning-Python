from typing import Any, Union
from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self._x: Union[int, float] = x
        self._y: Union[int, float] = y

    @property
    def x(self) -> Union[int, float]:
        """X value of the vector"""
        return self._x

    @x.setter
    def x(self, value: Any) -> None:
        if isinstance(value, float) or isinstance(value, int):
            self._x: Union[int, float] = value
        else:
            raise ValueError("X value of vector must be a valid number...")

    @property
    def y(self) -> Union[int, float]:
        """Y value of the vector"""
        return self._y

    @y.setter
    def y(self, value: Any) -> None:
        if isinstance(value, float) or isinstance(value, int):
            self._y = value
        else:
            raise ValueError("Y value of vector must be a valid number...")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == self.y
        else:
            return NotImplemented

    def __lt__(self, other: Any) -> bool:
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

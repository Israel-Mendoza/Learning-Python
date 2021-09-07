from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        """X value of the vector"""
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, float) or isinstance(value, int):
            self._x = value
        else:
            raise ValueError("X value of vector must be a valid number...")

    @property
    def y(self):
        """Y value of the vector"""
        return self._y

    @y.setter
    def y(self, value: float):
        if isinstance(value, float) or isinstance(value, int):
            self._y = value
        else:
            raise ValueError("Y value of vector must be a valid number...")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == self.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector):
            return self.x < other.x and self.y < other.y
        else:
            return NotImplemented


v1 = Vector(10, 20)
v2 = Vector(10, 20)
v3 = Vector(20, 30)

print(f"v1 >= v2 = {v1 is v2}")
print(f"v1 == v2 = {v1 == v2}")
print(f"v1 >= v3 = {v1 > v3}")

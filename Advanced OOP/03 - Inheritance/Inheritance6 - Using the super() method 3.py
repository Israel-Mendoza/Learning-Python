from __future__ import annotations
from typing import override
from math import pi
from typing import Optional

"""Using the super() method"""


class Circle:

    """A class to represent a circle"""

    def __init__(self, radius: int | float) -> None:
        self._radius_setter(radius)
        self._area: float | None = None
        self._perimeter: float | None = None

    def __str__(self: Circle) -> str:
        return f"Radius:\t\t{self.radius}\nArea:\t\t{self.area:.6f}\nPerimeter:\t{self.perimeter:.6f}"

    @property
    def radius(self) -> int | float:
        return self._radius

    @radius.setter
    def radius(self: Circle, new_radius: int | float) -> None:
        self._radius_setter(new_radius)

    def _radius_setter(self, new_radius: int | float) -> None:
        if isinstance(new_radius, (int, float)) and new_radius > 0:
            self._radius: int | float = new_radius
            self._area: float | None = None
            self._perimeter: float | None = None
        else:
            raise ValueError("Radius must be a positive number")

    @property
    def area(self) -> float:
        if self._area is None:
            self._area = pi * self.radius * self.radius
        return self._area

    @property
    def perimeter(self) -> float:
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):

    """UnitCircle class, with radius of value '1" as a read-only property"""

    # Overriding the __init__ method, so it doesn't accept arguments.
    # We will hard code the radius to be "1".
    def __init__(self) -> None:
        super().__init__(1)

    # Overriding the "radius" property to be a read-only property.
    @property
    def radius(self) -> int | float:
        return super().radius


uc: UnitCircle = UnitCircle()

print(uc)
# Radius:		1
# Area:		    3.141593
# Perimeter:	6.283195

from math import pi
from numbers import Real
from typing import Optional, Union


class Circle:
    def __init__(self, radius: Union[int, float]) -> None:
        self._radius_setter(radius)
        self._area = None
        self._perimeter = None

    @property
    def radius(self) -> Union[int, float]:
        return self._radius

    @radius.setter
    def radius(self, new_radius: Union[int, float]) -> None:
        self._radius_setter(new_radius)

    def _radius_setter(self, new_radius: Union[int, float]) -> None:
        if isinstance(new_radius, Real) and new_radius > 0:
            self._radius = new_radius
            self._area: Optional[float] = None
            self._perimeter = None
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

    def __str__(self) -> str:
        return f"Radius:\t\t{self.radius}\nArea:\t\t{self.area:.6f}\nPerimeter:\t{self.perimeter:.6f}"


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self) -> Union[int, float]:
        return super().radius


c = UnitCircle()

print(c)
# Radius:		1
# Area:		    3.141593
# Perimeter:	6.283195

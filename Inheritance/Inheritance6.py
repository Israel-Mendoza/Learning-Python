from numbers import Real
from math import pi


class Circle:
    def __init__(self, radius):
        self._radius_setter(radius)
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius_setter(new_radius)

    def _radius_setter(self, new_radius):
        if isinstance(new_radius, Real) and new_radius > 0:
            self._radius = new_radius
            self._area = None
            self._perimeter = None
        else:
            raise ValueError("Radius must be a positive number")

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius * self.radius
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter

    def __str__(self):
        return f"Radius:\t\t{self.radius}\nArea:\t\t{self.area}\nPerimeter:\t{self.perimeter}"


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius


c = UnitCircle()
print(c)

# Using read-only computed properties

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        """The radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("'radius' attribute must be a positive number")
        self._radius = value

    @property
    def area(self):  # Read-only calculated property
        """The area of the circle"""
        return pi * self.radius * self.radius


# Creating a circle instance
c = Circle(2)
print(f"Radius of 'c': {c.radius}")
print(f"Area of 'c': {c.area}")
print(f"\n")


# Creating the same class, caching the area value
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        """The radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("'radius' must be a positive value")
        print(f"Setting new radius value to {value}")
        self._radius = value
        # Deleting cached area value
        self._area = None

    @property
    def area(self):
        """The area of the circle"""
        if self._area is None:
            print("Calculating new area value...")
            self._area = pi * self.radius * self.radius
        return self._area


# Creating a circle instance
c = Circle(2)
print(f"Radius of 'c': {c.radius}")
print(f"Area of 'c': {c.area}")  # Calculates area and caches it
print(f"Area of 'c': {c.area}")
print(f"Area of 'c': {c.area}")
c.radius = 3
print(f"Area of 'c': {c.area}")  # Calculates are and caches it
print(f"Area of 'c': {c.area}")
print(f"Area of 'c': {c.area}")
print(f"\n")

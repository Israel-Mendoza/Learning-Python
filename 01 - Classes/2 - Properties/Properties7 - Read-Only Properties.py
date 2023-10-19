"""Using read-only computed properties"""

from math import pi


class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius  # Using the setter to set the initial self._radius attribute.

    @property
    def radius(self) -> int | float:
        """The radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError("'radius' attribute must be a positive number")
        self._radius: int | float = value

    @property
    def area(self) -> float:  # Read-only calculated property
        """The area of the circle"""
        return pi * self.radius * self.radius


# Creating a circle instance
c: Circle = Circle(2)
print(f"{c.radius = }")
# c.radius = 2
print(f"{c.area = :.2f}")
# c.area = 12.57
print(f"\n")


# Creating the same class, caching the area value
class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius
        self._area: float | None = None

    @property
    def radius(self) -> int | float:
        """The radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError("'radius' must be a positive value")
        print(f"Setting new radius value to {value}")
        self._radius: int | float = value
        # Deleting cached area value
        self._area: float | None = None

    @property
    def area(self) -> float:
        """The area of the circle"""
        if self._area is None:
            print("Calculating new area value...")
            self._area = pi * self.radius * self.radius
        return self._area


# Creating a circle instance
c: Circle = Circle(2)
# Setting new radius value to 2
print(f"{c.radius = :.2f}")
# c.radius = 2.00
print(f"{c.area = :.2f}")
# Calculating new area value...
# c.area = 12.57
print(f"{c.area = :.2f}")
# c.area = 12.57
print(f"{c.area = :.2f}")
# c.area = 12.57
print(f"{c.area = :.2f}")
# c.area = 12.57

# Setting new radius value to 3
c.radius = 3
print(f"{c.area = :.2f}")  # Calculates are and caches it
# Calculating new area value...
# Area of 'c': c.area = 28.27
print(f"{c.area = :.2f}")
# Area of 'c': c.area = 28.27
print(f"\n")

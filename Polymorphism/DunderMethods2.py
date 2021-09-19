# Creating a vector to test the dunder methods

# TODO: Fix annotations

from numbers import Real
from typing import Any, Tuple


class Vector:
    def __init__(self, *components: Real):
        if len(components) < 1:
            raise ValueError("Cannot create an empty Vector!")
        for component in components:
            if not isinstance(component, Real):
                raise ValueError("All components must be real numbers!")
        self._components: Tuple[Real, ...] = tuple(components)

    @property
    def components(self):
        """The Vector's components"""
        return self._components

    def __len__(self):
        return len(self.components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if self.validate(other):
            components = (x + y for x, y in zip(self.components, other.components))
            return Vector(*components)

    def __sub__(self, other):
        if self.validate(other):
            components = (x - y for x, y in zip(self.components, other.components))
            return Vector(*components)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                components = (x * y for x, y in zip(self.components, other.components))
                return Vector(*components)
            else:
                raise VectorError("Vectors must be of the same length!")
        else:
            if isinstance(other, int) or isinstance(other, float):
                components = (other * x for x in self.components)
                return Vector(*components)
            else:
                return NotImplemented

    def __rmul__(self, other):
        # No need to implement the logic again. The regular __mul__ can be used for this
        return self * other

    def __iadd__(self, other):
        # Implementing the += operator, as if Vector was a mutable object
        if self.validate(other):
            components = (x + y for x, y in zip(self.components, other.components))
            self._components = tuple(components)
            return self

    def __neg__(self):
        # Implementing the negation operator, as if Vector was a mutable object
        components = (x * -1 for x in self.components)
        self._components = tuple(components)
        return self

    def validate(self, other: Any) -> bool:
        """Returns true if the passed vector is the same length as self"""
        if Vector.validate_type(other):
            if len(self) == len(other):
                return True
            else:
                raise VectorError("Vectors must be of the same length!")
        else:
            raise VectorError("Both objects must be instances of Vector!")

    @staticmethod
    def validate_type(a_type: Any) -> bool:
        """Returns true if the passed argument is a Vector instance"""
        return isinstance(a_type, Vector)


class VectorError(TypeError):
    pass


v1 = Vector(2, 3)
v2 = Vector(15, 25)

# Checking that Vector is a mutable class
print(f"{v1} = {hex(id(v1)).upper()}")
v1 = -v1
print(f"{v1} = {hex(id(v1)).upper()}")

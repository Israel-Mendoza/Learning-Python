from __future__ import annotations

"""Dunder Methods"""

# Creating a vector to test the dunder methods

from numbers import Real
from typing import Any, Tuple, Union


class Vector:
    def __init__(self: Vector, *components: int | float) -> None:
        if len(components) < 1:
            raise ValueError("Cannot create an empty Vector!")
        for component in components:
            if not isinstance(component, Real):
                raise ValueError("All components must be real numbers!")
        self._components: tuple[int | float, ...] = tuple(components)

    @property
    def components(self: Vector) -> tuple[int | float, ...]:
        """The Vector's components"""
        return self._components

    def __len__(self: Vector) -> int:
        return len(self.components)

    def __repr__(self: Vector) -> str:
        return f"Vector{self.components}"

    def __add__(self: Vector, other: Vector) -> Vector:
        if self.validate(other):
            components = (x + y for x, y in zip(self.components, other.components))
            return Vector(*components)
        else:
            return self

    def __sub__(self: Vector, other: Vector) -> Vector:
        if self.validate(other):
            components = (x - y for x, y in zip(self.components, other.components))
            return Vector(*components)
        return self

    def __mul__(self: Vector, other: Vector) -> Vector:
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

    def __rmul__(self: Vector, other: Vector) -> Vector:
        # No need to implement the logic again. The regular __mul__ can be used for this
        return self * other

    def __iadd__(self: Vector, other: Vector) -> Vector:
        # Implementing the += operator, as if Vector was a mutable object
        if self.validate(other):
            components = (x + y for x, y in zip(self.components, other.components))
            self._components = tuple(components)
            return self

    def __neg__(self: Vector) -> Vector:
        # Implementing the negation operator, as if Vector was a mutable object
        components = (x * -1 for x in self.components)
        self._components = tuple(components)
        return self

    def validate(self: Vector, other: Any) -> bool:
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


v1: Vector = Vector(2, 3)
v2: Vector = Vector(15, 25)

# Checking that Vector is a mutable class
print(f"{v1} = {hex(id(v1)).upper()}")
# Vector(2, 3) = 0X7F06650EC5B0

v1 = -v1

print(f"{v1} = {hex(id(v1)).upper()}")
# Vector(-2, -3) = 0X7F06650EC5B0

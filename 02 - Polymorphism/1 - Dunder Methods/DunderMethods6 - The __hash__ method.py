from __future__ import annotations
from typing import Any

"""Implementing __hash__"""


# Remember that the __hash__ will be based on an immutable attribute in the object.
# We must enforce that this attribute will not be changed.


class Person:
    def __init__(self, name: str) -> None:
        if self._validate_name(name):
            self._name: str = name
        else:
            raise ValueError("Name must be a valid string")

    def __eq__(self: Person, other: Any) -> bool:
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self: Person) -> int:
        # self._name must be immutable and "read-only"
        return hash(self.name)

    def __repr__(self: Person) -> str:
        return f"Person('{self.name}')"

    @property
    def name(self) -> str:
        """The name of the person"""
        return self._name

    @staticmethod
    def _validate_name(a_name: Any) -> bool:
        return isinstance(a_name, str) and len(a_name.strip()) > 0


p1: Person = Person("Israel")
p2: Person = Person("Arturo")

print(f"{p1 = }")
# p1 = Person('Israel')
print(f"{p2 = }")
# p2 = Person('Arturo')
print(f"{p1 == p2 = }")
# p1 == p2 = False


# Because our object is hashable, we can now use it as dictionary keys:
people: dict[Person, str] = {p1: "Israel Mendoza", p2: "Arturo Sanchez"}

# Looping through the dictionary
for person in people:
    print(f"{person}: {person.name}")
# Person('Israel'): Israel
# Person('Arturo'): Arturo

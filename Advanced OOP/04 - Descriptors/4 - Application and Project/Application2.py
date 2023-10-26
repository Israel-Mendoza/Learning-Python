from __future__ import annotations
from typing import Any

"""Applying descriptors to validate types"""


class ValidType:
    def __init__(self, type_1: type, type_2: type = None) -> None:
        """
        Initializing the type (or types) that the descriptor
        will validate.
        A second type is optional.
        """
        self._type_1: type = type_1
        self._type_2: type = type_2

    def __set_name__(self, cls: type, name: str) -> None:
        """
        Storing the name of the variable the ValidType descriptor will be assigned to.
        """
        self.name: str = name

    def __set__(self, obj: Any, value: Any) -> None:
        """
        Checks whether the passed value is an instance of the valid type(s).
        """
        if self._type_validator(value):
            obj.__dict__[self.name] = value
            return
        # Raising the error:
        types: str = f"'{self._type_1.__name__}'" + (f" or '{self._type_2.__name__}'" if self._type_2 else "")
        raise ValueError(f"'{self.name}' must be of type {types}.")

    def __get__(self, obj: Any, cls: type) -> any:
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)

    def _type_validator(self, value: Any) -> bool:
        if self._type_2:
            return isinstance(value, self._type_2) or isinstance(value, self._type_1)
        return isinstance(value, self._type_1)


class Person:
    name = ValidType(str)
    age = ValidType(int)
    height = ValidType(int, float)

    def __init__(self, name: str, age: int, height: int | float):
        self.name: str = name
        self.age: int = age
        self.height: int | float = height
        print("Person instance was successfully created.")


p: Person | None = None

# Forcing the errors to be raised:
try:
    p = Person("Israel", 31, "1.76")
except ValueError as error:
    print(error)
# 'height' must be of type 'int' or 'float'.

try:
    p = Person("Israel", "31", 1.76)
except ValueError as error:
    print(error)
# 'age' must be of type 'int'.

try:
    p = Person(True, 31, 1.76)
except ValueError as error:
    print(error)
# 'name' must be of type 'str'.

# A Person instance should be created without any problems:
try:
    p = Person("Israel", 31, 1.76)
except ValueError as error:
    print(error)
# Person instance was successfully created.

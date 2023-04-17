from __future__ import annotations

"""Applying descriptors to validate types"""

from numbers import Real


class ValidType:
    def __init__(self, type_1: type, type_2: type = None) -> None:
        """
        Initialized the type (or types) that the descriptor
        will validate.
        A second type is optional.
        """
        self._type_1 = type_1
        self._type_2 = type_2

    def __set_name__(self, cls: type, name: str) -> None:
        self.name: str = name

    def __set__(self, obj: object, value: object) -> None:
        """
        Checks whether the passed value if an instance of the valid type(s).
        """
        if self._type_2:
            if isinstance(value, self._type_1) or isinstance(value, self._type_2):
                obj.__dict__[self.name] = value
                return
            else:
                types: str = f"'{self._type_1.__name__}' or '{self._type_2.__name__}'"
                error: str = f"'{self.name}' must be of type {types}."
                raise ValueError(error)
        if isinstance(value, self._type_1):
            obj.__dict__[self.name] = value
            return
        else:
            error: str = f"'{self.name}' must be of type '{self._type_1.__name__}'."
            raise ValueError(error)

    def __get__(self, obj: object, cls: type) -> any:
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)


class Person:
    name: ValidType = ValidType(str)
    age: ValidType = ValidType(int)
    height: ValidType = ValidType(int, float)

    def __init__(self, name: str, age: int, height: int | float):
        self.name: str = name
        self.age: int = age
        self.height: int | float = height
        print("Person instance was successfully created.")


try:
    p: Person = Person("Israel", 31, "1.76")
except ValueError as error:
    print(error)
# 'height' must be of type 'int' or 'float'.

try:
    p: Person = Person("Israel", "31", 1.76)
except ValueError as error:
    print(error)
# 'age' must be of type 'int'.

try:
    p: Person = Person("Israel", 31, 1.76)
except ValueError as error:
    print(error)
# Person instance was successfully created.

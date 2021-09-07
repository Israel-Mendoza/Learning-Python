"""Applying descriptors to validate types"""


from typing import Any


class Int:

    def __set_name__(self, cls, name) -> None:
        self.name = name

    def __set__(self, obj, value) -> None:
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be a valid integer")
        obj.__dict__[self.name] = value

    def __get__(self, obj, cls) -> Any:
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)


class Float:

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, obj, value):
        if not isinstance(value, float):
            raise ValueError(f"{self.name} must be a valid float")
        obj.__dict__[self.name] = value

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)


class List:

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, obj, value):
        if not isinstance(value, list):
            raise ValueError(f"{self.name} must be a valid list")
        obj.__dict__[self.name] = value

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)


class Person:

    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()


p = Person()

try:
    p.favorite_foods = "hello"
except ValueError as error:
    print(error)
# favorite_foods must be a valid list

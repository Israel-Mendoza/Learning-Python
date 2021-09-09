"""Applying descriptors to validate types"""

from numbers import Real


class ValidType:

    def __init__(self, type_):
        """
        Initialized the type that the descriptor
        will validate.
        """
        self._type = type_

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, obj, value):
        if isinstance(value, self._type):
            obj.__dict__[self.name] = value
        else:
            raise ValueError(
                f"{self.name} must be a valid {self._type.__name__}")

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)


class Person:

    age = ValidType(int)
    height = ValidType(Real)
    tags = ValidType(list)
    favorite_foods = ValidType(list)


p = Person()

try:
    p.height = "hello"
except ValueError as error:
    print(error)
# height must be a valid Real
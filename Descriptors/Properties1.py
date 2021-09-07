"""Remembering how the property class works"""

from numbers import Integral


class Person:

    @property
    def age(self):
        return getattr(self, "_age", None)

    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError("Age must be a valid integer")
        if value < 0:
            raise ValueError("Age must be a positive instance")
        setattr(self, "_age", value)


p = Person()
try:
    p.age = -10
except ValueError as error:
    print(error)
# Age must be a positive instance

class Person:

    def get_age(self):
        return getattr(self, "_age", None)

    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError("Age must be a valid integer")
        if value < 0:
            raise ValueError("Age must be a positive instance")
        setattr(self, "_age", value)

    age = property(get_age, set_age)


p = Person()
try:
    p.age = -10
except ValueError as error:
    print(error)
# Age must be a positive instance
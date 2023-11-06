from __future__ import annotations
from typing import Any


"""Using metaclasses and multiple inheritance"""

"""
    Python won't allow us to use multiple inheritance when 
    the parent classes were created with different metaclasses. 
"""


class Metaclass1(type):
    def __new__(cls, name: str, bases: tuple[Any, ...], namespace: dict[str, Any]):
        print("Using Metaclass1")
        return super().__new__(cls, name, bases, namespace)


class Metaclass2(type):
    def __new__(cls, name: str, bases: tuple[..., type], namespace: dict[str, Any]):
        print("Using Metaclass2")
        return super().__new__(cls, name, bases, namespace)


class Person1(metaclass=Metaclass1):
    pass
# Using Metaclass1


class Person2(metaclass=Metaclass2):
    pass
# Using Metaclass2


class Person3(metaclass=Metaclass1):
    pass
# Using Metaclass1


class Person4(Person1, Person3):  # Person1 and Person3 were created with the same metaclass
    pass
# Using Metaclass1


try:
    class Person4(Person1, Person2):  # Inheriting from multiple types that are subclasses of different metaclasses
        pass
except Exception as err:
    print(f"{type(err).__name__}: {err}")
# TypeError: metaclass conflict:
# the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

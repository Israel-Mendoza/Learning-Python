from __future__ import annotations
from utils.utility_functions import display_obj_namespace_with_class

"""Slotted attributes are data descriptors in the class instance"""


# Python allows (but does not require) to explicitly list
# the attributes an instance will store by naming
# them in a special class attribute called __slots__.
# This is an optimization technique primarily used to save space
# when there will be MANY instances of a class.
#
# When we create a class with slots, the slotted attributes
# will be special class attributes, which type is member_descriptor.
# Being a data descriptor, these class attributes will  store the
# corresponding instance's values accordingly.
#
# Because the instance won't be storing its values, __slots__ will
# prevent the instance to have a namespace (no __dict__ attribute).
# The class won't have neither __dict__ nor __weakref__ either.


class Person:
    # Any Person instance can only have
    # the following two instance attributes:
    __slots__: tuple[str, str] = ("_name", "age")

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name: str = new_name


p = Person("Israel", 28)


display_obj_namespace_with_class(Person)
# Class attribute '__module__': __main__ (<class 'str'>)
# Class attribute '__slots__': ('_name', 'age') (<class 'tuple'>)
# Class attribute '__init__': <function Person.__init__ at 0x7f5653f7bca0> (<class 'function'>)
# Class attribute 'name': <property object at 0x7f56540287c0> (<class 'property'>)
# Class attribute '_name': <member '_name' of 'Person' objects> (<class 'member_descriptor'>) // Slotted attribute
# Class attribute 'age': <member 'age' of 'Person' objects> (<class 'member_descriptor'>) // Slotted attribute
# Class attribute '__doc__': None (<class 'NoneType'>)

"""Analyzing Person.name (property - class attribute)"""

print(f"{type(Person.name)}: {Person.name}")
# type(Person.name) = <class 'property'>

# Person.name has both __set__ and __get__:
print(f"{hasattr(Person.name, '__set__') = }")
# hasattr(Person.name, '__set__') = True
print(f"{hasattr(Person.name, '__get__') = }")
# hasattr(Person.name, '__get__') = True

"""Analyzing Person.age (slotted attribute)"""

print(f"{type(Person.age)}: {Person.age}")
# <class 'member_descriptor'>: <member 'age' of 'Person' objects>

# Slotted attributes are data descriptors.
print(f"{hasattr(Person.age, '__set__') = }")
# hasattr(Person.age, '__set__') = True
print(f"{hasattr(Person.age, '__get__') = }")
# hasattr(Person.age, '__get__') = True

"""Analyzing Person._name (slotted attribute)"""

print(f"{type(Person._name)}: {Person._name}")
# <class 'member_descriptor'>: <member '_name' of 'Person' objects>

# Slotted attributes are data descriptors.
print(f"{hasattr(Person._name, '__set__') = }")
# hasattr(Person._name, '__set__') = True
print(f"{hasattr(Person._name, '__get__') = }")
# hasattr(Person._name, '__get__') = True


####################################################################
####################################################################

"""Instances of slotted classes won't have a __dict__ attribute"""

print(f"{hasattr(p, '__dict__') = }")
# hasattr(p, '__dict__') = False

# Trying to add a new instance attribute that's not in the __slots__ tuple:
try:
    p.email = "email@email.com"
except Exception as error:
    print(f"{type(error).__name__}: {error}")
# AttributeError: 'Person' object has no attribute 'email'

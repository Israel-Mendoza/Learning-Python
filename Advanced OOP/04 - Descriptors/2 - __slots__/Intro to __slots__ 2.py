from __future__ import annotations
from utils.utility_functions import display_obj_namespace_with_class

"""
    When we add "__dict__" to the slots in the class, 
    we're allowing the instance to have a namespace and store
    attributes not specified in the class' slots.
"""


class Person:
    __slots__: tuple[str, str] = "name", "__dict__"

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


display_obj_namespace_with_class(Person)
# Class attribute '__module__': __main__ (<class 'str'>)
# Class attribute '__slots__': ('name', '__dict__') (<class 'tuple'>)
# Class attribute '__init__': <function Person.__init__ at 0x7f96ee02daf0> (<class 'function'>)
# Class attribute 'name': <member 'name' of 'Person' objects> (<class 'member_descriptor'>) // Slotted attribute
# Class attribute '__dict__': <attribute '__dict__' of 'Person' objects> (<class 'getset_descriptor'>) !!!
# Class attribute '__doc__': None (<class 'NoneType'>)

p = Person("Israel", 28)

# Person attributes have a namespace because __dict__ was included in __slots__
print(f"p's namespace: {vars(p)}")
# p's namespace: {'age': 28}

# Having a __dict__ won't prevent us from adding new instance attributes:
p.email = "email@email.com"

# We see the items in __dict__, except for the slotted "name"
print(f"p's namespace: {vars(p)}")
# p's namespace: {'age': 28, 'email': 'email@email.com'}

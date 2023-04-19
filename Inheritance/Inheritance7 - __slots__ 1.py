from __future__ import annotations

"""Inheritance with __slots__"""

# When the superclass implements slots, but the inheriting class doesn't,
# the instances of the inheriting class will also inherit the superclass'
# slots, but will also have a namespace of its own (because the class it
# is instantiated from doesn't have slots).


class Person:
    __slots__: tuple[str] = ("name",)

    def __init__(self: Person, name: str) -> None:
        self.name: str = name


class Student(Person):
    """Subclass of Person"""


p: Person = Person("Margarita")
s: Student = Student("Israel")

# Person instances don't have a namespace:
try:
    print(f"Person namespace: {vars(p)}")
except TypeError as error:
    print("Person namespace: ")
    print(f"\tTypeError: {error}")
# Person namespace:
# TypeError: vars() argument must have __dict__ attribute

# Student instances DO have a namespace:
print(f"Student namespace: {vars(s)}")
# Student namespace: {}


# Because the Student subclass doesn't implement slots, it inherits the one
# from the parent class, but it also makes use of the __dict__ namespace dictionary.
s.major: str = "Computer Science"
s.name: str = "Israel"

print(s.major)
# Computer Science

# Printing the Student instance's namespace:
print(f"{s.__dict__ = }")
# s.__dict__ = {'major': 'Computer Science'}
print(f"Person class namespace: \n\t{vars(Person)}")
# Person class namespace: {'__module__': '__main__', 
#                           '__annotations__': {'__slots__': 'tuple[str]'}, 
#                           '__slots__': ('name',), 
#                           '__init__': <function Person.__init__ at 0x7f20a8ca05e0>, 
#                           'name': <member 'name' of 'Person' objects>, 
#                           '__doc__': None}

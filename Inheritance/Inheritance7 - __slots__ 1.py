"""Inheritance with __slots__"""

# When the superclass implements slots, but the inheriting class doesn't,
# the instances of the inheriting class will also inherit the superclass'
# slots, but will also have a namespace of its own (because the class it
# is instantiated from doesn't have slots).


class Person:
    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    """Subclass of Person"""


p = Person("Margarita")
s = Student("Israel")

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


# Because the Student subclass doesn't
# implement slots, it inherits the one
# from the parent class, but it also makes
# use of the __dict__ namespace dictionary.
s.major = "Computer Science"

print(s.major)
# Computer Science

# Printing the Student instance's namespace:
print(f"{s.__dict__ = }")
# s.__dict__ = {'major': 'Computer Science'}

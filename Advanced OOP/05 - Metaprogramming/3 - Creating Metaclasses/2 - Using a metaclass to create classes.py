from __future__ import annotations
from typing import Any

"""
Metaclasses are classes that are use to create other classes.
Remember that, in order to create a class using type(), we need:
    1. The name of the class
    2. The class bases the new class will inherit from (squeezed into a tuple)
    3. The namespace of the class (a dictionary)
"""


class CustomType(type):
    def __new__(cls, name: str, bases: tuple, namespace: dict[str, Any]) -> CustomType:
        print(f"Creating the {name} class.")
        new_class: CustomType = super().__new__(cls, name, bases, namespace)
        new_class.say_hello = lambda self: f"{self} says: Hello World!"
        return new_class


class Person(metaclass=type):  # metaclass=type is the default
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def introduce(self) -> None:
        print(f"My name is {self.name} and I'm {self.age} years old.")


class Student(Person, metaclass=CustomType):  # We'll use the CustomType metaclass to create "Student"
    def study(self) -> None:
        print(f"I'm {self.name} and I study hard!")

    def __str__(self) -> str:
        return f"Student called {self.name}"


"""Creating the Student class."""

print(f"Class name: {Person.__name__} - Type: {type(Person)}")
# Class name: Person - Type: <class 'type'>
print(f"Class name: {Student.__name__} - Type: {type(Student)}")
# Class name: Student - Type: <class '__main__.CustomType'>

s1 = Student("Israel", 28)
print(s1.say_hello())
# Student called Israel says: Hello World!

from __future__ import annotations
from typing import Any

"""Inheritance and __slots__"""

# When an object is created from a class that inherited slots,
# but doesn't implement them itself, the instance object will have a __dict__.
# When an object is created from a class that did NOT inherit slots,
# but the class itself implements them, the instance object will have a __dict__.
#
# In short, the final object will try to inherit the __dict__ when it can.


def display_obj_namespace(an_object: Any) -> None:
    """Simple function to print an object's namespace"""
    print(f"OBJECT'S NAMESPACE:")
    for k, v in vars(an_object).items():
        if "__slots__" in vars(an_object) and k in vars(an_object)["__slots__"]:
            print(f"Slotted attribute '{k}': {v}")
        else:
            print(f"Class attribute '{k}': {v}")


"""Super class doesn't have slots. Subclass has slots."""


class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Student(Person):
    __slots__: tuple[str, str] = "school", "student_number"

    def __init__(self, name: str, school: str, student_number: str) -> None:
        super().__init__(name)
        self.school: str = school
        self.student_number: str = student_number


# Because the Student subclass implements slots,
# but inherits from a class that doesn't,
# Student will have an instance dictionary as well

s: Student = Student("James Bond", "MI6 Prep School", "007")

# __dict__ and __weakref__ available:
display_obj_namespace(Person)
# OBJECT'S NAMESPACE:
# Class attribute '__module__': __main__
# Class attribute '__init__': <function Person.__init__ at 0x7f44ab610820>
# Class attribute '__dict__': <attribute '__dict__' of 'Person' objects>
# Class attribute '__weakref__': <attribute '__weakref__' of 'Person' objects>
# Class attribute '__doc__': None

# No __dict__ or __weakref__ available:
display_obj_namespace(Student)
# OBJECT'S NAMESPACE:
# Class attribute '__module__': __main__
# Class attribute '__slots__': ('school', 'student_number')
# Class attribute '__init__': <function Student.__init__ at 0x7f44ab6108b0>
# Slotted attribute 'school': <member 'school' of 'Student' objects>
# Slotted attribute 'student_number': <member 'student_number' of 'Student' objects>
# Class attribute '__doc__': None

# Student objects will have a __dict__!!!
display_obj_namespace(s)
# OBJECT'S NAMESPACE:
# Class attribute 'name': James Bond


"""Super class has slots. Subclass doesn't have slots."""


class Person:
    __slots__: tuple[str] = "name",

    def __init__(self, name: str) -> None:
        self.name: str = name


class Student(Person):
    def __init__(self, name: str, school: str, student_number: str) -> None:
        super().__init__(name)
        self.school: str = school
        self.student_number: str = student_number


# Because the Person class implements slots,
# but its subclass Student doesn't, Student
# will have an instance dictionary as well.

s: Student = Student("James Bond", "MI6 Prep School", "007")

display_obj_namespace(s)
# OBJECT'S NAMESPACE:
# Class attribute 'school': MI6 Prep School
# Class attribute 'student_number': 007

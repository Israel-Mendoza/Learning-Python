from __future__ import annotations

"""Inheritance with __slots__"""

# When the superclass implements slots, and the inheriting class implements
# them as well, the instances of the inheriting class will inherit both slots.
# Needless to say, the instance won't have a __dict__.


def display_obj_namespace(an_object: type) -> None:
    """Displays the namespace in a given class"""
    print(f"{an_object.__name__.upper()}'S NAMESPACE:")
    for k, v in vars(an_object).items():
        if "__slots__" in vars(an_object) and k in vars(an_object)["__slots__"]:
            print(f"Slotted attribute '{k}': {v}")
        else:
            print(f"Class attribute '{k}': {v}")


class Person:
    __slots__: tuple[str] = "name",

    def __init__(self, name: str) -> None:
        self.name: str = name


class Student(Person):

    __slots__: tuple[str, str] = "school", "student_number"

    def __init__(self, name: str, school: str, student_number: str) -> None:
        super().__init__(name)
        self.school: str = school
        self.student_number: str = student_number


# Instantiating a Student obkect:
s: Student = Student("James Bond", "MI6 Prep School", "007")

# Because the Student subclass also implements slots,
# there is no instance dictionary.
try:
    s.email: str = "email@email.com"
except Exception as error:
    print(f"{type(error).__name__}: {error}")
# AttributeError: 'Student' object has no attribute 'email'

# No __dict__ or __weakref__. Notice the slotted attribute:
display_obj_namespace(Person)
# PERSON'S NAMESPACE:
# Class attribute '__module__': __main__
# Class attribute '__slots__': ('name',)
# Class attribute '__init__': <function Person.__init__ at 0x7f4f2c93b790>
# Slotted attribute 'name': <member 'name' of 'Person' objects>
# Class attribute '__doc__': None

# No __dict__ or __weakref__. Notice the slotted attributes:
display_obj_namespace(Student)
# STUDENT'S NAMESPACE:
# Class attribute '__module__': __main__
# Class attribute '__slots__': ('school', 'student_number')
# Class attribute '__init__': <function Student.__init__ at 0x7f4f2c93b820>
# Slotted attribute 'school': <member 'school' of 'Student' objects>
# Slotted attribute 'student_number': <member 'student_number' of 'Student' objects>
# Class attribute '__doc__': None

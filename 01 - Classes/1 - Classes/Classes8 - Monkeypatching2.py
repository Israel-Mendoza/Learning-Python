from __future__ import annotations
from typing import Any
from types import MethodType
from collections.abc import Callable


class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name


p1: Person = Person("Israel")
p2: Person = Person("Mike")

print(f"{p1.__dict__ = }")
print(f"{p2.__dict__ = }")
# p1.__dict__ = {'name': 'Israel'}
# p2.__dict__ = {'name': 'Mike'}


# Creating a couple of functions to be added later as methods


def say_hello(self: Person):
    print(f"{self.name} says 'Hello!'")


def say_bye(self: Person):
    print(f"{self.name} says 'Bye!'")


# Setting "bound method" objects to attributes
p1.say_hello = MethodType(say_hello, p1) # setattr(p1, "say_hello", MethodType(say_bye, p1))
p1.say_bye = MethodType(say_bye, p1) # setattr(p1, "say_bye", MethodType(say_bye, p1))
print(f"{p1.__dict__ = }")
# p1.__dict__ = {
#  'name': 'Israel', 
# 'say_hello': <bound method say_hello of <__main__.Person object at 0x7f30fb148f40>>, 
# 'say_bye': <bound method say_bye of <__main__.Person object at 0x7f30fb148f40>>
# }
print(f"{p2.__dict__ = }")
# p2.__dict__ = {'name': 'Mike'}


"""Monkeypatching class instances using the MethodType object"""


class Employee:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.full_name: str = f"{first_name} {last_name}"

    def defining_work(self, func: Callable[[Employee], Any]) -> None:
        """
        Method which allows us to set the self.work() bound method.
        Args:
            func [Callable]: A function that accepts one arg (the instance). 
                                This function will be converted into a method type
                                and assigned to the self.work attribute.
        """
        # self.work = MethodType(func, self) or:
        setattr(self, "work", MethodType(func, self))

    def work(self):
        """
        Method will raise an error if not implemented
        using the "defining_work" method.
        """
        raise AttributeError("Use 'defining_work' before calling this method!")


e1: Employee = Employee("Israel", "Mendoza")
e2: Employee = Employee("Christopher", "Nolan")


# Creating the functions that will eventually be methods


def program(obj: Employee):
    print(f"{obj.full_name} is now programming.")


def movie_making(obj: Employee):
    print(f"{obj.full_name} is now making a movie.")


# Calling the 'work' method prior to implementation
try:
    e1.work()
except AttributeError as error:
    print(error)
# Use 'defining_work' before calling this method!

# Using the defining_work method to implement the work method
e1.defining_work(program)
e2.defining_work(movie_making)

# Calling the "same" method on both instances

e1.work()
# Israel Mendoza is now programming.
e2.work()
# Christopher Nolan is now making a movie.

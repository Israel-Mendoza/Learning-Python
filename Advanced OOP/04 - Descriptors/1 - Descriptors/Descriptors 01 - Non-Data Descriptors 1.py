from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo
from time import sleep as timer
from utils.utility_functions import print_address


"""Introducing descriptors"""


# Descriptors are classes, which instances are used as other class attributes,
# so they can be accessed either by this other class or their instances.
# There are two types of descriptors:
#
#     Non-data descriptors: Implement only the __get__ method.
#     Data descriptors: Implements the __set__ and/or __delete__ methods.
#
#
# These are the arguments that are automatically passed to the different descriptor methods:
#     __get__(self, instance, owner):
#             self:       The descriptor instance.
#             instance:   The instance on which the instance is accessed.
#             owner:      The superclass of the instance. None if the descriptor
#                       is accessed via the class itself.
#     __set__(self, instance, value):
#             self:       The descriptor instance.
#             instance:   The instance on which the instance is accessed.
#             value:      The value after the "=" sign, which triggers the __set__
#                   method in the first place.


class CurrentTime:
    """Instance intended to be used as a non-data descriptor"""

    def __init__(self) -> None:
        print("Creating a CurrentTime instance.")

    def __get__(self, instance: Any, owner: type):
        print(f"__get__ was accessed! Class: <{owner.__name__}> - Instance: {instance}")
        return datetime.now(tz=ZoneInfo("America/Mexico_City")).isoformat()


class Person:
    """Class to represent a person"""
    # CurrentTime instance created at compile time, 
    # meaning, the CurrentTime object will be created 
    # even before instantiating a Person object for the first time.
    time: CurrentTime = CurrentTime()  # Non-data descriptor

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        return f"<Person object at {hex(id(self)).upper()}>"

    def tell_time(self) -> None:
        # By accessing the time attribute, we are calling the descriptor's __get__ method.
        print(f"My name is {self.name} and the datetime is {self.time}")


# Creating a CurrentTime instance // Python prints this at this point!


p: Person = Person("Israel", 28)

print_address("p", p)
# p @ 0X100B5A270
print_address("Person", Person)
# Person @ 0X11860AE90

# Calling "tell_time()", which accesses the "time" descriptor via the Person instance
p.tell_time()
# __get__ was accessed! Class: <Person> - Instance: <Person object at 0X100B5A270>
# My name is Israel and the datetime is 2023-10-21T23:52:01.047229-06:00

# Killing three seconds...
timer(3)

# Calling the "tell_time" method three seconds later,
# which accesses the "time" descriptor via the Person instance
p.tell_time()
# __get__ was accessed! Class: <Person> - Instance: <Person object at 0X100B5A270>
# My name is Israel and the datetime is 2023-10-21T23:52:04.052600-06:00

# Accessing the "time" descriptor via the Person instance
print(p.time)
# __get__ was accessed! Class: <Person> - Instance: <Person object at 0X100B5A270>
# 2023-10-21T23:52:04.052674-06:00

# Accessing the "time" descriptor via the Person class
print(Person.time)
# __get__ was accessed! Class: <Person> - Instance: None
# 2023-10-21T23:52:04.052695-06:00

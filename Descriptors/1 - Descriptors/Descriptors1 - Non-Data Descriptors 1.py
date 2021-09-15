"""Introducing descriptors"""

# Descriptors are classes, which instances are
# used as other class attributes, so they can be accessed
# either by this other class or their instances.
# There are two types of descriptors:
#     Non-data descriptors: Implement only the __get__ method.
#     Data descriptors: Implements the __set__ and/or __delete__ methods.
# These are the arguments that are automatically passed 
# to the different descriptor methods:
#   __get__(self, instance, owner):
#           self: The descriptor instance.
#           instance: The instance on which the the instance is accessed.
#           owner: The superclass of the instance. None if the descriptor
#                   is accessed via the class itself.
#   __set__(self, instance, value):
#           self: The descriptor instance.
#           instance: The instance on which the the instance is accessed.
#           value: the value after the "=" sign, which triggers the __set__
#                   method in the first place.


from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep as timer


class CurrentTime:
    """Instance intended to be used as a non-data descriptor"""

    def __init__(self) -> None:
        print("Creating a CurrentTime instance.")

    def __get__(self, instance, owner):
        print(f"__get__ was accessed! Class: {owner} - Instance: {instance}")
        return datetime.now(tz=ZoneInfo("America/Mexico_City")).isoformat()


class Person:
    """Class to represent a person"""
    # CurrentTime instance created at compile time, 
    # meaning, the CurrentTime object will be created 
    # even before instantiating a Person object for the firt time.
    time = CurrentTime()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell_time(self):
        # By accessing the time attribute,
        # we are calling the descriptor's __get__ method.
        print(f"My name is {self.name} and the datetime is {self.time}")


# Creating a CurrentTime instance // Python prints this at this point!


p = Person("Israel", 28)

print(f"{hex(id(p)) = }")
# hex(id(p)) = '0x7fadef55a370'
print(f"{hex(id(Person)) = }")
# hex(id(Person)) = '0x1438d20'

# Calling "tell_time()", which accesses the "time" descriptor via the Person instance
p.tell_time()
# __get__ was accessed! Class: <class '__main__.Person'> - Instance: <__main__.Person object at 0x7fadef55a370>
# My name is Israel and the datetime is 2021-09-08T20:41:14.620325-05:00

# Killing three seconds...
timer(3)

# Calling the "tell_time" method three seconds later,
# which accesses the "time" descriptor via the Person instance
p.tell_time()
# __get__ was accessed! Class: <class '__main__.Person'> - Instance: <__main__.Person object at 0x7fadef55a370>
# My name is Israel and the datetime is 2021-09-08T20:41:17.623614-05:00

# Accessing the "time" descriptor via the Person instance
print(p.time)
# __get__ was accessed! Class: <class '__main__.Person'> - Instance: <__main__.Person object at 0x7fadef55a370>
# 2021-09-08T20:41:17.623685-05:00

# Accessing the "time" descriptor via the Person class
print(Person.time)
# __get__ was accessed! Class: <class '__main__.Person'> - Instance: None
# 2021-09-08T20:41:17.623721-05:00

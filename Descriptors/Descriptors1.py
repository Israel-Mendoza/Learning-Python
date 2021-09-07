"""
Introducing descriptors.
Descriptors are classes, which instances are
used as other class attributes, so they can be accessed
either by this other class or their instances.
There are two types of descriptors:
    Non-data descriptors: Implement only the __get__ method.
    Data descriptors: Implements the __set__ and/or __delete__ methods.
"""

from datetime import datetime
from time import sleep as timer


class CurrentTime:
    """Instance intended to be used as a non-data descriptor"""

    def __init__(self) -> None:
        print("Creating a CurrentTime instance.")

    def __get__(self, instance, owner):
        print(f"Class: {owner} - Instance: {instance}")
        return datetime.now().isoformat()


class Person:
    """Class to represent a person"""
    # CurrentTime instance created at compile time.
    time = CurrentTime()
    # -> Creating a CurrentTime instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell_time(self):
        # By accessing the time attribute,
        # we are calling the descriptor's __get__ method.
        print(f"My name is {self.name} and the datetime is {self.time}")





p = Person("Israel", 28)

# Calling the "tell_time" method, which accesses 
# the "time" descriptor via the Person instance
p.tell_time()
# Class: <class '__main__.Person'> - Instance: <__main__.Person object at 0x036E41F0>
# My name is Israel and the datetime is 2020-09-27T21:00:58.542787

timer(3)

# Calling the "tell_time" method three seconds later, 
# which accesses the "time" descriptor via the Person instance
p.tell_time()
# Class: <class '__main__.Person'> - Instance: <__main__.Person object at 0x02D90BF8>
# My name is Israel and the datetime is 2020-09-27T21:01:01.546067

# Accessing the "time" descriptor via the Person instance
print(p.time)
# Class: <class '__main__.Person'> - Instance: <__main__.Person object at 0x02D90BF8>
# 2020-09-27T21:01:01.546067

# Accessing the "time" descriptor via the Person class
print(Person.time)
# Class: <class '__main__.Person'> - Instance: None
# 2020-09-27T21:01:01.546067

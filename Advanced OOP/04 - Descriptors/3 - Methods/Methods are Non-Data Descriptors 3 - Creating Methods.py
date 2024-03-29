from __future__ import annotations
from types import MethodType
from typing import Any
from collections.abc import Callable

"""Creating a method the descriptor way"""

# In this example, we'll create a function that accepts two parameters:
# 1. A class instance.
# 2. A random argument (in this case, a string).
# Then, we will create a NON-DATA Descriptor that takes a function in its __init__ method.
# The __get__ method will return
# 1. The function when called from the class
# 2. The function converted into a Method bound to the calling instance.


# Creating a simple function that will serve as a method:
def say_hello(this: Any, message: str) -> None:
    print(f"{this.name} says '{message}'")


class CallableDescriptor:
    def __init__(self, a_func: Callable[[Any, str], None]) -> None:
        self.a_func: Callable[[Any, str], None] = a_func

    def __get__(self, obj: Any, cls: type) -> Callable[[Any, str], None] | MethodType:
        """
        Returns the self.a_func function when called from the class, and the
        Returns the MethodType version of self.a_func if called from the instance.
        """
        if obj is None:
            return self.a_func
        return MethodType(self.a_func, obj)  # Bounding the function to the passed instance


class Person:
    # A function, if called from Person.
    # A method, if called from a Person instance.
    say_something: CallableDescriptor = CallableDescriptor(say_hello)

    def __init__(self, name: str) -> None:
        self.name: str = name


p = Person("Israel")

# Analyzing the '__init__' attribute from the class and from the instance.
# This is just to see how a regular method looks like when created "normally".
print(f"{type(Person.__init__) = }")
# type(Person.__init__) = <class 'function'>
print(f"{type(p.__init__) = }")
# type(p.__init__) = <class 'method'>

# Analyzing the 'say_something' attribute, which is our CallableDescriptor descriptor:
print(f"{type(Person.say_something) = }")
# type(Person.say_something) = <class 'function'>
print(f"{type(p.say_something) = }")
# type(p.say_something) = <class 'method'>

# Calling the function, passing the instance as the first argument:
Person.say_something(p, "¡Buenos días!")
# Israel says '¡Buenos días!'
p.say_something("Bonjour!")
# Israel says 'Bonjour!'

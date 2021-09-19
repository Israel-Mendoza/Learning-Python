"""Creating a method the descriptor way"""


from typing import Union
from types import FunctionType, MethodType


def say_hello(this, message: str) -> None:
    print(f"{this.name} says '{message}'")


class CallableDescriptor:

    def __init__(self, a_func: FunctionType) -> None:
        self.a_func: FunctionType = a_func

    def __get__(self, obj, cls) -> Union[FunctionType, MethodType]:
        """
        Returns the self.a_func funtion when 
        called from the class, and the MethodType 
        version of self.a_func if called from the instance.
        """
        if obj is None:
            return self.a_func
        return MethodType(self.a_func, obj)


class Person:

    # A function if called from Person, and
    # a method if called from a Person instance.
    say_somethig = CallableDescriptor(say_hello)

    def __init__(self, name):
        self.name = name


p = Person("Israel")

# Analyzing the '__init__' attribute:
print(f"{type(Person.__init__) = }")
# type(Person.__init__) = <class 'function'>
print(f"{type(p.__init__) = }")
# type(p.__init__) = <class 'method'>

# Analyzing the 'say_something' attribute:
print(f"{type(Person.say_somethig) = }")
# type(Person.say_somethig) = <class 'function'>
print(f"{type(p.say_somethig) = }")
# type(p.say_somethig) = <class 'method'>

Person.say_somethig(p, "¡Buenos días!")
# Israel says '¡Buenos días!'
p.say_somethig("Bonjour!")
# Israel says 'Bonjour!'

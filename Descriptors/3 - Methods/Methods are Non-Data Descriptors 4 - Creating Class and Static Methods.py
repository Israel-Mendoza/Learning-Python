from __future__ import annotations

"""Descriptors replicating class and static methods"""


from typing import Any
from types import FunctionType


class MyClassMethod:
    def __init__(self, a_func: FunctionType) -> None:
        self.wrapped_function: FunctionType = a_func

    def __get__(self, instance: object, owner: type) -> Any:
        """
        Returns self.__call__ not before making sure
        we're setting self.owner as the actual class,
        whether it's called from the class or the instance.
        """
        if instance is None:
            self.owner: type = owner
        else:
            self.owner: type = instance.__class__
        return self.__call__

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Runs the self.wrapped_function, passing self.owner
        as the first argument, and then args and wkargs.
        Returns the result of the called function.
        """
        return self.wrapped_function(self.owner, *args, **kwds)


class MyStaticMethod:
    def __init__(self, a_func: FunctionType) -> None:
        self.wrapped_function: FunctionType = a_func

    def __get__(self, instance: object, owner: type) -> Any:
        """
        A static method doesn't care about the caller,
        that's why neither 'instance' nor 'owner' are used.
        Returns self.__call__
        """
        return self.__call__

    def __call__(self, *args, **kwargs) -> Any:
        """
        Runs self.wrapped_function, passing *args and **kwargs
        Returns the result of the called function.
        """
        return self.wrapped_function(*args, **kwargs)


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    @MyClassMethod
    def say_hello(cls, name, times):
        return f"{cls.__name__} says hi to {name} {times} times!"

    @MyStaticMethod
    def say_hi():
        return f"I just wanna say hi!"


class Student(Person):
    pass


p = Person("Israel")
s = Student("Israel")

print(Person.say_hello("Mago", 1000))
# Person says hi to Mago 1000 times!
print(p.say_hello("Mago", 1000))
# Person says hi to Mago 1000 times!

print(Person.say_hi())
# I just wanna say hi!
print(p.say_hi())
# I just wanna say hi!

print(Student.say_hello("Mago", 1000))
# Student says hi to Mago 1000 times!
print(s.say_hello("Mago", 1000))
# Student says hi to Mago 1000 times!

print(Student.say_hi())
# I just wanna say hi!
print(s.say_hi())
# I just wanna say hi!

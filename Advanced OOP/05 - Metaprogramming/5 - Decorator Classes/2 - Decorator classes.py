from __future__ import annotations
from typing import Any, Callable
from types import MethodType

"""Using a class as a decorator"""

"""
    We've seen it is a little bit tricky to use a class as a method decorator. 
    
    In this example, we'll make the decorator class implement the descriptor
    protocol.
    
    Without the descriptor protocol, any method we decorate with our decorator
    class will be a simple callable object that won't know how to react when
    called from either a class or an instance the same way a "native" method
    does. 
"""


class Logger:
    def __init__(self, a_func: Callable[..., Any]) -> None:
        self.func: Callable[..., Any] = a_func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

    def __get__(self, instance: object, owner: type) -> MethodType | Logger:
        """
        If accessed from an instance, we'll create a method type
        bounding the Logger instance (self) to the passed instance
        """
        print(f"Logger's __get__ method called: {instance}(instance) - {owner}(owner)")
        if instance:
            method = MethodType(self, instance)  # We can bind self with the instance because self is a callable
            print(f"Returning Logger instance bound: {method}")
            return method
        print("Returning Logger instance unbound...")
        return self


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    @Logger
    def say_hi(self) -> str:
        return f"{self.name} says 'Hello World!'"

    @classmethod
    @Logger
    def cls_method(cls) -> str:
        return f"{cls.__name__} says hello!"

    @staticmethod
    @Logger     # static methods are acting weird. You can decorate them as simple callables now :)
    def static_method() -> str:
        return "A static method says hello!"


p = Person("Israel")

# First, let's make sure the descriptor protocol is in place:
p.say_hi
# Logger's __get__ method called: <__main__.Person object at 0x1022d8800>(instance) - <class '__main__.Person'>(owner)
# Returning Logger instance bound: <bound method ? of <__main__.Person object at 0x1022d8800>>


# We can now call the wrapped method from an instance:
print(p.say_hi())
# Logger's __get__ method called: <__main__.Person object at 0x1022d8800>(instance) - <class '__main__.Person'>(owner)
# Returning Logger instance bound: <bound method ? of <__main__.Person object at 0x1022d8800>>
# Calling say_hi
# Israel says 'Hello World!'

print(p.cls_method())
# Logger's __get__ method called: <class '__main__.Person'>(instance) - <class '__main__.Person'>(owner)
# Returning Logger instance bound: <bound method ? of <class '__main__.Person'>>
# Calling cls_method
# Person says hello!

print(p.static_method())  # It's as if the decorated method calls the Logger's __call__ directly, bypassing __get__
# Calling static_method
# A static method says hello!

try:
    print(Person.say_hi())
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# Logger's __get__ method called: None(instance) - <class '__main__.Person'>(owner)
# Returning Logger instance unbound...
# Calling say_hi
# TypeError: say_hi() missing 1 required positional argument: 'self'

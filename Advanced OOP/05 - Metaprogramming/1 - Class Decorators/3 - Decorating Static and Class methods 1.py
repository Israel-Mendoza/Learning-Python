"""Caveats of using class decorators to decorate static and class methods"""


from functools import wraps
from typing import Any, Callable

AnyCallable = Callable[..., Any]


def function_logger(fn: AnyCallable) -> AnyCallable:
    """A function decorator"""
    @wraps(fn)
    def inner(*args: Any, **kwargs: Any) -> Any:
        result = fn(*args, **kwargs)
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        print(f"Returned value: {result}\n")
        return result

    return inner


def logger_to_class_callables(cls: type) -> type:
    """
    A class decorator that will take the 'function_logger' function 
    decorator and will decorate all callables in that function with it.
    """
    for attr_name, attr_value in vars(cls).items():
        if callable(attr_value):
            print(f"Decorating {cls.__name__}.{attr_name} with function_logger")
            setattr(cls, attr_name, function_logger(attr_value))

    return cls


@logger_to_class_callables
class Person1:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def instance_method(self) -> None:
        print(f"{self} instance says hello!")

    @staticmethod
    def static_method() -> None:
        print(f"Hello from the static method")

    @classmethod
    def class_method(cls) -> None:
        print(f"{cls.__name__} says hello!")


# Output:
# Decorating Person.__init__ with function_logger
# Decorating Person.instance_method with function_logger


p1 = Person1("Israel", 28)
# Output:
# Function called: Person1.__init__((<__main__.Person object at 0x0000027CC63A36A0>, 'Israel', 28), {})
# Returned value: None

p1.static_method()
# static_method called!
p1.class_method()
# Person says hello!

# Why weren't the class method and the static method decorated?
# Because these descriptors are not callable! They are descriptors.
# They execute the __get__ method when accessed, but not the __call__ method

print(type(Person1.__dict__["static_method"]))  # <class 'staticmethod'>
print(type(Person1.__dict__["class_method"]))  # <class 'classmethod'>
print(callable(Person1.__dict__["static_method"]))  # False
print(callable(Person1.__dict__["class_method"]))  # False


"""Decorating static and class methods"""

# If we want to decorate static and class methods, we must decorate them
# before making them static or class methods.
# If we do it the other way around, it won't work due to the same reason
# our logger_to_class_callables wasn't able to decorate them:
# function_loger will treat the staticmethod as a callable, and it's not!


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def instance_method(self):
        print(f"{self} instance says hello!")

    @staticmethod
    @function_logger
    def static_method():
        print(f"Hello from the static method")

    @classmethod
    @function_logger
    def class_method(cls):
        print(f"{cls.__name__} says hello!")


Person.static_method()
# Output:
# Hello from the static method
# Function called: Person.static_method((), {})
# Returned value: None

Person.class_method()
# Person says hello!
# Function called: Person.class_method((<class '__main__.Person'>,), {})
# Returned value: None

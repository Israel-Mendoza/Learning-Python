from __future__ import annotations
from functools import wraps
from typing import Any, Callable

"""Using class decorators to decorate all callables in a class"""


# Creating type annotation alias
AnyCallable = Callable[..., Any]


"""Decorating methods in a class one by one... Argh..."""


# Creating a simple function logger decorator to be used to decorate classes' methods
def function_logger(fn: AnyCallable) -> AnyCallable:
    """Function decorator to decorate functions and give them logging capabilities."""
    @wraps(fn)  # Using wraps to keep the function's annotations/docs. Don't overthink about it
    def inner(*args: Any, **kwargs: Any) -> Any:
        result: Any = fn(*args, **kwargs)  # Calling original function and storing its return value.
        # Printing the name of the function and the args it was called with:
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        # Printing the returned value of the called function:
        print(f"Returned value: {result}\n")
        return result

    return inner


class Person1:
    @function_logger
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    @function_logger
    def greet(self) -> str:
        return f"Hello, my name is {self.name}, and I'm {self.age} years old."


# Testing the logger.

p1 = Person1("Israel", 28)
# Function called: Person1.__init__((<__main__.Person1 object at 0x7f245e914590>, 'Israel', 28), {})
# Returned value: None

p1.greet()
# Function called: Person1.greet((<__main__.Person1 object at 0x7f245e914590>,), {})
# Returned value: Hello, my name is Israel, and I'm 28 years old.


"""Decorating with function_logger all methods in a class at once"""


# Creating a class decorator to decorate all class methods at once with hardcoded function
def logger_to_class_callables(cls: type) -> type:
    # Iterating through all the class attributes:
    for attr_name, attr_value in vars(cls).items():
        if callable(attr_value):  # If the attr_value is a callable...
            print(f"Decorating '{cls.__name__}.{attr_name}' with 'function_logger'")
            setattr(cls, attr_name, function_logger(attr_value))

    return cls


@logger_to_class_callables
class Person2:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def greet(self) -> str:
        return f"Hello, my name is {self.age}, and I'm {self.age} years old."


# Output:
# Decorating 'Person2.__init__' with 'function_logger'
# Decorating 'Person2.greet' with 'function_logger'


"""
Decorating with function all methods in a class at once,
being able to select the function that will serve as decorator.
"""


# Creating a parameterized class decorator to decorate all class methods at once
def func_decorator(fn: Callable[[AnyCallable], AnyCallable]) -> Callable[[type], type]:
    """Class decorator factory. Decorates all functions in a class with the passed function"""
    def _decorating_callables(cls: type) -> type:
        for attr_name, attr_value in vars(cls).items():
            if callable(attr_value):
                func_name = f"{cls.__name__}.{attr_name}"
                print(f"Decorating '{func_name}' with '{fn.__qualname__}'.")
                # Using setattr() because mapping proxy objects don't accept item assignment
                setattr(cls, attr_name, fn(attr_value))
        return cls

    return _decorating_callables


@func_decorator(function_logger)
class Person3:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def greet(self) -> str:
        return f"Hello, my name is {self.age}, and I'm {self.age} years old"


# Output:
# Decorating 'Person3.__init__' with 'function_logger'
# Decorating 'Person3.greet' with 'function_logger'


p1 = Person3("Israel", 28)
# Function called: Person.__init__((<__main__.Person object at 0x24E30D867C0>, 'Israel', 28), {})
# Returned value: None

p1.greet()
# Function called: Person.greet((<__main__.Person object at 0x24E30D867C0>,), {})
# Returned value: Hello, my name is 28, and I'm 28 years old.

from __future__ import annotations
from functools import wraps
from inspect import isroutine
from typing import Any, Callable


"""Using metaclass parameters"""

"""
    In this example, we'll create a metaclass.
    The metaclass will be in charge of tweaking the class creation
    by decorating all the routines in the class without having 
    to hardcode the function decorator. 
    
    We'll learn how to pass arguments to the metaclass, to help
    us tweaking the class we create with it. 
    
    We pass extra arguments to a metaclass by using keyword-only arguments.
"""


AnyCallable = Callable[..., Any]


def function_logger(fn: AnyCallable) -> AnyCallable:
    @wraps(fn)
    def _function_logger(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join([f"{arg}" for arg in args])
        kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        args_str += kwargs_str
        print(f"{fn.__qualname__}({args_str})")
        return fn(*args, **kwargs)

    return _function_logger


class LoggerType(type):
    def __new__(
        cls,
        name: str,
        bases: tuple[Any, ...],
        namespace: dict[str, Any],
        decorator: Callable[[AnyCallable], AnyCallable],  # The metaclass will accept an extra argument
    ) -> LoggerType:
        new_attr_value: property
        for attr_name, attr_value in namespace.items():
            if isinstance(attr_value, staticmethod) or isinstance(attr_value, classmethod):
                print(f"Decorating {attr_name} {type(attr_value).__name__} method!")
                func_descriptor: staticmethod | classmethod = type(attr_value)
                new_method: staticmethod | classmethod = func_descriptor(decorator(attr_value.__func__))
                namespace[attr_name] = new_method
            elif isinstance(attr_value, property):
                property_methods = {
                    "fget": "getter",
                    "fset": "setter",
                    "fdel": "deleter",
                }
                new_attr_value: property = property()
                for prop_attr, prop_method in property_methods.items():
                    if original_function := getattr(attr_value, prop_attr):
                        print(f"Decorating the {attr_name} property{prop_attr} function")
                        decorated: AnyCallable = decorator(original_function)
                        new_attr_value: property = getattr(attr_value, prop_method)(decorated)
                namespace[attr_name] = new_attr_value
            elif isroutine(attr_value):
                print(f"Decorating {attr_name} instance method!")
                namespace[attr_name] = decorator(attr_value)

        new_type: LoggerType = super().__new__(cls, name, bases, namespace)
        return new_type


# The extra parameters are passed as keyword-only arguments:
class Person(metaclass=LoggerType, decorator=function_logger):
    def __init__(self, name: str) -> None:
        self.name: str = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def do_something(self) -> None:
        print(f"{type(self).__name__} is doing something!")

    @classmethod
    def class_method(cls) -> None:
        print(f"The {cls.__name__} says hello!")

    @staticmethod
    def static_method(message: str) -> None:
        print(f"Using a class to say: {message}")


# Output:
# Decorating __init__ instance method!
# Decorating the name propertyfget function
# Decorating the name propertyfset function
# Decorating do_something instance method!
# Decorating class_method classmethod method!
# Decorating static_method staticmethod method!


class Student(Person, decorator=function_logger):
    def __init__(self, name: str, major: str) -> None:
        super().__init__(name)
        self.major = major

    def study(self):
        print(f"Student {self.name} is studying now!")

    def do_something(self):
        return self.study()


# Output:
# Decorating __init__ instance method!
# Decorating study instance method!
# Decorating do_something instance method!

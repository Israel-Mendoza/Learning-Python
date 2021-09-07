"""Caveats of decorating any callable in a class"""


from functools import wraps
from inspect import isroutine
from typing import Any, Callable, Optional, TypeVar


T = TypeVar("T")
AnyCallable = Callable[..., Any]


# Simple logger function to decorate functions
def function_logger(fn: AnyCallable) -> AnyCallable:
    @wraps(fn)
    def inner(*args: Any, **kwargs: Any) -> Any:
        result = fn(*args, **kwargs)
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        print(f"Returned value: {result}\n")
        return result

    return inner


# Class decorator that will decorate callables, properties, class and static
# methods in the decorated class using the function_logger decorator.
def class_decorator(wrapper_function: AnyCallable) -> Callable[[T], T]:
    def _func_decorator(cls: T) -> T:
        for name, value in vars(cls).items():
            if isinstance(value, classmethod) or isinstance(value, staticmethod):
                print(f"Decorating the '{name}' {type(value).__name__}")
                original_func = value.__func__
                method_type = type(value)
                new_method = method_type(wrapper_function(original_func))
                setattr(cls, name, new_method)
            elif isinstance(value, property):
                possible_attrs = {"fget": "getter", "fset": "setter", "fdel": "deleter"}
                for k, v in possible_attrs.items():
                    if func := getattr(value, k):
                        print(f"Decorating the '{name}' property {k} function!")
                        value = getattr(value, v)(wrapper_function(func))
                    setattr(cls, name, value)
            elif isroutine(value):
                print(f"Decorating the '{name}' instance method!")
                setattr(cls, name, wrapper_function(value))

        return cls

    return _func_decorator


@class_decorator(function_logger)
class MyClass:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def instance_method(self):
        print(f"{self.name} says hello!")

    @classmethod
    def class_method(cls):
        print(f"{cls.__name__} says hi!")

    @staticmethod
    def static_method():
        print(f"Hello from a static method")

    def __add__(self, other: Any) -> Optional[str]:
        if isinstance(other, MyClass):
            return f"{self.name} + {other.name}"

    class Other:
        def __call__(self):
            print("Other instance called!")

    other_instance = Other()


# Output:
# Decorating the '__init__' instance method!
# Decorating the 'name' property fget function!
# Decorating the 'name' property fset function!
# Decorating the 'instance_method' instance method!
# Decorating the 'class_method' classmethod
# Decorating the 'static_method' staticmethod
# Decorating the '__add__' instance method!

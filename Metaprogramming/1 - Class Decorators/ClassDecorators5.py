"""Caveats of decorating any callable in a class"""

from __future__ import annotations
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")
AnyCallable = Callable[..., Any]
FunctionDecorator = Callable[[AnyCallable], AnyCallable]

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
def class_decorator(wrapper_function: AnyCallable) -> Callable[[type], type]:
    """Parameterized Class Decorator"""

    def _class_decorator(cls: type) -> type:
        """Class Decorator"""
        for name, value in vars(cls).items():
            attr_name = f"{cls.__name__}.{name}"
            if callable(value):
                print(f"'{attr_name}' is a callable... Decorating it!")
                setattr(cls, name, wrapper_function(value))
            elif isinstance(value, classmethod):
                new_method = classmethod(wrapper_function(value.__func__))
                setattr(cls, name, new_method)
            elif isinstance(value, staticmethod):
                new_method = staticmethod(wrapper_function(value.__func__))
                setattr(cls, name, new_method)
            elif isinstance(value, property):
                if value.fget:
                    value = value.getter(wrapper_function(value.fget))
                if value.fset:
                    value = value.setter(wrapper_function(value.fset))
                if value.fdel:
                    value = value.deleter(wrapper_function(value.deleter))
                setattr(cls, name, value)

        return cls

    return _class_decorator


@class_decorator(function_logger)
class Person:
    # ACallable class is a callable.
    # It will be decorated!
    class MyClass:
        def __init__(self, callable_name: str) -> None:
            self._name = callable_name

        def __call__(self) -> None:
            print(f"{self._name} says hello!")

    # a_callable is callable! It will get decorated
    an_object = MyClass("Pancho")

    def __init__(self, name: str) -> None:
        self.name = name


# Output:
# 'ACallable' is a callable... Decorating it!
# 'a_callable' is a callable... Decorating it!
# '__init__' is a callable... Decorating it!


print(type(Person.MyClass))  # Expecting a class
# <class 'function'>
print(type(Person.an_object))  # Expecting a MyClass instance
# <class 'function'>

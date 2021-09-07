"""Implementing class decorator that will also decorate properties, and class and static methods"""


from functools import wraps
from typing import Any, Callable, TypeVar

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
            if callable(value):
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

    return _func_decorator


@class_decorator(function_logger)
class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

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
# Decorating Person.name getter with function_logger
# Decorating Person.name setter with function_logger
# Decorating Person.instance_method with function_logger
# Decorating Person.static_method with function_logger
# Decorating Person.class_method with function_logger


p1 = Person("Israel")
# Function called: Person.__init__((<__main__.Person object at 0x0000020A099B6FA0>, 'Israel', 28), {})
# Returned value: None

p1.instance_method()
# <__main__.Person object at 0x000002ACC8206FA0> instance says hello!
# Function called: Person.instance_method((<__main__.Person object at 0x000002ACC8206FA0>,), {})
# Returned value: None

p1.name
# Function called: Person.name((<__main__.Person object at 0x1E5A4686FA0>,), {})
# Returned value: Israel

p1.name = "Mike"
# Function called: Person.name((<__main__.Person object at 0x1E5A4686FA0>, 'Mike'), {})
# Returned value: None

Person.static_method()
# Hello from the static method
# Function called: Person.static_method((), {})
# Returned value: None

Person.class_method()
# Person says hello!
# Function called: Person.class_method((<class '__main__.Person'>,), {})
# Returned value: None

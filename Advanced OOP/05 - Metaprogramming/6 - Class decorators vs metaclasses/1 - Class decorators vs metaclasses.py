from __future__ import annotations
from functools import wraps
from inspect import isroutine
from typing import Any, Callable, Dict, Tuple, TypeVar

AnyCallable = Callable[..., Any]


# Simple logger function to decorate functions
def function_logger(fn: AnyCallable) -> AnyCallable:
    """A simple function decorator, that logs the wrapped function's calls"""
    @wraps(fn)
    def inner(*args: Any, **kwargs: Any) -> Any:
        result: Any = fn(*args, **kwargs)
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        print(f"Returned value: {result}\n")
        return result

    return inner


###############################################################################
###############################################################################


"""USING CLASS DECORATORS"""


def class_decorator(wrapper_function: AnyCallable) -> Callable[[type], type]:
    """
    Class decorator factory.
    It will use the passed function decorator to decorate callables,
    properties, class and static methods in the decorated class.
    """
    def _func_decorator(cls: type) -> type:
        for name, value in vars(cls).items():
            if isroutine(value):
                print(f"Decorating the '{name}' instance method!")
                setattr(cls, name, wrapper_function(value))
        return cls

    return _func_decorator


@class_decorator(function_logger)
class Person1:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def greet(self) -> None:
        print(f"{self.name} says hello!")


# Output:
# Decorating the '__init__' instance method!
# Decorating the 'greet' instance method!


p1 = Person1("Israel", 28)
# Function called: Person1.__init__((<__main__.Person object at 0x29D22E49370>, 'Israel', 28), {})
# Returned value: None

p1.greet()
# Israel says hello!
# Function called: Person1.greet((<__main__.Person object at 0x29D22E49370>,), {})
# Returned value: None


"""USING METACLASSES"""


class LoggerType(type):
    """A metaclass"""
    def __new__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> LoggerType:
        new_namespace: dict[str, Any] = {}  # A namespace with decorated callables. To be populated.
        for k, v in namespace.items():
            if callable(v):
                print(f"Decorating the '{k}' instance method!")
                v = function_logger(v)  # Function wrapper is hardcoded.
                new_namespace[k] = v
            else:
                new_namespace[k] = v
        new_class: LoggerType = super().__new__(cls, name, bases, new_namespace)
        return new_class


class Person2(metaclass=LoggerType):
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def greet(self) -> None:
        print(f"{self.name} says hello!")


# Output:
# Decorating the '__init__' instance method!
# Decorating the 'greet' instance method!


p1 = Person1("Israel", 28)
# Function called: Person.__init__((<__main__.Person object at 0x29D231C89D0>, 'Israel', 28), {})
# Returned value: None

p1.greet()
# Israel says hello!
# Function called: Person.greet((<__main__.Person object at 0x29D231C89D0>,), {})
# Returned value: None


"""WORKING WITH INHERITANCE AND DECORATED CLASSES"""

#####################################################################################
# When inheriting from a class that was decorated, the subclass won't be decorated. #
# We will only see the decoration when we call super() methods directly or by call- #
# ing inherited method in a subclass.                                               #
#####################################################################################


class Student1(Person1):  # Person1 was decorated using a parameterized class decorator
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age)  # Calling the method in super() will call a decorated function.
        self.student_id: int = student_id

    def study(self) -> None:
        print(f"{self.name} is studying now!")


s1 = Student1("Israel", 28, 28292000)
# Output:
# Function called: Person1.__init__((<__main__.Student1 object at 0x000002D6D655C610>, 'Israel', 28), {})
# Returned value: None

s1.greet()  # This method was inherited
# Israel says hello!
# Function called: Person1.greet((<__main__.Student1 object at 0x000002E2D0A8B6D0>,), {})
# Returned value: None

s1.study()  # This method was not inherited. So, it was not decorated.
# Israel is studying now!


"""WORKING WITH INHERITANCE AND CLASSES CREATED WITH A METACLASS"""

#####################################################################################
# With metaclasses, the subclass will also be created using the same metaclass      #
# as the parent class, meaning that, if there was any tweaking at class creation,   #
# the subclass will also be created the same way. THE METACLASS IS ALSO INHERITED!  #
#####################################################################################


class Student2(Person2):  # Person2 was created with a metaclass, which decorated all callables upon class creation
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying now!")


# Decorating the '__init__' instance method!
# Decorating the 'study' instance method!


s2 = Student2("Israel", 28, 28292000)
# Output:
# Function called: Person2.__init__((<__main__.Student2 object at 0x0000022179237220>, 'Israel', 28), {})
# Returned value: None
# Function called: Student2.__init__((<__main__.Student2 object at 0x0000022179237220>, 'Israel', 28, 28292000), {})
# Returned value: None

s2.greet()
# Israel says hello!
# Function called: Person2.greet((<__main__.Student2 object at 0x0000022179237220>,), {})
# Returned value: None

s2.study()
# Israel is studying now!
# Function called: Student2.study((<__main__.Student2 object at 0x0000022179237220>,), {})
# Returned value: None

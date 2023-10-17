from functools import wraps
from inspect import isroutine
from typing import Any, Callable, Dict, Tuple, TypeVar


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


"""USING CLASS DECORATORS"""


# Class decorator that will decorate callables, properties, class and static
# methods in the decorated class using the function_logger decorator.
def class_decorator(wrapper_function: AnyCallable) -> Callable[[T], T]:
    def _func_decorator(cls: T) -> T:
        for name, value in vars(cls).items():
            if isroutine(value):
                print(f"Decorating the '{name}' instance method!")
                setattr(cls, name, wrapper_function(value))
        return cls

    return _func_decorator


@class_decorator(function_logger)
class Person1:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

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
    def __new__(
        cls, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any]
    ) -> T:
        new_namespace = {}
        for k, v in namespace.items():
            if callable(v):
                print(f"Decorating the '{k}' instance method!")
                v = function_logger(v)
                new_namespace[k] = v
            else:
                new_namespace[k] = v
        new_class = super().__new__(cls, name, bases, new_namespace)
        return new_class


class Person2(metaclass=LoggerType):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

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


"""WORKING WITH INHERITANCE"""

#####################################################################################
# When inheriting from a class that was decorated, the subclass won't be decorated. #
# We will only see the decoration when calling super() methods.                     #
# With metaclasses, the subclass will also be created using the same metaclass      #
# as the parent class, meaning that, if there was any tweaking at class creation,   #
# the subclass will also be created the same way. THE METACLASS IS ALSO INHERITED!  #
# The problem may be multiple inheritance!                                          #
#####################################################################################


class Student1(Person1):
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying now!")


s1 = Student1("Israel", 28, 28292000)
# Output:
# Function called: Person1.__init__((<__main__.Student1 object at 0x000002D6D655C610>, 'Israel', 28), {})
# Returned value: None

s1.greet()
# Israel says hello!
# Function called: Person1.greet((<__main__.Student1 object at 0x000002E2D0A8B6D0>,), {})
# Returned value: None

s1.study()
# Israel is studying now!


print("\n\nWORKING WITH INHERITANCE - 2\n\n")


class Student2(Person2):
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

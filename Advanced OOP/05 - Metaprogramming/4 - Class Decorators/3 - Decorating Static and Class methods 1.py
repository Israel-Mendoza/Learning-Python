from functools import wraps
from typing import Any, Callable


"""Caveats of using class decorators to decorate static and class methods"""

"""
    Static methods used to be descriptors, not callables. 
    This changed in Python 3.10
    
    Before Python 3.10, trying to decorate a static method would be in vain.
    Line 33 would not see a static method as callable. 
    
    But since Python 3.10, line 33 would return True and the static method would
    be decorated, since static methods are now callable. 
"""


AnyCallable = Callable[..., Any]


def function_logger(fn: AnyCallable) -> AnyCallable:
    """A function decorator"""
    @wraps(fn)  # Using wraps to keep the function's annotations/docs. Don't overthink about it
    def inner(*args: Any, **kwargs: Any) -> Any:
        result: Any = fn(*args, **kwargs)
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        print(f"Returned value: {result}\n")
        return result

    return inner


def logger_to_class_callables(cls: type) -> type:
    """A class decorator that will decorate all callables in the class with the function_logger."""
    for attr_name, attr_value in vars(cls).items():
        if callable(attr_value):
            print(f"Decorating {cls.__name__}.{attr_name} with function_logger")
            setattr(cls, attr_name, function_logger(attr_value))

    return cls


@logger_to_class_callables
class Person1:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def instance_method(self) -> None:
        print(f"{self} instance says hello!")

    @staticmethod
    def static_method(*args) -> None:
        print(f"Hello from the static method - Passed arguments: {args}")

    @classmethod
    def class_method(cls) -> None:
        print(f"The {cls.__name__} class says hello!")


# Output:
# Decorating Person.__init__ with function_logger
# Decorating Person.instance_method with function_logger


p1 = Person1("Israel", 28)
# Output:
# Function called: Person1.__init__((<__main__.Person object at 0x0000027CC63A36A0>, 'Israel', 28), {})
# Returned value: None

"""Calling the static method:"""
p1.static_method()
# Output:
# Function called: Person1.static_method((<__main__.Person1 object at 0x103098f20>,), {})
# Returned value: None

Person1.static_method()
# Hello from the static method

"""Calling the class method"""
p1.class_method()
# The Person1 class says hello!

Person1.class_method()
# The Person1 class says hello!

"""
    Why wasn't the class method decorated? 
    
    The class method is not a callable. It is a descriptor!
    It executes the __get__ method when accessed, but not the __call__ method
    

    A word about the static method:
    The static method was decorated because it is a callable (at least since Python 3.10).
    And now, because it is a simple function under a class, it became an instance method. 
    It is no longer a static method. It's a method bound to the instantiated object.
    
"""

print(type(Person1.__dict__["static_method"]))  # <class 'function'>
print(type(Person1.__dict__["class_method"]))  # <class 'classmethod'>
print(callable(Person1.__dict__["static_method"]))  # True <--- Since Python 3.10
print(callable(Person1.__dict__["class_method"]))  # False


"""Decorating static and class methods"""


"""
    If we want to decorate static and class methods, we must decorate them
    before making them static or class methods.
    
    If we do it the other way around, the class method won't work due to the 
    same reason our logger_to_class_callables wasn't able to decorate them:
    
    function_loger will treat the class method as a callable, and it's not!
    
    For the static method, we saw how it became a simple instance method.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def instance_method(self) -> None:
        print(f"{self} instance says hello!")

    @staticmethod
    @function_logger  # Decorating the function before it becomes a static method
    def static_method():
        print(f"Hello from the static method")

    @classmethod
    @function_logger  # Decorating the function before it becomes a static method
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

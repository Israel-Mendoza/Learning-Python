"""Implementing class decorator that will also decorate properties, and class and static methods"""


from functools import wraps
from typing import Any, Callable

AnyCallable = Callable[..., Any]
FunctionDecorator = Callable[[AnyCallable], AnyCallable]

# Simple logger function to decorate functions
def function_logger(fn: AnyCallable) -> AnyCallable:
    @wraps(fn)
    def inner(*args: Any, **kwargs: Any) -> Any:
        # Runs the wrapped function first!
        # Then runs the logging print functions.
        result = fn(*args, **kwargs)
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        print(f"Returned value: {result}\n")
        return result

    return inner


# Class decorator that will decorate callables, property objects, class
# and static methods in the decorated class using the function_logger decorator.
def class_decorator(wrapper_func: FunctionDecorator) -> Callable[[type], type]:
    """Parameterized Class Decorator"""

    def _class_decorator(cls: type) -> type:
        """Class Decorator"""
        for name, value in vars(cls).items():
            attr_name = f"{cls.__name__}.{name}"
            if callable(value):
                # Attribute is a callable (an instance method)
                print(f"Decorating the method {attr_name}.")
                new_method = wrapper_func(value)
                setattr(cls, name, new_method)
            elif isinstance(value, classmethod):
                # Attribute is a class method. Retrieves the function
                # the class method wraps, wraps it with the wrapper_function,
                # then makes a class method out of the decorated function,
                # and reassigns the class method to the original symbol.
                print(f"Decorating the class method {attr_name}.")
                new_classmethod: classmethod = classmethod(wrapper_func(value.__func__))
                setattr(cls, name, new_classmethod)
            elif isinstance(value, staticmethod):
                # Attribute is a static method. Retrieves the function
                # the class method wraps, wraps it with the wrapper_function,
                # then makes a static  method out of the decorated function,
                # and reassigns the static method to the original symbol.
                print(f"Decorating the static method {attr_name}.")
                new_static: staticmethod = staticmethod(wrapper_func(value.__func__))
                setattr(cls, name, new_static)
            elif isinstance(value, property):
                # Attribute is a property object.
                # Checks the three possible attributes of the object:
                # if the attribute exists, we'll get the function it has,
                # will wrap it with the wrapper_function, and will set
                # it back to the property's attribute.
                # Finally, it'll assign the updated property to the original
                # symbol.
                if value.fget:
                    print(f"Decorating the property {attr_name}'s fget method.")
                    _value: property = value.getter(wrapper_func(value.fget))
                if value.fset:
                    print(f"Decorating the property {attr_name}'s fset method.")
                    _value: property = value.setter(wrapper_func(value.fset))
                if value.fdel:
                    print(f"Decorating the property {attr_name}'s fdel method.")
                    _value: property = value.deleter(wrapper_func(value.deleter))
                setattr(cls, name, _value)

        return cls

    return _class_decorator


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

    # If implemented, the program will fall into a recursive loop
    # because the wrapper function (from function_logger), will
    # print the passed arguments to __init__, with in its turn
    # will call __repr__ on the passed instance, which will cause
    # the wrapper function to be called with __repr__ again and again:
    #
    # def __repr__(self) -> str:
    #     f"Person('{self._name}')"


# Output:
# Decorating the method Person.__init__.
# Decorating the property Person.name's fget method.
# Decorating the property Person.name's fset method.
# Decorating the method Person.instance_method.
# Decorating the static method Person.static_method.
# Decorating the class method Person.class_method.


p1 = Person("Israel")
# Function called: Person.__init__((<__main__.Person object at 0x7f0006d928e0>, 'Israel'), {})
# Returned value: None

p1.instance_method()
# <__main__.Person object at 0x7f0006d928e0> instance says hello!
# Function called: Person.instance_method((<__main__.Person object at 0x7f0006d928e0>,), {})
# Returned value: None

p1.name
# Function called: Person.name((<__main__.Person object at 0x7f0006d928e0>,), {})
# Returned value: Israel

p1.name = "Mike"
# Function called: Person.name((<__main__.Person object at 0x7f0006d928e0>, 'Mike'), {})
# Returned value: None

Person.static_method()
# Hello from the static method
# Function called: Person.static_method((), {})
# Returned value: None

Person.class_method()
# Person says hello!
# Function called: Person.class_method((<class '__main__.Person'>,), {})
# Returned value: None

from typing import Any, Callable

"""Using a class as a decorator"""

AnyCallable = Callable[..., Any]
Number = int | float


class Logger:
    def __init__(self, a_func: AnyCallable) -> None:
        self.func: AnyCallable = a_func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"Calling {self.func.__name__}!!!")
        return self.func(*args, **kwargs)


@Logger
def add(a: Number, b: Number) -> Number:
    return a + b


print(type(add))  # <class '__main__.Logger'>
print(callable(add))  # True
print(add(10, 20))
# Calling add!!!
# 30


"""Can we use a Decorator Class to decorate a method? Let's give it a try!"""


class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name

    @Logger
    def say_hi(self) -> str:
        return f"{self.name} says 'Hello World!'"


p = Person("Israel")


try:
    p.say_hi()
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: say_hi() missing 1 required positional argument: 'self'


"""
    Why can't we call an callable object?

    Functions objects implement the Descriptor Protocol,
    which means that, when called on a class or a class instance,
    the __get__ method will be executed.
    The Logger class we're using as a decorator doesn't implement
    the __get__ method:
"""

print(hasattr(Person.__init__, "__get__"))  # True
print(hasattr(Person.say_hi, "__get__"))  # False

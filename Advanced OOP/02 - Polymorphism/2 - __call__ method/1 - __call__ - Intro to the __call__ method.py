from __future__ import annotations
from typing import Any, Callable


"""Implementing the __call__ method"""

# Implementing the __call__ method makes the instance callable.


class Person:
    def __call__(self) -> None:
        print("__call__ was called! LOL")


p: Person = Person()
p()
# __call__ was called! LOL


# Implementing the "partial" function as an object


class MyPartial:
    def __init__(self, func: Callable[..., Any], *args: Any) -> None:
        """
        Arguments:
            func [Callable[..., Any]] = A function that takes any number of arguments and returns anything.
            *args [Any] = Any number of arguments.
        """
        self._func: Callable[..., Any] = func
        self._args: tuple[Any, ...] = args

    def __call__(self, *args: Any) -> Any:
        """
        Making the object callable:
        Accepts any number of arguments, passes them to the
        self._func function right after the ones stored in
        self._args attribute, and returns the result.
        """
        return self._func(*self._args, *args)


def a_function(a: int, b: int, c: int) -> tuple[int, ...]:
    return a, b, c


partial_func: MyPartial = MyPartial(a_function, 1, 2)

print(f"{type(partial_func) = }")
# type(partial_func) = <class '__main__.MyPartial'>
print(partial_func(1))
# (1, 2, 1)
print(partial_func(5))
# (1, 2, 5)
print(partial_func(10))
# (1, 2, 10)
print(partial_func(30))
# (1, 2, 30)

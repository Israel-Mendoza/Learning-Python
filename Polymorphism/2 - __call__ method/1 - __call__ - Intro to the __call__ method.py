"""Implementing the __call__ method"""

# Implementing the __call__ method
# makes the instance callable.


from typing import Any, Callable, Tuple


class Person:
    def __call__(self):
        print("__call__ was called! LOL")


p = Person()
p()
# __call__ was called! LOL


# Implementing the "partial" function as an object


class MyPartial:
    def __init__(self, func: Callable[..., Any], *args: Any) -> None:
        self._func: Callable[..., Any] = func
        self._args: Tuple[Any, ...] = args

    def __call__(self, *args: Any) -> Any:
        """
        Making the object callable:
        Accepts any number of arguments, passes them to the
        self._func function after the ones stored in
        self._args, and returns the result.
        """
        return self._func(*self._args, *args)


def a_function(a: int, b: int, c: int) -> Tuple[int, ...]:
    return (a, b, c)


partial_func = MyPartial(a_function, 10, 20)

print(f"{type(partial_func) = }")
# type(partial_func) = <class '__main__.MyPartial'>
print(partial_func(30))
# (10, 20, 30)

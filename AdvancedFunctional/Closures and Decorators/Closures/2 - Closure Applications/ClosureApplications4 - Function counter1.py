"""Function counter"""

from typing import Any
from collections.abc import Callable


def counter(fn: Callable[..., Any]) -> Callable[..., Any]:
    """
    Returns a closure function that will keep count
    of the times the passed function is called and prints
    a message with the count information.
    """
    count = 0

    def inner(*args, **kwargs) -> Any:
        nonlocal count
        count += 1
        print(f"\n{fn.__name__} has been called {count} times")
        return fn(*args, **kwargs)

    return inner


def add(x: int, y: int):
    return x + y


add1 = counter(add)

print(add1.__code__.co_freevars)
# ('count', 'fn')
print(add1.__closure__)
# (<cell at 0x0000029E0C803FD0: int object at 0x0000029E0C546910>, <cell at 0x0000029E0C803FA0: function object at 0x0000029E0C807040>)
print(add1(1, 11))
# add has been called 1 times
# 12
print(add1(3, 1))
# add has been called 2 times
# 4
print(add1(5, 19))
# add has been called 3 times
# 24
print(add1(7, 15))
# add has been called 4 times
# 22
print(add1(8, 10))
# add has been called 5 times
# 18

"""Using the wraps() parameterized decorator to avoid function metadata loss"""


from typing import Any
from functools import wraps
from collections.abc import Callable


def counter(a_func: Callable[..., Any]) -> Callable[..., Any]:
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count = 0

    # @wraps(function)    <- Alternative notation to line 24
    def inner(*args, **kwargs) -> Any:
        nonlocal count # Working with outer scope "count" variable
        count += 1
        print(f"{a_func.__name__} has been called {count} times")
        return a_func(*args, **kwargs)

    # Transferring the metadata of the function to the closure using wraps
    inner = wraps(a_func)(inner)
    return inner


@counter
def add(x: int, y: int) -> int:
    """Returns the sum of the passed integers"""
    return x + y


print(add.__name__)  
# add
print(add.__code__.co_freevars) 
# ('a_func', 'count')
print(add.__closure__)
# (<cell at 0x7f97c81dde50: function object at 0x7f97c8239160>, <cell at 0x7f97c81dde20: int object at 0x7f97c802e910>)
print(add.__annotations__)  # Correct annotations!
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
help(add)  # Correct documentation, WRONG function signature:
# Help on function add in module __main__:

# add(x: int, y: int) -> int
#     Returns the sum of the passed integers
print()

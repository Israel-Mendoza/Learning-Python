from typing import Any, TypeAlias
from collections.abc import Callable

Number: TypeAlias = int | float


"""Attempt not to lose the original function's metadata"""


# Defining the decorator function
def counter(a_func: Callable[..., Any]) -> Callable[..., Any]:
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count: int = 0

    def inner(*args, **kwargs) -> Any:
        nonlocal count  # Free variable from outer scope
        count += 1
        print(f"{a_func.__name__} has been called {count} times")
        # Return wrapped function return value when called with passed args
        return a_func(*args, **kwargs)

    # Transferring the metadata of the function to the closure
    inner.__name__ = a_func.__name__
    inner.__doc__ = a_func.__doc__
    inner.__annotations__ = a_func.__annotations__
    return inner


@counter # Syntatic sugar for 'add = counter(add)'
def add(x: Number, y: Number) -> Number:
    """Returns the sum of the passed integers"""
    return x + y


# INSPECTING OUR FUNCTION:

print(add.__name__)  
# add
print(add.__code__.co_freevars)  
# ('a_func', 'count')
print(add.__closure__)  
# <cell at 0x7f93f01dde20: function object at 0x7f93f01e5ca0>,
# <cell at 0x7f93f01dddf0: int object at 0x7f93f002e910>)
print(add.__annotations__)  
# {'x': Number, 'y': Number, 'return': Number}

# Correct name and documentation. WRONG function signature:
help(add)
# Help on function add in module __main__:
#
# add(*args, **kwargs) -> int
#     Returns the sum of the passed integers

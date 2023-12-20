from typing import Any
from functools import wraps
from datetime import datetime
from zoneinfo import ZoneInfo
from collections.abc import Callable


"""Introducing and making a use case for MEMOIZATION"""


def function_logger(a_function: Callable[..., Any]) -> Callable[..., Any]:
    """Function decorator"""
    @wraps(a_function)
    def logger(*args, **kwargs) -> Any:
        """
        Wrapper function.
        Prints information about the time and arguments the
        wrapped function is called.
        """
        # Capturing time the function is called
        run_datetime: datetime = datetime.now(ZoneInfo("UTC"))
        # Storing the result of the called wrapped function
        result: Any = a_function(*args, **kwargs)

        # Capturing the arguments in a tuple
        _args: str = ", ".join((str(arg) for arg in args))
        _kwargs: str = ", ".join((f"'{key}'={value}" for key, value in kwargs.items()))
        all_args: str = _args + _kwargs

        # Printing the information
        print(f"{run_datetime}: called '{a_function.__name__}({all_args})'")

        # Returning the wrapped function's result
        return result

    # Returning the wrapped function
    return logger


# Using the decorated function on a fibonacci recursive function
@function_logger
def fibonacci(n: int) -> int:
    """A Fibonacci number generator, using recursion"""
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
Calling a decorated recursive function. 
Calculations are duplicated, which can be expensive.
"""

# Notice how many times functions are called when calling fibonacci(6)!!!
# fibonacci(1) - 3 times
# fibonacci(2) - 5 times
# fibonacci(3) - 3 times
# fibonacci(4) - 2 times
# fibonacci(5) - 1 time
# fibonacci(6) - 1 time
print(fibonacci(6))
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(1)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(3)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (2nd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(4)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (3rd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(1)' -> Already calculated (2nd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(3)' -> Already calculated (2nd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(5)'
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (4th time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(1)' -> Already calculated (3rd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(3)' -> Already calculated (3rd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(2)' -> Already calculated (5th time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(4)' -> Already calculated (2nd time)
# 2020-09-27 20:40:40.362964+00:00: called 'fibonacci(6)'
# 8


##############################################################################################
##############################################################################################

"""
Let's implement a dictionary in a class as a CACHING to prevent unnecessary calculations.
"""


class FibonacciClass:
    """
    A class that contains a fibonacci calculator.
    Class instance is callable, which is the fibonacci calculator.
    Implements a caching mechanism as a memoization system
    to avoid duplicated calculations.
    """
    def __init__(self) -> None:
        """
        Initializing the caching mechanism containing
        known values for fibonacci(1) and fibonacci(2).
        """
        self._cache: dict[int, int] = {1: 1, 2: 1}

    @property
    def cache(self) -> dict[int, int]:
        return self._cache

    def __call__(self, n: int) -> int:
        """
        When the class instance is called, it calculates
        fibonacci(n).
        First, it looks for the existing cached value;
        if found, returned, if not, calculates it and
        stores it in the cache dictionary.
        Args:
            n (int): the 'n'th Fibonacci number
        Returns:
            int: the calculated 'n'th fibonacci number
        """
        if n not in self._cache:
            # Prints the object calling only when values are calculated
            print(f"Calculating fib({n})")
            # Calculates and stores the result in the cache dictionary
            self._cache[n] = self(n - 1) + self(n - 2)
        # Returning the result from the cache dictionary
        return self._cache[n]


# Creating a FibonacciClass instance
f1 = FibonacciClass()

print(type(f1))  
# <class '__main__.FibonacciClass'>

help(f1)
# Help on FibonacciClass in module __main__ object:
#
# class FibonacciClass(builtins.object)
#  |  FibonacciClass() -> None
#  |
#  |  A class that contains a fibonacci calculator.
#  |  Class instance is callable, which is the fibonacci calculator.
#  |  Implements a caching mechanism as a memoization system
#  |  to avoid duplicated calculations.
#  |
#  |  Methods defined here:
#  |
#  |  __call__(self, n: int) -> int
#  |      When the class instance is called, it calculates
#  |      fibonacci(n).
#  |      First, it looks for the existing cached value;
#  |      if found, returned, if not, calculates it and
#  |      stores it in the cache dictionary.
#  |      Args:
#  |          n (int): the 'n'th Fibonacci number
#  |      Returns:
#  |          int: the calculated 'n'th fibonacci number
#  |
#  |  __init__(self) -> None
#  |      Initializing the caching mechanism containing
#  |      known values for fibonacci(1) and fibonacci(2).
#  |
#  |  ----------------------------------------------------------------------
#  |  Readonly properties defined here:
#  |
#  |  cache
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)

# Accessing the caching dictionary
print(f1.cache) 
# {1: 1, 2: 1}

# Notice how there are no duplicated calculations
print(f1(10))
# Calculating fib(10)
# Calculating fib(9)
# Calculating fib(8)
# Calculating fib(7)
# Calculating fib(6)
# Calculating fib(5)
# Calculating fib(4)
# Calculating fib(3)

# Accessing the caching dictionary
print(f1.cache) 
# {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}


"""
Let's implement a dictionary in a function as a CACHING to prevent unnecessary calculations.
"""


def fibonacci_function() -> Callable[[int], int]:
    """
    Returns a fibonacci calculator closure function.
    Returned function implements a caching dictionary 
    as a memoization mechanism.
    """
    # Initializing the caching mechanism containing
    # known values for fibonacci(1) and fibonacci(2).
    _cache: dict[int, int] = {1: 1, 2: 1}

    def fibonacci_function_inner(n: int) -> int:
        """
        When 'fibonacci_function_inner' is called, 
        it returns the 'n'th fibonacci number.
        First, it looks for the existing cached value in the
        free variable _cache dictionary.
        The value is returned if found, if not, calculates it 
        and stores it in the _cache dictionary, and then returns it.
        Args:
            n (int): the 'n'th Fibonacci number
        Returns:
            int: the calculated 'n'th fibonacci number
        """
        if n not in _cache:
            # Prints the object calling only when values are calculated
            print(f"Calculating fibonacci_function_inner({n})")
            # Calculates and stores the result in the cache dictionary
            _cache[n] = fibonacci_function_inner(n - 1) + fibonacci_function_inner(n - 2)
        # Returning the cached result
        return _cache[n]

    # Making the _cache dictionary available through an interface
    fibonacci_function_inner.cache = _cache
    # Returning the closure
    return fibonacci_function_inner


# Storing the returned function from 
# "fibonacci_function" to f2
f2 = fibonacci_function()

print(type(f2))
# <class 'function'>

help(fibonacci_function)
# Help on function fibonacci_function in module __main__:
#
# fibonacci_function() -> collections.abc.Callable[[int], int]
#     Returns a fibonacci calculator closure function.
#     Returned function implements a caching dictionary
#     as a memoization mechanism.

help(f2)
# Help on function fibonacci_function_inner in module __main__:
#
# fibonacci_function_inner(n: int) -> int
#     When 'fibonacci_function_inner' is called,
#     it returns the 'n'th fibonacci number.
#     First, it looks for the existing cached value in the
#     free variable _cache dictionary.
#     The value is returned if found, if not, calculates it
#     and stores it in the _cache dictionary, and then returns it.
#     Args:
#         n (int): the 'n'th Fibonacci number
#     Returns:
#         int: the calculated 'n'th fibonacci number

# Notice how there are no duplicated calculations
print(f2(10))
# Calculating fibonacci(10)
# Calculating fibonacci(9)
# Calculating fibonacci(8)
# Calculating fibonacci(7)
# Calculating fibonacci(6)
# Calculating fibonacci(5)
# Calculating fibonacci(4)
# Calculating fibonacci(3)

# Accessing the caching dictionary
print(f2.cache)
# {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}

# f2 is a closure
print(f2.__code__.co_freevars) 
# '_cache', 'fibonacci_function_inner')
print(f2.__closure__)
# (<cell: dict object>, <cell: function object>)

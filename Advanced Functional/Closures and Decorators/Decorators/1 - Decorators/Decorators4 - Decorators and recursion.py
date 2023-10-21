"""Caveats of decorating recursive functions"""


from typing import Any
from time import perf_counter
from functools import wraps, reduce
from collections.abc import Callable


def function_timer(fn: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator function. Wraps a function, and prints
    the time the function took to run and the passed arguments.
    Returned function keeps wrapped function's signature
    """
    @wraps(fn)  # Transferring the metadata of the function to the closure using wraps
    def inner(*args, **kwargs) -> Any:
        # Timing the function's execution time
        start = perf_counter()
        result = fn(*args, **kwargs)  # Here is where the function gets called
        end = perf_counter()
        elapsed = end - start
        # Capturing *args and **kwars in a string
        _args = [str(a) for a in args]
        _kwargs = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = _args + _kwargs
        all_args = ", ".join(all_args)
        # Printing timing results
        print(f"{fn.__name__}({all_args}) took {elapsed:.6f} seconds to run.")
        # Return wrapped function return value when called with passed args
        return result
    # Return decorated function
    return inner


######################################################################################
######################################################################################

"""USING THE DECORATOR"""

# Decorating a fibonacci function using a loop


@function_timer
def loop_fibonacci(n: int) -> int:
    # Getting rid of negative values
    n = abs(n)
    if n == 0:
        raise ValueError("Number of Fibonacci value must be other than zero")
    current_num = 0
    new_number = 1
    while n != 1:
        new_number, current_num = new_number + current_num, new_number
        n -= 1
    return new_number


# Avoiding innecesary calls to the decorator in recursive function
# by wrapping the recursive function in another function
@function_timer
def recursive_fibonacci(n: int) -> int:
    # Checking for positive numbers
    if n == 0:
        raise ValueError("Number of Fibonacci value must be other than zero")
    # Getting rid of negative numbers
    n = abs(n)

    def _recursive_fib(n: int) -> int:
        # Fibonacci of 1 and 2 = 1
        return 1 if n < 3 else _recursive_fib(n - 1) + _recursive_fib(n - 2)

    return _recursive_fib(n)


# Using the functools.reduce function
@function_timer
def reduce_fibonacci(n: int) -> int:
    # Setting an initial tuple
    # Index 0 is the previous number and index 1 is the new value
    initial = (0, 1)
    # A dummy number generator to keep the reduce function running
    dummy = range(n)
    # n will receive the number from the dummy. It won't be used in the function
    fib = reduce(lambda p, n: (p[1], p[0] + p[1]), dummy, initial)
    return fib[0]


"""Testing decorated functions"""
reduce_fibonacci(15) 
# reduce_fibonacci(15) took 0.000013 seconds to run. -> 610
loop_fibonacci(15)
# loop_fibonacci(15) took 0.000004 seconds to run. -> 610
recursive_fibonacci(15) 
# recursive_fibonacci(15) took 0.000284 seconds to run. -> 610

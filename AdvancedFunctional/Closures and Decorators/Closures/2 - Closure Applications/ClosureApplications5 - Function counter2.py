"""Function counter to dictionary"""

from random import choice, randint
from collections.abc import Callable, Mapping
from typing import Any


def counter(fn: Callable[..., Any], count_dict: Mapping):
    """
    Returns a closure function that will keep count
    of the times the passed function is called.
    Stores the records in the passed GOBAL dictionary
    """
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        count_dict[fn.__name__] = count  # No assigment, but mutability of the object
        return fn(*args, **kwargs)

    return inner


def add(x: int, y: int) -> int:
    return x + y


def substract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> float:
    return x / y


# Creating dictionaries where we will be recording our logs
fn_count_dict = dict()
fn_count_dict_2 = dict()

# Pulling out the closures:
add1 = counter(add, fn_count_dict)
sub1 = counter(substract, fn_count_dict)
mul1 = counter(multiply, fn_count_dict)
div1 = counter(divide, fn_count_dict)

# Appending the closures to a list:
my_functions = [add1, sub1, mul1, div1]

# Iterating 100 times and calling random functions from the "my_functions" list
for i in range(100):
    choice(my_functions)(randint(1, 20), randint(1, 20))

# Inspecting our record by iterating though the first dictionary and printing its logs:
for k in fn_count_dict.keys():
    print(f'Function "{k}" was called {fn_count_dict[k]} times')
print()
# Function "multiply" was called 29 times
# Function "divide" was called 27 times
# Function "substract" was called 23 times
# Function "add" was called 21 times

###############################################################################
###############################################################################

# Doing the same as above, but this time,
# we're overriding the original variable with the returned closures:
add = counter(add, fn_count_dict_2)
substract = counter(substract, fn_count_dict_2)
multiply = counter(multiply, fn_count_dict_2)
divide = counter(divide, fn_count_dict_2)

my_functions_2 = [add, substract, multiply, divide]

# Iterating 100 times and calling random functions from the "my_functions2" list
for i in range(100):
    choice(my_functions_2)(randint(1, 20), randint(1, 20))

# Inspecting our record by iterating though the first dictionary and printing its logs:
for k in fn_count_dict.keys():
    print(f'Function "{k}" was called {fn_count_dict_2[k]} times')
# Function "multiply" was called 29 times
# Function "divide" was called 21 times
# Function "substract" was called 29 times
# Function "add" was called 21 times

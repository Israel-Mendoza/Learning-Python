import random
from typing import Any, Callable

type Number = int | float

"""Function counter to dictionary"""


def counter(fn: Callable[..., Any], count_dict: dict[str, int]) -> Callable[..., Any]:
    """
    Returns a closure function that will keep count
    of the times the passed function is called.
    Stores the records in the passed GLOBAL dictionary
    """
    count: int = 0

    def inner(*args, **kwargs) -> Any:
        nonlocal count
        count += 1
        count_dict[fn.__name__] = count  # No assigment, but mutability of the object
        return fn(*args, **kwargs)

    return inner


def add(x: Number, y: Number) -> Number:
    return x + y


def subtract(x: Number, y: Number) -> Number:
    return x - y


def multiply(x: Number, y: Number) -> Number:
    return x * y


def divide(x: Number, y: Number) -> float:
    return x / y


# Creating dictionaries where we will be recording our logs
fn_count_dict: dict[str, int] = {}
fn_count_dict_2: dict[str, int] = {}

# Pulling out the closures:
add_closure: Callable[..., Any] = counter(add, fn_count_dict)
sub_closure: Callable[..., Any] = counter(subtract, fn_count_dict)
mul_closure: Callable[..., Any] = counter(multiply, fn_count_dict)
div_closure: Callable[..., Any] = counter(divide, fn_count_dict)

# Appending the closures to a list:
my_functions: list[Callable[..., Any]] = [add_closure, sub_closure, mul_closure, div_closure]

# Iterating 100 times and calling random functions from the "my_functions" list
for i in range(100):
    random.choice(my_functions)(random.randint(1, 20), random.randint(1, 20))

# Inspecting our record by iterating though the first dictionary and printing its logs:
for k in fn_count_dict.keys():
    print(f'Function "{k}" was called {fn_count_dict[k]} times')
print()
# Function "multiply" was called 29 times
# Function "divide" was called 27 times
# Function "subtract" was called 23 times
# Function "add" was called 21 times

###############################################################################
###############################################################################

# Doing the same as above, but this time,
# we're overriding the original variable with the returned closure:
add = counter(add, fn_count_dict_2)
subtract = counter(subtract, fn_count_dict_2)
multiply = counter(multiply, fn_count_dict_2)
divide = counter(divide, fn_count_dict_2)

my_functions = [add, subtract, multiply, divide]  # Re-using the variable to store the new closures

# Iterating 100 times and calling random functions from the "my_functions2" list
for i in range(100):
    random.choice(my_functions)(random.randint(1, 20), random.randint(1, 20))

# Inspecting our record by iterating though the first dictionary and printing its logs:
for k in fn_count_dict.keys():
    print(f'Function "{k}" was called {fn_count_dict_2[k]} times')
# Function "multiply" was called 29 times
# Function "divide" was called 21 times
# Function "subtract" was called 29 times
# Function "add" was called 21 times

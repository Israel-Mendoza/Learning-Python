from functools import wraps
from collections.abc import Callable


"""Memoizing any function using a decorator"""


def memoize(a_function: Callable[[int], int]) -> Callable[[int], int]:
    """
    A wrapper memoization function for a function which signature is Callable[[int], int].
    """
    # Implementing the cache dictionary:
    _cache: dict[int, int] = {}

    @wraps(a_function)
    def inner(n: int) -> int:
        """
        Calculating the return value only if
        it doesn't exist in the _cache dictionary
        """
        if n not in _cache:
            _cache[n] = a_function(n)
        return _cache[n]

    # Making the caching mechanism available
    # as a function property
    inner.cache = _cache

    return inner


help(memoize)
# Help on function memoize in module __main__:
#
# memoize(a_function: collections.abc.Callable[[int], int]) -> collections.abc.Callable[[int], int]
#     A wrapper memoization function for a function which signature is Callable[[int], int].


@memoize
def fibonacci(n: int) -> int:
    """
    A function that returns the passed
    Fibonacci sequence's index using recursion
    """
    if n < 3:
        return 1
    print(f"Calculating {n}!")
    return fibonacci(n - 1) + fibonacci(n - 2)


help(fibonacci)
# Help on function fibonacci in module __main__:
#
# fibonacci(n: int) -> int
#     A function that returns the passed
#     Fibonacci sequence's index using recursion


# Memoizing is preventing unnecessary function calls:
print(fibonacci(10))
# Calculating 10!
# Calculating 9!
# Calculating 8!
# Calculating 7!
# Calculating 6!
# Calculating 5!
# Calculating 4!
# Calculating 3!
# 55

print(fibonacci.cache)
# {2: 1, 1: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}

# Calculating fibonacci(10) again
# Notice how value is taken from caching dictionary
print(fibonacci(10))
# 55  // Final result

# Calculating fibonacci(8) again
# Notice how value is taken from caching dictionary
print(fibonacci(8))
# 21

# Calculating fibonacci(15)
# Notice how the precalculated values are taken from the caching dictionary.
# All new values are calculated.
print(fibonacci(15))
# Calculating 15!
# Calculating 14!
# Calculating 13!
# Calculating 12!
# Calculating 11!
# 610  // Final result

# Printing the cache dictionary
for arg, cached_val in fibonacci.cache.items():
    print(f"{arg}: {cached_val}")
# 2: 1
# 1: 1
# 3: 2
# 4: 3
# 5: 5
# 6: 8
# 7: 13
# 8: 21
# 9: 34
# 10: 55
# 11: 89
# 12: 144
# 13: 233
# 14: 377
# 15: 610

"""Creating our own simple reduce function"""


from typing import Any, Callable, Sequence


a_list = [5, 8, 6, 10, 9]
another_list1 = ["", 10, True, None, False]
another_list2 = ["0", 10, True, "Python"]


def _max(x: int, y: int) -> int:
    """Returns the biggest of two numbers"""
    return x if x > y else y


def _min(x: int, y: int) -> int:
    """Returns the smallest of two numbers"""
    return x if x < y else y


def _sum(x: int, y: int) -> int:
    """Returns the sum of two numbers"""
    return x + y


def _any(x: Any, y: Any) -> bool:
    """Returns True if any of the passed arguments is truthy"""
    return bool(x) or bool(y)


def _all(x: Any, y: Any) -> bool:
    """Returns True if both of the passed arguments are truthy"""
    return bool(x) and bool(y)


def _reduce(fn: Callable[[Any, Any], Any], sequence: Sequence, initial=None) -> Any:
    """
    A reduce high-order function that works with a sequence.
    This doesn't work with just any iterable.
    """
    if initial is None:
        accumulator = sequence[0]
        for item in sequence[1:]:
            accumulator = fn(accumulator, item)
    else:
        accumulator = initial
        for item in sequence:
            accumulator = fn(accumulator, item)
    return accumulator


"""Using our reduce function"""

max_result = _reduce(_max, a_list)
min_result = _reduce(_min, a_list)
sum_result = _reduce(_sum, a_list)
any_result1 = _reduce(_any, another_list1)
any_result2 = _reduce(_any, another_list2)
all_result1 = _reduce(_all, another_list1)
all_result2 = _reduce(_all, another_list2)


print(max_result)  # 5
print(min_result)  # 10
print(sum_result)  # 38
print(any_result1)  # True
print(any_result2)  # True
print(all_result1)  # False
print(all_result2)  # True


"""Trying with another iterable"""

try:
    result = _reduce(_max, {1, 2, 3, 4, 5})
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: 'set' object is not subscriptable

from time import perf_counter, sleep
from functools import wraps
from types import FunctionType
from random import random


def function_profiler(func: FunctionType) -> FunctionType:
    _counter = 0
    _total_time = 0
    _average_time = 0

    @wraps(func)
    def closure(*args, **kwargs):
        nonlocal _counter, _total_time, _average_time
        _counter += 1
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        _total_time += end_time - start_time
        return result

    def counter():
        return _counter

    def average_time():
        return _total_time / _counter

    closure.counter = counter
    closure.average_time = average_time
    return closure


def my_func() -> None:
    """A test function"""
    sleep(random())


# Decorating the 'counting' function
my_func = function_profiler(my_func)
# Introspecting the new decorated function
print(f"Type of my_func: {type(my_func)}")
print(f"Free variables in 'counting': {my_func.__code__.co_freevars}")

# Calling the function
for i in range(10):
    my_func()

# Accessing the free variables' values
print(f"Counter: {my_func.counter()} - Average time: {my_func.average_time():.4f}\n\n")


# ACHIEVING SAME FUNCTIONALITY WITH A CLASS


class FunctionProfiler:
    def __init__(self, func: FunctionType):
        self._func = func
        self._counter = 0
        self._total_time = 0
        self._average_time = None

    @property
    def counter(self):
        """The counter attribute of the object"""
        return self._counter

    @property
    def average_time(self):
        """The calculated average time"""
        if self._average_time is None:
            self._average_time = self._total_time / self._counter
        return self._average_time

    def __call__(self, *args, **kwargs):
        self._counter += 1
        start_time = perf_counter()
        result = self._func(*args, **kwargs)
        end_time = perf_counter()
        self._total_time += end_time - start_time
        self._average_time = None
        return result


def my_func() -> None:
    """A test function"""
    sleep(random())


# Decorating the 'counting' function
my_func = FunctionProfiler(my_func)
# Introspecting the new object:
print(f"Type of my_func: {type(my_func)}")
print(f"Attributes in 'counting': {my_func.__dict__}")

# Calling the function
for i in range(10):
    my_func()

print(f"Counter: {my_func.counter} - Average time: {my_func.average_time:.4f}\n\n")

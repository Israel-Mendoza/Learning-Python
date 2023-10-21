"""Implementing the same decorator using functions (closures) and classes"""


from random import random
from functools import wraps
from typing import Any, Callable, Optional
from time import perf_counter, sleep


"""Using a closure"""


def function_profiler(func: Callable[..., Any]) -> Callable[..., Any]:
    _counter: int = 0
    _total_time: float = 0
    _average_time: float = 0

    @wraps(func)
    def closure(*args: Any, **kwargs: Any) -> Any:
        nonlocal _counter, _total_time, _average_time
        _counter += 1
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        _total_time += end_time - start_time
        return result

    def counter() -> int:
        return _counter

    def average_time() -> float:
        return _total_time / _counter

    # Making counter and average_time available through the closure:
    setattr(closure, "counter", counter)
    setattr(closure, "average_time", average_time)

    return closure


def my_func() -> None:
    """A test function"""
    sleep(random())


# Decorating the 'counting' function
my_func = function_profiler(my_func)

# Introspecting the new decorated function
print(f"{type(my_func) = }")
# type(my_func) = <class 'function'>
print(f"{my_func.__code__.co_freevars}")
# ('_average_time', '_counter', '_total_time', 'func')

# Calling the function
for i in range(10):
    my_func()

# Accessing the free variables' values
print(f"{my_func.counter() = }")
# my_func.counter() = 10
print(f"{my_func.average_time()}")
# 0.3897147799999402


"""Using a class"""


class FunctionProfiler:
    def __init__(self, func: Callable[..., Any]) -> None:
        # What was done through free variables in the closure,
        # we'll do it using "private" instance attributes:
        self._func: Callable[..., Any] = func
        self._counter: int = 0
        self._total_time: float = 0
        self._average_time: Optional[float] = None

    @property
    def counter(self) -> int:
        """The counter attribute of the object"""
        return self._counter

    @property
    def average_time(self) -> float:
        """The calculated average time"""
        if self._average_time is None:
            self._average_time = self._total_time / self._counter
        return self._average_time

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self._counter += 1
        start_time = perf_counter()
        result = self._func(*args, **kwargs)
        end_time = perf_counter()
        ellapsed_time = end_time - start_time
        self._total_time += ellapsed_time
        self._average_time = None
        return result


def my_func2() -> None:
    """A test function"""
    sleep(random())


# Decorating the 'counting' function
my_func2 = FunctionProfiler(my_func)

# Introspecting the new object:
print(f"{type(my_func2) = }")
# type(my_func2) = <class '__main__.FunctionProfiler'>
print(f"{my_func2.__dict__ = }")
# my_func2.__dict__ = {
#                      '_func': <function my_func at 0x7f88e5f60700>,
#                      '_counter': 0,
#                      '_total_time': 0,
#                      '_average_time': None
#                     }

# Calling the function
for i in range(10):
    my_func2()

print(f"{my_func2.counter = }")
# my_func2.counter = 10
print(f"{my_func2.average_time:.4f}")
# 0.4428

from __future__ import annotations

"""Using a class' __call__ method to make it a decorator"""

from time import perf_counter
from types import FunctionType
from typing import Any, Callable


class FunctionProfiler:
    """
    A class intended to work as a function decorator.
    Every time the decorated function is called, 
    the decorator instance will calculate the time it took
    for the function to return, it will increase the counter
    of function calls by one, and will calculate the average
    time the function took to return. 
    """
    def __init__(self: FunctionProfiler, func: Callable[..., Any]) -> None:
        self.func: Callable[..., Any] = func
        self._count: int = 0
        self._execution_time: float = 0
        self._execution_avg: float | None = None

    @property
    def func(self: FunctionProfiler) -> Callable[..., Any]:
        """The function the object is wrapping"""
        return self._func

    @func.setter
    def func(self: FunctionProfiler, func: Callable[..., Any]) -> None:
        if isinstance(func, FunctionType):
            self._func: Callable[..., Any] = func

    @property
    def count(self: FunctionProfiler):
        """The count of times the object has been called"""
        return self._count

    @property
    def execution_avg(self: FunctionProfiler) -> float:
        """Returns the execution time average the wrapped function took"""
        if self._execution_avg is None:
            self._execution_avg = self._execution_time / self.count
            return self._execution_avg
        return self._execution_avg

    def __call__(self: FunctionProfiler, *args: Any) -> Any:
        """
        Adding extra functionality to the wrapped,
        function, calling it and returning its value.
        """
        self._execution_avg: float | None = None
        self._count += 1
        start_time: float = perf_counter()
        result: Any = self.func(*args)
        elapsed_time: float = perf_counter() - start_time
        print(f"Function '{self.func.__name__}' took {elapsed_time:.3f} seconds to run")
        self._execution_time += elapsed_time
        return result


@FunctionProfiler
def counting() -> None:
    """A counting function, which will only delay the app by 1000000 loops"""
    counter = 0
    for i in range(1000000):
        counter += i


# counting = FunctionProfiler(counting)

for i in range(10):
    counting()
# Function 'counting' took 0.026 seconds to run
# Function 'counting' took 0.027 seconds to run
# Function 'counting' took 0.028 seconds to run
# Function 'counting' took 0.029 seconds to run
# Function 'counting' took 0.029 seconds to run
# Function 'counting' took 0.028 seconds to run
# Function 'counting' took 0.029 seconds to run
# Function 'counting' took 0.029 seconds to run
# Function 'counting' took 0.027 seconds to run
# Function 'counting' took 0.032 seconds to run

print(
    f"Function called {counting.count} times with an average of "
    f"{counting.execution_avg:.3f} seconds per call"
)
# Function called 10 times with an average of 0.028 seconds per call

help(counting)
# Help on FunctionProfiler in module __main__ object:

# class FunctionProfiler(builtins.object)
#  |  FunctionProfiler(func: 'Callable[..., Any]') -> 'None'
#  |  
#  |  A class intended to work as a function decorator.
#  |  Every time the decorated function is called, 
#  |  the decorator instance will calculate the time it took
#  |  for the function to return, it will increase the counter
#  |  of function calls by one, and will calculate the average
#  |  time the function took to return.
#  |  
#  |  Methods defined here:
#  |  
#  |  __call__(self: 'FunctionProfiler', *args: 'Any') -> 'Any'
#  |      Adding extra functionality to the wrapped,
#  |      function, calling it and returning its value.
#  |  
#  |  __init__(self: 'FunctionProfiler', func: 'Callable[..., Any]') -> 'None'
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Readonly properties defined here:
#  |  
#  |  count
#  |      The count of times the object has been called
#  |  
#  |  execution_avg
#  |      Returns the execution time average the wrapped function took
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  func
#  |      The function the object is wrapping

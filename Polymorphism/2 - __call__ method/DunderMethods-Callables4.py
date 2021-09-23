from time import perf_counter
from types import FunctionType
from functools import wraps
from typing import Any, Callable, Optional

# TODO: Why can't I wrap in a class?


class FunctionProfiler:
    def __init__(self, func: Callable[..., Any]) -> None:
        self._func: Callable[..., Any] = func
        self._count: int = 0
        self._execution_time: float = 0
        self._execution_avg: Optional[float] = None

    @property
    def func(self) -> Callable[..., Any]:
        """The function the object is wrapping"""
        return self._func

    @func.setter
    def func(self, func: Callable[..., Any]) -> None:
        if isinstance(func, FunctionType):
            self._func: Callable[..., Any] = func

    @property
    def count(self):
        """The count of times the object has been called"""
        return self._count

    @property
    def execution_avg(self) -> float:
        if self._execution_avg is None:
            self._execution_avg = self._execution_time / self.count
            return self._execution_avg
        return self._execution_avg

    # @wraps(func)
    def __call__(self, *args: Any) -> Any:
        self._execution_avg = None
        self._count += 1
        start_time = perf_counter()
        result = self.func(*args)
        elapsed_time = perf_counter() - start_time
        print(f"Function '{self.func.__name__}' took {elapsed_time:.3f} seconds to run")
        self._execution_time += elapsed_time
        return result


@FunctionProfiler
def counting():
    """A counting function, which will only delay the app by 1000000 loops"""
    counter = 0
    for i in range(1000000):
        counter += i


# counting = FunctionProfiler(counting)

for i in range(10):
    counting()

print(
    f"Function called {counting.count} times with an average of "
    f"{counting.execution_avg:.3f} seconds per call"
)

help(counting)

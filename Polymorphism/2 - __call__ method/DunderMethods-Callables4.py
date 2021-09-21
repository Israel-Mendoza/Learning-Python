from time import perf_counter
from types import FunctionType
from functools import wraps


class FunctionProfiler:
    def __init__(self, func):
        self._func = func
        self._count = 0
        self._execution_time = 0
        self._execution_avg = None

    @property
    def func(self) -> FunctionType:
        """The function the object is wrapping"""
        return self._func

    @func.setter
    def func(self, func: FunctionType) -> None:
        if isinstance(func, FunctionType):
            self._func = func

    @property
    def count(self):
        """The count of times the object has been called"""
        return self._count

    @property
    def execution_avg(self):
        if self._execution_avg is None:
            self._execution_avg = self._execution_time / self.count
            return self._execution_avg
        return self._execution_avg

    @wraps(self.func)
    def __call__(self, *args):
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
    f"Counting function called {counting.count} times with an average of {counting.execution_avg:.3f} seconds per call"
)

help(counting)

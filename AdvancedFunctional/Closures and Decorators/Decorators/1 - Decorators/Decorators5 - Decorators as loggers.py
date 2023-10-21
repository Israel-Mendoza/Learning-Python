"""Using Decorators as loggers"""


from typing import Any
from functools import wraps
from datetime import datetime
from zoneinfo import ZoneInfo
from collections.abc import Callable


def function_logger(a_func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator function. Returns a closure that, when called,
    will print the time the function was called and a function
    call representation.
    """
    @wraps(a_func)
    def logger(*args, **kwargs) -> Any:
        # Capturing date and time object when wrapped function is called
        run_datetime = datetime.now(ZoneInfo("UTC"))
        # Running function and storing its return value
        result = a_func(*args, **kwargs)
        # Capturing args and kwargs in a tuple
        _args = list(args)
        _kwargs = [f"'{key}'={value}" for key, value in kwargs.items()]
        all_args = tuple(_args + _kwargs)
        # Printing logger info (to stdout but could be log server)
        print(f"{run_datetime}: called '{a_func.__name__}{all_args}'")
        return result
    return logger


@function_logger
def func1(a, b, c=10):
    pass


@function_logger
def func2():
    pass


func1(2, 5)  
# 2020-09-24 03:35:01.189122+00:00: called 'func1(2, 5)'
func2()  
# 2020-09-24 03:35:01.189122+00:00: called 'func2()'

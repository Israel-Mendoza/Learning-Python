from typing import Callable


def some() -> str:
    return "This is a string"


def func_returner() -> Callable[[], str]:
    return some


a: Callable[[], str] = func_returner()

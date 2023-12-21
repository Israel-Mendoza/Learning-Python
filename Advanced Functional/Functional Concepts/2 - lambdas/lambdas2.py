from typing import Any
from collections.abc import Callable


"""Using lambdas to pass functions to other functions"""


def apply_function(a: Any, fn: Callable[[Any], Any]) -> Any:
    """Passes 'a' to 'fn' and returns its value"""
    return fn(a)


print(apply_function("Israel", lambda name: f"Hello, {name}"))
# Hello, Israel
print(apply_function("Carlos", lambda name: f"Hello, {name}"))
# Hello, Carlos

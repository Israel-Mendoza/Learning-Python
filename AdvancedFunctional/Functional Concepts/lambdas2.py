"""Using lambdas to pass functions to other functions"""

from typing import Any, Callable


def apply_function(a: Any, fn: Callable) -> Any:
    """Passes a to fn and returns its value"""
    return fn(a)


print(apply_function("Israel", lambda name: f"Hello, {name}"))
# Hello, Israel
print(apply_function("Carlos", lambda name: f"Hello, {name}"))
# Hello, Carlos

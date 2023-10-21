"""DECORATOR FACTORIES w/ FUNCTIONS AND CLASSES"""


from typing import Any
from functools import wraps
from collections.abc import Callable


# Simple decorator factory using a FUNCTION


def simple_decorator(a: int, b: int) -> Callable[..., Any]:
    """Decorator factory"""
    def _simple_decorator(a_func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(a_func)
        def inner(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}" where a={a} and b={b}')
            return a_func(*args, **kwargs)
        return inner
    return _simple_decorator


# Simple decorator factory using a CLASS


class SimpleDecorator:
    """Decorator factory"""

    def __init__(self, a: int, b: int):
        """Initialized the desired "free variables" that self will store"""
        self._a = a
        self._b = b

    def __call__(self, a_func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Using __call__ as a decorator.
        When a SimpleDecorator instance is called,
        it returns a decorated function.
        Args:
            a_func [FunctionType] : Function to be decorated
        Returns:
            a_func decorated
        """
        @wraps(a_func)
        def simple_decorator(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}": a={self._a} and b={self._b}')
            return a_func(*args, **kwargs)
        return simple_decorator


@simple_decorator(10, 20) # Function-based decorator factory
def say_hello(name: str) -> None:
    print(f"Hello, {name}!\n")


@SimpleDecorator(100, 200) # Class-based decorator factory
def say_bye(name: str) -> None:
    print(f"Goodbye, {name}!\n")


say_hello("Israel")
# Running "say_hello" where a=10 and b=20
# Hello, Israel!
say_bye("Israel")
# Running "say_bye": a=100 and b=200
# Goodbye, Israel!


print(say_hello.__name__)
# say_hello  // Original name due to wraps()
print(say_hello.__code__.co_freevars)  
# ('a', 'a_func', 'b')
print(say_hello.__closure__) 
# (<cell: int object>, <cell: function object>, <cell: int object>)
print(say_hello.__annotations__)  #
# {'name': <class 'str'>, 'return': None}
help(say_hello)  # Original metadata due to wraps():
# Help on function say_hello in module __main__:

# say_hello(name: str) -> None
print()

print(say_bye.__name__)  
# say_bye  // Original name due to wraps()
print(say_bye.__code__.co_freevars)
# ('a_func', 'self') // self is the SimpleDecorator instance
print(say_bye.__closure__)
# ((<cell: function object>, <cell: SimpleDecorator object>)
print(say_bye.__annotations__)  
# {'name': <class 'str'>, 'return': None} // Original annotations
help(say_bye)  # Original metadata due to wraps():
# Help on function say_bye in module __main__:

# say_bye(name: str) -> None
print()

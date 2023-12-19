from typing import Any
from collections.abc import Callable
from functools import wraps


"""DECORATOR FACTORIES WITH FUNCTIONS AND CLASSES"""

"""FUNCTION VERSION"""


def simple_decorator(a: int, b: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory"""
    def _simple_decorator(a_func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(a_func)
        def inner(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}" where a={a} and b={b}')
            return a_func(*args, **kwargs)
        return inner
    return _simple_decorator


"""CLASS VERSION"""


class SimpleDecorator:
    """Decorator factory"""

    def __init__(self, a: int, b: int):
        """Initialized the desired "free variables" that self will store"""
        self._a: int = a
        self._b: int = b

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
        def decorator(*args, **kwargs) -> Any:
            print(f'Running "{a_func.__name__}": a={self._a} and b={self._b}')
            return a_func(*args, **kwargs)
        return decorator


@simple_decorator(10, 20)  # Function-based decorator factory
def say_hello(name: str) -> None:
    print(f"Hello, {name}!\n")


@SimpleDecorator(100, 200)  # Class-based decorator factory
def say_bye(name: str) -> None:
    print(f"Goodbye, {name}!\n")


say_hello("Israel")
# Running "say_hello" where a=10 and b=20
# Hello, Israel!
say_bye("Israel")
# Running "say_bye": a=100 and b=200
# Goodbye, Israel!


# ANALYSING THE FUNCTIONS

print(say_hello.__name__)
# say_hello  // Original name due to wraps()
print(say_hello.__code__.co_freevars)  
# ('a', 'a_func', 'b')
print(say_hello.__closure__) 
# (<cell at 0x102e73ee0: int object at 0x10366c4d0>,
# <cell at 0x102e90040: function object at 0x102ee11c0>,
# <cell at 0x102e73fa0: int object at 0x10366c610>)
print(say_hello.__annotations__)  #
# {'name': <class 'str'>, 'return': None}
help(say_hello)  # Original metadata due to wraps():
# Help on function say_hello in module __main__:
#
# say_hello(name: str) -> None


print(say_bye.__name__)  
# say_bye  // Original name due to wraps()
print(say_bye.__code__.co_freevars)
# ('a_func', 'self') // self is the SimpleDecorator instance
print(say_bye.__closure__)
# (<cell at 0x102e913c0: function object at 0x102e7e200>,
# <cell at 0x102e90fa0: SimpleDecorator object at 0x102e907d0>)
print(say_bye.__annotations__)  
# {'name': <class 'str'>, 'return': None} // Original annotations
help(say_bye)  # Original metadata due to wraps():
# Help on function say_bye in module __main__:
#
# say_bye(name: str) -> None

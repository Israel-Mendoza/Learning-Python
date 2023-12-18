from typing import Any, Callable
from functools import wraps

"""Stacked decorators breakdown."""


def decorator_1(a_func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(a_func)
    def inner(*args, **kwargs) -> Any:
        print("Running decorator 1!")
        result: Any = a_func(*args, **kwargs)
        return result
    return inner


def decorator_2(a_func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(a_func)
    def inner(*args, **kwargs) -> Any:
        result: Any = a_func(*args, **kwargs)
        print("Running decorator 2!")
        return result
    return inner


def simple_function(name: str) -> None:
    """Simple function that greets the passed name"""
    print(f"Hello, {name}!")


# Decorating the simple_function function with decorator_1
simple_function_1 = decorator_1(simple_function)

# Stacking another decorator to the already decorated function
simple_function_1 = decorator_2(simple_function_1)

# Another way of stacking decorators to the function:
simple_function_2 = decorator_2(decorator_1(simple_function))

# Another way of decorating the function (reversed than the previous ones):


@decorator_1
@decorator_2
def simple_function_3(name: str) -> None:
    """Simple function that greets the passed name"""
    print(f"Hello, {name}!")


# Running all three decorated functions
simple_function_1("Israel")
# Running decorator 1!
# Hello, Israel!
# Running decorator 2!
print()
simple_function_2("Israel")
# Running decorator 1!
# Hello, Israel!
# Running decorator 2!
print()
simple_function_3("Israel")
# Running decorator 1!
# Hello, Israel!
# Running decorator 2!

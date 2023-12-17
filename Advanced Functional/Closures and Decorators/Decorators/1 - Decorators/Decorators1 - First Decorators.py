from typing import Any, Callable

type Number = int | float


"""Introducing decorators"""


# Defining the decorator function
def counter(a_func: Callable[..., Any]) -> Callable[..., Any]:
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count: int = 0

    def inner(*args, **kwargs) -> Any:
        nonlocal count  # Free variable from outer scope
        count += 1
        print(f"{a_func.__name__} has been called {count} times")
        # Return wrapped function return value when called with passed args
        return a_func(*args, **kwargs)
    # Return the closure
    return inner


"""Implementing the decorator with traditional and @ notation"""


def add(x: Number, y: Number) -> Number:
    """Returns the sum of the passed integers"""
    return x + y


# Original syntax of function decorator
add: Callable[..., Any] = counter(add)


@counter  # Syntactic sugar that replaces line 45
def sub(x: Number, y: Number) -> Number:
    """Returns the subtraction of the passed integers"""
    return x - y


# sub = counter(sub)  // Original syntax of function decorator


"""ORIGINAL METADATA IS LOST. INNER'S WILL BE DISPLAYED"""

print(add.__name__)
# "inner" // name of the closure
print(add.__code__.co_freevars)
# ('a_func', 'count')
print(add.__closure__)
# (<cell at 0x7f92f0166fd0: function object at 0x7f92f016eca0>,
# <cell at 0x7f92f0166fa0: int object at 0x7f92f000e910>)
print(add.__annotations__)  
# {'return': typing.Any}
help(add)  # Metadata of "inner" because of the closure:
# Help on function inner in module __main__:
#
# inner(*args, **kwargs) -> Any

print(sub.__name__)  
# "inner" // name of the closure
print(sub.__code__.co_freevars)  
# ('a_func', 'count')
print(sub.__closure__)
# <cell at 0x7f92f0166d90: function object at 0x7f92f0222790>,
# <cell at 0x7f92f0166d60: int object at 0x7f92f000e910>)
print(sub.__annotations__)  
# {'return': typing.Any}
help(sub)  # Metadata of "inner" because of the closure:
# Help on function inner in module __main__:
#
# inner(*args, **kwargs) -> Any

"""Using the decorated functions"""

print(add(10, 20))  
# add has been called 1 times 
# 30
print(add(20, 30))  
# add has been called 2 times
# 50
print(add(30, 40))  
# add has been called 3 times 
# 70
print()
print(sub(10, 20))  
# sub has been called 1 times
# -10
print(sub(20, 30))  
# sub has been called 2 times 
# -10
print(sub(30, 40))  
# sub has been called 3 times 
# -10

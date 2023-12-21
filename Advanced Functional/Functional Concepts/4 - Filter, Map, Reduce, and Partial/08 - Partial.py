from functools import partial


"""
    A partial function is made up of a callback function 
    and a series of predefined arguments.
    A new callable object is created, and the arguments we 
    passed during its creation will always be passed when 
    this object is called. The remaining arguments (if any) 
    will have to be passed upon the partial class calling. 
"""


"""HARD CODING A PARTIAL FUNCTION"""


def my_func(a: int, b: int, c: int) -> None:
    """Prints the three passed arguments"""
    print(f"a: {a} - b: {b} - c: {c}")


def my_calling_func(a: int, b: int) -> None:
    """Calls my_func and passes 'a' as the first argument,
    'b' as the second argument, and 1000 as the third."""
    my_func(a, b, 1000)


my_func(10, 20, 30)  # a: 10 - b: 20 - c: 30
my_calling_func(10, 20)  # a: 10 - b: 20 - c: 1000
my_calling_func(100, 200)  # a: 100 - b: 200 - c: 1000


"""USING THE PARTIAL CLASS FROM FUNCTOOLS"""

my_partial_func = partial(my_func, 10000)  # Giving it the first argument
my_partial_func(2, 3)  # a: 10000 - b: 20 - c: 30

my_partial_func = partial(my_func, 10000, 20000)  # Giving it the first two arguments
my_partial_func(3)  # a: 10000 - b: 20000 - c: 3

my_partial_func = partial(my_func, 10000, 20000, 30000)  # Giving it all the arguments 'my_func' needs
my_partial_func()  # a: 10000 - b: 20000 - c: 30000

try:
    my_partial_func(10)
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: my_func() takes 3 positional arguments but 4 were given

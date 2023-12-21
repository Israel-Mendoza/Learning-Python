import inspect

"""Using the inspect module to inspect (duh!) functions..."""


# TODO: Are you really just returning True?
def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float) -> bool:
    """A simple function"""
    i = 10
    j = 20
    return True


# Grabbing the source code of the "my_func" function:
my_func_source: str = inspect.getsource(my_func)

print(my_func_source)
# def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float) -> bool:
#     """A simple function"""
#     i = 10
#     j = 20
#     return True

try:
    print(inspect.getsource(print))
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: module, class, method, function, traceback, frame,
# or code object was expected, got builtin_function_or_method

print(inspect.getmodule(my_func))
# <module '__main__' from '/Users/.../FunctionIntrospection3.py'>
print(inspect.getmodule(print))
# <module 'builtins' (built-in)>

my_func_comments: str = inspect.getcomments(my_func)
print(my_func_comments)
# TODO: Are you really just returning True?

import inspect

# TODO: Are you really just returning True?
def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float):
    """A simple function"""
    i = 10
    j = 20
    return True


print(inspect.getsource(my_func))
# def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float):
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
# <module '__main__' from 'c:...FunctionIntrospection3.py'>
print(inspect.getmodule(print))
# <module 'builtins' (built-in)>

print(inspect.getcomments(my_func))
# -> # TODO: Are you really just returning True?

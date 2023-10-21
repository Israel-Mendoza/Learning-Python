def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float):
    """A simple function"""
    i = 10
    j = 20
    return True


"""Introspecting the code object"""

print(my_func.__code__)  # -> <class 'code'>
# <code object my_func at 0x000001F4C960BDF0, file "c:..., line 4>

"""Available attributes from the code object"""
for attr in dir(my_func.__code__):
    print(attr)
# __class__
# __delattr__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __le__
# __lt__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__
# co_argcount
# co_cellvars
# co_code
# co_consts
# co_filename
# co_firstlineno
# co_flags
# co_freevars
# co_kwonlyargcount
# co_lnotab
# co_name
# co_names
# co_nlocals
# co_posonlyargcount
# co_stacksize
# co_varnames
# replace

print(my_func.__code__.co_name)  # -> str // name of the function
# my_func

print(my_func.__code__.co_varnames)  # -> tuple // variable names
# ('a', 'b', 'kw1', 'args', 'kwargs', 'i', 'j')

print(my_func.__code__.co_argcount)  # -> int // argument count without args and kwargs
# 2

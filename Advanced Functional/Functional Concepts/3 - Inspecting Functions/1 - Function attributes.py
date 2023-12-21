"""ANALYSING THE FUNCTION'S ATTRIBUTES"""


def my_func(a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float):
    """A simple function"""
    i = 10
    j = 20
    return True


"""We can add properties to functions because they're objects"""

my_func.description = "A funny short description"
my_func.another_description = "Hahaha"

print(my_func.description)
# A funny short description
print(my_func.another_description)
# Hahaha


"""Available attributes from this object"""
for attr in dir(my_func):
    print(attr)
# __annotations__
# __call__
# __class__
# __closure__
# __code__
# __defaults__
# __delattr__
# __dict__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __get__
# __getattribute__
# __globals__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __kwdefaults__
# __le__
# __lt__
# __module__
# __name__
# __ne__
# __new__
# __qualname__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__
# another_description   !!!
# description           !!!

"""Introspecting these attributes"""


print(my_func.__doc__)  # -> str
# A simple function

print(my_func.__annotations__)  # -> dict
# {'a': list[str],
# 'b': <class 'int'>,
# 'args': <class 'str'>,
# 'kw1': <class 'int'>,
# 'kwargs': <class 'float'>}

print(my_func.__name__)  # -> str
# my_func


print(my_func.__defaults__)  # -> tuple
# (1,)

print(my_func.__kwdefaults__)  # -> dict
# {'kw1': 100}

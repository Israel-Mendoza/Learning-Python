import inspect
from collections.abc import Callable


# TODO: Are you really just returning True?
def my_func[T](a: list[str], b: int = 1, *args: str, kw1: int = 100, **kwargs: float) -> Callable[[T], T]:
    """A simple function"""
    i = 10
    j = 20
    return lambda x: x * x


def simple_func():
    pass


# Grabbing both functions' signatures:
my_func_signature: inspect.Signature = inspect.signature(my_func)
simple_func_signature: inspect.Signature = inspect.signature(simple_func)

print(my_func_signature)  # -> <class 'inspect.Signature'>
# (a: list, b: int = 1, *args: str, kw1: int = 100, **kwargs: float) -> bool
print(simple_func_signature)  # -> <class 'inspect.Signature'>
# ()

# Grabbing my_func's return type... If none is specified, we'll get <inspect._empty>
my_func_return_type: type = my_func_signature.return_annotation
simple_func_return_type: type = simple_func_signature.return_annotation

if my_func_return_type == inspect.Signature.empty:
    print(f"{my_func_return_type}: There is no return type defined")
else:
    print(f"Function's return type is {my_func_return_type}")
# Function's return type is collections.abc.Callable[[T], T]

if simple_func_return_type == inspect.Signature.empty:
    print(f"{simple_func_return_type}: There is no return type defined.")
else:
    print(f"Function's return type is {my_func_return_type}")
# <class 'inspect._empty'>: There is no return type defined.

# Analysing a inspect.Signature's namespace:
for attr in dir(my_func_signature):
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
# __module__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __setstate__
# __sizeof__
# __slots__
# __str__
# __subclasshook__
# _bind
# _bound_arguments_cls
# _hash_basis
# _parameter_cls
# _parameters
# _return_annotation
# bind
# bind_partial
# empty
# from_builtin
# from_callable
# from_function
# parameters
# replace
# return_annotation


for k, param in my_func_signature.parameters.items():
    print(f"Key: {k}")  # str
    print(f"\tName: {param.name}")  # str (same as key)
    print(f"\tDefault: {param.default}")  # Any (inspect._empty if not specified)
    print(f"\tAnnotation: {param.annotation}")  # Any (annotation value)
    print(f"\tKind: {param.kind}")
# Key: a
# 	Name: a
# 	Default: <class 'inspect._empty'>
# 	Annotation: list[str]
# 	Kind: POSITIONAL_OR_KEYWORD
# Key: b
# 	Name: b
# 	Default: 1
# 	Annotation: <class 'int'>
# 	Kind: POSITIONAL_OR_KEYWORD
# Key: args
# 	Name: args
# 	Default: <class 'inspect._empty'>
# 	Annotation: <class 'str'>
# 	Kind: VAR_POSITIONAL
# Key: kw1
# 	Name: kw1
# 	Default: 100
# 	Annotation: <class 'int'>
# 	Kind: KEYWORD_ONLY
# Key: kwargs
# 	Name: kwargs
# 	Default: <class 'inspect._empty'>
# 	Annotation: <class 'float'>
# 	Kind: VAR_KEYWORD

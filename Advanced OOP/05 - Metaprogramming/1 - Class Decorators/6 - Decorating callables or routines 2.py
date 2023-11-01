import inspect
from types import FunctionType


"""Inspecting a class members to know what we need to decorate!"""

"""
    The inspect module provides us with functions that will detect the type of some "callables".
    We'll use these functions to detect what is the actual type of callables we want to decorate. 
"""


class MyClass:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def instance_method(self):
        print(f"{self.name} says hello!")

    @classmethod
    def class_method(cls):
        print(f"{cls.__name__} says hi!")

    @staticmethod
    def static_method():
        print(f"Hello from a static method")

    def __add__(self, other):
        if isinstance(other, MyClass):
            return f"{self.name} + {other.name}"

    class Other:  # Other class is callable itself
        def __call__(self):
            print("Other instance called!")

    other_instance = Other()  # Callable Other instance


# Attributes to analyse
keys = (
    "__init__",
    "name",
    "instance_method",
    "class_method",
    "static_method",
    "__add__",
    "Other",
    "other_instance",
)

# Functions from inspect to use to inspect the keys
inspect_funcs = (
    "isroutine",
    "ismethod",
    "isfunction",
    "isbuiltin",
    "ismethoddescriptor",
)

# Grabbing the longest word in each tuple (keys and inspect_funcs) for formatting only.
max_header: int = max(len(key) for key in keys)
max_funcs_len: int = max(len(func) for func in inspect_funcs)

# Printing header
print(
    format("", f"{max_header}s"),
    "\t".join(format(key, f"{max_header}") for key in keys),
)

# Inspecting each key with each function in inspect
for inspect_func in inspect_funcs:
    fn: FunctionType = getattr(inspect, inspect_func)
    inspect_results = (
        format(str(fn(MyClass.__dict__[key])), f"{max_header}s") for key in keys
    )
    print(format(inspect_func, f"{max_funcs_len}s"), "\t".join(inspect_results))
#                    __init__    name    instance_method	class_method   	static_method  	__add__   Other   other_instance
# isroutine          True        False   True           	True           	True           	True      False   False
# ismethod           False       False   False          	False          	False          	False     False   False
# isfunction         True        False   True           	False          	False          	True      False   False
# isbuiltin          False       False   False          	False          	False          	False     False   False
# ismethoddescriptor False       False   False          	True           	True           	False     False   False


# WHAT WE WANT TO DECORATE ARE ROUTINES!!!

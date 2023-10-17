"""Inspecting a class members to know what we need to decorate!"""


import inspect


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

    class Other:
        def __call__(self):
            print("Other instance called!")

    other_instance = Other()


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

max_header = max(len(key) for key in keys)
max_funcs_len = max(len(func) for func in inspect_funcs)

# Printing header
print(
    format("", f"{max_header}s"),
    "\t".join(format(key, f"{max_header}") for key in keys),
)

# Inspecting each key with each function in inspect
for inspect_func in inspect_funcs:
    fn = getattr(inspect, inspect_func)
    inspect_results = (
        format(str(fn(MyClass.__dict__[key])), f"{max_header}s") for key in keys
    )
    print(format(inspect_func, f"{max_funcs_len}s"), "\t".join(inspect_results))


# WHAT WE WANT TO DECORATE ARE ROUTINES!!!

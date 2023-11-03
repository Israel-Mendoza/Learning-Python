"""__init__ will only be called when __new__ returns the right instance type"""


class Person:
    def __new__(cls, name: str) -> str:
        """Returning a string instead."""
        print(f"__new__ called! Creating {cls.__name__}... Na!")
        instance = str.__new__(str, name)
        print(f"Returning a {type(instance).__name__} instance!")
        return instance

    def __init__(self, name: str) -> None:
        print(f"__init__ called!")
        self.name = name


# Notice how __init__ is not called:
p1 = Person("Israel")
# __new__ called! Creating Person... Na!
# Returning a str instance!

print(f"{p1}: {type(p1)}")
# Israel: <class 'str'>

p1.__init__("Arturo")
# No output because __init__ is taken from the str class, not Person!!!
print(p1)
# Israel (No changes because a str object is initialized using __new__, not __init__)

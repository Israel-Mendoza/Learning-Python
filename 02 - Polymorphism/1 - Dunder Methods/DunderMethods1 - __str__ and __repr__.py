from __future__ import annotations

"""Playing with the __str__ and the __repr__ methods"""

# If only __repr__ is overriden, it'll take precedence to __str__


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        print("__repr__ called")
        return f"Person(name='{self.name}', age={self.age})"


p: Person = Person("Israel", 28)

# Only __repr__ was implemented.
print(repr(p))
# __repr__ called
# Person(name='Israel', age=28)
print(p, end="\n\n")
# __repr__ called
# Person(name='Israel', age=28)


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __str__(self: Person) -> str:
        print("__str__ called")
        return f"Person(name='{self.name}', age={self.age})"


p: Person = Person("Israel", 28)

# Only __str__ was implemented:
print(repr(p))
# <__main__.Person object at 0x7f3611c62e20>
print(p, end="\n\n")
# __str__ called
# Person(name='Israel', age=28)


class Person:
    def __init__(self: Person, name: str, age: int) -> None:
        self.name: str = name
        self.age: str = age

    def __repr__(self: Person) -> str:
        print("__repr__ called")
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self: Person) -> str:
        print("__str__ called")
        return f"{self.name} is {self.age} years old"


p: Person = Person("Israel", 28)

# Both __repr__ and __str__ were implemented:
print(repr(p))
# __repr__ called
# Person(name='Israel', age=28)
print(p)
# __str__ called
# Israel is 28 years old

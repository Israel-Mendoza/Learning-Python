from __future__ import annotations
from typing import override

"""Overriding inherited methods and calling super()"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        print(f"Calling Person(\"{name}\", {age})")
        self.name: str = name
        self.age: int = age

    def __repr__(self: Person) -> str:
        return f"{type(self).__name__}('{self.name}', {self.age})"

    def hello(self) -> None:
        print(f"{self} says hello!")


# Overriding ALL inherited methods and using super()
class Student(Person):
    @override
    def __init__(self, name: str, age: int, major: str) -> None:
        print(f"Calling Student('{name}', {age}, '{major}')")
        super().__init__(name, age)  # Calling the "original" __init__
        self.major: str = major  # Assigning the extra argument the original __init__ didn't account for

    @override
    def __repr__(self: Student) -> str:
        # Overriding the __repr__ method as well.
        return f"{type(self).__name__}({self.name}, {self.age}, {self.major})"

    @override
    def hello(self: Student) -> None:
        print(f"{self} says hello!")  # Doing something extra.
        super().hello()  # Calling the "original" hello() method.


# Creating a Person and a Student instance (calls the __init__ method):
p: Person = Person("Arturo", 74)
# Calling Person(Arturo, 74)
s: Student = Student("Israel", 31, "Computer Science")
# Calling Student('Israel', 31, 'Computer Science')
# Calling Person(Israel, 31)

p.hello()
# Person('Arturo', 74) says hello!
s.hello()
# Student(Israel, 31, Computer Science) says hello!
# Student(Israel, 31, Computer Science) says hello!

from __future__ import annotations
from typing import override


"""Inheriting methods"""


class Person:
    # We could also get the name of the class by calling self.__class__.__name__
    def eat(self) -> None:
        print(f"{type(self).__name__} eats.")

    def work(self) -> None:
        print(f"{type(self).__name__} works.")

    def sleep(self) -> None:
        print(f"{type(self).__name__} sleeps.")

    def routine(self) -> None:
        self.eat()
        self.work()
        self.sleep()


class Student(Person):

    # Student inherits the methods eat() and routine()

    @override
    def work(self: Student) -> None:
        print(f"{type(self).__name__} goes to school.")

    @override
    def sleep(self: Student) -> None:
        print(f"{self.__class__.__name__} rarely sleeps.")


p: Person = Person()
s: Student = Student()

p.routine()
# Person eats.
# Person works.
# Person sleeps.

s.routine()
# Student eats.
# Student goes to school.
# Student rarely sleeps.

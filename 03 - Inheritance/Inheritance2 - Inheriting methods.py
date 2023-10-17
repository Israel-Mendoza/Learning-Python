from __future__ import annotations


"""Inheriting methods"""


class Person:
    def eat(self: Person) -> None:
        print(f"{self.__class__.__name__} eats.")

    def work(self: Person) -> None:
        print(f"{self.__class__.__name__} works.")

    def sleep(self: Person) -> None:
        print(f"{self.__class__.__name__} sleeps.")

    def routine(self: Person) -> None:
        self.eat()
        self.work()
        self.sleep()


class Student(Person):

    # Student inherits the methods eat() and routine()

    # Overriding the 'work' method
    def work(self: Student) -> None:
        print(f"{self.__class__.__name__} goes to school.")

    # Overriding the 'sleep' method
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

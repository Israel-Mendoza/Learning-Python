"""Inheriting methods"""


class Person:
    def eat(self):
        print(f"{self.__class__.__name__} eats")

    def work(self):
        print(f"{self.__class__.__name__} works")

    def sleep(self):
        print(f"{self.__class__.__name__} sleeps")

    def routine(self):
        self.eat()
        self.work()
        self.sleep()


class Student(Person):

    # Student inherits the methods eat() and routine()

    # Overriding the 'work' method
    def work(self):
        print(f"{self.__class__.__name__} goes to school")

    # Overriding the 'sleep' method
    def sleep(self):
        print(f"{self.__class__.__name__} doesn't sleep")


p = Person()
s = Student()

p.routine()
# Person eats
# Person works
# Person sleeps

s.routine()
# Student eats
# Student goes to school
# Student doesn't sleep

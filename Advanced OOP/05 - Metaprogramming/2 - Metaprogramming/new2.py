"""Working with __new__ and __init__ to create class instances"""

from typing import Union

# When calling the class, Python will call the __new__ method
# on the class, and will pass the class as the first argument.
# Then, __init__ will be called on the recently created instance.
# If we want these two methods to work we must make sure that:
#   1. __new__ returns an instance of the class
#   2. __new__ and __init__ must accept the same number of arguments.


class Point:
    def __new__(cls, x: Union[int, float], y: Union[int, float]) -> "Point":
        """
        When Point.__new__ is called,
        cls will be set as the calling class itself.
        Returns an instance of Point.
        """
        print("__new__ called! Creating instance...")
        # Creating a Point instance.
        # object.__new__() accepts only the class to be instantiated.
        point_instance = super().__new__(cls)
        # Returning the created instance
        return point_instance

    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        """Initializing the newly created instance"""
        print("__init__ called! Initializing instance...")
        self.x = x
        self.y = y


p1 = Point(10, 10)
# __new__ called! Creating instance...
# __init__ called! Initializing instance...


"""__new__ in inheritance"""


class Squared(int):
    """A class that represents an int"""

    def __new__(cls, x: int) -> "Squared":
        # super() == int
        # int.__new__ requires an expression to be converted to an int.
        # int.__init__ doesn't take arguments. The instance creation is
        # delegated to the __new__ method.
        # Similar as writing: new_instance = int(x ** 2)
        new_instance = super().__new__(cls, x ** 2)
        return new_instance


my_num1 = Squared.__new__(Squared, 4)
my_num2 = Squared(4)
print(my_num1)  # 16
print(my_num2)  # 16

print(type(my_num1))  # <class '__main__.Squared'>
print(isinstance(my_num1, Squared))  # True
print(isinstance(my_num1, int))  # True


"""Argument list must match between __new__ and __init__"""


class Person:
    def __new__(cls, name: str) -> "Person":
        print(f"Creating a {cls.__name__} instance...")
        # Using object to create the instance.
        instance = object.__new__(cls)
        print(f"Person instance created at address {hex(id(instance)).upper()}")
        return instance

    def __init__(self, name: str) -> None:
        print(f"Initializing Person instance at address {hex(id(self)).upper()}")
        self.name = name


class Student(Person):
    def __new__(cls, name: str, major: str) -> "Student":
        print(f"Creating a {cls.__name__} instance...")
        # Using object to create the instance again
        instance = object.__new__(cls)
        print(f"Student instance created at address {hex(id(instance)).upper()}")
        return instance

    def __init__(self, name: str, major: str) -> None:
        print(f"Initializing Student instance at address {hex(id(self)).upper()}")
        super().__init__(name)
        self.major = major


p1 = Person("Israel")
# Creating a Person instance...
# Person instance created at address 0X266FA9B3F40
# Initializing Person instance at address 0X266FA9B3F40

# See how the Person.__new__() method was not called,
# because we're creating the instance using object.__new__()
s1 = Student("Israel", "Music")
# Creating a Student instance... Student.__new__()
# Student instance created at address 0X26391F66A30 Student.__new__()
# Initializing Student instance at address 0X26391F66A30 (Student.__init__())
# Initializing Person instance at address 0X26391F66A30 (super().__init__())


"""
We must make sure we use super().__new__() and not object.__new__()
when overriding __new__, because we might miss additional tweakings
from the parent class!
Warning! We must pay attention to the parameters the super().__new__ 
method required. 

i.e. object.__new__() will only required the class. If other arguments 
are passed, we will have a TypeError:

TypeError: object.__new__() takes exactly one argument (the type to instantiate)

"""


class Student(Person):
    def __new__(cls, name: str, major: str) -> "Student":
        print(f"Creating a {cls.__name__} instance...")
        # Using object to create the instance again
        instance = super().__new__(cls, name)
        print(f"Student instance created at address {hex(id(instance)).upper()}")
        return instance

    def __init__(self, name: str, major: str) -> None:
        print(f"Initializing Student instance at address {hex(id(self)).upper()}")
        super().__init__(name)
        self.major = major


s1 = Student("Israel", "Music")
# Creating a Student instance...    (Student.__new__())
# Creating a Student instance...    (super().__new__())
# Person instance created at address 0X1BC26978A60 (super().__new__())
# Student instance created at address 0X1BC26978A60 (Student.__new__())
# Initializing Student instance at address 0X1BC26978A60 (Student.__init__())
# Initializing Person instance at address 0X1BC26978A60 (super().__init__())

import pytz
from datetime import datetime

"""
Decorating classes by "monkey patching" them
by adding a new instance method to their namespace.
"""

"""Setting up the decorator"""


# Function(instance method) to be added to a class
def current_object_info(self) -> list[str | dict[str, str]]:
    """
    Returns a list containing a snapshot of the passed object.
    """
    results: list[str | dict[str, str]] = [f"Time: {datetime.now(pytz.UTC)}",
                                           f"Class name: {self.__class__.__name__}",
                                           f"Memory address: {hex(id(self)).upper()}"]
    values: dict[str, str] = {}
    for key, value in self.__dict__.items():
        values[key] = value
    results.append(values)
    return results


# Class decorator. Monkey patches the passed class
def debug_info(cls: type) -> type:
    """
    Class decorator.
    Sets a new attribute called "debug", which 
    returns the "current_object_info" function.
    Returns class with a new attribute called "debug".
    """
    cls.debug = current_object_info
    return cls


"""Decorating the classes at creation time"""


@debug_info  # Decorating the class with the "@" notation
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: name = name
        self.age: int = age

    def __str__(self) -> str:
        return f'Person "{self.name}" is {self.age} years old'


@debug_info  # Decorating the class with the "@" notation
class Car:
    def __init__(self, brand: str, model: str, year: int, top_speed: int) -> None:
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.top_speed: int = top_speed
        self._current_speed: int = 0

    @property
    def current_speed(self) -> int:
        """The Car's current speed"""
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value: int) -> None:
        """
        Sets the current speed if the value is lesser
        or equal to the top_speed.
        Otherwise, raises a ValueError
        """
        value = abs(value)
        if value < self.top_speed:
            self._current_speed = value
        else:
            raise ValueError("Current speed cannot be more than top speed")

    def __str__(self) -> str:
        return f'Car "{self.brand} {self.model} {self.year}"'


"""Working with the classes' instances"""

# Creating a Person and a Car instance
p1 = Person("Israel Mendoza", 28)
c1 = Car("Audi", "T", 2022, 250)

# Capturing the snapshot list
person_info = p1.debug()
car_info = c1.debug()

# Printing the snapshot list item by item
for info in person_info:
    print(info)
# Time: 2020-09-26 05:46:08.088330+00:00
# Class name: Person
# Memory address: 0X11FF5C8
# {'name': 'Israel Mendoza', 'age': 28}

# Printing the snapshot list item by item
for info in car_info:
    print(info)
# Time: 2020-09-26 05:46:08.088330+00:00
# Class name: Car
# Memory address: 0X30A5190
# {'brand': 'Audi', 'model': 'T', 'year': 2015, 'top_speed': 250, '_current_speed': 0}

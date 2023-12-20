from collections.abc import Callable

"""Creating a class decorator factory"""


def debug_info(storing_list: list) -> Callable[[type], type]:
    """
    Decorator factory. Accepts an empty list, which will
    be used as a storing mechanism to the class that gets
    decorated by the returned decorator.
    """
    import pytz
    from datetime import datetime

    def _debug_info(cls: type) -> type:
        """
        Class decorator. Monkey patches the class with a new attribute.
        Sets attribute "debug" to the passed class by assigning the 
        "inner" function.
        """

        def inner(self) -> None:
            """
            Creates and appends the instance snapshot 
            to the "storing_list" free variable.
            """
            print(f"Storing debugging information for {self.__class__.__name__} object @ {hex(id(self)).upper()}")
            # Creating the snapshot list
            results: list[str | dict[str, str]] = [f"Time: {datetime.now(pytz.UTC)}",
                                                   f"Class name: {self.__class__.__name__}",
                                                   f"Memory address: {hex(id(self)).upper()}"]
            values: dict[str, str] = {}
            for key, value in self.__dict__.items():
                values[key] = value
            results.append(values)
            # Appending the snapshot list to the "storing list"
            storing_list.append(results)

        # Setting the attribute
        setattr(cls, "debug", inner)
        # Returning the monkey patched class
        return cls

    # Returning the class decorator
    return _debug_info


"""Creating and decorating classes"""

# Empty list, which will store the instances' snapshots.
my_results: list[str | dict[str, str]] = []


@debug_info(my_results)
class Person:
    """A simple representation of a person"""

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return f'Person "{self.name}" is {self.age} years old'


@debug_info(my_results)
class Car:
    """A simple representation of a car"""

    def __init__(self, brand: str, model: str, year: int, top_speed: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._current_speed = 0

    @property
    def current_speed(self) -> int:
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value: int) -> None:
        value = abs(value)
        if value < self.top_speed:
            self._current_speed = value
        else:
            raise ValueError("Current speed cannot be more than top speed")

    def __str__(self) -> str:
        return f'Car "{self.brand} {self.model} {self.year}"'


# Confirming that classes have the "debug" attribute

print(hasattr(Person, "debug"))  # True
print(hasattr(Car, "debug"))  # True

"""Working with patched class instances"""

# Creating class instances
p1 = Person("Israel", 28)
c1 = Car("Audi", "T", 2015, 250)

# Calling the "debug" method on the instances
p1.debug()
# Storing debugging information for Person object @ 0X39AB2E0
c1.debug()
# Storing debugging information for Car object @ 0X39AB700

# Printing the stored debug information
for result in my_results:
    print("Class snapshot:")
    for info in result:
        print(f"\t{info}")
# Class snapshot:
# 	Time: 2020-09-27 01:54:32.233456+00:00
# 	Class name: Person
# 	Memory address: 0X39AB2E0
# 	{'name': 'Israel', 'age': 28}

# Class snapshot:
# 	Time: 2020-09-27 01:54:32.233456+00:00
# 	Class name: Car
# 	Memory address: 0X39AB700
# 	{'brand': 'Audi', 'model': 'T', 'year': 2015, 'top_speed': 250, '_current_speed': 0}

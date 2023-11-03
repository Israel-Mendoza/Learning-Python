from math import pi

"""Let's learn about class creation"""


# Declaring a simple class
class Circle:
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2


# Circle is a symbol in this module.
# globals() is a dict[str, Any] containing the current scope's global variables
print("Circle" in globals())
# True

# Circle is an instance of type
print(type(Circle))
# <class 'type'>
print(isinstance(Circle, type))
# True

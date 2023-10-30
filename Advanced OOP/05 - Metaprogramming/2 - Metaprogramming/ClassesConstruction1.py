"""Let's learn about class creation"""


from math import pi
from typing import Union


# Declaring a simple class
class Circle:
    def __init__(self, radius: Union[int, float]) -> None:
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


# Circle is a symbol in this module
# globals() -> dict[str, Any] containing
# the current scope's global variables
print("Circle" in globals())
# True

# Circle is an instance of type
print(type(Circle))
# <class 'type'>
print(isinstance(Circle, type))
# True

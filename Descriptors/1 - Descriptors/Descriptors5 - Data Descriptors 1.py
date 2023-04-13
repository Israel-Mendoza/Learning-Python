from __future__ import annotations

"""Introducing data descriptors"""


class IntegerValue:

    """A data descriptor"""

    # This is a data descriptor because it has the __set__ method implemented.

    def __set__(self, instance: any, value: any) -> None:
        """A message gets printed when the setter is called"""
        print(f"__set__ called!!!")
        print(f"{instance = } | {value = }")

    def __get__(self, instance: any, owner: type)-> None:
        # A message describing which object called the attribute
        if instance is None:
            print(f"__get__ called from class '{owner}' (class)!")
        else:
            print(f"__get__ called from '{instance}' (instance)!")


class Point2D:
    x: IntegerValue = IntegerValue()
    y: IntegerValue = IntegerValue()

    def __init__(self, name: str) -> None:
        self.name: str = name

    def __repr__(self) -> str:
        return f"Point2D instance @ {hex(id(self)).upper()}"


p = Point2D("A Point")

"""Calling the __get__ and __set__ of the data descriptor"""

# Accessing the attribute (reading it) will call the __get__ method (as usual):
Point2D.x
# __get__ called from class '<class '__main__.Point2D'>' (class)!
p.x
# __get__ called from 'Point2D instance @ 0X7FA08ACF73D0' (instance)!!

# If we try to "assign" anything to the descriptor attribute through the instance, 
# the  descriptor's __set__ method will be called
p.x = 10
# __set__ called!!!
# instance = Point2D instance @ 0X7F2AC7E07390 | value = 10

# Trying to call the setter from the class will override the attribue value:
Point2D.x = "A random string"

# Notice how the descritor wasn't called, but rather overriden:
print(f"{Point2D.x}")
# A random string
print(f"{p.x = }")
# p.x = 'A random string'

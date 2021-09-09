"""Introducing data descriptors"""


class IntegerValue:

    """A data descriptor"""

    # This is a data descriptor because it has the __set__ method implemented.

    def __set__(self, intance, value) -> None:
        """A message gets printed when the setter is called"""
        print(f"__set__ called!!!")

    def __get__(self, instance, owner)-> None:
        # A message describing which object called the attribute
        if instance is None:
            print(f"__get__ called from class {owner}!")
        else:
            print(f"__get__ called from the class instance {instance}!")


class Point2D:
    x = IntegerValue()
    y = IntegerValue()

    def __init__(self, name: str) -> None:
        self.name = name


p = Point2D("A Point")

"""Calling the __get__ and __set__ of the data descriptor"""

# If only read, the descriptor's __get__ method is called:
Point2D.x
# __get__ called from class <class '__main__.Point2D'>!
p.x
# __get__ called from the class instance <__main__.Point2D object at 0x017D0BF8>!

# If we try to "assign" anything to the descriptor attribute, 
# the  descriptor's __set__ method will be called
p.x = 10
# __set__ called!!!

# Trying to call the setter from the class:
Point2D.x = "A random string"

# Notice how the descritor wasn't called, but rather overriden:
print(f"{p.x = }")
# p.x = 'A random string'

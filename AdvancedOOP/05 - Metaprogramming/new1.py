"""Introducing the __new__ method"""

from typing import Union

# When creating an instance of a class, the __new__ static method
# of the class is caled and passes the class itself as the first parameter:
#
# my_obj = MyClass.__new__(MyClass)
#
# If this method is not defined in the class, it will call it from the
# parent class, as expected.


class Point:
    # Defining __init__ only
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        print(f"__init__ was called - self: {self}")
        self.x = x
        self.y = y


# When the class is called to create an instance, __new__ is called to
# create it and return it without us noticing.
# Then __init__ is then called automatically after __new__,
# passing the recently created instance returned by the __new__ method
# as the first argument.
p1 = Point(10, 20)
# __init__ was called - self: <__main__.Point object at 0x27C57B43FD0>


"""If we don't want to have __init__ called, we must call __new__ directly:"""

p2 = Point.__new__(Point)  # (No output)
p3 = object.__new__(Point)  # (No output)

print(type(p1))  # <class '__main__.Point'>
print(type(p2))  # <class '__main__.Point'>
print(type(p3))  # <class '__main__.Point'>


"""Creating instances using object.__new__()"""


# Notice how __init__ is not called!
p1 = object.__new__(Point, 10, 20)
# (No output from __init__)

# Confirming that __init__ was not called and the namespace is empty
print(p1.__dict__)
# {}

# Calling __init__ ourselves:
p1.__init__(10, 10)
# __init__ was called - self: <__main__.Point object at 0x27C57B428B0>


# Confirming that __init__ was called and the namespace is not empty
print(p1.__dict__)
# {'x': 10, 'y': 10}

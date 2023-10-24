from __future__ import annotations

from typing import Any

"""
    Using a data descriptor to access an instance attribute.
    
    Basically, when using a data descriptor, no matter how deep we 
    manage to store an instance attribute, when the value in question
    is shadowed by a symbol matching the data descriptor, the data descriptor
    will have priority when reading from that symbol. 
    
    When writing a value in an instance namespace, which symbol is the same as 
    the non-data descriptor, the value stored in the namespace will be returned
    since the contents of the instance namespace will have priority over the
    non-data descriptor.
    
    
    obj.a_value -> The data descriptor's __get__ method will be called, no matter
                        if there is an "a_value" key in the object's __dict__
    obj.a_value -> The value of the key "a_value" will be returned if there is one 
                        in the object's __dict__

"""


"""USING A DATA DESCRIPTOR!"""


class IntegerValue:
    def __get__(self, instance: Any, owner: type) -> IntegerValue | None:
        if instance is None:
            return self
        print("__get__ called!")

    def __set__(self, instance: Any, value: int) -> None:
        print("__set__ called!")


class Point:
    x: IntegerValue = IntegerValue()


p: Point = Point()

# Setting and getting a value through the descriptor
# (no instance attribute has the name "x")
p.x = 10
# __set__ called!
p.x
# __get__ called!

# Forcing an entry with the name "x" into the instance's namespace
p.__dict__["x"] = 100000

# Accessing this "new" attribute.
# The descriptor has a priority because it's a DATA DESCRIPTOR
p.x
# __get__ called!


"""USING A NON-DATA DESCRIPTOR!"""


class IntegerValue:
    def __get__(self, instance: Any, owner: type):
        print("__get__ called!")


class Point:
    x: IntegerValue = IntegerValue()


p: Point = Point()

# Getting a value through the descriptor
# (no instance attribute has the name "x")
p.x
# __get__ called!

# Forcing an entry with the name "x" in the instance dictionary
p.__dict__["x"] = 100000

# Accessing this new attribute.
# The entry in the dictionary will be called
# because we are using a NON-DATA DESCRIPTOR
print(p.x)
# 100000

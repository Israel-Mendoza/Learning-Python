from __future__ import annotations

from typing import Any

from utils.utility_functions import print_obj_namespace

"""Using data descriptor's __set__ to store data"""


"""
    At this point, we can start calling the data descriptor's instance a PROPERTY.

    WHAT'S NOT SUPPOSED TO BE DONE:

    Using an INSTANCE ATTRIBUTE to write to and read from, 
    which symbol/name is HARDCODED in the __set__ and __get__ methods.

    Why is this a bad idea?
        1. It's always a bad idea to hardcode attribute names for other objects.
        3. If used, __slots__ must include the name of the hardcoded attribute.
        2. If there is more than one property in the class, they will end up using 
            the same hardcoded instance attribute. 
        We'll be basically stepping on our own toes.
"""


class IntegerValue:
    """Data descriptor to be used as a property for an integer value"""

    def __set__(self, instance: Any, value: int) -> None:
        """
        Storing the value into and instance attribute called "stored_value".
        The user instance class must not implement __slots__,
        or __slots__ must include "stored_value".
            -> This is not supposed to be done, because if we implement more than
               one descriptor in another class, both of them will be overriding
               the "stored_value" attribute in the class instance.
        """
        print(f"{instance}.stored_value = {value}")
        setattr(instance, "stored_value", value)

    def __get__(self, instance: Any, owner: type) -> IntegerValue | int:
        """
        Returns the value stored in the instance's "stored_value" attribute,
        in case the attribute exists. Otherwise, returns None.
        """
        if instance is None:
            return self
        return getattr(instance, "stored_value", None)


class Point1D:
    """A one-dimension point"""
    x: IntegerValue = IntegerValue()

    def __repr__(self) -> str:
        return f"(Point1D object @ {hex(id(self)).upper()})"


class Point2D:
    """A two-dimension point"""
    # This is not supposed to be done:
    x: IntegerValue = IntegerValue()
    y: IntegerValue = IntegerValue()

    def __repr__(self) -> str:
        return f"(Point2D object @ {hex(id(self)).upper()})"


# Creating Point1D instances
p1: Point1D = Point1D()
p2: Point1D = Point1D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# (Point1D object @ 0X7F856C5B7F50)'s NAMESPACE:
print_obj_namespace(p2)
# (Point1D object @ 0X7F856C5B7F90)'s NAMESPACE:

p1.x = 10
# (Point1D object @ 0X7F856C5B7F50).stored_value = 10
p2.x = 20
# (Point1D object @ 0X7F856C5B7F90).stored_value = 20

# p1 and p2's namespaces are populated by the setter
print_obj_namespace(p1)
# (Point1D object @ 0X7F856C5B7F50)'s NAMESPACE:
# (Point1D object @ 0X7F856C5B7F50).stored_value -> 10
print_obj_namespace(p2)
# (Point1D object @ 0X7F856C5B7F90)'s NAMESPACE:
# (Point1D object @ 0X7F856C5B7F90).stored_value -> 20


#########################################################################
#########################################################################

# USING Point2D class

# Creating Point2D instances
p1: Point2D = Point2D()
p2: Point2D = Point2D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# (Point2D object @ 0X7F856C5B7FD0)'s NAMESPACE:

print_obj_namespace(p2)
# (Point2D object @ 0X7F856C5B7F50)'s NAMESPACE:


# Using the setters to set the instance's attribute
p1.x = 100
# (Point2D instance @ 0X7F856C5B7FD0).stored_value = 100
p1.y = 200
# (Point2D instance @ 0X7F856C5B7FD0).stored_value = 200
p2.x = 1000
# (Point2D instance @ 0X7F856C5B7F50).stored_value = 1000
p2.y = 2000
# (Point2D instance @ 0X7F856C5B7F50).stored_value = 2000

# p1 and p2's namespaces are populated by the setter but not as we imagined,
# because the setter is OVERRIDING the same attribute ("stored_value")
# Where are the 100 and 1000 integers now???

print_obj_namespace(p1)
# (Point2D instance @ 0X7F856C5B7FD0)'s NAMESPACE:
# (Point2D instance @ 0X7F856C5B7FD0).stored_value -> 200

print_obj_namespace(p2)
# (Point2D instance @ 0X7F856C5B7F50)'s NAMESPACE:
# (Point2D instance @ 0X7F856C5B7F50).stored_value -> 2000

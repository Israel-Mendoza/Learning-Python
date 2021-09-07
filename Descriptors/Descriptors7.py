"""Using data descriptor's __set__ to store data"""


# WHAT'S NOT SUPPOSED TO BE DONE

# Storing the setter's passed value to an instance attribute,
# which name has been hardcoded in the __set__ method.


from typing import Any


def print_obj_namespace(an_obj: Any) -> None:
    print(f"{an_obj} NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


class IntegerValue:
    """Data descriptor"""

    def __set__(self, instance, value):
        """
        Storing the passed value the instance attribute 
        called "stored_value".
        The instance class must not implement __slots__
        or __slots__ must include "stored_value".
        """
        print(f"{instance}.stored_value = {value}")
        instance.stored_value = value

    def __get__(self, instance, owner):
        """
        Returns the value of instance.stored_value, in
        case the attribute exists. Otherwise, returns None.
        """
        if instance is None:
            return self
        return getattr(instance, "stored_value", None)


class Point1D:
    """A one-dimension point"""
    x = IntegerValue()


class Point2D:
    """A two-dimension point"""
    x = IntegerValue()
    y = IntegerValue()


# Creating Point1D instances
p1 = Point1D()
p2 = Point1D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
print_obj_namespace(p2)
# <__main__.Point1D object at 0x03050A78> NAMESPACE:
# <__main__.Point1D object at 0x03050FD0> NAMESPACE:

p1.x = 10
# <__main__.Point1D object at 0x03650A78>.stored_value = 10
p2.x = 20
# <__main__.Point1D object at 0x03650FD0>.stored_value = 20
print()

# p1 and p2's namespaces are populated by the setter
print_obj_namespace(p1)
# <__main__.Point1D object at 0x014C0A78> NAMESPACE:
# <__main__.Point1D object at 0x014C0A78>.stored_value -> 10
print_obj_namespace(p2)
# <__main__.Point1D object at 0x014C0FD0> NAMESPACE:
# <__main__.Point1D object at 0x014C0FD0>.stored_value -> 20



# USING Point2D class
print("*" * 50)

# Creating Point2D instances
p1 = Point2D()
p2 = Point2D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# <__main__.Point2D object at 0x03548538> NAMESPACE:

print_obj_namespace(p2)
# <__main__.Point2D object at 0x01070A78> NAMESPACE:


# Using the setters to set the instance's attribute
p1.x = 100
# <__main__.Point2D object at 0x03548538>.stored_value = 100
p1.y = 200
# <__main__.Point2D object at 0x03548538>.stored_value = 200
p2.x = 1000
# <__main__.Point2D object at 0x01070A78>.stored_value = 1000
p2.y = 2000
# <__main__.Point2D object at 0x01070A78>.stored_value = 2000
print()

# p1 and p2's namespaces are populated by the setter
# but not as we imagine (because the setter is overriding the same attribute)
print_obj_namespace(p1)
# <__main__.Point2D object at 0x03548538> NAMESPACE:
# <__main__.Point2D object at 0x03548538>.stored_value -> 200

print_obj_namespace(p2)
# <__main__.Point2D object at 0x01070A78> NAMESPACE:
# <__main__.Point2D object at 0x01070A78>.stored_value -> 2000

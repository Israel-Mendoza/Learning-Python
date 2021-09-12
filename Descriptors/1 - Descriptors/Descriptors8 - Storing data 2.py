"""Using data descriptor's __set__ to store data"""

# WHAT'S NOT SUPPOSED TO BE DONE

# Using an INSTANCE ATTRIBUTE to write to and read from, 
# which name is specified when initializing the property instance.
# 
# Why is this a bad idead?
#   1. The name of the class attribute must be set twice (x = Descriptor("x")) 
#   2. We are assuming the name if the instance attribute ("_" + attribute) 
#       is not used by the instance namespace. If it is, we can be overriding 
#       its contents. 
#   3. Using __slots__ will be even more difficult, since the name of the instance attribute
#       will habe to be calculated beforehand in order to be included in __slots__

from typing import Any, Type


def print_obj_namespace(an_obj):
    """A simple function that prints the namespace of any passed object"""
    print(f"{an_obj} NAMESPACE:")
    print(f"{an_obj.__dict__}\n")


class IntegerValue:

    def __init__(self, name: str) -> None:
        """
        Initializing the descriptor by storing the name 
        of the instance attribute we'll use to store
        the intance attribute's value.
        The name will be preceeded by an underscore.
        The instance class must not implement __slots__
        or __slots__ must include "_" + name.
        For instance, if the string "foo" is passed, 
        the descriptor will be writing and reading
        to and from the instance attribute "_foo".
        """
        self.storage_name = f"_{name}"

    def __set__(self, instance: Any, value: Any) -> None:
        """
        Sets the passed value to the instance attribute,
        which name is contained in self.storage_name
        Notice how the value is stored in the actual 
        instance's namespace.
        """
        print(f"{instance}.{self.storage_name} = {value}")
        setattr(instance, self.storage_name, value)

    def __get__(self, instance: Any, owner: Type) -> Any:
        """
        Gets the the instance attribute,
        which name is contained in self.storage_name 
        in case the attribute exists. Otherwise, returns None.
        """
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


class Point1D:
    # Class attribute "x" is an IntegerValue 
    # data descriptor, which will be writing to 
    # and reading from a Point1D instance called "_x"
    x = IntegerValue("x")


class Point2D:
    # Class attributes "x" and "y" are IntegerValue 
    # data descriptors, that will be writing to 
    # and reading from a Point1D instance attributes 
    # called "_x" and "_y", respectively.
    x = IntegerValue("x")
    y = IntegerValue("y")


p1 = Point1D()
p2 = Point1D()

# p1 and p2's namespaces are now empty:
print_obj_namespace(p1)
# <__main__.Point1D object at 0x03480FE8> NAMESPACE: 
# {}
print_obj_namespace(p2)
# <__main__.Point1D object at 0x034A2310> NAMESPACE: 
# {}

# Using the IntegerValue descriptor to set values:
p1.x = 10
# <__main__.Point1D object at 0x03480FE8>._x = 10
p2.x = 20
# <__main__.Point1D object at 0x034A2310>._x = 20
print()

# p1 and p2's namespaces were updated by the setter:
print_obj_namespace(p1)
# <__main__.Point1D object at 0x03480FE8> NAMESPACE:
# {'_x': 10}

print_obj_namespace(p2)
# <__main__.Point1D object at 0x034A2310> NAMESPACE:
# {'_x': 20}

######################################################################
######################################################################

# Reinstiantiating p1 and p2 as Point2D objects
p1 = Point2D()
p2 = Point2D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# <__main__.Point2D object at 0x03799550> NAMESPACE:
# {}

print_obj_namespace(p2)
# <__main__.Point2D object at 0x012A0FE8> NAMESPACE:
# {}

# Using the IntegerValue descriptor to set values:
p1.x = 100
# <__main__.Point2D object at 0x03799550>._x = 100
p1.y = 200
# <__main__.Point2D object at 0x03799550>._y = 200
p2.x = 1000
# <__main__.Point2D object at 0x012A0FE8>._x = 1000
p2.y = 2000
# <__main__.Point2D object at 0x012A0FE8>._y = 2000
print()


# p1 and p2's namespaces were populated by the setter
print_obj_namespace(p1)
# <__main__.Point2D object at 0x03799550> NAMESPACE:
# {'_x': 100, '_y': 200}

print_obj_namespace(p2)
# <__main__.Point2D object at 0x012A0FE8> NAMESPACE:
# {'_x': 1000, '_y': 2000}

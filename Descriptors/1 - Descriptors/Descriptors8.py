"""Using data descriptor's __set__ to store data"""

# WHAT'S NOT SUPPOSED TO BE DONE

# Storing the setter's passed value
# to an instance attribute, which name is specified
# when initializing the data descriptor's instance


from typing import Any, Type


def print_obj_namespace(an_obj):
    print(f"{an_obj} NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


class IntegerValue:

    def __init__(self, name: str) -> None:
        """
        Initializing the name of the instance attribute the descriptor
        will be getting from and setting to.
        The name will be preceeded by an underscore.
        The instance class must not implement __slots__
        or __slots__ must include "_" + name.
        """
        self.storage_name = f"_{name}"

    def __set__(self, instance: Any, value: Any) -> None:
        """
        Sets the passed value to the instance attribute,
        which name is contained in self.storage_name
        """
        print(f"{instance}.{self.storage_name} = {value}")
        instance.__dict__[self.storage_name] = value

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

    x = IntegerValue("x")


class Point2D:

    x = IntegerValue("x")
    y = IntegerValue("y")


p1 = Point1D()
p2 = Point1D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# <__main__.Point1D object at 0x03480FE8> NAMESPACE:

print_obj_namespace(p2)
# <__main__.Point1D object at 0x034A2310> NAMESPACE:

p1.x = 10
# <__main__.Point1D object at 0x03480FE8>._x = 10
p2.x = 20
# <__main__.Point1D object at 0x034A2310>._x = 20
print()

# p1 and p2's namespaces are populated by the setter
print_obj_namespace(p1)
# <__main__.Point1D object at 0x03480FE8> NAMESPACE:
# <__main__.Point1D object at 0x03480FE8>._x           -> 10

print_obj_namespace(p2)
# <__main__.Point1D object at 0x034A2310> NAMESPACE:
# <__main__.Point1D object at 0x034A2310>._x           -> 20

# USING Point2D class
print("*" * 50)

p1 = Point2D()
p2 = Point2D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# <__main__.Point2D object at 0x03799550> NAMESPACE:

print_obj_namespace(p2)
# <__main__.Point2D object at 0x012A0FE8> NAMESPACE:

# Using the setters to set the instance's attribute
p1.x = 100
# <__main__.Point2D object at 0x03799550>._x = 100
p1.y = 200
# <__main__.Point2D object at 0x03799550>._y = 200
p2.x = 1000
# <__main__.Point2D object at 0x012A0FE8>._x = 1000
p2.y = 2000
# <__main__.Point2D object at 0x012A0FE8>._y = 2000
print()


# p1 and p2's namespaces are populated by the setter
print_obj_namespace(p1)
# <__main__.Point2D object at 0x03799550> NAMESPACE:
# <__main__.Point2D object at 0x03799550>._x           -> 100
# <__main__.Point2D object at 0x03799550>._y           -> 200

print_obj_namespace(p2)
# <__main__.Point2D object at 0x012A0FE8> NAMESPACE:
# <__main__.Point2D object at 0x012A0FE8>._x           -> 1000
# <__main__.Point2D object at 0x012A0FE8>._y           -> 2000

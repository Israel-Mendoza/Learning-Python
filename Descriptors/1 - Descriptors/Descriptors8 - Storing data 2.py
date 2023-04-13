from __future__ import annotations

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
#       will have to be calculated beforehand in order to be included in __slots__


def print_obj_namespace(an_obj: any) -> None:
    """
    A simple function that prints the namespace of any passed object.
    This is for debugging purposes. 
    """
    print(f"{an_obj}'s NAMESPACE:")
    print(f"{an_obj.__dict__}\n")


class IntegerValue:

    def __init__(self, name: str) -> None:
        """
        Initializing the descriptor by storing the name 
        of the instance attribute we'll use to store
        the intance attribute's value.
        We'll prefix the passed name with an underscore.
        The instance class must not implement __slots__
        or __slots__ must include "_" + the passed name.
        For instance, if the string "foo" is passed, 
        the descriptor will be writing and reading
        to and from the instance attribute "_foo".
        """
        self.storage_name = f"_{name}"

    def __set__(self, instance: any, value: int) -> None:
        """
        Sets the passed value to the instance attribute,
        which name is contained in self.storage_name
        Notice how the value is stored in the actual 
        instance's namespace.
        """
        print(f"{instance}.{self.storage_name} = {value}")
        setattr(instance, self.storage_name, value)

    def __get__(self, instance: any, owner: type) -> IntegerValue | int:
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

    def __repr__(self) -> str:
        return f"(Point1D instance @ {hex(id(self)).upper()})"


class Point2D:
    # Class attributes "x" and "y" are IntegerValue 
    # data descriptors, that will be writing to 
    # and reading from a Point1D instance attributes 
    # called "_x" and "_y", respectively.
    x = IntegerValue("x")
    y = IntegerValue("y")

    def __repr__(self) -> str:
        return f"(Point1D instance @ {hex(id(self)).upper()})"


p1: Point1D = Point1D()
p2: Point1D = Point1D()

# p1 and p2's namespaces are now empty:
print_obj_namespace(p1)
# (Point1D instance @ 0X7F44BE1206D0)'s NAMESPACE:
# {}
print_obj_namespace(p2)
# (Point1D instance @ 0X7F44BE120710)'s NAMESPACE:
# {}

# Using the IntegerValue descriptor to set values:
p1.x = 10
# (Point1D instance @ 0X7F44BE1206D0)._x = 10
p2.x = 20
# (Point1D instance @ 0X7F44BE120710)._x = 20
print()

# p1 and p2's namespaces were updated by the setter:
print_obj_namespace(p1)
# (Point1D instance @ 0X7F44BE1206D0)'s NAMESPACE:
# {'_x': 10}

print_obj_namespace(p2)
# (Point1D instance @ 0X7F44BE120710)'s NAMESPACE:
# {'_x': 20}

######################################################################
######################################################################

# Reinstiantiating p1 and p2 as Point2D objects
p1: Point2D = Point2D()
p2: Point2D = Point2D()

# p1 and p2's namespaces are now empty
print_obj_namespace(p1)
# (Point1D instance @ 0X7F44BE120750)'s NAMESPACE:
# {}

print_obj_namespace(p2)
# (Point1D instance @ 0X7F44BE1206D0)'s NAMESPACE:
# {}

# Using the IntegerValue descriptor to set values:
p1.x = 100
# (Point1D instance @ 0X7F44BE120750)._x = 100
p1.y = 200
# (Point1D instance @ 0X7F44BE120750)._y = 200
p2.x = 1000
# (Point1D instance @ 0X7F44BE1206D0)._x = 1000
p2.y = 2000
# (Point1D instance @ 0X7F44BE1206D0)._y = 2000
print()


# p1 and p2's namespaces were populated by the setter
print_obj_namespace(p1)
# (Point1D instance @ 0X7F44BE120750)'s NAMESPACE:
# {'_x': 100, '_y': 200}}

print_obj_namespace(p2)
# (Point1D instance @ 0X7F44BE1206D0)'s NAMESPACE:
# {'_x': 1000, '_y': 2000}

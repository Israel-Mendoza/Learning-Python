"""Using data descriptor's __set__ to store data"""

# WHAT'S NOT SUPPOSED TO BE DONE

# Using a dictionary in the descriptor to store 
# the instance's attributes.
# The instance is the key, the value, the value.
# 
# Why is this a bad idea?
# 1. Because the storing dictionary may keep containing
#       references to objects that may stop existing in the main
#       scope of the program, which will prevent the Garbage Collector
#       from claiming that object's memory.
# 2. This can be memory expensive, and may return the wrong value
#       if Python decides to reuse the same memory address.
# 3. The key in the dictionary (the passed instance) must be a hashable object.


import ctypes


def get_ref_count(address: int):
    """
    A simple function that returns the number of 
    references to a given object in memory, 
    which address is the passed integer.
    """
    return ctypes.c_long.from_address(address).value


def print_obj_namespace(an_obj):
    """A simple function that prints the namespace of any passed object"""
    print(f"{an_obj} NAMESPACE:")
    print(f"{an_obj.__dict__}\n")


class IntegerValue:

    def __init__(self):
        """
        Initializing an empty dict where the intances will be keys,
        and the set values, the values.
        The instance must be hashable and a reference to the instance
        will be held in the self.values dictionary until it gets deleted.
        This can prevent the Garbage Collector from releasing the instance 
        memory.
        """
        self.values = {}

    def __set__(self, instance, value):
        """
        Adds/updates an entry to the self.values dictionary
        where the key is the instance, and the value, the passed value
        """
        print(f"Adding/Updating instance's value in descriptor.")
        self.values[instance] = value

    def __get__(self, instance, owner):
        """
        Returns the value of the instance, in
        case the entry exists in the self.values dictionary. 
        Otherwise, returns None.
        """
        if instance is None:
            return self
        print(f"Getting instance's value from descriptor")
        return self.values.get(instance, None)


class Point1D:

    x = IntegerValue()

    # Feel free to use slots, since the x property won't 
    # be using the instance's namespace to store any data.
    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name

    def __hash__(self) -> int:
        # Remember that the object must be hashable if we want 
        # the IntegerValue property to store values for this instance
        return hash(self.name)

    def show_x_descriptor(self) -> None:
        """
        Prints the contents of the "values" dictionary
        in the data descriptor instance.
        """
        for k, v in self.__class__.x.values.items():
            print(f"{k} -> {v}")


# Creating two instances of Point1D
p1 = Point1D("p1")
p2 = Point1D("p2")

# Storing p1's address into a variable
p1_address = id(p1)
print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 1

# Using the descriptor to set and get:
p1.x = 10
# Adding/Updating instance's value in descriptor.
p2.x = 20
# Adding/Updating instance's value in descriptor.
p1.x
# Getting instance's value from descriptor
p2.x
# Getting instance's value from descriptor

# Repeated info, because the descriptor holds the data for
# all of the instances that have used it:
p1.show_x_descriptor()
# <__main__.Point1D object at 0x03890C28> -> 10 // (p1)
# <__main__.Point1D object at 0x03890748> -> 20 // (p2)
p2.show_x_descriptor()
# <__main__.Point1D object at 0x03890C28> -> 10 // (p1)
# <__main__.Point1D object at 0x03890748> -> 20 // (p2)
print()

"""Memory caveats. Possible memory leaks."""

print(f"{hex(p1_address).upper() = }")
# p1 memory address: 0X3890C28
print(f"{get_ref_count(p1_address) = }")
# p1 reference count: 2
print(f"{'p1' in globals() = }") # Does "p1" exist in the global scope?
# 'p1' in globals() = True

# Deleting p1 from global scope
del p1

print(f"{'p1' in globals() = }") # Does "p1" exist in the global scope?
# 'p1' in globals() = False
print(f"p1 reference count: {get_ref_count(p1_address)}")
# p1 reference count: 1

print("Where is this reference to this object?")
print(f"Address in the descriptor's dict: "
      f"{hex(id(list(Point1D.x.values.keys())[0])).upper()}")
# Address in the descriptor's dict: 0X3890C28
print(p1_address == id(list(Point1D.x.values.keys())[0]))
# True

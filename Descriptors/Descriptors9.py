"""Using data descriptor's __set__ to store data"""

# WHAT'S NOT SUPPOSED TO BE DONE

# Using a dictionary within the descriptor's instance
# to store the instance's attributes.
# The instance is the key, the value, the value.

from ctypes import c_long


def get_ref_count(address: int):
    return c_long.from_address(address).value


def print_obj_namespace(an_obj):
    print(f"{an_obj} NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


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

    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name

    def __hash__(self) -> int:
        return hash(self.name)

    def show_x_descriptor(self) -> None:
        """
        Prints the contents of the "values" dictionary
        in the data descriptor instance.
        """
        for k, v in self.__class__.x.values.items():
            print(f"{k} -> {v}")


p1 = Point1D("p1")
p2 = Point1D("p2")

p1_address = id(p1)
print(f"p1 reference count: {get_ref_count(p1_address)}")
# p1 reference count: 1

p1.x = 10
# Adding/Updating instance's value in descriptor.
p2.x = 20
# Adding/Updating instance's value in descriptor.
p1.x
# Getting instance's value from descriptor
p2.x
# Getting instance's value from descriptor

# Repeated info, because there is a single descriptor
# object holding the values:
p1.show_x_descriptor()
# <__main__.Point1D object at 0x03890C28> -> 10
# <__main__.Point1D object at 0x03890748> -> 20
p2.show_x_descriptor()
# <__main__.Point1D object at 0x03890C28> -> 10
# <__main__.Point1D object at 0x03890748> -> 20
print()

"""Memory caveats. Possible memory leaks."""

p1_address = id(p1)
print(f"p1 memory address: {hex(p1_address).upper()}")
# p1 memory address: 0X3890C28
print(f"p1 reference count: {get_ref_count(p1_address)}")
# p1 reference count: 2
print(f"Is p1 in the global scope? {'p1' in globals()}")
# Is p1 in the global scope? True

# Deleting p1 from global scope
print(f"Deleting p1 from the global scope.")
del p1

print(f"Is p1 in the global scope still? {'p1' in globals()}")
# Is p1 in the global scope still? False
print(f"p1 reference count: {get_ref_count(p1_address)}")
# p1 reference count: 1
print("Where is this reference to this object?")
print(f"Address in the descriptor's dict: "
      f"{hex(id(list(Point1D.x.values.keys())[0])).upper()}")
# Address in the descriptor's dict: 0X3890C28
print(p1_address == id(list(Point1D.x.values.keys())[0]))
# True

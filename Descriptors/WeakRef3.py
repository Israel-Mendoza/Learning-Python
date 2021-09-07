"""
Using WeakKeyDictionary in a data descriptor to store 
the instance as the key, and the value as the value.
The keys are only weak references.
Pros:
    The WeakKeyDictionary doesn't create a direct reference
    to the instance, which prevents memory leaks.
Cons:
    Instance must be hashable to be used as a key for the dictionary.
"""

import weakref
from ctypes import c_long


def get_ref_count(address: int) -> int:
    """
    Returns the reference count to the object
    in the passed address.
    """
    return c_long.from_address(address).value


class IntegerValue:

    def __init__(self):
        """
        Initializing an empty WeakKeyDictionary intance where the intances 
        will be keys, and the set values, the values.
        Instances used as keys must be hashable.
        """
        # Creating an empty WeakKeyDictionary to store 
        # the instances and their values 
        self.values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        """
        Creates/updates an entry in the self.value WeakKeyDictionary instance,
        where the key is the passed instance and the value is the passed value.
        The instance must be a hashable object!
        """
        self.values[instance] = value

    def __get__(self, instance, owner):
        """
        Returns the instance's corresponding value from the
        self.values WeakKeyReference dictionary.
        """
        if instance is None:
            return self
        return self.values.get(instance, None)


class Point1D:

    x = IntegerValue()

    @classmethod
    def show_x_descriptor(cls):
        print(f"{cls.__name__}.x's values:")
        for k, v in cls.x.values.items():
            print(f"{k} : {v}")


# Creating a couple of Point1D instances and 
# storing their address information.
p1 = Point1D()
p1_address = id(p1)
p1_hex_address = hex(p1_address).upper()
p2 = Point1D()
p2_address = id(p2)
p2_hex_address = hex(p2_address)

print(f"p1's address: {p1_hex_address}") # p1's address: 0X31A4868
print(f"References to {p1_hex_address}: {get_ref_count(p1_address)}")
# References to 0X31A4868: 1
print()
p1.x = 10
p2.x = 20
print(f"p1.x = {p1.x}")
# p1.x = 10
print()

print(f"References to {p1_hex_address}: {get_ref_count(p1_address)}")
# References to 0X31A4868: 1
print()

Point1D.show_x_descriptor()
# Point1D.x's values:
# <__main__.Point1D object at 0x031A4868> : 10
# <__main__.Point1D object at 0x031A4880> : 20
print()

print(f"Deleting p1")
del p1
print()

Point1D.show_x_descriptor()
# Point1D.x's values:
# <__main__.Point1D object at 0x031A4880> : 20
print()

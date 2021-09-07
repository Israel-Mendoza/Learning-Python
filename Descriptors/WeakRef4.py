"""
Using a dictionary in a data descriptor to store 
the instance's address as the key, and the value as the value.
Pros:
    Instances don't have to be hashable.
Cons:
    The key will remain in the dictionary even though the object
    is destroyed. 
    This can be memory expensive, and may return the wrong value
    if Python decides to reuse the same memory address.
"""

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
        Initializing an empty dictionary where the intances 
        will be keys, and the set values, the values.
        """
        self.values = {}

    def __set__(self, instance, value):
        """
        Creates an entry in the self.value dictionary,
        where the key is the passed instance's address
        and the value is the passed value.
        """
        self.values[id(instance)] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.values.get(id(instance), None)


class Point1D:

    x = IntegerValue()

    def __eq__(self, other):
        """
        Implementing the = operator for the class.
        Also, making sure this is not a hashable object.
        """
        if isinstance(other, self.__class__):
            return self.x == other.x
        else:
            return NotImplemented

    @classmethod
    def show_x_descriptor(cls):
        print(f"{cls.__name__}.x's values:")
        for k, v in cls.x.values.items():
            print(f"Address {hex(k).upper()}:{v}")


p1 = Point1D()
p1_address = id(p1)
p1_hex_address = hex(p1_address).upper()
p2 = Point1D()
p2_address = id(p2)
p2_hex_address = hex(p2_address)

print(f"p1's address: {p1_hex_address}")
print(f"References to {p1_hex_address}: {get_ref_count(p1_address)}")
print()
print(f"p2's address: {p2_hex_address}")
print(f"References to {p2_hex_address}: {get_ref_count(p2_address)}")
print()
p1.x = 10
p2.x = 20
print(f"p1.x = {p1.x}")
print(f"p2.x = {p2.x}")
print()

print(f"References to {p1_hex_address}: {get_ref_count(p1_address)}")
print(f"References to {p2_hex_address}: {get_ref_count(p2_address)}")
print()

Point1D.show_x_descriptor()
print()

print(f"Deleting both p1 and p2!!!")
del p1, p2
print()

try:
    print(p1)
except NameError as error:
    print(error)

try:
    print(p2)
except NameError as error:
    print(error)
print()

Point1D.show_x_descriptor()
print("ENTRIES ARE STILL THERE!!!")
print()

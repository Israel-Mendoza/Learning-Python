"""
Using the weak reference class.
weakref.ref is an alias for weakref.ReferenceType(Generic[_T]):
"""

import weakref
from ctypes import c_long


def get_ref_count(address: int) -> int:
    """
    Returns the reference count to the object
    in the passed address.
    """
    return c_long.from_address(address).value


class Person:
    """A class that represents a person"""
    def __init__(self, name: str) -> None:
        """Initializing the name of the Person"""
        self.name = name

    def __repr__(self):
        """The string representation of the Person instance"""
        return f"Person('{self.name}')"


p1 = Person("Israel")
p1_address = id(p1)
p1_hex_address = hex(p1_address).upper()

print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
# Reference count on 0X2DAF5C8: 1
print()

p2 = p1
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
# Reference count on 0X2DAF5C8: 2
print()

# Creating a weak reference object
weak1 = weakref.ref(p1)
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
# Reference count on 0X2DAF5C8: 2
print()

print(f"What is 'weak1' pointing to then? {weak1}")
# What is 'weak1' pointing to then? <weakref at 0x01C230C8; to 'Person' at 0x01BDF5C8>
print()

# The weak reference object is a callable that returns the object it point to
p3 = weak1()
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
# Reference count on 0X1BDF5C8: 3
print()

print("Deleting p3.")
del p3
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
# Reference count on 0X387F5C8: 2
print()

print("Deleting p1 and p2.")
del p1, p2
print(f"Reference count on {p1_hex_address}: {get_ref_count(p1_address)}")
# Reference count on 0X387F5C8: 0
print()

print(f"What is weak1 pointing to? {weak1} --> {weak1()}")
# What is weak1 pointing to? <weakref at 0x03BC7BB8; dead> --> None

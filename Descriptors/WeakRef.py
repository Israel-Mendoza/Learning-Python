"""
Understanding why weak references are necessary.
Reviewing how reference count works.
"""

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
p2 = p1
obj_address = id(p1)
obj_hex_address = hex(obj_address).upper()

print(f"id(p1) = {hex(id(p1)).upper()}") # 0X329F5C8
print(f"id(p2) = {hex(id(p2)).upper()}") # 0X329F5C8
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X329F5C8: 2
print()

# Deleting p1
print(f"Deleting p1")
del p1
print()

print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X329F5C8: 1
print()

# Deleting p1
print(f"Deleting p2")
del p2
print()

# The reference count is now meaningless
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X329F5C8: 2

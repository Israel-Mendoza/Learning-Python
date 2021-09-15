"""Understanding why weak references are necessary."""

# Playing around with strong references and the strong reference count.


import ctypes


def get_ref_count(address: int) -> int:
    """
    A simple function that returns
    the number or references to a
    given object in memory, which
    address is the passed integer.
    """
    return ctypes.c_long.from_address(address).value


class Person:
    def __init__(self, name: str) -> None:
        """Initializing the name of the Person"""
        self.name = name


p1 = Person("Israel")
p2 = p1
obj_address = id(p1)
obj_hex_address = hex(obj_address).upper()

print(f"{hex(id(p1)).upper() = }")
# hex(id(p1)).upper() = '0X7F113094DFA0'
print(f"{hex(id(p2)).upper() = }")
# hex(id(p2)).upper() = '0X7F113094DFA0'
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X7F113094DFA0: 2

# 'p1' and 'p2' are in in the global scope:
print(f"{'p1' in globals() = }")
# 'p1' in globals() = True
print(f"{'p2' in globals() = }")
# 'p2' in globals() = True

# Deleting p1
del p1

print(f"{'p1' in globals() = }")
# 'p1' in globals() = False

print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X7F113094DFA0: 1

# Deleting p1
del p2

print(f"{'p2' in globals() = }")
# 'p2' in globals() = False

# The reference count is now meaningless 
# (printing this twice to see if there are any changes):
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X7F113094DFA0: 0
# Reference count on 0X7F113094DFA0: 0

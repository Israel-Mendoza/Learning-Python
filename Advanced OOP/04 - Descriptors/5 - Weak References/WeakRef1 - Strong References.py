from __future__ import annotations
from utils.utility_functions import get_ref_count, print_address
from time import sleep

"""Understanding why weak references are necessary."""

# Playing around with strong references and the strong reference count.


class Person:
    def __init__(self, name: str) -> None:
        """Initializing the name of the Person"""
        self.name: str = name


# Creating a Person instance and two symbols to point to it.
# Storing the object's address in memory in a variable.
p1 = Person("Israel")
p2: Person = p1
obj_address: int = id(p1)
obj_hex_address: str = hex(obj_address).upper()

# Checking that both p1 and p2 point to the same object:
print_address("p1", p1)
# p1 @ 0X100939010
print_address("p2", p2)
# p2 @ 0X100939010

# Address in question has two symbols pointing to it:
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X100939010: 2

# 'p1' and 'p2' are in the global scope:
print(f"{'p1' in globals() = }")
# 'p1' in globals() = True
print(f"{'p2' in globals() = }")
# 'p2' in globals() = True

# Deleting p1
del p1

# Showing that p1 no longer exists:
print(f"{'p1' in globals() = }")
# 'p1' in globals() = False

# There is just one reference to the object in question:
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X100939010: 1

# Deleting p1
del p2

# Showing that p2 no longer exists:
print(f"{'p2' in globals() = }")
# 'p2' in globals() = False

# The reference count is now meaningless
# (printing this twice to see if there are any changes):
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
print(f"Reference count on {obj_hex_address}: {get_ref_count(obj_address)}")
# Reference count on 0X100939010: 0
# Reference count on 0X100939010: 100

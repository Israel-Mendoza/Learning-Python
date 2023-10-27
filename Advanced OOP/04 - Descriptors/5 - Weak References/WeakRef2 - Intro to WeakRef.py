from __future__ import annotations
import weakref
from utils.utility_functions import get_ref_count

"""Using the weak reference class."""

"""
    weakref.ref is an alias for weakref.ReferenceType(Generic[_T]):
    
    class ReferenceType(Generic[_T]):
        __callback__: Callable[[ReferenceType[_T]], Any]
        def __init__(self, o: _T, callback: Callable[[ReferenceType[_T]], Any] | None = ...) -> None: ...
        def __call__(self) -> _T | None: ...
        def __hash__(self) -> int: ...
        if sys.version_info >= (3, 9):
            def __class_getitem__(cls, item: Any) -> GenericAlias: ...
"""


class Person:
    def __init__(self, name: str) -> None:
        """Initializing the name of the Person"""
        self.name: str = name


# Initializing a Person instance and storing
# its address into a couple of variables
p1 = Person("Israel")
p1_address = id(p1)
p1_hex_address = hex(p1_address).upper()
print(f"{p1_hex_address = }")
# p1_hex_address = '0X7F631615DFD0'

# Having a second symbol point to the same object:
p2: Person = p1

print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 2

# Creating a weak reference object:
weak1 = weakref.ref(p1)

# The amount of strong references to the object didn't increase:
print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 2

# What is 'weak1' pointing to then?
# It's pointing to the same object p1 and p2 do:
print(f"{weak1 = }")
# weak1 = <weakref at 0x7f6316179400; to 'Person' at 0x7f631615dfd0>

# The weakref object is a callable that returns the object it points to:
p3: Person = weak1()
print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 3

###############################################################################
###############################################################################

del p3
print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 2

del p1, p2
print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 0

# What is weak1 pointing to? It is DEAD!
print(f"{weak1 = } --> {weak1() = }")
# weak1 = <weakref at 0x7f6316179400; dead> --> weak1() = None

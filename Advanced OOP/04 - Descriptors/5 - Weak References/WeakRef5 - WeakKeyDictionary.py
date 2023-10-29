from __future__ import annotations
import weakref
from typing import Any
from utils.utility_functions import get_ref_count

"""WeakKeyDictionary in data descriptors"""

"""
    Using WeakKeyDictionary in a data descriptor to store
    the instance as the key, and the value as the value.
    
    See file ../"Descriptors9 - Storing data 3.py"
    
    The keys are only weak references.
    Pros:
        The WeakKeyDictionary doesn't create a direct reference
        to the instance, which prevents memory leaks.
        Once the instance is destroyed, so is the weak reference key.
    Cons:
        Instance must be hashable to be used as a key for the dictionary.
"""


class IntegerValue:
    def __init__(self) -> None:
        """
        Initializing an empty WeakKeyDictionary instance
        where the instances will be keys, and the values, the values.
        Instances used as keys must be HASHABLE.
        """
        # Creating an empty WeakKeyDictionary to store
        # the instances and their values
        self.values: weakref.WeakKeyDictionary[Any, Any] = weakref.WeakKeyDictionary()

    def __set__(self, instance: Any, value: Any) -> None:
        """
        Creates/updates an entry in the self.value WeakKeyDictionary instance,
        where the key is the passed instance and the value is the passed value.
        The instance must be a hashable object!
        """
        self.values[instance] = value

    def __get__(self, instance: Any, _: type) -> Any | None:
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
    def show_x_descriptor(cls) -> None:
        """
        A class method that will print a dictionary version
        of the WeakRefDictionary in the x property,
        holding the instances values.
        """
        print(f"{cls.__name__}.x's values:")
        try:
            for k, v in dict(cls.x.values).items():
                print(f"Object at {hex(id(k)).upper()} has a value of {v}")
        except AttributeError as error:
            print(f"{error.__class__.__name__}: {error}")


# Creating a couple of Point1D instances and
# storing their address information.
p1 = Point1D()
p1_address: int = id(p1)
p1_hex_address: str = hex(p1_address).upper()

p2 = Point1D()
p2_address: int = id(p2)
p2_hex_address: str = hex(p2_address).upper()

print(f"{p1_hex_address = }")
# p1_hex_address = '0X7F411FA983A0'
print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 1

# Calling the __set__ method of the x descriptor,
# thus creating two entries in the weakdict instance.
p1.x = 10
p2.x = 20
print(f"{p1.x = }")
# p1.x = 10

print(f"{get_ref_count(p1_address) = }")
# get_ref_count(p1_address) = 1
print()

Point1D.show_x_descriptor()
# Point1D.x's values:
# Object at 0x7f411fA983A0 has a value of 10
# Object at 0x7F411fAA0880 has a value of 20

print(f"Deleting p1")
del p1

Point1D.show_x_descriptor()
# Point1D.x's values:
# Object at 0x7f411fAA0880 has a value of 20

del p2
Point1D.show_x_descriptor()
# Point1D.x's values:
# {}

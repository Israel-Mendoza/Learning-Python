"""Let's keep usong a dictionary in a data descriptor"""

# The dictionary in the property will be used to store like this:
#   Key [int]: The instance address location.
#   Value [tuple[weakref.ref, value]]: A tuple containing a weakref object
#                                      created with an instance to the object
#                                      it's supposed to point to, and a callback
#                                      function, which is supposed to run to delete
#                                      the remaining reference.
# Pros:
#     1. Instances don't have to be hashable (the key in the dictionary will be the int
#        representing the instance's address).
#     2. The dictionary can be freed up by using the weak reference's 
#        callback function.
# Cons:
#     1. Doesn't work if __slots__ are impletemted, since __slots__ this prevents 
#        __weakref__ from keeping weak references).
#     2. If __slots__ are in place, make sure they include __weakref__



import ctypes
import weakref
from typing import Any


def get_ref_count(address: int) -> int:
    """
    A simple function that returns the number of
    references to a given object in memory,
    which address is the passed integer.
    """
    return ctypes.c_long.from_address(address).value


class IntegerValue:
    """
    A Data Descriptor that stores the instance's values 
    in a dictionary under the descriptor instance's namespace.
    """

    def __init__(self) -> None:
        """
        Initializes an empty dictionary where the
        instance information and values will be stored.
        """
        self.values = {}

    def __get__(self, instance, owner) -> Any:
        """
        Returns the descriptor instance if called from a class.
        Returns the passed intance's value in the self.values dictionary.
        """
        if instance is None:
            # Returns the descriptor's intance, 
            # since it was called from the class
            return self
        # Returning the value assigned to the instance.
        address = id(instance)
        return self.values[address][1]

    def __set__(self, instance, value) -> None:
        """
        Stores the passed value in the self.values dictionary, 
        where the key will be the instance memory address.
        The value will be a tuple containing:
            at index 0: a weakref object instantiated with the instance 
                        it'll point to, and a callback method to be called 
                        when the instance is elligible for garbage collection.
            at index 1: The actual value of the instance.
        """
        address: int = id(instance)
        self.values[address] = (weakref.ref(instance, self._remove_item), value)

    def _remove_item(self, weakref_obj: weakref.ref) -> None:
        """
        Intended as a callback method.
        When called, it iterates through the self.values dictionary,
        looking for the key-value pair where the passed weak_ref
        object is.
        Once found, it deletes the dictionary entry.
        """
        for k, v in self.values.items():
            if id(weakref_obj) == id(v[0]):
                print(f"Removing item {weakref_obj} from the descriptor's dictionary!")
                del self.values[k]
                break


class Point1D:

    x = IntegerValue()

    def __eq__(self, other):
        """
        Implementing the == operator for the class.
        Also, making sure this is not a hashable object.
        """
        if isinstance(other, self.__class__):
            return self.x == other.x
        else:
            return NotImplemented

    @classmethod
    def show_x_descriptor(cls):
        """
        A class method that will print a dictionary version
        of the WeakRefDictionary in the x property,
        holding the instances values.
        """
        print(f"{cls.__name__}.x's values:")
        for k, v in dict(cls.x.values).items():
            print(f"Object at {hex(id(k)).upper()} has a value of {v}")


p1 = Point1D()
p2 = Point1D()

p1.x = 10
p2.x = 20

Point1D.show_x_descriptor()
# Point1D.x's values:
# Address 0X1BF0C28:(<weakref at 0x01C17CD0; to 'Point1D' at 0x01BF0C28>, 10)
# Address 0X1BF0550:(<weakref at 0x01C17D20; to 'Point1D' at 0x01BF0550>, 20)
print()

print(f"Deleting p1!")
del p1
print()

Point1D.show_x_descriptor()
# Point1D.x's values:
# Address 0X1BF0550:(<weakref at 0x01C17D20; to 'Point1D' at 0x01BF0550>, 20)
print()

del p2
print()

Point1D.show_x_descriptor()
# Point1D.x's values:

print()

from __future__ import annotations

"""Let's keep using a dictionary in a data descriptor"""

# The dictionary in the property will be used to store like this:
#   Key [int]: The instance's address in memory.
#   Value [tuple[weakref.ref, value]]: A tuple containing a weakref object created
#                                      with the instance it's supposed to point to
#                                      and a callback function that runs to delete
#                                      current dictionary entry.
# Pros:
#     1. Instances don't have to be hashable because the key in the storing dictio-
#        nary in the property is the int representing the instance's address.
#     2. The weak reference dictionary entry can be freed up by using the weak refe-
#        rence's callback function.
# Cons:
#     1. __slots__ prevents __weakref__ from keeping weak references. If __slots__ 
#        are in place, make sure they include __weakref__


import weakref


class IntegerValue:
    """
    A Data Descriptor that stores the instance's values in 
    a dictionary under the descriptor instance's namespace.
    """

    def __init__(self: IntegerValue) -> None:
        """
        Initializes an empty dictionary where the
        instance information and values will be stored.
        """
        self.values: dict[int, tuple[weakref[Point1D], int]] = {}

    def __get__(self: IntegerValue, instance: Point1D, _: type) -> int | IntegerValue:
        """
        Returns the descriptor instance if called from a class.
        Returns the passed intance's value in the self.values dictionary.
        """
        if instance is None:
            # Returns the descriptor's intance, 
            # since it was called from the class
            return self
        # Returning the value assigned to the instance.
        address: int = id(instance)
        return self.values[address][1]

    def __set__(self: IntegerValue, instance: Point1D, value: int) -> None:
        """
        Stores the passed value in the self.values dictionary, 
        where the key will be the instance's address in memory.
        The value will be a tuple[weakref.ref[Point1D], int] containing:
            at index 0: a weakref.ref object instantiated with the instance 
                        it'll point to, and a callback method to be called 
                        when the instance is elligible for garbage collection.
            at index 1: The actual value of the instance.
        """
        address: int = id(instance)
        self.values[address] = (weakref.ref(instance, self._remove_item), value)

    def _remove_item(self: IntegerValue, weakref_obj: weakref.ref[Point1D]) -> None:
        """
        Intended as a callback method.
        When called, it iterates through the self.values dictionary,
        looking for the key-value pair where the passed weak_ref
        object is.
        Once found, it deletes the dictionary entry.
        """
        for k, v in self.values.items():
            if id(weakref_obj) == id(v[0]):
                print(f"Removing {weakref_obj} from IntegerValue() @ {hex(id(self)).upper()}'s values dictionary!")
                del self.values[k]
                break


class Point1D:

    x: IntegerValue = IntegerValue()

    def __eq__(self: Point1D, other: Point1D) -> bool:
        """
        Implementing the == operator for the class.
        Also, making sure this is not a hashable object.
        """
        if isinstance(other, self.__class__):
            return self.x == other.x
        else:
            return NotImplemented

    @classmethod
    def show_x_descriptor(cls: type) -> None:
        """
        A class method that will print a dictionary version
        of the WeakRefDictionary in the x property,
        holding the instances values.
        """
        print(f"{cls.__name__}.x's values:")
        for k, v in dict(cls.x.values).items():
            print(f"{hex(id(k)).upper()} -> {v}")


p1: Point1D = Point1D()
p2: Point1D = Point1D()

p1.x = 10
p2.x = 20

Point1D.show_x_descriptor()
# Point1D.x's values:
# 0X7F038D7313B0 -> (<weakref at 0x7f038d7ed9f0; to 'Point1D' at 0x7f038d86d8b0>, 10)
# 0X7F038D7313D0 -> (<weakref at 0x7f038d7f7630; to 'Point1D' at 0x7f038d86d940>, 20)
print()

# Confirming the callback function in both dictionary entries:
print(Point1D.x.values[id(p1)][0].__callback__)
# <bound method IntegerValue._remove_item of <__main__.IntegerValue object at 0x7f038d86dcd0>>
print(Point1D.x.values[id(p2)][0].__callback__)
# <bound method IntegerValue._remove_item of <__main__.IntegerValue object at 0x7f038d86dcd0>>

del p1
# Removing <weakref at 0x7f038d7ed9f0; dead> from IntegerValue() at 0X7F038D86DCD0's values dictionary!
print()

Point1D.show_x_descriptor()
# Point1D.x's values:
# 0X7F038D7313D0 -> (<weakref at 0x7f038d7f7630; to 'Point1D' at 0x7f038d86d940>, 20)
print()

del p2
# Removing <weakref at 0x7f038d7f7630; dead> from IntegerValue() at 0X7F038D86DCD0's values dictionary!
print()

# The storing dictionary is empty! 
# All references, strong and weak are destroyed.
Point1D.show_x_descriptor()
# Point1D.x's values:

print()

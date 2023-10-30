from __future__ import annotations
import weakref

"""Let's keep using a dictionary in a data descriptor"""

"""
    The dictionary in the property will be used to store like this:
      Key [int]: The memory address where the instance is stored.
      Value [tuple[weakref.ref, value]]: A tuple containing a weakref object created
                                         with the instance it's supposed to point to
                                         and a callback function that runs to delete
                                         current dictionary entry.
                                         The value is the value we want to store for
                                         the given instance.
    Pros:
        1. Instances don't have to be hashable because the key in the storing dictio-
           nary in the property is the int representing the instance's address.
        2. The weak reference dictionary entry can be freed up by using the weak refe-
           rence's callback function.
    Cons:
        1. __slots__ prevents __weakref__ from keeping weak references. If __slots__ 
           are in place, make sure they include __weakref__
"""


class ValidString:
    """
    A Data Descriptor that hols a valid string, which length falls
    in the ranges provided when creating the ValidString instance.
    """

    def __init__(self, min_length: int = 0, max_length: int = 25) -> None:
        """
        Sets the length boundaries the string should have and creates
        the dictionary holding the values the instances will store.
        """
        self._min_length: int = min_length
        self._max_length: int = max_length
        self._data: dict[int, tuple[str, weakref.ref[Person]]] = {}

    def __set_name__(self, _: type, name: str) -> None:
        self._attribute_name: str = name

    def __get__(self, instance: Person, _: type) -> str | dict[int, tuple[str, weakref.ref[Person]]]:
        """
        Returns the self._data dictionary if called from a class.
        Returns the corresponding instance value if called from an instance.
        """
        if instance is None:
            return self._data
        address: int = id(instance)  # This should be the key we'll use to query the self._data dictionary
        value: tuple[str, weakref.ref[Person]] | None = self._data.get(address, None)  # Querying for the value
        if value:  # If the value exists (if it is not None)
            return value[0]
        else:
            raise AttributeError(f"{instance} does not have attribute '{self._attribute_name}'")

    def __set__(self, instance: Person, value: str) -> None:
        """
        Creates/updates the entry in the self._data dictionary. 
            Key [int] -> Instance's address in memory.
            Value [tuple[str, weakref.ref]] -> The value and weak ref to the instance.
        """
        if self._check_string(value):  # Confirming the passed value is a valid string
            address: int = id(instance)
            instance_weak_ref: weakref.ref[Person] = weakref.ref(instance, self._clear_data_entry)
            self._data[address] = (value, instance_weak_ref)
        else:
            raise ValueError(f"Attribute '{self._attribute_name}' must be a string between "
                             f"{self._min_length} and {self._max_length} characters long...")

    def _check_string(self, a_string: str) -> bool:
        """Checks whether the passed string is within the string limits"""
        length: int = len(a_string)
        return self._min_length < length < self._max_length

    def _clear_data_entry(self, weak_ref_obj: weakref.ref[Person]) -> None:
        """
        Deletes the entry from self._data once the object is destroyed.
        Its use is intended to be a callback function for the weakref object.
        """
        target_address: int = id(weak_ref_obj)
        for key, value in self._data.items():  # Iterating through the self._data dictionary
            if id(value[1]) == target_address:  # If the current tuple contains the passed weak reference
                print(f"Deleting {weak_ref_obj} from the dictionary!!!")
                del self._data[key]
                break


class Person:

    __slots__: tuple[str] = "__weakref__",

    first_name = ValidString(1, 20)
    last_name = ValidString(1, 20)

    def __repr__(self: Person) -> str:
        return f"Person() @ {hex(id(self)).upper()}"


p1 = Person()
p2 = Person()

# Trying to access the descriptor before we update the dictionary:
try:
    print(p1.first_name)
except AttributeError as error:
    print(f"{type(error).__name__}: {error}")
# AttributeError: Person() @ 0X7FBABA76C310 does not have attribute 'first_name'

# Using the descriptors' __set__ methods to update the holding dictionaries:
p1.first_name = "Israel"
p1.last_name = "Mendoza"

# Accessing the descriptors after updating the dictionaries:
print(p1.first_name, p1.last_name)
# Israel Mendoza

# Printing the holding dictionaries:
print(Person.first_name)
# {140439968989968: ('Israel', <weakref at 0x7fbaba792930; to 'Person' at 0x7fbaba76c310>)}
print(Person.last_name)
# {140439968989968: ('Mendoza', <weakref at 0x7fbaba792840; to 'Person' at 0x7fbaba76c310>)}

# Testing the Descriptor's ability to reject short strings:
try:
    p1.first_name = ""
except ValueError as error:
    print(f"{type(error).__name__}: {error}")
# ValueError: Attribute 'first_name' must be a string between 1 and 20 characters long...

# Deleting the Person instance will also get rid of its entries in the different
# weakref instances that use to hold its data (first_name and last_name).
del p1
# Deleting <weakref at 0x7fbaba792840; dead> from the dictionary!!!
# Deleting <weakref at 0x7fbaba792930; dead> from the dictionary!!!

"""Let's keep using a dictionary in a data descriptor"""

# The dictionary in the property will be used to store like this:
#   Key [int]: The instance address.
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
#     1. __slots__ prevents __weakref__ from keeping weak references, so if __slots__ 
#        are in place, make sure they include __weakref__


import weakref


class ValidString:

    def __init__(self, min_length: int = 0, max_length: int = 25):
        self._min_length: int = min_length
        self._max_length: int = max_length
        self._data: dict = {}

    def __get__(self, instance, owner_class) -> str:
        """
        Returns the self._data dictionary if called from a class.
        Returns the corresponding instance value if called from an instance.
        """
        if instance is None:
            return self._data
        address: int = id(instance)
        value = self._data.get(address, None)
        if value is not None:
            return value[0]
        else:
            raise AttributeError(f"{instance} does not this attribute!")

    def __set__(self, instance, value: str):
        """
        Creates/updates the entry in the self._data dictionary. 
            Key [int] -> Instance memory address.
            Value [tuple[Any, weakref.ref]] -> The value and weak ref to the instance.
        """
        if self._check_string(value):
            address: int = id(instance)
            # intance_weak_ref: weakref.ref = weakref.ref(instance, self._clear_data_entry)
            intance_weak_ref: weakref.ref = weakref.ref(instance)
            self._data[address] = (value, intance_weak_ref)
        else:
            raise ValueError(f"String must be between {self._min_length} "
                             f"and {self._max_length} characters long!")

    def _check_string(self, a_string: str) -> bool:
        """Checks whether the passed string is within the string limits"""
        length = len(a_string)
        return self._min_length < length < self._max_length

    def _clear_data_entry(self, weak_ref_obj: weakref.ref):
        """Deletes the entry from self._data once the object is destroyed"""
        target_address: int = id(weak_ref_obj)
        for key, value in self._data.items():
            if id(value[1]) == target_address:
                del self._data[key]
                break


class Person:

    __slots__ = ("__weakref__",)

    first_name = ValidString(1, 20)
    last_name = ValidString(1, 20)


p1 = Person()
p2 = Person()

test = weakref.ref(p1)

try:
    print(p1.first_name)
except AttributeError as error:
    print(f"{type(error).__name__}: {error}")
# AttributeError: <__main__.Person object at 0x7fde6742e6a0> does not this attribute!

p1.first_name = "Israel"
p1.last_name = "Mendoza"

print(p1.first_name, p1.last_name)
# Israel Mendoza

print(Person.first_name)
# {140593191904928: ('Israel', <weakref at 0x7fde67434270; to 'Person' at 0x7fde6742e6a0>)}
print(Person.last_name)
# {140593191904928: ('Mendoza', <weakref at 0x7fde6743a450; to 'Person' at 0x7fde6742e6a0>)}

try:
    p1.first_name = ""
except ValueError as error:
    print(error)
# String must be between 1 and 20 characters long!

"""Using __weakref__ and __slots__"""


# When we create a weak reference to an object,
# the weak reference is also stored in the instance's
# namespace under the attribute "__weakref__".
#
# If we're using __slots__ in the class, we must know that:
#   1. Creating a weak reference to an object means the reference
#      will be added to the original object's namespace under
#      the __weakref__ attribute. This means that '__weakref__'
#      must be included in __slots__, otherwise Python won't
#      allow us to create the weak reference.


import weakref


class Person:
    # We are not including '__weakref__' in __slots__
    __slots__: tuple[str] = ("fname",)

    def __init__(self, full_name: str) -> None:
        self.fname: str = full_name


p1: Person = Person("Israel Mendoza")

# What happens if we try to add an unslotted attribute?
try:
    p1.email_address = "im@email.com"
except Exception as error:
    print(f"{type(error).__name__}: {error}")
# AttributeError: 'Person' object has no attribute 'email_address'

# What happens if we try to create a weak reference?
try:
    wr1: weakref.ref[Person] = weakref.ref(p1)
except Exception as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: cannot create weak reference to 'Person' object


###############################################################################
###############################################################################


class Person:
    # Including '__weakref__' in __slots__
    __slots__ = ("fname", "__weakref__")

    def __init__(self, full_name: str) -> None:
        self.fname: str = full_name


p1 = Person("Israel Mendoza")

# We can now create a weak reference:
wr1: weakref.ref[Person] = weakref.ref(p1)
wr2: weakref.ref[Person] = weakref.ref(p1)


# Python doesn't create more than one
# weak reference to the same object:ce
print(f"{wr1 = }")
# wr1 = <weakref at 0x7ff622bceea0; to 'Person' at 0x7ff622bc9d00>
print(f"{wr2 = }")
# wr2 = <weakref at 0x7ff622bceea0; to 'Person' at 0x7ff622bc9d00>
print(f"{wr1 is wr2 = }")
# wr1 is wr2 = True

# Let's see the weak reference in p1:
print(f"{p1.__weakref__ = }")
# p1.__weakref__ = <weakref at 0x7ff622bceea0; to 'Person' at 0x7ff622bc9d00>

print(f"{wr1 is wr2 is p1.__weakref__ = }")
# wr1 is wr2 is p1.__weakref__ = True

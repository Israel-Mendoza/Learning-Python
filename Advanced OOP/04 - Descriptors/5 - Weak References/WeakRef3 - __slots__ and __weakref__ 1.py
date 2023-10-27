import weakref

"""Using __weakref__ and __slots__"""

"""
    When we instantiate a weak reference that points to an object,
    that weak reference instance will also be stored in the object's
    namespace, under the "__weakref__" attribute.
    
    Think of this as if it was a "double reference". 
    
    If we want to use __slots__, we must make sure to include __weakref__
    so the instance is able to store the weak references we create for it.
    If we fail to do this, Python won't allow us to create weak references
    to a slotted object.
"""


class Person:
    # We are not including '__weakref__' in __slots__
    __slots__: tuple[str] = "fname",

    def __init__(self, full_name: str) -> None:
        self.fname: str = full_name


p1 = Person("Israel Mendoza")

# What happens if we try to add an un-slotted attribute?
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
    __slots__ = "fname", "__weakref__"

    def __init__(self, full_name: str) -> None:
        self.fname: str = full_name


p1 = Person("Israel Mendoza")

# We can now create a weak reference:
wr1: weakref.ref[Person] = weakref.ref(p1)
wr2: weakref.ref[Person] = weakref.ref(p1)


"""We can only have ONE weak reference to a given object"""


# Python doesn't create more than one weak reference to the same object:
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

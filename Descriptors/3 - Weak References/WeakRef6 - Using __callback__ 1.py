"""What can we do with the weakref.ref's __callback__ attribute?"""

# We will be using function storedd in the weakref.ref's __callback__
# class attribute to distroy the current weakreference instance when 
# the object it points to is destroyed.
# This will prevent us from having potential memory leak when an object
# gets destroyed.


import weakref


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Person('{self.name}') at {hex(id(self)).upper()}"


def my_callback(a_weakref: weakref.ref) -> None:
    # Iterating through the my_references list and
    # deleting the passed weak references from the
    # my_references list, thus deleting all remains to
    # the object, which destruction will call this function.
    for reference in my_references:
        if reference is a_weakref:
            print(f"Removing {a_weakref} from my_references!")
            my_references.remove(reference)


p1 = Person("Israel")
p2 = Person("Arturo")
# p3 points to the same object as p2:
p3 = p2

my_references = [weakref.ref(p1, my_callback), weakref.ref(p2, my_callback)]

print(f"\nmy_references = \n{my_references}\n")
# my_references = 
# [<weakref at 0x7f82b8c699f0; to 'Person' at 0x7f82b8c6cfa0>, <weakref at 0x7f82b8c71db0; to 'Person' at 0x7f82b8c6cd60>]


# The weakref's __callback__ is called because 
# the only strong reference to the object is killed
del p1
# Removing <weakref at 0x7f82b8c699f0; dead> from my_references!

# The weakref's __callback__ is not called 
# because the reference is still alive with 'p3'
del p2

del p3
# Removing <weakref at 0x7f82b8c71db0; dead> from my_references!

# The weak references are now gone too!
print(f"my_references = {my_references}")
# my_references = []

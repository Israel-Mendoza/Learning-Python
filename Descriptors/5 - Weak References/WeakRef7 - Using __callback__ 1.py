from __future__ import annotations

"""Practical applications of the weakref's __callback__"""

# We will be using function storedd in the weakref.ref's __callback__
# class attribute to distroy the current weakreference instance when 
# the object it points to is destroyed.
# This will prevent us from having potential memory leak when an object
# gets destroyed.


import weakref


class Person:
    def __init__(self: Person, name: str) -> None:
        self.name: str = name

    def __repr__(self: Person) -> str:
        return f"Person('{self.name}') @ {hex(id(self)).upper()}."


def my_callback(person_weakref: weakref.ref) -> None:
    # Iterating through the references_list list (in the global scope)
    # and deleting the passed weak references from it, thus deleting 
    # all remains to the object, which destruction will call this function.
    for reference in references_list:
        if reference is person_weakref:
            print(f"Removing {person_weakref} from my_references!")
            references_list.remove(reference)


p1 = Person("Israel")
p2 = Person("Arturo")
# p3 points to the same object as p2:
p3 = p2

# Creating a list that will hold the created weakrefs:
references_list: list[weakref.ref[Person]] = [weakref.ref(p1, my_callback), weakref.ref(p2, my_callback)]

print(f"\nreferences_list = \n{references_list}\n")
# references_list = 
# [<weakref at 0x7f82b8c699f0; to 'Person' at 0x7f82b8c6cfa0>, <weakref at 0x7f82b8c71db0; to 'Person' at 0x7f82b8c6cd60>]


# The weakref's __callback__ is called because 
# the only strong reference to the object is killed
del p1
# Removing <weakref at 0x7f82b8c699f0; dead> from references_list!

# The weakref's __callback__ is not called 
# because the reference is still alive with 'p3'
del p2

del p3
# Removing <weakref at 0x7f82b8c71db0; dead> from references_list!

# The weak references are now gone too!
print(f"references_list = {references_list}")
# references_list = []

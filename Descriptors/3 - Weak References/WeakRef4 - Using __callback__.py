"""Working with the weakref.ref's __callback__ attribute"""

# We've seen how the weakref.ref object helps us get hold of an object
# in memory without creating a strong reference to it, allowing the 
# garbage collector reclaim an object's memory when the last strong 
# reference is destroyed.
# 
# When creating a weakref.ref object, we can also pass a callback function
# when instantiating the reference. 
# This callback function will be stored in the weakref.ref's __callback__
# class attribute, and will be called automatically once the object the weakref
# points to is destroyed. 

# TODO: Show how we can use the callback function in __callback__ to 
# delete all traces references to destroyed objects.

from typing import List
import weakref

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Person('{self.name}') at {hex(id(self)).upper()}"


def my_callback(the_wk: weakref.ref) -> None: ...


p1 = Person("Israel")
p2 = Person("Arturo")
# p3 points to the same object as p2:
p3 = p2

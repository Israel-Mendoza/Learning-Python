from __future__ import annotations
import weakref

"""Working with the weakref.ref's __callback__ attribute"""

"""
    We've seen how the weakref.ref object helps us get hold of an object
    in memory without creating a strong reference to it, allowing the 
    garbage collector reclaim an object's memory when the last strong 
    reference is destroyed.
    
    When creating a weakref.ref object, we can also pass a callback function
    when instantiating the reference. This is optional, of course. 
    When called, this callback function will be passed the weak reference
    instance it is bound to.
    
    The callback function will be stored in the weakref.ref's __callback__
    class attribute, and will be called automatically once the object the weakref
    points to is destroyed.
    
    Remember!!! 
        The instance will keep a copy of the actual weak reference we create for it.
        An instance can have ONLY ONE weak reference attached to it. 
        So, if we create a weak reference like this:
        
        w1 = weakref.ref(o1)
        w1 == o1.__weakref__ <--- TRUE!
"""


class Person:
    
    def __init__(self, name: str) -> None:
        # The following line doesn't really create a __weakref__ attr.
        # It's already there, as part of the instance's namespace
        # Remember where the weakrefs will be stored (in the instance's namespace):
        self.__weakref__: weakref.ref[Person]  # Just showing where the weakref's will be stored.
        self.name: str = name

    def __repr__(self) -> str:
        return f"Person('{self.name}') @ {hex(id(self)).upper()}"


# Creating a callback function to be added to the weakref object's __callback__ attribute.
def my_callback(person_weak_ref: weakref.ref[Person]) -> None:
    """
    Simple callback function.
    Args:
        person_weak_ref [weakref.ref[Person]]: A weakref object pointing to a Person's instance.
    """
    print(f"What a lovely callback. The passed weakref is '{person_weak_ref}'.")


# Creating a couple of Person instances.
p1 = Person("Israel")
p2 = Person("Arturo")
# p3 points to the same object as p2:
p3 = p2

# Printing the "three" Person objects and their addresses:
print(f"{p1 = }")
# p1 = Person('Israel') @ 0X7F6D30A35850
print(f"{p2 = }")
# p2 = Person('Arturo') @ 0X7F6D30A374D0
print(f"{p3 = }")
# p3 = Person('Arturo') @ 0X7F6D30A374D0 <<< (same as p2)

# Creating two weak references to the two Person instances in memory
# and passing the previously created callback to the initializer.
wk1 = weakref.ref(p1, my_callback)
wk2 = weakref.ref(p2, my_callback)

# Printing the weak references and the objects they point to:
print(f"{wk1 = }")
# wk1 = <weakref at 0x7f6d30a2d940; to 'Person' at 0x7f6d30a35850>
print(f"{wk1() = }")
# wk1() = Person('Israel') @ 0X7F6D30A35850
print(f"{wk2 = }")
# wk2 = <weakref at 0x7f6d30a4e390; to 'Person' at 0x7f6d30a374d0>
print(f"{wk2() = }")
# wk2() = Person('Arturo') @ 0X7F6D30A374D0

# What's stored in the __callback__ attribute?
print(f"{wk1.__callback__ = }")
# wk1.__callback__ = <function my_callback at 0x7f6d30a03b00>
print(f"{wk2.__callback__ = }")
# wk2.__callback__ = <function my_callback at 0x7f6d30a03b00>
print(f"{wk1.__callback__ is my_callback = }")
# wk1.__callback__ is my_callback = True

# We can call the weak reference's callback from the actual instance.
# Remember that the weakref is stored in the instance's __weakref__ attribute:
p1.__weakref__.__callback__(p1.__weakref__)
# What a lovely callback. The passed weakref is '<weakref at 0x7f6d30a2d940; to 'Person' at 0x7f6d30a35850>'.

# Deleting p1.
# Notice how the callback in wk1 is called, 
# passing the weak ref's instance as the only argument:
del p1
# What a lovely callback. The passed weakref is '<weakref at 0x7f6d30a2d940; dead>'.

# Checking the weak reference to the recently deleted p1:
print(f"{wk1 = }")
# wk1 = <weakref at 0x7f6d30a2d940; dead>
print(f"{wk1() = }")
# wk1() = None

# Deleting p2
# Notice how the callback in wk2 is not called, because
# variable p3 is maintaining the Person at 0X7F6936843C70 alive:
del p2

# Checking the weak reference to the recently deleted p2.
# Notice how wk2 is still pointing to the Person('Arturo') at 0X7F6936843C70, 
# because p3 is maintaining that object alive:
print(f"{wk2 = }")
# wk2 = <weakref at 0x7f6d30a4e390; to 'Person' at 0x7f6d30a374d0>
print(f"{wk2() = }")
# wk2() = Person('Arturo') @ 0X7F6D30A374D0

# Deleting p3
# Notice how the callback in wk2 is called this time, because we're
# deleting the last strong reference to the Person at 0X7F6936843C70 object:
del p3
# What a lovely callback. The passed weakref is '<weakref at 0x7f6d30a4e390; dead>'.

# Checking the weak reference to the recently deleted p3 (and p2) instance:
print(f"{wk2() = }")
# wk2() = None

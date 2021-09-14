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

import weakref

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Person('{self.name}') at {hex(id(self)).upper()}"


def my_callback(the_wk: weakref.ref) -> None:
    print(f"What a lovely callback, where the passed weakref is '{the_wk}'")

p1 = Person("Israel")
p2 = Person("Arturo")
# p3 points to the same object as p2:
p3 = p2

# Printing the "three" Person objects and their addresses:
print(f"{p1 = }")
# p1 = Person('Israel') at 0X7F6936843FA0
print(f"{p2 = }")
# p2 = Person('Arturo') at 0X7F6936843C70
print(f"{p3 = }")
# p2 = Person('Arturo') at 0X7F6936843C70

# Creating two weakreferences to the two Person objects in memory:
wk1 = weakref.ref(p1, my_callback)
wk2 = weakref.ref(p2, my_callback)

# Printing the weak references and the objects they point to:
print(f"{wk1 = }")
# wk1 = <weakref at 0x7f69368bff40; to 'Person' at 0x7f6936843fa0>
print(f"{wk1() = }")
# wk1() = Person('Israel') at 0X7F6936843FA0
print(f"{wk2 = }")
# wk2 = <weakref at 0x7f6936848bd0; to 'Person' at 0x7f6936843c70>
print(f"{wk2() = }")
# wk2() = Person('Arturo') at 0X7F6936843C70 (p2 and p3)

# What's stored in the __callback__ attribute?
print(f"{wk1.__callback__ = }")
# wk1.__callback__ = <function my_callback at 0x7f727bbad280>
print(f"{wk2.__callback__ = }")
# wk2.__callback__ = <function my_callback at 0x7f727bbad280>
print(f"{wk1.__callback__ is my_callback = }")
# wk1.__callback__ is my_callback = True

# Deleting p1.
# Notice how the callback in wk1 is called.
del p1
# What a lovely callback, where the passed weakref is '<weakref at 0x7f69368bff40; dead>'

# Checking the weak reference to the recently deleted p1:
print(f"{wk1 = }")
# wk1 = <weakref at 0x7f69368bff40; dead>
print(f"{wk1() = }")
# wk1() = None

# Deleting p2
# Notice how the callback in wk2 is not called,
# because p3 is mantaining the Person at 0X7F6936843C70 alive:
del p2

# Checking the weak reference to the recently deleted p2.
# Notice how wk2 is still pointing to the Person('Arturo') at 0X7F6936843C70, 
# because p3 is mantaining that object alive:
print(f"{wk2 = }")
# wk2 = <weakref at 0x7f6936848bd0; to 'Person' at 0x7f6936843c70>
print(f"{wk2() = }")
# wk2() = Person('Arturo') at 0X7F6936843C70

# Deleting p3
# Notice how the callback in wk2 is called this time,because we're 
# deleting the last strong reference to the Person at 0X7F6936843C70 object:
del p3
# What a lovely callback, where the passed weakref is '<weakref at 0x7f6936848bd0; dead>'

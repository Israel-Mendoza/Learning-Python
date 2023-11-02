from __future__ import annotations

"""Introducing the __new__ method"""

"""
    When we create an instance of a class, the __new__ static method
    in the class is called and passes the class itself as the first parameter.
    
    This is what happens behind the scenes:
    
    my_obj = MyClass.__new__(MyClass)
    
    If this method is not defined in the class, it will call it from the
    parent class, as expected. This could be chained up until the implementation
    of __new__ in the "object" class.
    
    Remember: 
            __new__ is  a static method and accepts the class it is being 
            called on as the first parameter. 
            However, Python is well aware of this, so it is NOT necessary
            to decorate this method with @staticmethod.
    
    So, basically, the __new__ method is the method that actually CREATES
    the instance, and the __init__ method is the one that INITIALIZES it.
"""


class Point:
    # Defining __init__ only
    def __init__(self, x: int | float, y: int | float) -> None:
        print(f"__init__ was called - self: {self}")
        self.x = x
        self.y = y


# When the class is called to create an instance, __new__ is
# called to create and return it without us noticing.
# Then __init__ is then called automatically after __new__,
# passing the recently created instance returned by the __new__ method
# as the first argument.
p1 = Point(10, 20)
# __init__ was called - self: <__main__.Point object at 0x27C57B43FD0>


"""If we don't want to have __init__ called, we must call __new__ directly:"""

p2 = Point.__new__(Point)  # (No output)
p3 = object.__new__(Point)  # (No output)

# These objects were created as expected:
print(type(p1))  # <class '__main__.Point'>
print(type(p2))  # <class '__main__.Point'>
print(type(p3))  # <class '__main__.Point'>


"""Creating instances using object.__new__()"""


# Notice how __init__ is not called!
p1 = object.__new__(Point, 10, 20)  # 10 and 20 are unexpected arguments
# (No output from __init__)

# Confirming that __init__ was not called and the namespace is empty
print(p1.__dict__)
# {}

# Calling __init__ ourselves:
p1.__init__(10, 10)
# __init__ was called - self: <__main__.Point object at 0x27C57B428B0>


# Confirming that __init__ was called and the namespace is not empty
print(p1.__dict__)
# {'x': 10, 'y': 10}

# We can call __init__ as many times as we want:
p1.__init__(100, 200)
# __init__ was called - self: <__main__.Point object at 0x27C57B428B0>
print(p1.__dict__)
# {'x': 100, 'y': 200}

p1.__init__(1000, 2000)
# __init__ was called - self: <__main__.Point object at 0x27C57B428B0>
print(p1.__dict__)
# {'x': 1000, 'y': 2000}

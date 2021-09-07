"""
Why would we want to override the __new__ method?
Why not use __new__ to initialize the instance all the time then?
"""

from typing import Union

# Sometimes, we may actually want to tweak some of the instantiation process.
# Also, we can definitely use the __new__ method to initialize the instance
# without having to use the __init__ method.
# The only drawback is that, by using __new__ method to instantiate AND initialize
# the instance, we would have to take care of the instance creation all the time.


"""Tweaking the class before creating an instance"""


class Square:
    def __new__(cls, width: Union[int, float], height: Union[int, float]) -> "Square":
        """Tweaking class before instantiating """
        print("__new__ called!")
        # Adding a method to the class.
        # Note: Everytime a new instance is created, a new  lambda is also created,
        # and will override the previous .area attribute in the class:
        cls.area = lambda self: self.width * self.height
        instance = super().__new__(cls)
        return instance

    def __init__(self, width: Union[int, float], height: Union[int, float]) -> None:
        print("__init__ called!")
        self.width = width
        self.height = height


s1 = Square(10, 10)
# __new__ called!
# __init__ called!

print(s1.__dict__)  # {'width': 10, 'height': 10}

print("area" in Square.__dict__)  # True


"""Tweaking the instance before returning it"""


class Square:
    def __new__(cls, width: Union[int, float], height: Union[int, float]) -> "Square":
        print("__new__ called!")
        # Adding a method to the class.
        # Note: Everytime a new instance is created, a new  lambda is also created,
        # and will override the previous .area attribute in the class:
        cls.area = lambda self: self.width * self.height
        instance = super().__new__(cls)
        # Initializing the instance before it's returned:
        instance.width = width
        instance.height = height
        return instance

    def __init__(self, width: Union[int, float], height: Union[int, float]) -> None:
        print("__init__ was called, but doesn't do much!")


# When calling the class, both __new__ and __init__ will be called.
s2 = Square(10, 20)
# __new__ called!
# __init__ was called, but doesn't do much!
print(s2.__dict__)  # {'width': 10, 'height': 10} (Populated by __new__)

# Notice again how __init__ is not called!
s3 = Square.__new__(Square, 10, 30)
# __new__ called!
print(s3.__dict__)  # {'width': 10, 'height': 10} (Populated by __new__)

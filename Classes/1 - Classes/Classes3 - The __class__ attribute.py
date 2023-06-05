"""Playing with the __class__ attribute of an object"""


class MyClass:
    pass


# Instantiating an object out of MyClass
my_obj = MyClass()

print(f"{type(my_obj) = }")
# type(my_obj) = <class '__main__.MyClass'>
print(f"{my_obj.__class__ = }")
# my_obj.__class__ = <class '__main__.MyClass'>
print(type(my_obj) == my_obj.__class__)
# True
print(f"{isinstance(my_obj, MyClass) = }")
# isinstance(my_obj, MyClass) = True
print(f"{isinstance(my_obj, str) = }")
# isinstance(my_obj, str) = False


"""Overwriting the __class__ attribute"""


class MyClass:
    __class__ = str


my_obj = MyClass()  # Instantiating an object out of MyClass

# type() is not fooled by the change:
print(f"{type(my_obj) = }" )
# type(my_obj) = <class '__main__.MyClass'>
print(f"{my_obj.__class__ = }")
# my_obj.__class__ = <class 'str'>
print(f"{type(my_obj) == my_obj.__class__ = }")
# type(my_obj) == my_obj.__class__ = False

# isinstance() will look at the actual class...
print(f"{isinstance(my_obj, MyClass) = }")
# isinstance(my_obj, MyClass) = True

# ... AND the __class__ attribute:
print(f"{isinstance(my_obj, str) = }")
# isinstance(my_obj, str) = True

# Just keep in mind that, in doubt, always use type()

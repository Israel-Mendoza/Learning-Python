# Playing with the __class__ attribute of an object


class MyClass:
    pass


my_obj = MyClass()  # Instantiating an object out of MyClass

print(type(my_obj) == my_obj.__class__)
# True
print(isinstance(my_obj, MyClass))
# True
print(isinstance(my_obj, str))
# False


# Overwriting the __class__ attribute


class MyClass:
    __class__ = str


my_obj = MyClass()  # Instantiating an object out of MyClass

print(type(my_obj) == my_obj.__class__)
# False
print(isinstance(my_obj, MyClass))
# True
print(isinstance(my_obj, str))
# True

# Playing with the __class__ attribute of an object


class MyClass:
    pass


my_obj = MyClass()  # Instantiating an object out of MyClass

print(f"type(my_obj) == my_obj.__class__ => " + f"{type(my_obj) == my_obj.__class__}")
print(f"Is 'my_obj' an instance of 'MyClass'? => {isinstance(my_obj, MyClass)}")
print(f"Is 'my_obj' an instance of 'str'? => {isinstance(my_obj, str)}\n")


# Overwriting the __class__ attribute


class MyClass:
    __class__ = str


my_obj = MyClass()  # Instantiating an object out of MyClass

print(f"type(my_obj) == my_obj.__class__ => " + f"{type(my_obj) == my_obj.__class__}")
print(f"Is 'my_obj' an instance of 'MyClass'? => {isinstance(my_obj, MyClass)}")
print(f"Is 'my_obj' an instance of 'str'? => {isinstance(my_obj, str)}\n")

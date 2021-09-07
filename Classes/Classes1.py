class MyClass:
    pass


# Instanciating from MyClass
obj = MyClass()

print(f"Name of MyClass: {MyClass.__name__}")
print(f"Type of MyClass: {type(MyClass)}")
print(f"Is 'MyClass' an instance of 'type'? {isinstance(MyClass, type)}")
print(f"Is 'obj' instance of 'MyClass'? {isinstance(obj, MyClass)}")
print(f"What's the type of 'obj'? {obj.__class__} or {type(obj)}")

class MyClass:
    pass


# Instanciating from MyClass
obj = MyClass()

print(MyClass.__name__)
# MyClass
print(type(MyClass))
# <class 'type'>
print(isinstance(MyClass, type))
# True|
print(isinstance(obj, MyClass))
# True
print(obj.__class__, type(obj))
# <class '__main__.MyClass'> <class '__main__.MyClass'>

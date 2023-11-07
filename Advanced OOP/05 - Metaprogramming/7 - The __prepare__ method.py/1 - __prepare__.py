from __future__ import annotations
from typing import Any, Mapping

"""The class dictionary gets created somewhere before being passed to the __new__ method, right?"""

"""
    The namespace dictionary is created in the __prepare__ static method in the metaclass.
    
    It takes at least two arguments: the name and the bases.
                 
    It must return a mapping type, to be passed to the __new__ method   
    as the class namespace dictionary.          
    Once the dictionary is returned by the __prepare__ method, 
    Python injects whatever is necessary (module, qualname, namespace).
"""


"""Confirming that the __prepare__ only returns a dict (__prepare__ takes at least the name and the bases):"""


test: Mapping[str, object] = type.__prepare__("Israel", ())
print(f"Test type: {type(test)}")
# Test type: <class 'dict'>
print(f"test contents: {test}")
# test contents: {}


class MyType1(type):
    """A metaclass"""
    def __new__(cls, name: str, bases: tuple[type, ...], cls_dict: dict[str, Any]) -> type:
        print(f"MyType1.__new__ called with the following arguments:")
        print(f"\tcls: {cls}({type(cls)})")
        print(f"\tname: {name}({type(name)})")
        print(f"\tbases: {bases}({type(bases)})")
        print(f"\tcls_dict: {cls_dict}({type(cls_dict)})\n")  # <-- Comes from __prepare__
        new_class: MyType1 = super().__new__(cls, name, bases, cls_dict)
        return new_class


class Person1(metaclass=MyType1):
    pass


# MyType1.__new__ called with the following arguments:
# 	cls: <class '__main__.MyType1'>(<class 'type'>)
# 	name: Person1(<class 'str'>)
# 	bases: ()(<class 'tuple'>)
# 	cls_dict: {'__module__': '__main__', '__qualname__': 'Person1'}(<class 'dict'>)  <-- Comes from __prepare__


class MyType2(type):
    @staticmethod
    def __prepare__(name: str, bases: tuple[type, ...], **kwargs) -> Mapping[str, Any]:
        print(f"MyType2.__prepare__ called with the following arguments: ")
        print(f"\tname: {name}({type(name)})")
        print(f"\tbases: {bases}({type(bases)})")
        print(f"\targs: {kwargs}({type(kwargs)})\n")
        return {"a": 1, "b": 2}

    @staticmethod
    def __new__(cls: type, name: str, bases: tuple[type, ...], cls_dict: dict[str, Any]) -> MyType2:
        print(f"MyType2.__new__ called with the following arguments:")
        print(f"\tcls: {cls}({type(cls)})")
        print(f"\tname: {name}({type(name)})")
        print(f"\tbases: {bases}({type(bases)})")
        print(f"\tcls_dict: {cls_dict}({type(cls_dict)})\n")  # <-- Comes from __prepare__
        new_class: MyType2 = super().__new__(cls, name, bases, cls_dict)
        return new_class


class Person2(metaclass=MyType2):
    pass


# MyType2.__prepare__ called with the following arguments:
# 	name: Person2(<class 'str'>)
# 	bases: ()(<class 'tuple'>)
# 	args: ()(<class 'tuple'>)

# MyType2.__new__ called with the following arguments:
# 	cls: <class '__main__.MyType2'> - <class 'type'>
# 	name: Person2 - <class 'str'>
# 	bases: () - <class 'tuple'>
# 	cls_dict: {'a': 1, 'b': 2, '__module__': '__main__', '__qualname__': 'Person2'} - <class 'dict'>


class MyType3(type):
    """Metaclass that injects the passed keyword arguments to the final class' dictionary"""
    @staticmethod
    def __prepare__(name: str, bases: tuple[type, ...], **kwargs: Any) -> Mapping[str, Any]:
        print(f"MyType3.__prepare__ called with the following arguments: ")
        print(f"\tname: {name}({type(name)})")
        print(f"\tbases: {bases}({type(bases)})")
        print(f"\tkwargs: {kwargs}(type({kwargs})\n")
        cls_dict = {**kwargs}  # Returning the passed keyword arguments in the form of a dictionary
        return cls_dict

    @staticmethod
    def __new__(cls: type, name: str, bases: tuple[type, ...], cls_dict: dict[str, Any], **kwargs: Any) -> type:
        print(f"MyType3.__new__ called with the following arguments:")
        print(f"\tcls: {cls}({type(cls)})")
        print(f"\tname: {name}({type(name)})")
        print(f"\tbases: {bases}({type(bases)})")
        print(f"\tcls_dict: {cls_dict}({type(cls_dict)}")
        print(f"\tkwargs: {kwargs}({type(kwargs)})\n")
        new_class: MyType3 = super().__new__(cls, name, bases, cls_dict)
        return new_class


# Simple function to be injected to the class through the __prepare__ method:
def hello(self):
    print(f"{self} says hello")


class Person3(metaclass=MyType3, a=1, b=2, hello=hello):  # Keyword arguments passed to __prepare__ go here
    pass


# MyType3.__prepare__ called with the following arguments:
# 	name: Person3(<class 'str'>)
# 	bases: ()(<class 'tuple'>)
# 	kwargs: {'a': 1, 'b': 2, 'hello': <function hello at 0x105129120>}
#   	(type({'a': 1, 'b': 2, 'hello': <function hello at 0x105129120>})

# MyType3.__new__ called with the following arguments:
# 	cls: <class '__main__.MyType3'>(<class 'type'>)
# 	name: Person3(<class 'str'>)
# 	bases: ()(<class 'tuple'>)
# 	cls_dict: {'a': 1, 'b': 2, '__module__': '__main__', '__qualname__': 'Person3'}(<class 'dict'>
# 	kwargs: {'a': 1, 'b': 2, 'hello': <function hello at 0x105129120>}(<class 'dict'>)


print("Person3 class namespace: ")
for k, v in vars(Person3).items():
    print(f"{k}: {v}")

# Person3 class namespace:
# a: 1
# b: 2
# hello: <function hello at 0x105129120>
# __module__: __main__
# __dict__: <attribute '__dict__' of 'Person3' objects>
# __weakref__: <attribute '__weakref__' of 'Person3' objects>
# __doc__: None

p = Person3()
p.hello()
# <__main__.Person3 object at 0x100b7bd40> says hello

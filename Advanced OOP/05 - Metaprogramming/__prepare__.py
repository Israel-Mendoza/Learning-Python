from typing import Any, Dict, Tuple, Type

"""The class dictionary gets created somewhere, right?"""


#########################################################################
# The namespace dictionary is created in the __prepare__ static method. #
# It takes at least two arguments: the name and the bases.              #
# It must return a mapping type, to be taken by the __new__ method      #
# as the class namespace dictionary.                                    #
# Once the dictionary is returned by the __prepare__ method,            #
# Python injects whatever is necessary (module, qualname, namespace)    #
#########################################################################


# Confirming that the __prepare__ only returns a dict:
test = type.__prepare__("Israel", ())
print(f"Test type: {type(test)}")
# Test type: <class 'dict'>
print(f"test contents: {test}")
# test contents: {}


class MyType1(type):
    def __new__(
        cls, name: str, bases: Tuple[type, ...], cls_dict: Dict[str, Any]
    ) -> type:
        print(f"MyType1.__new__ called with the following arguments:")
        print(f"\tcls: {cls} - {type(cls)}")
        print(f"\tname: {name} - {type(name)}")
        print(f"\tbases: {bases} - {type(bases)}")
        print(f"\tcls_dict: {cls_dict} - {type(cls_dict)}\n")
        new_class = super().__new__(cls, name, bases, cls_dict)
        return new_class


class Person1(metaclass=MyType1):
    pass


# MyType1.__new__ called with the following arguments:
# 	cls: <class '__main__.MyType1'> - <class 'type'>
# 	name: Person1 - <class 'str'>
# 	bases: () - <class 'tuple'>
# 	cls_dict: {'__module__': '__main__', '__qualname__': 'Person1'} - <class 'dict'>


class MyType2(type):
    @staticmethod
    def __prepare__(name: str, bases: Tuple[type, ...]) -> Dict[str, Any]:
        print(f"MyType2.__prepare__ called with the following arguments: ")
        print(f"\tname: {name} - {type(name)}")
        print(f"\tbases: {bases} - {type(bases)}\n")
        return {"a": 1, "b": 2}

    @staticmethod
    def __new__(
        cls: Type[type], name: str, bases: Tuple[type, ...], cls_dict: Dict[str, Any]
    ) -> type:
        print(f"MyType2.__new__ called with the following arguments:")
        print(f"\tcls: {cls} - {type(cls)}")
        print(f"\tname: {name} - {type(name)}")
        print(f"\tbases: {bases} - {type(bases)}")
        print(f"\tcls_dict: {cls_dict} - {type(cls_dict)}\n")
        new_class = super().__new__(cls, name, bases, cls_dict)
        return new_class


class Person2(metaclass=MyType2):
    pass


# MyType2.__prepare__ called with the following arguments:
# 	name: Person2 - <class 'str'>
# 	bases: () - <class 'tuple'>

# MyType2.__new__ called with the following arguments:
# 	cls: <class '__main__.MyType2'> - <class 'type'>
# 	name: Person2 - <class 'str'>
# 	bases: () - <class 'tuple'>
# 	cls_dict: {'a': 1, 'b': 2, '__module__': '__main__', '__qualname__': 'Person2'} - <class 'dict'>


class MyType3(type):
    @staticmethod
    def __prepare__(
        name: str, bases: Tuple[type, ...], **kwargs: Any
    ) -> Dict[str, Any]:
        print(f"MyType3.__prepare__ called with the following arguments: ")
        print(f"\tname: {name} - {type(name)}")
        print(f"\tbases: {bases} - {type(bases)}")
        print(f"\tkwargs: {kwargs}\n")
        cls_dict = {**kwargs}
        return cls_dict

    @staticmethod
    def __new__(
        cls: Type[type],
        name: str,
        bases: Tuple[type, ...],
        cls_dict: Dict[str, Any],
        **kwargs: Any,
    ) -> type:
        print(f"MyType3.__new__ called with the following arguments:")
        print(f"\tcls: {cls} - {type(cls)}")
        print(f"\tname: {name} - {type(name)}")
        print(f"\tbases: {bases} - {type(bases)}")
        print(f"\tcls_dict: {cls_dict} - {type(cls_dict)}")
        print(f"\tkwargs: {kwargs}\n")
        new_class = super().__new__(cls, name, bases, cls_dict)
        return new_class


class Person3(metaclass=MyType3, a=1, b=2):
    pass


# MyType3.__prepare__ called with the following arguments:
# 	name: Person3 - <class 'str'>
# 	bases: () - <class 'tuple'>
# 	kwargs: {'a': 1, 'b': 2}

# MyType3.__new__ called with the following arguments:
# 	cls: <class '__main__.MyType3'> - <class 'type'>
# 	name: Person3 - <class 'str'>
# 	bases: () - <class 'tuple'>
# 	cls_dict: {'a': 1, 'b': 2, '__module__': '__main__', '__qualname__': 'Person3'} - <class 'dict'>
# 	kwargs: {'a': 1, 'b': 2}


print("Person3 class namespace: ")
for k, v in vars(Person3).items():
    print(f"{k}: {v}")

# Person3 class namespace:
# a: 1
# b: 2
# __module__: __main__
# __dict__: <attribute '__dict__' of 'Person3' objects>
# __weakref__: <attribute '__weakref__' of 'Person3' objects>
# __doc__: None

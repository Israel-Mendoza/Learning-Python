from __future__ import annotations
from typing import Mapping


class MetaClass(type):
    @staticmethod
    def __prepare__(name: str, bases: tuple[type, ...], **kwargs) -> Mapping[str, object]:
        print(f"MetaClass __prepare__ called.")
        print(f"{name = } - {bases = } - {kwargs = }")
        return {"One": "Uno"}

    @staticmethod
    def __new__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, object], **kwargs) -> MetaClass:
        print(f"MetaClass __new__ called.")
        print(f"{name = }\n{bases = }\n{namespace = }\n{kwargs = }")
        return super().__new__(cls, name, bases, namespace)


class Person(metaclass=MetaClass, something="Hello!"):
    def __init__(self, name: str) -> None:
        self.name: str = name


# MetaClass __prepare__ called.
# name = 'Person' - bases = () - kwargs = {'something': 'Hello!'}

# MetaClass __new__ called.
# name = 'Person'
# bases = ()
# namespace = {
#   'One': 'Uno',  <-- Comes from the __prepare__ method!!!
#   '__module__': '__main__',
#   '__qualname__': 'Person',
#   '__init__': <function Person.__init__ at 0x104e21d00>
#   }
# kwargs = {'something': 'Hello!'}

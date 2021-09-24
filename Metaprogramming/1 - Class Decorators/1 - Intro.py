"""Using simple class decorators"""


# Creating a couple of class decorators.
# These decorators won't be doing anything else
# but to monkeypatch the class by adding new
# class attributes.

from __future__ import annotations
from typing import Callable


def savings(cls: type[Account]) -> type[Account]:
    cls.account_type = "savings"
    return cls


def checking(cls: type[Account]) -> type[Account]:
    cls.account_type = "checking"
    return cls


# Decorating classes with these class decorators


class Account:
    pass


@savings
class BankSavings01(Account):
    pass


@savings
class BankSavings02(Account):
    pass


@checking
class BankChecking01(Account):
    pass


@checking
class BankChecking02(Account):
    pass


# The "account_type" attribute was injected to the
# classes by the decorators 'savings' and 'checking':
print(vars(BankSavings01))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankSavings02))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankChecking01))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}
print(vars(BankChecking02))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}


"""Recreating the same as above, but using a parameterized decorator"""

# Creating a parameterized class decorator


def account_type(acc_type: str) -> Callable[[type[Account]], type[Account]]:
    """Decorator factory"""

    def class_decorator(cls: type[Account]) -> type[Account]:
        """A class decorator"""
        cls.account_type = acc_type
        return cls

    return class_decorator


# Decorating classes with the parameterized class decorators


@account_type("savings")
class BankSavings1(Account):
    pass


@account_type("savings")
class BankSavings2(Account):
    pass


@account_type("checking")
class BankChecking1(Account):
    pass


@account_type("checking")
class BankChecking2(Account):
    pass


# The "account_type" attribute was injected to the
# classes by the decorators 'savings' and 'checking':
print(vars(BankSavings1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankSavings2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankChecking1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}
print(vars(BankChecking2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}


"""Using class decorator to add a function to the decorated class"""


def adding_greeting(cls: type[Person]) -> type[Person]:
    def _adding_greeting(self: Person) -> str:
        return f"{self} says hello!"

    cls.say_hello = _adding_greeting

    return cls


@adding_greeting
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return self.name


print(vars(Person))
# {
#   '__module__': '__main__',
#   '__init__': <function Person.__init__ at 0x7fe662ec8ee0>,
#   '__str__': <function Person.__str__ at 0x7fe662ec8f70>,
#   '__dict__': <attribute '__dict__' of 'Person' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Person' objects>,
#   '__doc__': None,
#   'say_hello': <function adding_greeting.<locals>._adding_greeting at 0x7fe662ec8e50>
# }

from __future__ import annotations
from typing import Callable, Any

"""Using simple class decorators"""

"""
    In this file, we will be creating class decorators.
    
    These decorators won't be doing anything special.
    They will only monkeypatch the class by adding new class attributes
    and extra methods.
"""


def savings(cls: type) -> type:
    """
    Class decorator. It adds a class attribute called 'account type'.
    Args:
        cls [type] = A class
    Returns:
        cls [type] = A class with an extra class attribute, which value is "savings"
    """
    cls.account_type = "savings"
    return cls


def checking(cls: type) -> type:
    """
    Class decorator. It adds a class attribute called 'account type'.
    Args:
        cls [type] = A class
    Returns:
        cls [type] = A class with an extra class attribute, which value is "checking"
    """
    cls.account_type = "checking"
    return cls


"""Decorating classes with these class decorators"""


# Base class
class Account:
    pass


@savings
class BankSavings01(Account):
    pass


@savings
class BankSavings02(Account):
    pass


###############################


@checking
class BankChecking01(Account):
    pass


@checking
class BankChecking02(Account):
    pass


###############################


# The "account_type" attribute was injected to the classes by the decorators 'savings' and 'checking':

print(vars(BankSavings01))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankSavings02))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}

print(vars(BankChecking01))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}
print(vars(BankChecking02))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}


"""Recreating the same as above, but using a parameterized decorator"""

"""
    In the example below, we will be creating a decorator factory.
    In other works, a function that returns a class decorator. 
    
    Decorator factories will allow us to pass parameters we can use 
    to decorate the final classes. 
"""


def account_type(acc_type: str) -> Callable[[type[Account]], type[Account]]:
    """
    Decorator factory.
    Args:
        acc_type [str] = A string value representing the account type.
    Returns:
        class_decorator [Callable[type], type] = A class decorator.
    """

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


##############################


@account_type("checking")
class BankChecking1(Account):
    pass


@account_type("checking")
class BankChecking2(Account):
    pass


##############################

# The "account_type" attribute was injected to the classes by the decorators 'savings' and 'checking':

print(vars(BankSavings1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankSavings2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}

print(vars(BankChecking1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}
print(vars(BankChecking2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}


"""Using class decorator to add a function to the decorated class"""


def adding_greeting(cls: type) -> type:
    def _adding_greeting(self: Any) -> str:
        return f"'{self}' says hello!"

    cls.say_hello: Callable[[Any], str] = _adding_greeting

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

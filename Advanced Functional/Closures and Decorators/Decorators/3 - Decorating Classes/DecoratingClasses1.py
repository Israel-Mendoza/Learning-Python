"""
Decorating classes by "monkey patching" them
by adding a new instance method to their namespace.
"""


from typing import Type
from fractions import Fraction


def add_instance_method(cls: Type) -> Type:
    """
    Sets a function/method to the passed class as a "speak"
    attribute (monkey patching)
    Returns the class for reassigment.
    """
    # If intended as an instance method, 
    # remember to include the "self" argument
    def speak(self, message: str) -> str:
        """Function that could serve as a method"""
        return f'{self.__class__.__name__} says "{message}"'
    # Monkey patching the passed class
    setattr(cls, "speak", speak)
    # Returns the class
    return cls


class Person:
    """Simple representation of a person"""

    def __init__(self, name: str, age: int) -> None:
        """Initializing the Person instance"""
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        """The Person's name"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def age(self) -> int:
        """The Person's age"""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value


"""Working with a custom class"""

# Checking Person's namespace
print(vars(Person)) # {... __init__, "name", "age"...}

# Confirming that the attribute "speak" doesn't exist yet
print(hasattr(Person, "speak")) # False

# Creating a Person instance
p1 = Person("Israel Mendoza", 28)

# Trying the "speak" attribute
try:
    print(p1.speak("Je pense, donc je suis."))
except AttributeError as ex:
    print(ex) # 'Person' object has no attribute 'speak'

# Decorating the class (monkey patching it)
Person = add_instance_method(Person)

# Checking Person's namespace
print(vars(Person)) # {... __init__, "name", "age", "speak"...}

# Confirming that the attribute "speak" exists now
print(hasattr(Person, "speak")) # True

# Trying the "speak" attribute
try:
    print(p1.speak("Je pense, donc je suis.")) # Person says "Je pense, donc je suis."
except AttributeError as ex:
    print(ex)


"""Working with an existing class"""


# Confirming that the attribute "speak" doesn't exist yet
print(hasattr(Fraction, "speak")) # False

# Creating a Fraction instance
f1 = Fraction(1 / 3)

# Trying the "speak" attribute
try:
    print(f1.speak("To be or not to be?"))
except AttributeError as ex:
    print(ex) # 'Fraction' object has no attribute 'speak'

# Decorating the class (monkey patching it)
Fraction = add_instance_method(Fraction)

# Confirming that the attribute "speak" exists now
print(hasattr(Fraction, "speak")) # True

# Trying the "speak" attribute
try:
    print(f1.speak("To be or not to be?")) # Fraction says "To be or not to be?"
except AttributeError as ex:
    print(ex)

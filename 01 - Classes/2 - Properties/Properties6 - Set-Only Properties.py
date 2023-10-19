"""Defining a set-only property"""


# Using the traditional approach


class Person:
    def __init__(self, name: str) -> None:
        self._name: str = name

    def set_name(self, new_name: str) -> None:
        print("Setter called!!!")
        self._name: str = new_name

    name: property = property(
        fset=set_name, doc="Write-only property represents the name of the person"
    )


p: Person = Person("Israel")
try:
    p.name
except AttributeError as error:
    print(f"{error}\n")
# unreadable attribute

p.name = "Arturo"
# Setter called!!!
print()


# Using the @property notation


class Person:
    def __init__(self, name: str) -> None:
        self._name: str = name

    # Create an empty property object (otherwise, the first function risks of being the getter (fget)):
    name: property = property(doc="Write-only property represents the name of the person")

    # Continue chaining the property as usual
    @name.setter
    def name(self, new_name: str) -> None:
        print("Setter called!!!")
        self._name: str = new_name


p: Person = Person("Israel")
try:
    p.name
except AttributeError as error:
    print(f"{error}\n")
# unreadable attribute

p.name = "Arturo"
# Setter called!!!
print()


# Accessing the property documentation
help(Person.name)
# Help on property:

#     Write-only property represents the name of the person

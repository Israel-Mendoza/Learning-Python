# Defining a set-only property


# Using the traditional approach


class Person:
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name: str):
        print("Setter called!!!")
        self._name = new_name

    name = property(
        fset=set_name, doc="Write-only property represents the name of the person"
    )


p = Person("Israel")
try:
    p.name
except AttributeError as error:
    print(f"{error}\n")

p.name = "Arturo"
print()


# Using the @property notation


class Person:
    def __init__(self, name):
        self._name = name

    # Create an empty property object
    name = property(doc="Write-only property represents the name of the person")

    # Continue chaining the property as usual
    @name.setter
    def name(self, new_name):
        print("Setter called!!!")
        self._name = new_name


p = Person("Israel")
try:
    p.name
except AttributeError as error:
    print(f"{error}\n")

p.name = "Arturo"
print()


# Accessing the property documentation
help(Person.name)

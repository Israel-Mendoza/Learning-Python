class Person:
    """This is a Person object"""

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:  # Getter
        return self._name

    def set_name(self, value: str):  # Setter
        if isinstance(value, str):
            value = value.strip()
            if len(value) > 1:
                self._name = value
                print(f"{self}.name = '{self.get_name()}'\n")
            else:
                raise ValueError(f"'{value}' is too short for a name!\n")
        else:
            raise ValueError(f"'{value}' is not a valid string for a name!\n")

    def del_name(self):
        print(f"It's not a good idea to delete an attribute, my friend...")
        print(f"\n.\n.\n.\n.\nBut as you wish...")
        del self._name

    # Creating a 'name' property object
    name = property(
        fget=get_name, fset=set_name, fdel=del_name, doc="The person's name"
    )


# Instantiating the class
p = Person("Israel")
# Seeing the namespace of "p"
print(f"namespace of 'p': {p.__dict__}\n")

# Trying to set an int as the name using the name property
try:
    p.name = 155225
except ValueError as error:
    print(error)

# Trying to set an empty string as the name using the name property
try:
    p.name = "      "
except ValueError as error:
    print(error)

# Trying to set a valid string as the name using the name property
try:
    p.name = "Coco"
except ValueError as error:
    print(error)

# If we try to 'mask' the property name in the object's namespace,
# Python will still prioritize the property attribute
p.__dict__["name"] = "Nacho"
print(p.__dict__)
print(p.name)  # -> "Coco"
print(getattr(p, "name", None))

# Using the deleter out of the property name
del p.name

# The object doesn't have the _name attribute anymore
print(f"namespace of 'p': {p.__dict__}")

# We can still use the setter out of the property,
# because THE PROPERTY WAS NOT DELERED
p.name = "Pancho"
print(f"namespace of 'p': {p.__dict__}\n")

# Displaying the docstring of the name property
help(Person.name)

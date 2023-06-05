"""The PROPERTY object"""

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

    def del_name(self): # Deleter
        print(f"It's not a good idea to delete an attribute, my friend...")
        print(f".\n.\n.\nBut as you wish...")
        del self._name

    # Creating a 'name' property object
    name = property(
        fget=get_name, fset=set_name, fdel=del_name, doc="The person's name"
    )


# Instantiating the class
p = Person("Israel")

print(f"{p.__dict__ = }")
# p.__dict__ = {'_name': 'Israel'}


# Trying to set an int as the name using the name property
try:
    p.name = 155225
except ValueError as error:
    print(error)
# '155225' is not a valid string for a name!

# Trying to set an empty string as the name using the name property
try:
    p.name = "      "
except ValueError as error:
    print(error)
# '' is too short for a name!

# Trying to set a valid string as the name using the name property
try:
    p.name = "Coco"
except ValueError as error:
    print(error)
# <__main__.Person object at 0x7fcf9418ddf0>.name = 'Coco'

# If we try to 'mask' the property name in the object's namespace,
# Python will still prioritize the property attribute
p.__dict__["name"] = "Nacho"
print(p.__dict__)
# {'_name': 'Coco', 'name': 'Nacho'}
print(p.name)  
# Coco
print(getattr(p, "name", None))
# Coco

# Using the deleter out of the property name
del p.name
# It's not a good idea to delete an attribute, my friend...
# .
# .
# .
# But as you wish...

# The object doesn't have the _name attribute anymore:
print(f"{p.__dict__ = }")
# p.__dict__ = {'name': 'Nacho'}

# We can still use the setter out of the property,
# because THE PROPERTY WAS NOT DELERED
p.name = "Pancho"
print(f"{p.__dict__ = }\n")
# p.__dict__ = {'name': 'Nacho', '_name': 'Pancho'}

# Displaying the docstring of the name property
help(Person.name)
# Help on property:

#     The person's name

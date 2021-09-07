# Working with a property object

# Checking the property class namespace
print(f"\nChecking the 'property' class namespace: ")
for key in property.__dict__:
    print(f"{key}: {property.__dict__[key]}")
print("\n")


# Defining functions that will eventually be passed as
# arguments when creating a property object:


def get_prop(self):
    print("Getter called")


def set_prop(self, value):
    print("Setter called")


def del_prop(self):
    print("Deleter called")


# Creating a property object
# Passing the 'get_prop' function as the fget argument
print("Creating a property object called 'prop' with only the getter function:")
prop = property(get_prop)
print(f"type(prop) = {type(prop)}")
print(f"hex(id(prop)) = {hex(id(prop))}\n")

# Using the .setter attribute to add the set_prop function
# Assigning the result to a new variable
print(f"Adding a setter function to 'prop' and assigning return to 'prop_s'")
prop_s = prop.setter(set_prop)
print(f"type(prop_s) = {type(prop_s)}")
print(f"hex(id(prop_s)) = {hex(id(prop_s))}")
print(f"But most importantly: prop is prop_s = {prop is prop_s}\n")

# Using the .deleter attribute to add the del_prop function
# Assigning the result to a new variable
print(f"Adding a deleter function to 'prop_s' and assigning return to 'prop_d'")
prop_d = prop.deleter(del_prop)
print(f"type(prop_d) = {type(prop_d)}")
print(f"hex(id(prop_d)) = {hex(id(prop_d))}")
print(f"But most importantly: prop_s is prop_d = {prop is prop_s}\n")

print(f"prop: {prop}\nprop_s: {prop_s}\nprop_d: {prop_d}\n")

# We can, however, add and assign the returned objects to the same symbol

prop = property(get_prop)
prop = prop.setter(set_prop)
prop = prop.deleter(del_prop)
print(f"'prop' containing three different members: {prop}\n\n")

# Adding our existant 'prop' object to a real property within a class


class MyClass:
    name = prop


obj = MyClass()

# Using the getter function
obj.name
# Using the setter function
obj.name = "Israel"
# Using the deleter function
del obj.name

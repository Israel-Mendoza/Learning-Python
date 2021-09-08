from sys import getrefcount

# Working with the property object

# Defining a "getter" function
def name(self):
    print("Getter called...")


func_name_address = hex(id(name)).upper()
print(f"{func_name_address = }")


# Creating a property object out of 'name' and assigning it to 'name'
name = property(name)
property_name = hex(id(name)).upper()
print(f"{property_name = }")
print(f"name.fget:\t\t {hex(id(name.fget)).upper()}")

# 'name' is no longer poiting to the function, but the name.fget attribute is:
print(f"\nRef count to the original 'name' function: {getrefcount(func_name_address) - 1}")
# Ref count to the original 'name' function: 1
print(f"{hex(id(name.fget)) == func_name_address = }\n")
# hex(id(name.fget)) == func_name_address = False


# Saving the name property in a temp variable
temp_name_prop = name


# Re-defining the name function, now as a setter
def name(self, value):
    print("Setter called...")


# Recovering the name property, now with the setter
name = temp_name_prop.setter(name)

# Saving the name property in a tem variable again
temp_name_prop = name

# Re-defining the name function, now as a deleter
def name(self):
    print("Deleter called...")


# Recovering the name property, not with a deleter
name = temp_name_prop.deleter(name)


# Using the property object "name" within a class


class MyClass:
    name = name # name (class attribute) = name (property)


p1 = MyClass()

p1.name
p1.name = "Israel"
del p1.name
# Getter called...
# Setter called...
# Deleter called...

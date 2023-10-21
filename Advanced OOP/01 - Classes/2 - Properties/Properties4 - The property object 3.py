from sys import getrefcount

"""Working with the property object"""


# Defining a "getter" function
def name(self):
    print("Getter called...")


"""Grabbing the address where the name function is stored:"""
func_name_address: str = hex(id(name)).upper()
print(f"{func_name_address = }")
# func_name_address = '0X104884CC0'

"""Creating a property object out of 'name' and assigning it to 'name'"""
name: property = property(name)  # Assigning the getter. Re-using the "name" variable for the property.
name_property_address: str = hex(id(name)).upper()
name_fget_address: str = hex(id(name.fget)).upper()
print(f"{name_property_address = }")
# name_property_address = '0X104969990'
print(f"name.fget: {name_fget_address}")
# name.fget: 0X104884CC0

""""'name' is no longer pointing to the function, but the name.fget attribute is:"""
print(f"\nRef count to the original 'name' function in line 7: {getrefcount(func_name_address) - 1}")
# Ref count to the original 'name' function in line 7: 1
print(f"{name_fget_address == func_name_address = }\n")
# name_fget_address == func_name_address = True


"""Saving the name property in a temp variable"""
temp_name_prop: property = name


def name(self, value):  # Re-defining the name function, now as a setter
    print("Setter called...")


"""Recovering the name property, now with the setter"""
name: property = temp_name_prop.setter(name)

"""Saving the name property in a tem variable again"""
temp_name_prop: property = name


def name(self):  # Re-defining the name function, now as a deleter
    print("Deleter called...")


"""Recovering the name property, not with a deleter"""
name: property = temp_name_prop.deleter(name)


"""Using the property object "name" within a class"""


class MyClass:
    name: property = name  # name (class attribute) = name (property)


p1: MyClass = MyClass()

p1.name
# Getter called...
p1.name = "Israel"
# Setter called...
del p1.name
# Deleter called...

"""The PROPERTY object"""

# The property object has three attributes that will 
# allow us to add the functions to be called.

print(f"\nChecking the 'property' class namespace: ")
for key in property.__dict__:
    print(f"{key}: {property.__dict__[key]}")
print("\n")
# __getattribute__: <slot wrapper '__getattribute__' of 'property' objects>
# __get__: <slot wrapper '__get__' of 'property' objects>
# __set__: <slot wrapper '__set__' of 'property' objects>
# __delete__: <slot wrapper '__delete__' of 'property' objects>
# __init__: <slot wrapper '__init__' of 'property' objects>
# __new__: <built-in method __new__ of type object at 0x903d40>
# getter: <method 'getter' of 'property' objects>
# setter: <method 'setter' of 'property' objects>
# deleter: <method 'deleter' of 'property' objects>
# fget: <member 'fget' of 'property' objects>
# fset: <member 'fset' of 'property' objects>
# fdel: <member 'fdel' of 'property' objects>
# __doc__: <member '__doc__' of 'property' objects>
# __isabstractmethod__: <attribute '__isabstractmethod__' of 'property' objects>


# Defining functions that will eventually be passed as arguments when creating a property object:


def get_prop(self):
    print("Getter called")


def set_prop(self, value):
    print("Setter called")


def del_prop(self):
    print("Deleter called")


# Creating a property object
# Passing the 'get_prop' function as the fget argument
prop: property = property(get_prop)
print(f"{type(prop) = }")
# type(prop) = <class 'property'>
print(f"{hex(id(prop)) = }\n")
# hex(id(prop)) = '0x7f4944ec3950'

# Using the .setter attribute to add the set_prop function.
# It returns a NEW property object. Assigning the result to a new variable.
prop_s: property = prop.setter(set_prop)  # The .setter method returns a new version of the property
print(f"{type(prop_s) = }")
print(f"{hex(id(prop_s)) = }")
# hex(id(prop_s)) = '0x7f4944ec3a40'
print(f"But most importantly: prop is prop_s ? = {prop is prop_s}\n")
# But most importantly: prop is prop_s ? = False

# Using the .deleter attribute to add the del_prop function.
# It returns a NEW property object. Assigning the result to a new variable.
prop_d: property = prop.deleter(del_prop)

print(f"{type(prop_d) = }")
# type(prop_d) = <class 'property'>
print(f"{hex(id(prop_d)) = }")
# hex(id(prop_d)) = '0x7f4944ec3ae0'
print(f"But most importantly: prop_s is prop_d ? = {prop_s is prop_d}\n")
# But most importantly: prop_s is prop_d ? = False

print(f"prop: {prop}\nprop_s: {prop_s}\nprop_d: {prop_d}\n")
# prop: <property object at 0x7f4944ec3950>
# prop_s: <property object at 0x7f4944ec3a40>
# prop_d: <property object at 0x7f4944ec3ae0>

# We can, however, add and assign the returned objects to the same symbol

prop: property = property(get_prop)  # The first argument will be the getter
prop: property = prop.setter(set_prop)
prop: property = prop.deleter(del_prop)
print(f"'prop' containing three different members: {prop}\n\n")
# 'prop' containing three different members: <property object at 0x7f4944ec3b30>


# Adding our existent 'prop' object to a real property within a class


class MyClass:
    name: property = prop


obj: MyClass = MyClass()

# Using the getter function
obj.name
# Getter called

# Using the setter function
obj.name = "Israel"
# Setter called

# Using the deleter function
del obj.name
# Deleter called

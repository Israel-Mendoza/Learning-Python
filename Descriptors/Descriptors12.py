"""Using a data descriptor to access an instance attribute"""


class IntegerValue:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("__get__ called!")

    def __set__(self, instance, value):
        print("__set__ called!")


class Point:

    x = IntegerValue()


print("USING A DATA DESCRIPTOR!!!")
p = Point()

# Setting and getting a value through the descriptor
# (no instance attribute has the name "x")
p.x = 10
# __set__ called!
p.x
# __get__ called!

# Forcing an entry with the name "x" in the instance dictionary
p.__dict__["x"] = 100000
# Accessing this "new" attribute.
# The descriptor will be called because it is a DATA DESCRIPTOR
p.x
# __get__ called!
print("\n")


"""Using a non-data descriptor to access an instance attribute"""


class IntegerValue:

    def __get__(self, instance, owner):
        print("__get__ called!")


class Point:

    x = IntegerValue()


print("USING A NON-DATA DESCRIPTOR!!!")

p = Point()

# Getting a value through the descriptor
# (no instance attribute has the name "x")
p.x
# __get__ called!

# Forcing an entry with the name "x" in the instance dictionary
p.__dict__["x"] = 100000
# Accessing this new attribute.
# The entry in the dictionary will be called
# because we are using a NON-DATA DESCRIPTOR
print(p.x)
# 100000
"""Using a data descriptor to access an instance attribute"""


# USING A DATA DESCRIPTOR!


class IntegerValue:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print("__get__ called!")

    def __set__(self, instance, value):
        print("__set__ called!")


class Point:

    x = IntegerValue()


p = Point()

# Setting and getting a value through the descriptor
# (no instance attribute has the name "x")
p.x = 10
# __set__ called!
p.x
# __get__ called!

# Forcing an entry with the name "x" into the instance's namespace
p.__dict__["x"] = 100000

# Accessing this "new" attribute.
# The descriptor has a priority because it's a DATA DESCRIPTOR
p.x
# __get__ called!


"""Using a non-data descriptor to access an instance attribute"""


# USING A NON-DATA DESCRIPTOR!


class IntegerValue:

    def __get__(self, instance, owner):
        print("__get__ called!")


class Point:

    x = IntegerValue()


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

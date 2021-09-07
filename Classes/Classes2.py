# Working with attributes


class Program:
    # Setting attributed from within the class
    language = "Python"
    version = "3.6"

    @staticmethod
    def say_hello():
        print(f"Hello from {Program.language}")


# Accessing attributes
print(Program.language)
print(Program.version)
print(getattr(Program, "language", None))
print(getattr(Program, "version", None))
print()

# Accessing attributes that don't exist
try:
    print(f"{Program.operating_system}\n")
except AttributeError:
    print("We're sorry, but the 'operating_system' attribute doesn't exist\n")

# Avoiding the try-except block by using the "getattr" function
if getattr(Program, "operating_system", None):
    print(print(f"{Program.operating_system}\n"))
else:
    print("We're sorry, but the 'operating_system' attribute doesn't exist\n")


# Setting existing attributes
Program.version = "3.7"
print(f"New version of 'MyClass': {Program.version}")

setattr(Program, "version", "3.8")
print(f"New version of 'MyClass': {getattr(Program, 'version', None)}\n")

# Setting inexistent attributes
setattr(Program, "operating_system", "Windows 10")
print(f"New attribute of Program: {getattr(Program, 'operating_system', None)}\n")

# Object dictionaty (mappingproxy)
print(f"'Program' mappingproxy:")
for k in Program.__dict__:
    print(f"{Program.__name__}.{k}: {Program.__dict__[k]}")
print()

# Deleting attributes
print(f"Deleting the 'operating_system' attribute:")
delattr(Program, "operating_system")
for k in Program.__dict__:
    print(f"Program.{k}: {Program.__dict__[k]}")
print()

# Retrieving callables from the class' namespace:
a_func = getattr(Program, "say_hello", None)
if a_func:
    a_func()

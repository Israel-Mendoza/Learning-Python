# Working with function attributes


class Person:
    # Defining a class function
    def say_hello():
        print("Hello")


print(f"Address of 'Person': {hex(id(Person))}")
print(f"Person.say_hello: {Person.say_hello}\n")

# Creating an instance of Person
p = Person()
print(f"Address of 'p': {hex(id(p))}")
print(f"p.say_hello: {p.say_hello}\n")

# Comparing types of "say_hello"
print(f"{type(Person.say_hello)} - {type(p.say_hello)}\n")

# Calling the "say_hello" function from the instance
try:
    p.say_hello()
except TypeError as te:
    print(f"'say_hello' called from the p instance of Person!\n{te}\n\n")


# Fixing the TypeError when calling the 'say_hello' from an instance


class Person:
    # Defininf an instance method
    def say_hello(*args):
        print(f"Passed arguments to say_hello: {args}")


p = Person()
print(f"Address of 'p': {hex(id(p)).upper()}\n")

# Trying to call the method again:
try:
    p.say_hello()
except TypeError as te:
    print(f"'say_hello' called from the p instance of Person!\n{te}")
finally:
    print(end="\n\n")


# Working with instance methods


class Person:
    def set_name(self, new_name):
        self.name = new_name


p = Person()
p.set_name("Israel")
print(f"Namespace of 'p': {p.__dict__}\n")


# Working with the method's attributes

print(f"p.set_name.__func__: {p.set_name.__func__}")
print(f"p.set_name.__self__: {p.set_name.__self__}")

# Calling the method the way Python does it under the hood
p.set_name.__func__(p.set_name.__self__, "Arturo")
print(f"Namespace of 'p': {p.__dict__}\n")

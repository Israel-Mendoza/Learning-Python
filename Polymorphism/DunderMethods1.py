# Implementing the __str__ and the __repr__ methods


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print("__repr__ called")
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Israel", 28)
print("Only __repr__ was implemented:")
print(repr(p))  # Calling the implemented __repr__
print(p, end="\n\n")  # Calling __repr__ because __str__ was implemented


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print("__str__ called")
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Israel", 28)
print("Only __str__ was implemented:")
print(repr(p))  # Calling the __repr__ from object
print(p, end="\n\n")  # Calling the implemented __str__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print("__repr__ called")
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        print("__str__ called")
        return f"{self.name} is {self.age} years old"


p = Person("Israel", 28)
print("Both __repr__ and __str__ were implemented:")
print(repr(p))  # Calling the implemented __repr__
print(p)  # Calling the implemented __str__

class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"{self.name} says hello!"


p = Person("Israel")

# Getting the return value from the __get__ method:
a_function = Person.say_hello.__get__(None, Person)
a_method = Person.say_hello.__get__(p, Person)
print(Person.say_hello, a_function)
print(p.say_hello, a_method)
print()

# The method stores the function under __func__
print(p.say_hello.__func__)

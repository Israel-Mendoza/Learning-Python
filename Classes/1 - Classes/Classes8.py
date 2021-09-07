from types import MethodType


class Person:
    def __init__(self, name):
        self.name = name


p1 = Person("Israel")
p2 = Person("Mike")

print(f"{p1.__dict__} - {p2.__dict__}")


# Creating a couple of functions to be added later as a method


def say_hello(self):
    print(f"{self.name} says 'Hello!'")


def say_bye(self):
    print(f"{self.name} says 'Bye!'")


# Setting "bound method" objects to attributes
p1.say_hello = MethodType(say_hello, p1)
setattr(p1, "say_bye", MethodType(say_bye, p1))
print(f"\np1 namespace: \n{p1.__dict__}\n\np2 namespace: \n{p2.__dict__}\n")


# Using the MethodType object to set different methods among different instances


class Employee:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"

    def defining_work(self, func):
        """
        Method which allows us 
        to set the self.work() bound method
        """
        setattr(self, "work", MethodType(func, self))
        # self.work = MethodType(func, self)

    def work(self):
        """
        Method will raise an error if not implemented
        using the "defining_work" method
        """
        raise AttributeError("Use 'defining_work' before calling this method!")


e1 = Employee("Israel", "Mendoza")
e2 = Employee("Christopher", "Nolan")

# Creating the functions that will eventually be methods


def program(obj):
    print(f"{obj.full_name} is now programming.")


def movie_making(obj):
    print(f"{obj.full_name} is now making a movie.")


# Calling the 'work' method prior to implementation
try:
    e1.work()
except AttributeError as error:
    print(error, end="\n\n")

# Adding the functions as bound methods

e1.defining_work(program)
e2.defining_work(movie_making)

# Calling the "same" method on both instances

emp = [e1, e2]
for e in emp:
    e.work()

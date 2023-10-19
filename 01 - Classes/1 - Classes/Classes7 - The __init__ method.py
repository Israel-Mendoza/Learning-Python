""" Instance creation and object initialization"""


class Person:
    def init(self, name):
        """A fake init method, to be called on-demand"""
        setattr(self, "name", name) # Or self.name = name


p: Person = Person()

# After creation, the object namespace is empty
print(f"{p.__dict__ = }")
# p.__dict__ = {}
print()

# Calling out fake "init" method
p.init("Israel")
print(f"{p.__dict__ = }")
# p.__dict__ = {'name': 'Israel'}


"""Seeing the __init__ method in action"""


class Person:
    def __init__(self, name: str, age: int, nationality: str) -> None:
        """The __init__ method is called on the newly created instance"""
        print("$" * 60, end="\n")
        print("__init__ started running!!!\n")
        print(f"The object's namespace is empty: {self.__dict__}")
        print("The object's namespace will be populated: ")
        self.name = name
        print(self.__dict__)
        self.age = age
        print(self.__dict__)
        self.nationality = nationality
        print(self.__dict__)
        print("\n__init__ finished running!!!")
        print("$" * 60, end="\n\n")


p: Person = Person("Israel", 28, "Mexican")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# __init__ started running!!!

# The object's namespace is empty: {}
# The object's namespace will be populated: 
# {'name': 'Israel'}
# {'name': 'Israel', 'age': 28}
# {'name': 'Israel', 'age': 28, 'nationality': 'Mexican'}

# __init__ finished running!!!
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

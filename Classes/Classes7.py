# Playing with instance creation and object initialization


class Person:
    def init(self, name):
        setattr(self, "name", name)


p = Person()

# After creation, the object namespace is empty
print(f"Without __init__ method, the object's namespace is empty: ")
print(p.__dict__)
print()

# Calling out customed "init" method
print(f"Simutating the __init__ method with a custom one: ")
p.init("Israel")
print(f"Checking the objects namespace: {p.__dict__}\n")


# Seeing the __init__ method in action


class Person:
    def __init__(self, name: str, age: int, nationality: str) -> None:
        print("%" * 60, end="\n")
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
        print("%" * 60, end="\n\n")


p = Person("Israel", 28, "Mexican")

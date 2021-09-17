"""Overriding inherited methods and calling super()"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        print(f"Calling Person({name}, {age})")
        self.name: str = name
        self.age: int = age

    def hello(self) -> None:
        print(f"{self} says hello!")

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name}, {self.age})"


# Overriding all inherited methods and using super()
class Student(Person):
    def __init__(self, name: str, age: int, major: str):
        print(f"Calling Student({name}, {age}, {major})")
        super().__init__(name, age)
        self.major: str = major

    def hello(self) -> None:
        print(f"{self} says hello!")
        super().hello()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name}, {self.age}, {self.major})"


p = Person("Arturo", 71)
# Calling Person(Arturo, 71)
s = Student("Israel", 28, "Computer Science")
# Calling Student(Israel, 28, Computer Science)
# Calling Person(Israel, 28)  <- From super()

p.hello()
# Person(Arturo, 71) says hello!
s.hello()
# Student(Israel, 28, Computer Science) says hello!
# Student(Israel, 28, Computer Science) says hello! <- From super()

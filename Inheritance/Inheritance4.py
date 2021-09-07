class Person:
    def __init__(self, name, age):
        print(f"Calling Person({name}, {age})")
        self.name = name
        self.age = age

    def hello(self):
        print(f"{self} says hello!")

    def __repr__(self):
        return f"{type(self).__name__}({self.name}, {self.age})"


class Student(Person):
    def __init__(self, name, age, major):
        print(f"Calling Student({name}, {age}, {major})")
        super().__init__(name, age)
        self.major = major

    def hello(self):
        print(f"{self} says hello!")
        super().hello()

    def __repr__(self):
        return f"{type(self).__name__}({self.name}, {self.age}, {self.major})"


p = Person("Arturo", 71)
s = Student("Israel", 28, "Computer Science")
print()
p.hello()
s.hello()

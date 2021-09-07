class Person:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


p = Person("Margarita")
s = Student("Israel")

print(f"Student namespace: {vars(s)}")
try:
    print(f"Person namespace: {vars(p)}")
except TypeError as error:
    print("Person namespace: ")
    print(f"\tTypeError: {error}")
print()

# Because the Student subclass doesn't implement slots,
# it inherits the one from the parent class, but it also
# makes use of the __dict__ namespace dictionary.

s.major = "Computer Science"
print(s.major)

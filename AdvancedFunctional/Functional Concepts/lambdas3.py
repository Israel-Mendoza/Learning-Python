"""Using lambdas with the sorted function"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


p1 = Person("Israel", 28)
p2 = Person("Victor", 25)
p3 = Person("Roberto", 32)
p4 = Person("Luis", 30)

people = [p1, p2, p3, p4]
sorted_people = []

try:
    sorted_people = sorted(people)
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
else:
    for person in sorted_people:
        print(f"{person.name} is {person.age} years old")


try:
    sorted_people = sorted(people, key=lambda person: person.age, reverse=True)
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
else:
    for person in sorted_people:
        print(f"{person.name} is {person.age} years old")
# Roberto is 32 years old
# Luis is 30 years old
# Israel is 28 years old
# Victor is 25 years old


try:
    sorted_people = sorted(people, key=lambda person: person.name[-1])
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
else:
    for person in sorted_people:
        print(f"{person.name}")
# Israel
# Roberto
# Victor
# Luis

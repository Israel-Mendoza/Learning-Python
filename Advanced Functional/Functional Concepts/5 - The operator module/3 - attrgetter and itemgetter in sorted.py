from operator import attrgetter, itemgetter


"""Using attrgetter in sorted"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.age})"


p1 = Person("Israel", 28)
p2 = Person("Carlos", 32)
p3 = Person("Victor", 25)
p4 = Person("Margarita", 27)

people: list[Person] = [p1, p2, p3, p4]
my_tuples: list[tuple[int, ...]] = [(1, 2, 3), (2, 1, 4), (5, 2, 4), (5, 5, 5), (3, 4, 0)]

# attrgetter("age") returns a callable, perfect for use in sorted
sorted_people: list[Person] = sorted(people, key=attrgetter("age"))
# itemgetter(1) returns a callable, perfect for use in sorted
sorted_tuples: list[tuple[int, ...]] = sorted(my_tuples, key=itemgetter(1))

print(people)
# [Person('Israel', 28), Person('Carlos', 32), Person('Victor', 25), Person('Margarita', 27)]
print(sorted_people)
# [Person('Victor', 25), Person('Margarita', 27), Person('Israel', 28), Person('Carlos', 32)]

print(my_tuples)
# [(1, 2, 3), (2, 1, 4), (5, 2, 4), (5, 5, 5), (3, 4, 0)]
print(sorted_tuples)
# [(2, 1, 4), (1, 2, 3), (5, 2, 4), (3, 4, 0), (5, 5, 5)]

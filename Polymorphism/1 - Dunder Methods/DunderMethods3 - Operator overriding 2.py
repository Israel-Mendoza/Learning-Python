from __future__ import annotations

""""""

from typing import Any


class Person:
    def __init__(self: Person, name: str) -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self: Person, new_name: str) -> None:
        if len(new_name.strip()) > 0:
            self._name: str = new_name
        else:
            raise ValueError("Name must be a valid string...")

    def __repr__(self: Person) -> str:
        return f"Person('{self.name}')"


class Family:
    def __init__(self: Family, mother: Person, father: Person) -> None:
        self.mother: Person = mother
        self.father: Person = father
        self.children: list[Person] = []
        self.num_of_children: int = 0

    def __iadd__(self: Family, child: Person) -> Family:
        # Family is a mutable object because it returns itself
        if self.check_child(child):
            self.children.append(child)
            self.num_of_children += 1
            return self
        else:
            raise ValueError("Child must be an instance of Person")

    def __len__(self: Family) -> int:
        return len(self.children) + 2

    def __repr__(self: Family) -> str:
        return f"A Family living in {hex(id(self)).upper()}"

    def introduce_family(self: Family) -> None:
        print(f"This is the family living at {hex(id(self)).upper()}")
        print(f"\tFather: {self.father}")
        print(f"\tMother: {self.mother}")
        if self.num_of_children > 0:
            print("\tChild:" if self.num_of_children == 1 else "\tChildren:")
            for child in self.children:
                print(f"\t\t{child}")

    @staticmethod
    def check_child(a_child: Any) -> bool:
        return isinstance(a_child, Person)


my_family: Family = Family(Person("Marge"), Person("Homer"))

print(my_family)
# A Family living in 0X7F97C0B927F0

my_family += Person("Bart")

print(my_family)
# A Family living in 0X7F97C0B927F0

my_family += Person("Lisa")

print(my_family)
# A Family living in 0X7F97C0B927F0

my_family += Person("Maggie")

print(my_family)
# A Family living in 0X7F97C0B927F0

print(f"Children: {my_family.children}")
# Children: [Person('Perry'), Person('Ginny')]

my_family.introduce_family()
# This is the family living at 0X7F97C0B927F0
# 	Father: Person('Homer')
# 	Mother: Person('Marge')
# 	Children:
# 		Person('Bart')
# 		Person('Lisa')
# 		Person('Maggie')

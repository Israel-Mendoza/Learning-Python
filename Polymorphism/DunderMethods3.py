class Person:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if len(new_name.strip()) < 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a valid string...")

    def __repr__(self):
        return f"Person('{self.name}')"


class Family:
    def __init__(self, mother, father):
        self.mother = mother
        self.father = father
        self.children = []

    def __iadd__(self, child: Person):
        # Family is a mutable object
        if isinstance(child, Person):
            self.children.append(child)
            return self
        else:
            raise ValueError("Child must be an instance of Person")

    def __repr__(self):
        return f"A Family living in {hex(id(self)).upper()}"


my_family = Family(Person("Antonia"), Person("Arturo"))
print(my_family)
my_family += Person("Israel")
print(my_family)
my_family += Person("Mogo")
print(my_family)
print(f"Children: {my_family.children}")

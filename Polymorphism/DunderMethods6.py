# Implementing __hash__
# Remember that the __hash__ will be based on an immutable attribute in the object
# We must enforce that this attribute will not be changed


class Person:
    def __init__(self, name: str):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a valid string")

    @property
    def name(self):
        """The name of the person"""
        return self._name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        # self._name must be immutable and "read-only"
        return hash(self.name)

    def __repr__(self):
        return f"Person('{self.name}')"


p1 = Person("Israel")
p2 = Person("Arturo")

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 == p2 = {p1 == p2}")


# Because our object is hashable, we can now use it as dictionary keys:
people = {p1: "Israel Mendoza", p2: "Arturo Sanchez"}

# Looping thorugh the dictionary
for person in people:
    print(f"{person} = {person.name}")

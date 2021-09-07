class Person:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        print(f"Setting .name attribute to '{new_name}'")
        self._name = new_name

    # When chaining property decorators, the decorator will take the name
    # of the function it wraps
    @name.deleter
    def names(self):
        print("Deleting .name attribute...")
        del self._name


p = Person("Israel")
# Using "names" as the property, because that is the last name of the property
print(p.names)
p.names = "Arturo"
print(p.name)
del p.names

try:
    print(p.name)
except AttributeError as error:
    print(error)


class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    # name = property(name)
    @property
    def name(self) -> str:
        return self._name

    # When chaining property decorators, the decorator will take the name
    # of the function it wraps: name = name.setter(name)
    @name.setter
    def name(self, new_name: str) -> None:
        print(f"Setting .name attribute to '{new_name}'")
        self._name = new_name

    # names (with an "s") will be the final name of the property
    # names = name.deleter(name)
    @name.deleter
    def names(self) -> None:
        print("Deleting .name attribute...")
        del self._name


p: Person = Person("Israel")
# Using "names" as the property, because that is the last name of the property
print(p.names)
# Israel
p.names = "Arturo"
# Setting .name attribute to 'Arturo'
print(p.names)
# Arturo
del p.names
# Deleting .name attribute...
try:
    print(p.name)
except AttributeError as error:
    print(error)
# 'Person' object has no attribute '_name'

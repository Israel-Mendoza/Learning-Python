def display_obj_namespace(an_object):
    print(f"OBJECT'S NAMESPACE:")
    for k, v in vars(an_object).items():
        if "__slots__" in vars(an_object) and k in vars(an_object)["__slots__"]:
            print(f"Slotted attribute '{k}': {v}")
        else:
            print(f"Class attribute '{k}': {v}")


class Person:
    __slots__ = "_name", "age"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


p = Person("Israel", 28)
display_obj_namespace(Person)
print()
print(f"Descriptors' types: {type(Person.name)} - {type(Person.age)}")
print(f"Does Person.name has __set__ and __get__ attributes?")
print(f"{hasattr(Person.name, '__set__')} and {hasattr(Person.name, '__get__')}")
print(f"Does Person.age has __set__ and __get__ attributes?")
print(f"{hasattr(Person.age, '__set__')} and {hasattr(Person.age, '__get__')}")

def display_obj_namespace(an_object):
    print(f"OBJECT'S NAMESPACE:")
    for k, v in vars(an_object).items():
        if "__slots__" in vars(an_object) and k in vars(an_object)["__slots__"]:
            print(f"Slotted attribute '{k}': {v}")
        else:
            print(f"Class attribute '{k}': {v}")


class Person:
    __slots__ = "name", "__dict__"

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Israel", 28)
display_obj_namespace(Person)
print()
print(f"p's namespace: {vars(p)}")

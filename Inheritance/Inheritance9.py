def display_obj_namespace(an_object):
    print(f"{an_object.__name__.upper()}'S NAMESPACE:")
    for k, v in vars(an_object).items():
        if "__slots__" in vars(an_object) and k in vars(an_object)["__slots__"]:
            print(f"Slotted attribute '{k}': {v}")
        else:
            print(f"Class attribute '{k}': {v}")


class Person:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


class Student(Person):
    __slots__ = ("school", "student_number")

    def __init__(self, name, school, student_number):
        super().__init__(name)
        self.school = school
        self.student_number = student_number


# Because the Student subclass also implements slots,
# there is no instance dictionary.

s = Student("James Bond", "MI6 Prep School", "007")
display_obj_namespace(Person)
print()
display_obj_namespace(Student)

def display_obj_namespace(an_object):
    print(f"OBJECT'S NAMESPACE:")
    for k, v in vars(an_object).items():
        if "__slots__" in vars(an_object) and k in vars(an_object)["__slots__"]:
            print(f"Slotted attribute '{k}': {v}")
        else:
            print(f"Class attribute '{k}': {v}")


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    __slots__ = ("school", "student_number")

    def __init__(self, name, school, student_number):
        super().__init__(name)
        self.school = school
        self.student_number = student_number


# Because the Student subclass implements slots,
# but inherits from a class that doesn't,
# Student will have an instance dictionary as well

s = Student("James Bond", "MI6 Prep School", "007")
display_obj_namespace(Person)
print()
display_obj_namespace(Student)
print()
display_obj_namespace(s)
print()


class Person:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, school, student_number):
        super().__init__(name)
        self.school = school
        self.student_number = student_number


# Because the Person class implements slots,
# but its subclass Student doesn't,
# Student will have an instance dictionary as well

s = Student("James Bond", "MI6 Prep School", "007")
display_obj_namespace(s)

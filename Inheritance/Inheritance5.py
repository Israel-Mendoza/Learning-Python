class Person:
    def work(self):
        return f"{type(self).__name__} at {hex(id(self))} works..."


class Student(Person):
    def work(self):
        result = super().work()
        return f"{type(self).__name__} at {hex(id(self))} studies... and {result}"


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f"{type(self).__name__} at {hex(id(self))} codes... and {result}"


ps = PythonStudent()
print(ps.work())

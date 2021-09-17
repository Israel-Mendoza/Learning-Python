"""Using the super() method"""


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
# PythonStudent at 0x7f03dfea0c70 codes... and PythonStudent at 0x7f03dfea0c70 studies... and PythonStudent at 0x7f03dfea0c70 works...

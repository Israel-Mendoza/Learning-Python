from __future__ import annotations
from typing import override


"""Using the super() method"""


class Person:
    def work(self: Person) -> str:
        return f"{type(self).__name__} at {hex(id(self))} works..."


class Student(Person):
    @override
    def work(self: Student) -> str:
        result: str = super().work()
        return f"{type(self).__name__} at {hex(id(self))} studies... and {result}"


class PythonStudent(Student):
    @override
    def work(self):
        result = super().work()
        return f"{type(self).__name__} at {hex(id(self))} codes... and {result}"


p: Person = Person()
s: Student = Student()
ps: PythonStudent = PythonStudent()

print(p.work())
# Person at 0x7fb09ad54c90 works...
print(s.work())
# Student at 0x7fb09ad55f50 studies... and Student at 0x7fb09ad55f50 works...
print(ps.work())
# PythonStudent at 0x7fb09ad54ed0 codes... and PythonStudent at 0x7fb09ad54ed0 studies... and PythonStudent at
# 0x7fb09ad54ed0 works...

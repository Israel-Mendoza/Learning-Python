from __future__ import annotations


"""Using class methods to create alternative constructors"""


class Employee:
    raise_amount: float = 1.04  # 4% salary raise

    def __init__(self, first_name: str, last_name: str, age: int, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.full_name} is {self.age} years old and has a monthly salary of ${self.salary:.2f}"

    @property
    def first_name(self) -> str:
        """The Employee's first name"""
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name: str) -> None:
        if len(new_first_name.strip()) > 0:
            self._first_name: str = new_first_name
        else:
            raise ValueError("New first name must be a valid string...")

    @property
    def last_name(self) -> str:
        """The Employee's last name"""
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name: str) -> None:
        if len(new_last_name.strip()) > 0:
            self._last_name: str = new_last_name

    @property
    def full_name(self) -> str:
        """The Employee's full name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        """The Employee's age"""
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        self._age: int = Employee.age_format_checker(new_age)

    @property
    def salary(self) -> float:
        """The Employee's salary"""
        return self._salary

    @salary.setter
    def salary(self, new_salary: float) -> None:
        if isinstance(new_salary, int) or isinstance(new_salary, float):
            self._salary: float = float(abs(new_salary))
        else:
            try:
                new_salary: float = float(new_salary)
                self._salary: float = new_salary
            except ValueError:
                raise ValueError("Salary must be a valid number...")

    def apply_raise(self) -> None:
        """
        Applies raise to the class instances,
        based on the raise amount rate
        """
        self.salary *= self.raise_amount

    @classmethod
    def from_string(cls, emp_str: str, separator: str) -> Employee:
        """
        Alternative constructor.
        args:
            emp_str [str]: A string containing the employee info
            separator [str]: The string separating the employee info
        returns: An employee object
        """
        first, last, age, salary = emp_str.split(separator)
        return cls(first, last, age, salary)

    @staticmethod
    def age_format_checker(age: any) -> int:
        """
        Check that the passed age argument is a valid integer,
        excluding numbers between -17 and 17.
        Returns valid positive int
        Raises ValueError if numbers between -17 and 17 or not a
        valid int
        """
        checker: int = 0
        if isinstance(age, int):
            age: int = abs(age)
            if age >= 18:
                return age
            else:
                checker = -1
        else:
            try:
                age = abs(int(age))
                if age >= 18:
                    return age
            except ValueError:
                checker = 1
        if checker == -1:
            raise ValueError("Age must be at least 18...")
        else:
            raise ValueError("Age must be a valid number...")


e1: str = "Ezra--Kaltenberg--31--52000"
e2: str = "Mike--Schmidt--26--26000"
e3: str = "Edward--Rodriguez--27--17000"

emp_strings: list[str] = [e1, e2, e3]
emp_objects: list[Employee] = []

for employee in emp_strings:
    temp_emp: Employee = Employee.from_string(employee, "--")
    emp_objects.append(temp_emp)

for employee in emp_objects:
    print(employee)
# Ezra Kaltenberg is 31 years old and has a monthly salary of $52000.00
# Mike Schmidt is 26 years old and has a monthly salary of $26000.00
# Edward Rodriguez is 27 years old and has a monthly salary of $17000.00

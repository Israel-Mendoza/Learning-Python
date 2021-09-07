# Using class methods to create alternative constructors


class Employee:

    raise_amount = 1.04  # 4% salary raise

    def __init__(self, first_name: str, last_name: str, age: int, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def first_name(self):
        """The Employee's first name"""
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name: str):
        if len(new_first_name.strip()) > 0:
            self._first_name = new_first_name
        else:
            raise ValueError("New first name must be a valid string...")

    @property
    def last_name(self):
        """The Employee's last name"""
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name: str):
        if len(new_last_name.strip()) > 0:
            self._last_name = new_last_name

    @property
    def full_name(self):
        """The Employee's full name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        """The Employee's age"""
        return self._age

    @age.setter
    def age(self, new_age: int):
        self._age = Employee.age_format_checker(new_age)

    @property
    def salary(self):
        """The Employee's salary"""
        return self._salary

    @salary.setter
    def salary(self, new_salary: float):
        if isinstance(new_salary, int) or isinstance(new_salary, float):
            self._salary = abs(new_salary)
        else:
            try:
                new_salary = float(new_salary)
                self._salary = new_salary
            except ValueError:
                raise ValueError("Salary must be a valid number...")

    def apply_raise(self) -> None:
        """
        Applies raise to the class instances,
        based on the raise amount rate
        """
        self.salary *= self.raise_amount

    @classmethod
    def from_string(cls, emp_str: str, separator: str):
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
        checker = 0
        if isinstance(age, int):
            age = abs(age)
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

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and has a monthly salary of ${self.salary:.2f}"


e1 = "Ezra--Kaltberg--28--28000"
e2 = "Mike--Schmidt--26--26000"
e3 = "Edward--Rodriguez--27--17000"

emp_strings = [e1, e2, e3]
emp_objects = []

for employee in emp_strings:
    # Appending employee objects after creating them with the alternative constructor
    emp_objects.append(Employee.from_string(employee, "--"))

for employee in emp_objects:
    print(employee)

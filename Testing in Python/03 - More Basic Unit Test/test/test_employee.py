import unittest
from src.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.employee = Employee("Israel", "Mendoza", 300_000)

    def test_employee_receives_correct_default_raise(self) -> None:
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 305000)

    def test_employee_receives_correct_custom_raise(self) -> None:
        self.employee.give_raise(20000)
        self.assertEqual(self.employee.annual_salary, 320000)

class Employee:
	
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first}.{last}@company.com"

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee("Israel", "Mendoza", 21000)
emp_2 = Employee("Margarita", "Mendoza", 15000)

#print(emp_1)
#print(emp_2)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

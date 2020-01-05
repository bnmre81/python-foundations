

class Employee():
		
	def __init__(self, name, age, salary, employment_year):

		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year

	def __str__(self):
		return ('''
Name: {}, Age: {}, Salary: {}, Working Years: {}'''.format(self.name, self.age, self.salary, self.employment_year))


class Manager(Employee):
	def __init__(self, name, age, salary, employment_year, bonus):
		super().__init__(name, age, salary, employment_year)
		self.bonus = bonus

	def __str__(self):
		return ('''
Name: {}, Age: {}, Salary: {}, Working Years: {}, bonus: {}'''.format(self.name, self.age, self.salary, self.employment_year, self.bonus))
		

menu = '''
Welcome to HR Pro 2020
Options:
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit'''

employees_list = []

managers_list = []


while True:
	print(menu)

	choice = input("What would you like to do? ")
	print('-----------------')
	if choice == '5':
		break
	elif choice == '3':
		name = input('enter name: ')
		age = input("enter age: ")
		salary = input("enter salary: ")
		employment_year = input("enter working years: ")
		emplyee_profile = Employee(name, age, salary, employment_year)
		employees_list.append(emplyee_profile)
	elif choice == '1':
		for item in employees_list:
			print(item)
	elif choice == '4':
		name = input('enter name: ')
		age = input("enter age: ")
		salary = input("enter salary: ")
		employment_year = input("enter working years: ")
		bonus = input("enter Bonus Percentage: ")
		manager_profile = Manager(name, age, salary, employment_year, bonus)
		managers_list.append(manager_profile)
	elif choice == '2':
		for item in managers_list:
			print(item)

	




	
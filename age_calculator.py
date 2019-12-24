import datetime

def check_birthdate(year, month, day):
	birth = datetime.datetime(year, month, day)
	age = (datetime.datetime.now() - birth)
	convert_days = int(age.days)
	convert_years = convert_days // 365
	if convert_years > 0:
		return True
	else:
		return False

def calculate_age(year, month, day):
	birth = datetime.datetime(year, month, day)
	age = (datetime.datetime.now() - birth)
	convert_days = int(age.days)
	convert_years = convert_days // 365
	print("You are " + str(convert_years) + " years old!")

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

if check_birthdate(year, month, day) == True:
	print(calculate_age(year, month, day))
else:
	print("The birthdate is invalid!")

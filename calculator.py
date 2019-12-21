x = input("Enter the first number: ")

if x.isdigit():
	x = int(x)
else:
	print("You must enter a number!")
	exit()

y = input("Enter a second number: ")

if y.isdigit():
	y = int(y)
else:
	print("You must enter a number!")
	exit()

z = input("Choose the operation(+, -, /, *): ")

if z == "+":
	print(x + y)
elif z == "-":
	print(x - y)
elif z == "/":
	print(x / y)
elif z == "*":
	print(x * y)
else:
	print("The operation is not valid!")
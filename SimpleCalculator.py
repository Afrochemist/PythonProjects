#The calculator will incorporate many functions for addition, substraction, multiplicationa dn division


#addition
def addition(p,q):
	return p + q

#substraction
def substraction(p,q):
	return p - q

#multiplication
def multiplication(p,q):
	return p * q

#division
def division(p,q):
	return p / q



#Allowing the user to choose an option
print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")


#Condition statement

while True:
	#Take input from the user
	choice = input("Enter choice(1/2/3/4): ")

	#Check if choice is one of the four options
	if choice in ('1','2','3','4'):
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		
		if choice == '1':
			print(num1, "+", num2, "=", add(num1, num2))

		elif choice == '2':
			print(num1, "-", num2, "=", substract(num1, num2))
		
		elif choice == '3':
                        print(num1, "*", num2, "=", multiplication(num1, num2))
		
		elif choice == '4':
                        print(num1, "/", num2, "=", division(num1, num2))
		break
	else:
		print("Invalid input")


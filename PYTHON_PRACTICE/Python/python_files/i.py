Opretaor = input("Enter what opration to perform (* , + , - , / , **) : ")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if Opretaor == '**' :
	result = num1 ** num2
	print("Exponential of these number : ", result)
elif Opretaor == '/' :
	result = num1 / num2 
	print("Division of these number : ", result)
elif Opretaor == '*' :
	result = num1 * num2 
	print("Multiplication of these number : ", result)
elif Opretaor == '+' :
	result = num1 + num2
	print("Addition of these number : ", result)
elif Opretaor == '-' :
	result = num1 - num2
	print("Diffrence of two number is : ", result)
else:
	print("Invalid Opretaor!")
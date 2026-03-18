num = int(input("Enter a number : "))

if num < 0 :
	print("Factorial of negative number is not possible !")

elif num == 0 :
	print("Factorial of zero is 1 !")

else:
	factorial = 1
	for i in range(1,num+1):
		factorial *= i 
	print(factorial)

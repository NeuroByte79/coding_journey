"""Write a program which can compute the factorial of a given numbers. 
The results should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320"""

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input("Enter number: "))
# print(fact(x))

num =  int(input("Enter a number : "))
if num < 0 :
	print("Factorial of negative number is not possible. ")
elif num == 0:
	print("Factorial of zero is 1.")
else:
	fact = 1
	for i in range(1,num + 1):
		fact *= i
	print("Factorial is : ", fact)
# Armstrong Number in Python - A number where the sum of its digits raised to the power of number of digits equals the number itself

num = int(input("Enter a number : "))

original = num 
sum_digit = 0 
n = len(str(num))
while num > 0 :
	reminder = num % 10
	sum_digit += reminder ** n
	num = num // 10

if original == sum_digit :
	print(original, "is a Armstrong number")
else : 
	print(original,"is a NOT Armstrong number ")

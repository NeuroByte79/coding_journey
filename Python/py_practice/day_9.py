# check positive and negative in python
# 1. Using if-elif-else
num = 10

if num > 0 :
	print("Positive Number")
elif num < 0 :
	print("Negative Number")
else:
	print("Zero")

# 2. Taking user input

num = int(input("Enter a number : "))

if num > 0 :
	print("Positive Number")
elif num < 0 :
	print("Negative Number")
else:
	print("Zero")

# 3. Using a function 

def check_number(n):
	if n > 0 :
		return "Positve Number"
	elif n < 0 :
		return "Negative Number"
	else:
		return "Zero"

print(check_number(10))


# 4. Using nested conditions

num = -7 
if num >= 0 :
	if num == 0 :
		print("Zero")
	else:
		print("Positive Number")
else:
	print("Negative")
# 1. print all natural number from 1 to n using while loop
n = int(input("Enter a number: "))
i = 1    # Start from 1
while i <= n:      # loop run until i becomes greater than n
	print(i)
	i += 1  # Increase by 1 each time




# 2. print all natural number from 0 to n in reverse order using while loop
n = int(input("Enter a number :"))
i = n
while i >= 1:
	print(i)
	i -= 1


# 3. print all alphabets from a to z using while loop
i = ord('a')   # ASCII value of 'a'

while i <= ord('z'):
    print(chr(i))
    i += 1 


# 4. write a program to print all even number between 0 to 100 using while loop
i = 1
while i <= 100:
	if i % 2 == 0:
		print(i)
	i += 1


# 5.  write a program to print all even number between 0 to 100 using while loop
i = 1
while i <= 100:
	if i % 2 != 0:
		print(i)
	i += 1
# 6. find the sum of all natural number from 1 to n
n = int(input("Enter a number : "))
i = 1
total = 0
while i <= n:
	total += i
	i += 1

print("Sum is :", total)


# 7. find the sum of all even or odd natural number between 1 to n sepretely
n = int(input("Enter a number :"))
i = 1
total = 0
while i <= n:
	if n % 2 == 0:
		total += i 
		i += 1

	else:
		total += i 
		i += 1

print("Sum is :", total)















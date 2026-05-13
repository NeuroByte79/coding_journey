# 1. print all prime number in given interval
start = 1
end = 1000
print("prime number between", start, "and", end, "are :")
for i in range (start, end + 1):
	if i > 1:
		for j in range(2,i):
			if(i % j == 0):
				break
		else:
			print(i)




# 2. print squre root of given number
n = int(input("Enter a number : "))
print("Squre is :", n * n)

# 3. print table of a given number 
n = int(input("Enter a number : "))
for i in range (1,11):
	print(i * n)

# 4. programm to add two number 
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
sum = num1 + num2 
print("The sum of two given number is :", sum)

# 5. find factorial of given number
num = int(input("Enter a number : "))
fact = 1
for i in range(1,num + 1):
	fact *= i 
	print(fact)



# 5. write a program to add to matrix
x = [[12,13,14],
     [4,5,6],
     [7,8,9]]

y =  [[12,13,14],
      [4,5,6],
      [7,8,9]]

# Initialize result matrix with same dimensions (3x3)
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Add matrices using nested loops
for i in range(len(x)):
    for j in range(len(x[0])):  # Use len(x[0]) for columns
        result[i][j] = x[i][j] + y[i][j]

# Print result
print("Result matrix:")
for r in result:
    print(r)









































































































































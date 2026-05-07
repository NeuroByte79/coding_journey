# Basic program 

num = int(input("Enter a number : " ))

for i in range(1, 11):
	print(num, "x", i, "=", num * i)


# Custom range table 

start = int(input("Enter a start range :"))
end = int(input("Enter a end range : "))

for i in range(start, end + 1):
	print(num, "x", i, "=", num * i)



# using function 
def multiplication_table(num,upto=10):
	print(f'\nMultiplication Table of {num}')
	print("-"* 25)
	for i in range(1, upto + 1):
		print(f'{num} x {i:2} = {num * i}')
multiplication_table(7)


#Tables of multiple number 

numbers = [7,8,9]

for num in numbers:
	print(f'\nTable of {num}:')
	for i in range(1,11):
		print(f'{num} x {i} = {num * i}')

# Using while loop

i = 1 

while i <= 10 :
	print(num, "x", i, "=", num * i)
	i += 1


























# Increasing trangle pattern
num = int(input("Enter a number : "))

for i in range(num):
	for j in range(1,i+1):
		print(j,end=" ")
	print()
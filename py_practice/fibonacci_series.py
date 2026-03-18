# fibonacci series = Each number is the sum of the two preceding numbers

num = int(input("Enter how many terms : "))
a , b = 0 ,1
print("fabonacci series!")

for i in range(num):
	print(a,end=" ")
	a , b = b , a + b

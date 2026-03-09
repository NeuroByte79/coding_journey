# pattern printing

n = int(input("Enter a number: " ))
for i in range(1,n):
	for j in range(1,n):
		print(j,end=" ")
	print()
print("\n")

# hollow square pattern
for i in range(1,n):
	for j in range(1,n):
		if i == 1 or i == n - 1 or j == 1 or j == n - 1:
		    print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
print("\n")


for i in range(1,n):
	for j in range(1,n):
		print(j%2,end=" ")
	print()
print("\n")


































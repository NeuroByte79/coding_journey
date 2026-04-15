# Square star pattern
n = 8
for i in range(1,n+1):    # rows
	for j in range(8):    # columns
		print("*",end=" ")
	print()
print("\n")


# # Hollow square star pattern
n = 8
for i in range(n):
	for j in range (n):
		if i == 0 or i == n-1 or j == 0 or j == n-1:
			print("*",end=" ")
		else:
		 	print(" ",end=" ")
	print()
print('\n')

# Hollo square pattern with diagonal

n = 5

for i in range(n):
    for j in range(n):
        # Border OR Diagonal condition
        if (i == 0 or i == n-1 or 
            j == 0 or j == n-1 or 
            i == j or 
            i + j == n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print('\n')


# Rhombus star pattren
n = int(input("Enter a number :" ))
for i in range(n):
	# For space
	for j in range(n - i - 1):
		print(" ", end = " ")


	# For star printing
	for j in range(n):
		print("*",end=" ")
	print()
print("\n")


# Hollo rhombus star pattern
n = int(input("Enter a number: "))

for i in range(n):

    # spaces
    for s in range(n - i - 1):
        print(" ", end=" ")

    # stars
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# mirrored Rhombus star pattern
n =int(input("Enter a number: " ))
for i in range(n):
	# leading spaces (increasing)
    for s in range(i):
	    print(" ",end=" ")

		# Star with hollow condition
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*",end=" ")
        else:
        	print(" ", end=" ")

    print()
print("\n")


# Right angle tringle pattern
n = int(input("Enter a number: " ))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n")

# Hollow right angle tringle
n = int(input("Enetr a number: "))

for i in range(1, n + 1):
	for j in range(i):
		if j == 0 or j == i - 1 or i == n:
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
print("\n")

# mirrored right angle tringle 
n = int(input("Enter a number: " ))
for i in range(n,0,-1):
	for j in range(i):
		print("*", end=" ")
	print()










































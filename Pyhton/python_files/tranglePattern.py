# Right angle pattern 
for i in range(1,7):
	print("*  "*i)

print('\n')

# Inverted right angle pattern
for i in range(7,0,-1):
	print("*  "*i)

print("\n")

# pyramid pattern 
for i in range(1,11,2):
	print("* " *i)
print("\n")

# inverted pyramid pattern 
for i in range(11,1,-2):
	print("* " *i)
print("\n")

# Diamond pattern 
for i in range(1,11,2):
	print("*   " *i)
for j in range(5,0,-1):
	print("*   "*j)

# Right angle tringle using numbers
for i in range(0,7):
	print(" ".join(str(x)for x in range(1,i+1)))
print("\n")

# Inverted Right angle tringle using numbers
for i in range(7,0,-1):
	print(" ".join(str(x)for x in range(1,i+1)))































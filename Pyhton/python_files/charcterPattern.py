# Alphabet Matrix Patterns” or “Character Grid Patterns”.
# Pattern 1. (columns increment):
for i in range(ord('a'), ord('h') + 1):
    for j in range(ord('a'), ord('h') + 1):
        print(chr(j),end=" ")
    print()
print("\n")

# Pattern 2. (rows increment):

for i in range(ord('a'),ord('h') + 1):
	for j in range(ord('a'), ord('h') + 1):
		print(chr(i), end=" ")
	print()
print("\n")

# Pattern 3. (reverse rows):

for i in range(ord('h'),ord('a') - 1, -1):
	for j in range(ord('h'), ord('a') - 1, -1):
		print(chr(i), end=" ")
	print()
print("\n")

# Pattern 4. (reverse columns):

for i in range(ord('h'),ord('a') - 1, -1):
	for j in range(ord('h'), ord('a') - 1, -1):
		print(chr(j), end=" ")
	print()



"""Collective Name
Together, these demonstrate “Fixed Alphabet Grid Variations” - specifically:
	•	Horizontal repetition pattern
	•	Vertical repetition pattern
	•	Reverse horizontal pattern"""
print("\n")



row = 5 
for i in range(1 , row + 1):
	print(' ' * (row - i) + '*'* (2 * i - 1))
print("\n")


row = 5 
for i in range(row , 0 ,-1):
	print(' ' * (row - i) + '*' * (2 * i - 1))
print("\n")


row = 5 
for i in range(1 , row + 1):
	print(' ' * (row - i) + '*'* (2 * i - 1))
row = 5 
for i in range(row , 0 ,-1):
	print(' ' * (row - i) + '*' * (2 * i - 1))

print("\n")


























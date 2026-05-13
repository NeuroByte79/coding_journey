# 6 HOLLOW PYRAMID IN PYTHON
row = 5
for i in range(1 , row + 1):
	for j in range(1, 2*row):
		if j == row - i + 1 or j == row + i - 1 or i == row:
			print("*" ,end=" ")
		else:
			print(" " ,end=" ")
	print()
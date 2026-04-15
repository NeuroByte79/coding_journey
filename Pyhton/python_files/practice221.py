# 7 HOLLOW PYRAMID IN PYTHON
n = 4 
size = 2 * n - 1 
for i in range(size):
	for j in range(size):
		value = n - min(i , j , size - i - 1 , size - j - 1)
		print(value,end=" ")
	print()
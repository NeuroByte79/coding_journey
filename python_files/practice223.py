# 5 STAR DIAMOND IN PYTHON
rows= 5

# UPPER HALF
for i in range(1, rows + 1):
	print(" " * (rows - i) + "* " * i)

# LOWER HALF
for i in range(rows - 1 , 0 , -1):
	print(" " * (rows - i) + "* " * i)
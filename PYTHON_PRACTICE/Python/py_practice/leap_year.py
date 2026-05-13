years = int(input("Enter a year : "))

if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
	print("Leap Year")
else:
	print("Not Leap Year")
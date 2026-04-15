num = input("Enter a number : ")

n = len(num)

total = sum(int(d) ** n for d in num)

if int(num) == total :
	print(num ,"is a Armstrong number")
else:
	print(num,"is NOT a Armstrong number")

num = int(input("Enter a number : "))

if num < 2 : 
	print(num , " is NOT prime")
else:
	for i in range(2,num):
		if num % i == 0:
		    print(num ," is NOT prime")
		    break
	else:
		print(num , " is prime") 
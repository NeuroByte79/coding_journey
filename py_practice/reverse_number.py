num = int(input("Enter a number"))
original = num
reverse = 0
while num > 0 :
 	 reminder = num % 10 
 	 reverse = (reverse * 10) + reminder
 	 num = num // 10
print("Reverse of ",original,"=",reverse)
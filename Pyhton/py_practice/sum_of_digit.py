num = int(input("Enter a digit : "))

original_num = num 
sum_of_digit = 0

while num > 0 :
	digit = num % 10 # get last digit
	sum_of_digit += digit # add to sum 
	num  = num // 10   # remove last digit 

print("Sumof digit is", original_num , "=", sum_of_digit)
# palindrome number = A number that read the same forward as well as backward
num = int(input("Enter a number : "))
original = num 
reverse = 0 

while num > 0 :
	reminder = num % 10     # get last digit or reminder
	reverse = (reverse * 10) + reminder     # build reverse 
	num = num // 10     # remove last digit

if original == reverse :
	print(original, "is a palindrome number")
else :
	print(original, "is a NOT palindrome")
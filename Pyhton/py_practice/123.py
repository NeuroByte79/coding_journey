# Palindrome check

num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print(f"{original} is palindrome number !")
else:
    print(f"{original} is not a palindrome number !")



# reverse the enter number

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(f"The reverse number  of {original} is {rev}")


#
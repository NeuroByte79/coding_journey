# version0.1
# Simple calculator
print("@@@@ Welcome to self made calculator $$$$$$ ")
operator = input("Enter operator('+','-','*','/') : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*' :
    result = num1 * num2
elif operator == '/' :
    result = num1 / num2
else:
    print("Invalid choice!\nPlz Enter a valid option.")

print(f'The {operator} is in between the {num1},{num2} is : {result}')
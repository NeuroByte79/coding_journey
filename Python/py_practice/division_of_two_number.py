# Basic methode
a = 10
b = 5
result = a / b
print(result)
print(a/b)

# Taking user input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Division:", a/b)

# using Function

def divide(x,y):
    return x / y
print(divide(10,2))

# using lambda function (one-line function)

divide = lambda x ,y : x/y
print(divide(10,4))


# using operator
import operator
print(operator.truediv(10,5))
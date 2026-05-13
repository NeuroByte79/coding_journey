# Using if-elif-else

print(f"Simple Calculator!")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

operation = input("Enter operation (+,-,*,/) : ")

if operation == "+":
    print("Result : ",num1 + num2)
elif operation == "-":
    print("Result : ",num1 - num2)
elif operation == "*":
    print("Result : ",num1 * num2)
elif operation == "/":
    print("Result : ",num1/num2)
else:
    print("Invalid Choice !")

# Using function
def Simple_cal(num1, num2):
    operation = input("Enter operation (+,-,*,/) : ")
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid Chioce !"


print(Simple_cal(10,2))


# Using lambda function


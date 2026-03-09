# 1. Write a program to print "Hello,World!"

print("Hello, World!")
print("\n")

# 2. Write a program to do arithmetical oprations addition and division

num1 = float(input("Enter number first :"))
num2 = float(input("Enter second number :"))
sum_result = num1 + num2
print(f"sum : {num1} + {num2} = {sum_result}")
print("\n")

num3 = float(input("Enter the dividend for division : "))
num4 = float(input("Enter the divisor for division : "))
if num4 == 0:
	print("Error : Division by zero is not possible")
else:
	div_result = num3 / num4
	print(f"Division : {num3} / {num4} = {div_result}")
print("\n")


# 3. Write a python program to calculate area of triangle.

Base = float(input("Enter the base of triangle : "))
Height = float(input("Enter the height of triangle : "))
result_area = 1/2*(Height * Base)
print(f"Area of triangle is : {result_area} \n")

# 4. Write a python program to swap two number

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(f"Original value : a = {a}, b = {b} ")     # Dispaly the original values
# Swap the values using temporary variable
temp = a 
a = b 
b = temp
print(f"Swapped value : a = {a}, b = {b} \n")      # Dispaly Swapped number  

# 5.Write a python program to generate a random number.

import random
print(f"Random number : {random.randint(1, 100)} \n") # num = random.randint(1,100)


# 6. # Write a program to convert kilometer to miles.

Kilometer = float(input("Enter distance in kilometer : "))
# conversion factor : 1 kilometer  = 0.621371
conversion_factor = 0.621371     # 1.6 kilometer = 1 mile

miles = Kilometer * conversion_factor

print(f"{Kilometer} kilometer is equal to {miles} miles.\n")



# 7. Write a progarm to convert celsius to fahrenheit.

Tem_Celsius = float(input("Enter temperature in celsius : "))
# conversion factor : fahrenheit = (celsius * 9/5) + 32
fahrenheit = (Tem_Celsius * 9/5) + 32
print(f"{Tem_Celsius} degrees celsius is equal to {fahrenheit} fahrenheit degrees. \n")


# 8. Write a python program to display calendar.
import calendar
year  = int(input("Enter year : "))
month = int(input("Enter month  : "))
cal = calendar.month(year, month)
print(cal,"\n")


# 9. Write a python programto to solve quadratic equation.





# 10. Write a python program to swap two number without using one other variable.
a = 5
b = 6
# swapped without a temporary variable
a, b = b, a
print("After swapping : ")
print("a = ",a)
print("b = ",b,'\n')


# 11. Write a python program to check if number is positive , negative or zero.
num = float(input("Enter a nmber : "))
if num > 0 :
    print("Positive number ")
elif  num == 0 : 
	print("Zero")
else:
	print("Negative number")


# 12. Write a python progarm to check number even or odd .

number = int(input("Enter a number : "))
if number % 2 == 0 :
	print("This is a even number ")
else:
	print("This is a odd number")
print("\n")

# 13. Write a python program to check leap year .
year = int(input("Enter a year : "))
# divided by 100 means century years (Ending with 00)
# century year divided by 400 is leap year 
if (year % 400 == 0) and (year % 100 == 0):
	print("{0} is a leap year ".format(year))
# not divided by 100 means not a century year 
# year divided by 4 is a leap year 
elif (year % 4 == 0) and (year % 100 != 0):
	print("{0} is leap year".format(year))
# if not divided by both 400 (century year) and 4 (leap year) 
# year is not a leap year
else:
    print("{0} is not a leap year",format(year))  














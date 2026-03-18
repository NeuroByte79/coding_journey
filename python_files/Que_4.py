""" Write a program which accepts a sequence of
 comma-separated numbers from console and generate a list and a tuple which contains every number.
  Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: 
['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')"""


# Take input from user 
number = input("Enter comma-separated number : ")

# Split by comma to create a list
my_list = number.split(",")

# Convert list to tuple
my_tuple = tuple(my_list)

# print both
print(my_list)
print(my_tuple)
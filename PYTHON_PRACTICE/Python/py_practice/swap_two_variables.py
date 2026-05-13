# Method1 - Using a Temporary variable
a = 5
b = 8

temp = a
a = b
b = temp

print("a = ",a)
print("b = ",b)

# Method2 - Pythonic Way(Tuple Swapping)

a = 13
b = 19

a,b = b, a
print("a = ",a)
print("b = ",b)

# Method3 - Using Addition and Subtraction

a = 5
b = 10

a = a + b
b = a - b
a = a - b
print("a = ",a)
print("b = ",b)

# Method4 - Using Multiplication and Division

a = 23
b = 34
a = a * b
b = a / b
a = a / b
print("a = ",a)
print("b = ",b)
# Income Tax Calculator

# Taking annual income input from user
income = float(input("Enter your Annual Income (₹): "))

tax = 0

# Tax calculation based on slabs
if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

# Adding 4% Health & Education Cess
cess = tax * 0.04
total_tax = tax + cess

# Displaying results
print("\n------ Tax Details ------")
print("Income: ₹", income)
print("Income Tax: ₹", round(tax, 2))
print("Health & Education Cess (4%): ₹", round(cess, 2))
print("Total Tax Payable: ₹", round(total_tax, 2))
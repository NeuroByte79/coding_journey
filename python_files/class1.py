# Write a python program to build an income tax calculator on the basis of anual income of the person,
Anual_income_of_the_person = int(input("Enter Anual Income  : "))
if Anual_income_of_the_person < 250000:
	tax = 0 
elif Anual_income_of_the_person <= 500000:
    tax =  (Anual_income_of_the_person - 250000) * 0.05
elif Anual_income_of_the_person <= 1000000:
	tax = (250000 * 0.05) + (Anual_income_of_the_person - 500000) * 0.2
else:
	tax = (250000 * 0.05) + (500000 * 0.2) + (Anual_income_of_the_person - 1000000) * 0.3
# Additionall income edudition or health 4%
cess = tax * 0.04
total_tax = tax + cess

# Displaying results
print("\n------ Tax Details ------")
print("Income: ₹", Anual_income_of_the_person)
print("Income Tax: ₹", tax)
print("Health & Education Cess (4%): ₹", cess)
print("Total Tax Payable: ₹", total_tax )




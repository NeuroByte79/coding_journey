"""Lab Task (Advance)

Build a Bank Loan EMI & Eligibility System in python on the basis of below case scenario:

A bank wants to automate loan processing.

The system must:
- Take customer details
- Calculate EMI by using EMI formula
- Check loan eligibility
- Display decision with proper formatted output

Eligibility Rules:
- Minimum monthly salary ≥ ₹25,000;
- Maximum EMI allowed = 40% of monthly salary;
- Age must be between 21 and 60
- If EMI > 40% of salary-- Loan Rejected"""




# For customer details 
Monthly_income_of_customer = int(input("Enter monthly income of the customer in ₹ : "))
Age_of_customer = int(input("Enter age : "))
Loan_Amount = int(input("Required Loan Amount :"))
Number_of_monthly_installments = int(input("Time period for payment of installments in month : "))
Monthly_interest_rate = float(input("Interest rate given by bank : "))

if 21 < Age_of_customer < 60:
    if Monthly_income_of_customer >= 25000:  # Confirm your intended logic
        print("Your age and your income is satisfied for Loan.")
        p = Loan_Amount
        n = Number_of_monthly_installments
        r = Monthly_interest_rate
        EMI = (p * r * (1 + r)**n)/((1 + r)**n - 1)
        if EMI < 0.4 * Monthly_income_of_customer:
            print("EMI for your loan amount is :", EMI)
        else:
            print("_____Loan Rejected_____")
    else:
        print("You are not applicable for loan")
        print("Loan Rejected")
else:
    print("*****_____Loan Rejected_____*****\n") 

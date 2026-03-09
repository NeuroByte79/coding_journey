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





# 1. Collect ALL inputs FIRST
Monthly_income_of_customer = int(input("Enter monthly income of the customer in ₹ : "))
Age_of_customer = int(input("Enter age : "))
Monthly_interest_rate = float(input("Interest rate given by bank : ")) 
Loan_Amount = int(input("Required Loan Amount : "))
Number_of_monthly_installments = int(input("Time period for payment of installments in month : "))

# 2. Check eligibility FIRST
if Age_of_customer > 21 and Age_of_customer < 60 and Monthly_income_of_customer >= 25000:
    # 3. Calculate EMI
    p = Loan_Amount
    n = Number_of_monthly_installments
    r = Monthly_interest_rate / 100 / 12  
    EMI = (p * r * (1 + r)**n) / ((1 + r)**n - 1)
    
    # 4. Final EMI check (40% rule)
    if EMI <= 0.4 * Monthly_income_of_customer:
        print(f"✓ LOAN APPROVED")
        print(f"EMI: ₹{EMI:.2f}")
    else:
        print("✗ LOAN REJECTED - EMI exceeds 40% of income")
else:
    print("✗ LOAN REJECTED - Age or Income criteria not met")




















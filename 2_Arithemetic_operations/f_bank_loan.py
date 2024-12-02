"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A   =   final amount
                        P   =   initial principal balance
                        r   =   annual interest rate
                        t   =   time (in years)

Ref: https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php
"""

# Simple Interest Calculation

P = float(input("Enter the initial principal balance (P): "))
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 5% = 0.05): "))
t = float(input("Enter the time (t) in years: "))
A = P * (1 + r * t)
print("The final amount after Simple Interest is: ", A)


# Compound Interest Calculation

P = float(input("Enter the initial principal balance (P): "))
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 5% = 0.05): "))
t = float(input("Enter the time (t) in years: "))
n = int(input("Enter the number of times interest is compounded per year (n): "))
A = P * (1 + r/n)**(n * t)
print("The final amount after Compound Interest is: ", A)
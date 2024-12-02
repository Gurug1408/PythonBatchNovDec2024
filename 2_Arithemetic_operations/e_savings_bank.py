"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create a variable 'balance' with initial value 0
Step 2: Initial Deposit of minimum balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

balance = 0
balance += 1500  
print("Balance after Initial Deposit:", balance)
salary = 3300
balance += salary 
print("Balance after Salary Credited:", balance)
online_purchase = 33.33
balance -= online_purchase 
print("Balance after Online Purchase:", balance)
house_rent = 1500
balance -= house_rent 
print("Balance after House Rent Paid:", balance)
print("Final Balance:", balance)
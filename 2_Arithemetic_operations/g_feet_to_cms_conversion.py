"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet value in runtime
Step 2: Compute from feet to centimeters
            - Convert feet to inches, then
            - Convert inches to centimeters
Step 3: Display the results
"""

feet = float(input("Enter the value in feet: "))
inches = feet * 12  
centimeters = inches * 2.54 
print(f"{feet} feet is equal to {centimeters} centimeters.")
"""
Purpose: short-circuit logic
"""

expr3 = 0 and 5  
print("expr3=", expr3)

expr4 = 6 and 2  
print("expr4=", expr4)

expr4 = 8 and 4 and 16  
print("expr4=", expr4)

expr4 = 7 and 18 and 5  
print("expr4=", expr4)  
print()

expr5 = 0 or 6  
print("expr5=", expr5)

expr6 = 8 or 2  
print("expr6=", expr6)

expr6 = 4 or 9 or 11  
print("expr6=", expr6)

expr6 = 14 or 8 or 2  
print("expr6=", expr6)  

expr6 = 0 or 0 or 7 or 5  
print("expr6=", expr6)  
int()

# and - returns 0 if anyone is 0; else the last value
print(f"{0 and 6 and 7 and 3 = }")  
print(f"{1 and 3 and 5 and 9 = }")  
print(f"{1 and 2 and 0 and 5 = }")  
print(f"{2 and 4 and 7 = }")  
print()

# or - will take the first boolean True value
print(f"{0 or 3 or 7 or 9 = }")  
print(f"{2 or 4 or 5 or 6 = }")  
print(f"{3.3 or 4 or 5 or 6 = }")  
print()

print(f"{0 or 4 and 6 or 2 = }")  
print(f"{0 or (3 and 6) or 2 = }")  
print()

num1 = 125

num1 > 0 and num1 <= 0 and num1 != 0  
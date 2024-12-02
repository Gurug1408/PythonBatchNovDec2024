"""
Purpose: Logical Operations
    - Will result in a boolean value (True or False)

    and - if  all are True, result is True
    or  - if any one of them is True, result is True
    not - negate the existing value
"""

print("\n and operation ")
print("True and True  ", True and True) 
print("True and False ", True and False)
print("False and True  ", False and True)
print("False and False ", False and False)
print()

print("\n or operation ")
print("True or True  ", True or True)
print("True or False ", True or False)
print("False or True  ", False or True)
print("False or False ", False or False)  
print("\n not operation ")
print("not True ", not True)
print("not False", not False)
print("not not True = ", not not True)
print("not not False = ", not not False)
print()



print(
    "not not not not not not not not not not not not True",
    not not not not not not not not not not not not True,
)
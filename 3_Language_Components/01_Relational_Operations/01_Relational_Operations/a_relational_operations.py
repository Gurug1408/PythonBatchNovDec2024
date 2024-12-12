#!/usr/bin/python3
# print(f"{us_dollar <> canadian_dollar = }")  # works only in python 2.x
"""
Purpose: Relational Operations
    - These operations will result in a boolean value (True or False)

     <  lesser
     >  greater
     == equal to
     <= less than or equal to
     >= greater than or equal to
     != not equal to
     <> not equal to  ( in python 2 only)
"""

us_dollar = 84
canadian_dollar = 78

print("us_dollar        = ", us_dollar)
print("canadian_dollar  = ", canadian_dollar)
print()

print(f"us_dollar       = {us_dollar}")
print(f"canadian_dollar = {canadian_dollar}")
print()

print(f"{us_dollar      =}")
print(f"{canadian_dollar=}")
print()

print("us_dollar == canadian_dollar:", us_dollar == canadian_dollar)
print(f"{us_dollar == canadian_dollar = }")

print(f"{us_dollar > canadian_dollar  = }")
print(f"{us_dollar >= canadian_dollar = }")
print(f"{us_dollar < canadian_dollar  = }")
print(f"{us_dollar <= canadian_dollar = }")
print(f"{us_dollar != canadian_dollar = }")



print()
print(f"{78 == 50 =}")
print(f"{78 != 50 =}")
print(f"{78 >  50 =}")
print(f"{78 >= 50 =}")
print(f"{78 <  50 =}")
print(f"{78 <= 50 =}")
print()


num1 = 50 

num1 = 50
num2 = num1

num1 == 50
50 == num1
50 == 50
50 == 67
print()

str1 = "abc"
str2 = "abc"
print(f"{str1 == str2 =}")
print(f"{str1 >  str2 =}")
print(f"{str1 >= str2 =}")
print(f"{str1 <  str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 != str2 =}")
print()

str1 = "abc"
str2 = "bc"
print(f"{str1 == str2 =}")
print(f"{str1 >  str2 =}")
print(f"{str1 >= str2 =}")
print(f"{str1 <  str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 != str2 =}")
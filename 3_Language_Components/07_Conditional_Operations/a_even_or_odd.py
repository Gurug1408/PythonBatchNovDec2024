# Purpose: Check if a number is even or odd

number = 33
print(f"number = {number}")
print(f"number / 2 = {number / 2}")
print(f"number % 2 = {number % 2}")
print(f"number % 2 == 0 = {number % 2 == 0}")

# Check if the number is non-zero
if number != 0:
    print(f"{number} is non-zero")

if number:
    print(f"{number} is non-zero")  # Checks if the number is not 0, None, or False

# Even or odd check
if number % 2 == 0:
    print(f"{number} is Even")

if number % 2 != 0:
    print(f"{number} is Odd")

# --------------------
print()  # Line break for readability

number = 13
print(f"number = {number}")
print(f"number % 2 = {number % 2}")
print(f"number % 2 == 0 = {number % 2 == 0}")

# Check even or odd for number = 13
if number % 2 != 0:
    print(f"{number} is Odd")

if number % 2 == 0:
    print(f"{number} is Even")

# --------------------
# Simplified check with else
if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# Alternate check
if number % 2 != 0:
    print(f"{number} is ODD")
else:
    print(f"{number} is EVEN")

# --------------------
# Assignment: Print even numbers between 45 and 137
for num in range(45, 138): 
    if num % 2 == 0: 
        print(f"{num} is Even")
"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""

import sys

i = 0
while i <= 7:
    i += 1
    print(i, end=" ")


print("\n importance of break")
i = 0
while i <= 7:
    i += 1
    if i != 2 and i % 2 == 0:
        break
    print(i, end=" ")


print("\n importance of continue")
i = 0
while i <= 7:
    i += 1
    if i != 2 and i % 2 == 0:
        continue
    print(i, end=" ")


print("\n importance of pass")
i = 0
while i <= 7:
    i += 1
    if i % 2 == 0:
        pass  # It acts as a placeholder
    print(i, end=" ")

def myfunc():
    pass

class Myclass:
    pass 


print("\nimportance of sys.exit")
i = 0
while i < 7:
    i += 1
    if i % 2 == 0:
        sys.exit(0)
    print(i, end=" ")


# exit code 0 - successful/normal termination
# exit code non-zero - abnormal termination
print("next statement")

# Assignment: Try these break, continue, pass, on a for loop example

#Break
print("\nExample of break in a for loop:")
for i in range(1, 11):  # Loop from 1 to 10
    if i == 6:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i equals 6
    print(i, end=" ")

#Continue
print("\nExample of continue in a for loop:")
for i in range(1, 11):  # Loop from 1 to 10
    if i % 2 == 0:  # Skip even numbers
        continue  # Skip the iteration for even numbers
    print(i, end=" ")

#Pass
print("\nExample of pass in a for loop:")
for i in range(1, 11):  # Loop from 1 to 10
    if i == 5:  # Just a placeholder when i equals 5
        pass  # Does nothing for i = 5
    else:
        print(i, end=" ")
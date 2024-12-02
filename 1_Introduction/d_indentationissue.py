"""
Purpose: Importance of Indentation - 4 spaces is a constant 
"""

print("Hello world 1")
#  print("Hello world 2")  # IndentationError: unexpected indent
print("Hello world 2")
print("Hello world 3")


# block code - if, else, elif, for, while, def , class, ...
# if 18 > 5:
# print('12 is greater than 3')
# IndentationError: expected an indented block after 'if' statement on line 11
# tabs vs white-space
# PEP 8 (Python Enhancement Proposal) - code style guide
# Prefer white-spaces, to tabs; four white-spaces

if 18 > 5:
    print("12 is greater than 3")


if 18 > 40:
    print("greater")
else:
    print("It is lesser")


if 11 < 22:
    print("case 1")
elif 22 > 11:
    print("case 2")
else:
    print("case 3")


if 11 < 22:
    if 22 < 33:
        if 33 < 44:
            if 44 < 55:
                print("LESS NUMBER")
            else:
                print("OTHER")
        else:
            print("OTHER")
    else:
        print("OTHER")


for i in range(9):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, "*", j, "=", i * j)
        j += 1
    print()
    i += 1


def my_func():
    return "hello world"


class MyClass:
    def __init__(self):
        pass

#!/usr/bin/python3  - commenting in usr drive of linux
"""
Purpose: Basic PEP 8 guidelines and 
       shebang line


    PEP - Python Enhancement Proposal
    PEP 8 - coding style guide

This is docstring

"""

# print as a statement in python 2  - no need of parenthesis
# print "Hello world!"
# print as a function in python  2 & 3

print("Hello world!")
print(True)
print("True", 123, None)

def wishes(name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("Udhay")

def వందనాలు(పేరు):
    వందనం = "మీరు ఎలా ఉన్నారు {0}?".format(పేరు)
    print(వందనం)

వందనాలు("పేరు")
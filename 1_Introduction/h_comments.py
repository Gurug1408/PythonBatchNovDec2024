#!/usr/bin/python3
"""
Purpose: Working with comment operator
    - Once # is encountered, complete line from that position is ignored
    - PEP 8 recommends one white space after # operator
    - comments
        - Single Line comment  #
        - Multi-line comment - Python doesn't support
Python dont have multi-line comment operator because it is a interpreter based language, means each line executes separately
Python code --> line by line -> c code  -> asssembly -> Machine
ctrl + / - multi-line comment/uncomment

"""
'''
Used to handle multi-line strings or in cases where multiple single and double quotes are present in string

'''


"""
used for docstrings

ex: print 'Hello World8'
"""

# print('Hello world3')
# any operator within quotes with be treated as ordinary character
# print('Hello world8'#)
# SyntaxError: '(' was never closed
# sldkjlkdj;wl kf'w;  dp'kwf';e kr'!@#$%^&*()


print('Hello world1')
print('Hello world2')


print("Hello #world4")
print("Hello", "world5", sep="#")

print("Hello world6")  
print("Hello world7")  

print("Hello world7")

"""
Purpose: print() function syntax and usage
"""
# NOTE: Python is dynamic typed language

name = "Almighty"

print("name =", name)
print("Name of student is name")
print("Name of student is" +  name)
print("Name of student is " +  name)
print()

# Str
print("Name of student is", name)
print("Name of student is", name, sep=" ")
print("Name of student is", name, sep="-")
print("Name of student is", name, sep="")
print()

#   Default sep
print(1, 2, 3, 4, 5, 6)
print(1, 2, 3, 4, 5, 6, sep=" ")
print()
print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="_")
print(1, 2, 3, 4, 5, 6, sep=":")
print()

name = 1232
print("Name of Student is", name)

# str with int
# print('Name of Student is'+ name)
# TypeError: can only concatenate str (not "int") to str

# NOTE: Python is a strictly typed language
# int addition
print("1 + 2        =", 1 + 2)
# string concatenation
print("'1' + '2'    =", "1" + "2")
print()

# 1 + '2' 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# type converters - str(), int(), float()

print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")

print()
print("int('234')   =", int("234"))

# print("int('23.4')  =", int('23.4')) 
# ValueError: invalid literal for int() with base 10: '23.4'
# print("int('two')  =", int('two')) 
# ValueError: invalid literal for int() with base 10: 'two'


print("Name of Student is" + str(name))
print("Name of Student is" + " " + str(name))
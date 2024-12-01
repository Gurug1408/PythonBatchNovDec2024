"""
Purpose: Python is a dynamic Typed Language.
    Progamming Languages
        - Classficiation
            1. Static-Typed Languages
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            2. Dynamic Typed Languages
                 - create when you need. No declaration needed
                    num1 = 123
                 - line or block based execution

    python code -> pytohn byte code -> pythonInterpreter -> c compiler -> machine
    so, python is slower compared to compiler based languages

"""
# NOTE: Strings need to be declared in quotes

num1 = 1
type(num1)

print(type(num1))

print(num1)
print("num1")

print("num1", num1)
print("num1 =", num1)

print("num1 =", num1, "type =", type(num1))

# works in both static and dynamic typing
num1 = 3
print("num1 =", num1, "type =", type(num1))  # int


# Python is a dynamic-typed language
num1 = 3.0
print("num1 =", num1, "type =", type(num1))  # float

num1 = 3.
print("num1 =", num1, "type =", type(num1))  # float


num1 = 3,
print("num1 =", num1, "type =", type(num1))  # Tuple


num1 = (3,)
print("num1 =", num1, "type =", type(num1))  # Tuple

print()

num1 = 3.0
print("num1 =", num1, "type =", type(num1))  # float

num1 = -0.01
print("num1 =", num1, "type =", type(num1))  # float

num1 = -0.01j
print("num1 =", num1, "type =", type(num1))  # complex
print()

num1 = "3"
print("num1 =", num1, "type =", type(num1))  # string

num1 = "three"
print("num1 =", num1, "type =", type(num1))  # string
print()

num1 = True
# num1 = true  # PYTHON IS A CASE-SENSITIVE LANGUAGE
print("num1 =", num1, "type =", type(num1)) 

num1 = False
print("num1 =", num1, "type =", type(num1))  # bool

num1 = None
print("num1 =", num1, "type =", type(num1))  # none

num1 = "NONE"
print("num1 =", num1, "type =", type(num1))  # string

num1 = "none"
print("num1 =", num1, "type =", type(num1))  # string

vowels = "aeiou"
char = input("Enter a character: ")

# Algorithm:
# 1) Check if input is empty
# 2) Check if it is an alphabet
# 3) Check if it's a vowel or consonant

if len(char) == 0:
    print("No input provided.")
elif not char.isalpha():
    print("Invalid input. Please enter an alphabet.")
elif char.lower() in vowels:
    print(f"{char} is a vowel.")
else:  
    print(f"{char} is a consonant.")
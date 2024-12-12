#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check for a sentence

    Palindrome sentences
        - "A man a plan a canal Panama"
        - "Was it a car or a cat I saw?"

Algorithm:
-----------
Step 1: Take the sentence as input from the user.
Step 2: Remove any spaces and convert the string to lowercase for case-insensitive comparison.
Step 3: Reverse the string.
Step 4: Compare the original and reversed strings to check if they are the same.
Step 5: Display whether the sentence is a palindrome or not.
"""


test_string = input("Enter any sentence: ")
print("Original test_string    :", test_string)

processed_string = test_string.replace(" ", "").lower()
print("Processed string         :", processed_string)

reverse_string = processed_string[::-1]
print("Reversed processed string:", reverse_string)

if processed_string == reverse_string:
    print(test_string, "is a palindrome")
else:
    print(test_string, "is NOT a palindrome")

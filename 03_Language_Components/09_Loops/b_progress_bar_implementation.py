#!/usr/bin/python3
"""
Purpose: Progress Status Bar Implementation

    Escape Sequences:
        \t - tab space
        \n - new line
        \r - carriage return
"""

print("Udhay Prakash")
print("Udhay\tPrakash")
print("Udhay\nPrakash")
print()

print("Udhay\rPrakash")  # change 'Udhay' with 'Prakash'
print("Prakash\rUdhay")  # change 'Prakash' with 'Udhay'

print("1234567890\rDOG")  # Replaces '1234567890' with 'DOG'
print("abcdef\r123")  # Replaces 'abcdef' with '123'

data_set = range(-100, 10_00_000) 
data_set_length = len(data_set)  

for loop_index, _ in enumerate(data_set):
    percent_completed = (loop_index / data_set_length) * 100  
    percent_completed = round(percent_completed, 2)  

    print(f"\r[{ '*' * int(percent_completed // 10):<10}] {percent_completed}% completed", end="")

    #Assignment

   def print_progress_bar(percentage):
    bar_length = 10  # Length of the progress bar (number of '*' characters)
    num_stars = int(percentage // 10)  # Calculate how many '*' to print based on percentage (10% per star)
    print(f"[{'*' * num_stars:<{bar_length}}] {percentage}% completed")

# Simulate progress bar from 0% to 100% in increments of 10%
for i in range(0, 101, 10):
    print_progress_bar(i)
#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


temp_input = input("Enter temperature (e.g., 23C, 23F): ").strip()

if temp_input[-1].upper() == 'C':  
    try:
        celsius = float(temp_input[:-1])  
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    except ValueError:
        print("Invalid input. Please enter a valid number with C for Celsius.")
elif temp_input[-1].upper() == 'F':  
    try:
        fahrenheit = float(temp_input[:-1]) 
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    except ValueError:
        print("Invalid input. Please enter a valid number with F for Fahrenheit.")
else:
    print("Invalid input. Please specify the unit (C or F).")
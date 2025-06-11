"""
Author:  Ryan Rooney
Date written: 6/9/2025
Assignment:   Module 1 Programming Assignment Part 1.
Short Desc:   Write a program that converts Celsius temperatures to 
Fahrenheit temperatures.

"""

celsiusInput = int(input("Enter a temperature in celsius: ")) # user input for celsius
celsiusF = 9/5 * celsiusInput + 32 # celsius to fahrenheit calculation
print(f"The temperature is {celsiusF}°F.")
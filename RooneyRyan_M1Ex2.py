"""
Author:  Ryan Rooney
Date written: 6/9/2025
Assignment:   Module 1 Programming Assignment Part 2.
Short Desc:   Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food, then calculate the 
amounts of a 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total.

"""

foodCharge = int(input("Please enter the total food charge: "))

salesTax = foodCharge * 0.07 # sales tax calculation
print(f"Sales tax amount: ${salesTax}.")

tip = foodCharge * 0.18 # tip calculation
print(f"Tip amount: ${tip}.")

total = foodCharge + salesTax + tip # total calculation
print(f"The total is: ${total}.")
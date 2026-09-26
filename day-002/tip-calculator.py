# AUTHOR: Casey Jones
# CREATED: 9/25/2026
# PROJECT: Udemy - 100 Days of Python - Day 002 - Tip Calculator

# This program prompts the user to input the bill total and the percent amount they would like to tip.
# It then divides the amount by the number of people to give the total each person owes.
# Tax is not factored into this calculator.

# Program Title
print("|| Welcome to the Tip Calculator ||\n")

# User input prompts
bill_total = float(input("What was the total bill amount? "))
tip_amount = float(input("How much would you like to tip? "))
tip_amount_converted = float(tip_amount / 100)
split_amount = int(input("How many people are in your party?"))

# Program performs calculations
total_with_tip = bill_total * tip_amount_converted + bill_total
each_person = total_with_tip / split_amount

# Program displays results
print("\n*************************************")
print(f"The bill total with tip is: ${total_with_tip:.2f}")
print(f"Each person should pay: ${each_person:.2f}")
print("**************************************")
"""
Project: Hello Profile
Chapter: 01 - Running Python & Basic Expressions
Author: Kenneth Imade
Description:
    Convert miles to kilometers using variables.
Concepts:
    - interpreter, scripts, print, arithmetic
"""

miles = float(input("Provide the distance in miles: "))
kilometers = miles * 1.60934

print(f"{miles} miles is equal to {round(kilometers, 2)} km")

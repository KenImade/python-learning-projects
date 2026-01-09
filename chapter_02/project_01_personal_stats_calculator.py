"""
Project: Personal Stats Calculator
Chapter: 02 - Variables, Types, Operators
Author: Kenneth Imade
Description:
    User provides information such as their height and its printed in the terminal.
Concepts:
    - int, float, str, bool, comparisons
"""

age = int(input("How old are you?: "))
height = float(input("How tall are you? (Provide answer in feet): "))

print(f"You are currently {age * 12} months old.")
print(f"You are {round(height * 30.48, 2)} cm tall.")

"""
Project: Temperature Converter
Chapter: 02 - Variables, Types, Operators
Author: Kenneth Imade
Description:
    Converts Celsius to Farenheit.
Concepts:
    - int, float, str, bool, comparisons
"""

temperature = float(input("What is the temperature in Celsuis?: "))

degree = "\u2070"

farenheit = (temperature * 9 / 5) + 32

print(f"{temperature}{degree}C is {float(round(farenheit, 2))}{degree}F")

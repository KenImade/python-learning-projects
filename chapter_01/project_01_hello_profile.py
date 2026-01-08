"""
Project: Hello Profile
Chapter: 01 - Running Python & Basic Expressions
Author: Kenneth Imade
Description:
    User provides information and its printed in the terminal.
Concepts:
    - interpreter, scripts, print, arithmetic
"""

user_info = input("What is your name?: ")
goal = input("What is your goal?: ")
date = input(
    "What date do you plan on achieving this goal? "
    "(Write your date in this format 09 January 2026)"
)

print(
    f"Hi {user_info}, your goal is '{goal}' by '{date}'. Goodluck ;) you've got this."
)

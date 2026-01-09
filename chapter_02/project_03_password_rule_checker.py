"""
Project: Password Rule Checker (no loops)
Chapter: 02 - Variables, Types, Operators
Author: Kenneth Imade
Description:
    Checks if a password follows the below rules.
        1. The password must be at least 8 characters long.
        2. The password must contain at least one digit (0–9).
        3. The password must contain at least one of these characters: @ or #.

    Constraints:
        1. Do not use loops (for, while).
        2. Do not use functions.
        3. Use only basic string operations, comparisons, and logical operators.
Concepts:
    - int, float, str, bool, comparisons
"""

print("Hi there and welcome to the password checker.")
print(
    "The password you choose must follow the below rules: \n"
    "1. The password must be at least 8 characters long.\n"
    "2. The password must contain at least one digit (0-9)\n"
    "3. The password must contain at least one of these characters: @ or #\n"
)
password = input("Provide a password: ")

has_digit = (
    "0" in password
    or "1" in password
    or "2" in password
    or "3" in password
    or "4" in password
    or "5" in password
    or "6" in password
    or "7" in password
    or "8" in password
    or "9" in password
)

if (
    len(password) < 8
    or (password.count("@") < 1 and password.count("#") < 1)
    or has_digit is False
):
    print("The password is invalid.")
else:
    print("The password is valid.")

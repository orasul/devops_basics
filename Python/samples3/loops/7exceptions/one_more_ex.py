#!/usr/bin/python3
"""
Базовый синтаксис
"""

try:
    num = 1/float(input("\nEnter a number: "))
    raise ZeroDivisionError
except ValueError:
    print("That was not a number!")
except ZeroDivisionError:
    print("That was 0 number!")
else:
    print("You entered the number", num)

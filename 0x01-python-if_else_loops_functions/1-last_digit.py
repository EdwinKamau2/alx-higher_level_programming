#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    last_digit < 6 != 0
    print(f"Last digit of {number} is {last_digit} and not 0")

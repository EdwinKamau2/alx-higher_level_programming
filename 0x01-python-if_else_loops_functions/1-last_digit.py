#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if 0 > number:
    last_digit = ((number * (-1)) % 10) * -1
else:
    last_digit = number % 10

print(f"Last digit of {number} is {last_digit} ", end="")

if last_digit == 0:
    print("and is 0")
elif last_digit < 6:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")

#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        digit1 = number % 10
    else:
        digit1 = number % -10
        digit1 *= -1

    print("{:d}".format(digit1), end='')
    return (digit1)

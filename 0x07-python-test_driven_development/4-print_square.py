#!/usr/bin/python3
"""
    Is the print_square module
"""


def print_square(size):
    """ Prints a square with a certain size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    print(f"{('#' * size + chr(10)) * size}", end="")

#!/usr/bin/python3
"""
    the 3-say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """ Is a Function that prints a name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

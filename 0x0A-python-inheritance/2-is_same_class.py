#!/usr/bin/python3
"""
    2-is_same_class module
"""


def is_same_class(obj, a_class):
    """ This Checks if the object is an instance of a_class and return boolean """
    return type(obj) is a_class

#!/usr/bin/python3
"""
    base_geometry module
"""


class BaseGeometry:
    """ The BaseGeometry class """

    def area(self):
        """ This Returns the area (not implemented) """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Is a Function that validates a value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

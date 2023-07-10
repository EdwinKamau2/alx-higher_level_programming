#!/usr/bin/python3
"""
    rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The Rectangle class """

    def __init__(self, width, height):
        """ This Initializes an instance of Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

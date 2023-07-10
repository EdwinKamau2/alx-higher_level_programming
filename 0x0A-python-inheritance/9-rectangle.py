#!/usr/bin/python3
"""
    rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Is the Rectangle class """

    def __init__(self, width, height):
        """ This Initializes an instance of Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ This Returns the area """
        return self.__width * self.__height

    def __str__(self):
        """ This Returns the description of a rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"

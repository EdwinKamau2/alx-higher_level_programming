#!/usr/bin/python3
"""
    square module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initializes an instance of Square class """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area """
        return self.__size ** 2

    def __str__(self):
        """ Returns the description of a square """
        return f"[Square] {self.__size}/{self.__size}"

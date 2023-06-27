#!/usr/bin/python3

""" is a class that Defines Square class """


class Square:
    """ Initializes a square

    Args:
        size (int): size of new square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    """ Sets and checks if the size of the new square is valid

    Args:
        value (int): size of new square
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Returns the current area of the new square """
    def area(self):
        return self.__size ** 2

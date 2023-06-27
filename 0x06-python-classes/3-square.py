#!/usr/bin/python3

""" Class square that Defines Square class """


class Square:
    """ Initializes and checks if the size of the new square is valid

    Args:
        size (int): size of new square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Returns the current area of the new square """
    def area(self):
        return self.__size ** 2

#!/usr/bin/python3
""" Defines asquare class """


class Square:
    """ Initializes a square
    Args:
        size (int): size of new square
        position (int): position of new square
    """

    def __init__(self, size=0, position=(0, 0)):
        if isinstance(position, tuple) and len(position) == 2:
            for value in position:
                if not isinstance(value, int) or value < 0:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, int) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (value)

    def area(self):
        """ Returns the current area of the new square """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square """
        if self.size > 0 and self.position[1] > 0:
            for _ in range(self.position[1]):
                print()

        if self.size != 0:
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
        else:
            print()

#!/usr/bin/python3

""" This Defines Rectangle class """


class Rectangle:
    """ Defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle
        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of new rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of new rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the new rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of the new rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Prints the new rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n")
                * self.__height).strip("\n")

    def __repr__(self):
        """ Returns the representation of the new rectangle """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Prints a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares and returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance """
        return cls(size, size)

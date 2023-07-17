#!/usr/bin/python3
"""
    Is the rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """ Is Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This Initializes an instance of Rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Is Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Is Setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Is Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Is Setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Is Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Is Setter for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Is Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Is the Setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This Returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ This Prints the Rectangle instance with the character # """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ This Returns details about the Rectangle instance """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ This Assigns an argument to each attribute """
        if args and args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "width":
                    self.width = kwargs.get(key)
                if key == "height":
                    self.height = kwargs.get(key)
                if key == "x":
                    self.x = kwargs.get(key)
                if key == "y":
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """ This Returns the dictionary representation of a Rectangle """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

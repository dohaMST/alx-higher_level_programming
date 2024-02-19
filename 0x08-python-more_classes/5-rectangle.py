#!/usr/bin/python3
"""defining the rectangle class"""


class Rectangle:
    """representing the rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height != 0 and self.width != 0):
            return 2 * (self.height + self.width)
        return 0

    def __str__(self):
        if (self.width == 0 or self.height == 0):
            return ""
        return ((("#" * self.width) + '\n') * self.height)[:-1]

    def __repr__(self):
        """Print the rectangle using eval"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")

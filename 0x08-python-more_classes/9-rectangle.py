#!/usr/bin/python3
"""Create a Rectangle class."""


class Rectangle:
    """Rectangle(width, height)"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size."""
        return (cls(size, size))

    def __str__(self):
        if (self.width == 0 or self.height == 0):
            return ""
        string = ""
        for i in range(self.height):
            string += (str(self.print_symbol) * self.width)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Print the rectangle using eval"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return (rect_2)

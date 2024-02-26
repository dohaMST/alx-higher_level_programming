#!/bin/usr/python3
"""importing the base"""
from models.base import Base
"""defining the class"""


class Rectangle(Base):
    """representing the class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """the new rectangle."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """to get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """to set x"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """to set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """it returns the area"""
        return self.width * self.height

    def display(self):
        """printing the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """representing the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y,self.width, self.height)

    def update(self, *args, **kwargs):
        """updating the values of rectangle"""
        if args and len(args) != 0:
            x = 1
            for arg in args:
                if x == 1:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 2:
                    self.width = arg
                elif x == 3:
                    self.height = arg
                elif x == 4:
                    self.x = arg
                elif x == 5:
                    self.y = arg
                x += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val


    def to_dictionary(self):
        """representing the rectangle by dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

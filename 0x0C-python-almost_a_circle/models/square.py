#!/usr/bin/python3
"""defining the class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """representing the class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """to get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """to set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating the values of square"""
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def __str__(self):
        """representing the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)

    def to_dictionary(self):
        """representing the square by dictionary"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

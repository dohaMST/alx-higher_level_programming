#!/usr/bin/python3
'''defining the class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''representing the class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''the constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''representing the class: string info about this class'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''get the size'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''updating instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''updating the instances'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''dict representation for the class'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

#!/usr/bin/python3
""" Write The Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ _Init_ """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Size """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update """

        if len(args) == 0:

            for key, val in kwargs.items():
                self.__setattr__(key, val)

            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

    def __str__(self):
        """ _STR_ """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """ To Dictionary """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}

#!/usr/bin/python3
""" Write a class Square that inherits from Rectangle(9-rectangle.py) """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size):
        """ Initialize """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

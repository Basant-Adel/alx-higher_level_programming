#!/usr/bin/python3
"""
A funcyion to Write a class Rectangle
that defines a rectangle
by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ 0-rectangle """

    def __init__(self, width=0, height=0):
        """
        The instance method called when
        a class is called for the first time
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Private instance attribute: width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width must be an integer,
        otherwise raise a TypeError exception
        with the message width must be an integer
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Private instance attribute: height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height must be an integer,
        otherwise raise a TypeError exception
        with the message height must be an integer
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

#!/usr/bin/python3
"""
A function to Write a class Rectangle
that defines a rectangle
by: (based on 2-rectangle.py)
"""


class Rectangle:
    """ 3-rectangle """

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

    def area(self):
        """
        Public instance method: def area(self):
        that returns the rectangle area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Public instance method: def perimeter(self):
        that returns the rectangle perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Instance method that prints an “informal”
        and nicely printable string representation of an instance
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []

        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]

            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))

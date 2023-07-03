#!/usr/bin/python3
"""
A function to Write a class Rectangle
that defines a rectangle
by: (based on 4-rectangle.py)
"""


class Rectangle:
    """ 5-rectangle """

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

        return (self.height * self.width)

    def perimeter(self):
        """
        Public instance method: def perimeter(self):
        that returns the rectangle perimeter
        """

        if self.height == 0 or self.width == 0:
            return (00)
        return (2 * (self.height + self.width))

    def __str__(self):
        """
        Instance method that prints an “informal”
        and nicely printable string representation of an instance
        """

        if self.height == 0 or self.width == 0:
            return ("")
        s = (self.width * "#" + "\n") * (self.height - 1) + (self.width * "#")
        return (s)

    def __repr__(self):
        """
        Instance method that prints an “official”
        string representation of an instance
        """

        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        Instance method that removes the last character of an instance
        """

        print("Bye rectangle...")

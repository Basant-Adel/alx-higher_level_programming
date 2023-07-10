#!/usr/bin/python3
""" 9-rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle """

    def __init__(self, width, height):
        """
        Write a class Rectangle that inherits from BaseGeometry
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ AREA """
        return self.__width * self.__height

    def __str__(self):
        """ Return-> STR-> The following rectangle description """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

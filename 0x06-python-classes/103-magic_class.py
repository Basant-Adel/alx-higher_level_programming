#!/usr/bin/python3
""" Math """

import math


class MagicClass:
    """ Magic Class """

    def __init__(self, radius=0):
        """ Init """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """ Area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Math """
        return 2 * math.pi * self.__radius

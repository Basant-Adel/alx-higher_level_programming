import math


class MagicClass:
    """ Magic Class """
    def __init__(self, radius):
        self.__radius = 0

        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """ Area """
        return self.__radius * self.__radius * math.pi

    def circumference(self):
        """ Math"""
        return 2 * math.pi * self.__radius

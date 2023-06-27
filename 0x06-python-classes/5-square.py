#!/usr/bin/python3
""" Defines Square """


class Square:
    """ Square """

    def __init__(self, size=0):
        """
            Private instance attribute: size

        """
        self.size = size

    @property
    def size(self):
        """ Size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Area """
        return self.__size * self.__size

    def my_print(self):
        """ Print # """

        for i in range(self.size):
            print("#" * self.size)

        if self.size == 0:
            print()

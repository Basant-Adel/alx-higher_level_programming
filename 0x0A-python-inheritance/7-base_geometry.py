#!/usr/bin/python3
"""
Write a class BaseGeometry
(based on 6-base_geometry.py)
"""


class BaseGeometry:
    """
    Base Geometry
    """

    def area(self):
        """
        method not implemented yet
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        you can assume name is always a string
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

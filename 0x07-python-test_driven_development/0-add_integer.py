#!/usr/bin/python3
"""
Write A function to add 2 integers
"""


def add_integer(a, b=98):
    """ Add Integer """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """
    Returns an integer -> the addition of a and b
    """
    a = int(a)
    b = int(b)
    return (a + b)

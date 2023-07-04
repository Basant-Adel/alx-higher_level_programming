#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Matrix Divided
    """

    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError()
    if len(matrix) == 0:
        raise TypeError(m)
    if not isinstance(matrix[0], list):
        raise TypeError(m)
    if len(matrix[0]) == 0:
        raise TypeError(m)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if not all(isinstance(x, (int, float)) for x in matrix[0]):
        raise TypeError(m)
    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """ Returns a new matrix """
    return [[round(x / div, 2) for x in row] for row in matrix]

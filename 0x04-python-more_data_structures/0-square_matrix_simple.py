#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()
    for b in range(len(matrix)):
        n_matrix[b] = list(map(lambda n: n ** 2, matrix[b]))
    return (n_matrix)

#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Matrix division function
    Args:  matrix: matrix div: divisor
    Returns:  A new matrix """

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(message)

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)

        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for elem in row:
            if (not isinstance(elem, int) and not isinstance(elem, float)):
                raise TypeError(message)
            new_row += [round(elem / div, 2)]
        new_matrix += [new_row]

    return new_matrix

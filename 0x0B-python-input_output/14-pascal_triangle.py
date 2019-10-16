#!/usr/bin/python3
"""
This is the "14-pascal_triangle" module.
It supplies one function, pascal_triangle.
"""


def pascal_triangle(n):
    """pascal_triangle"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            elem = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(elem)
        row.append(1)
        triangle.append(row)
    return triangle

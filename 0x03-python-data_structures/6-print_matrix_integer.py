#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    if len(matrix[0]) == 0:
        print()
    for row in matrix:
        for j in row:
            print("{:d}".format(j), end="")
            i += 1
            if i % len(row):
                print(end=" ")
            else:
                print()

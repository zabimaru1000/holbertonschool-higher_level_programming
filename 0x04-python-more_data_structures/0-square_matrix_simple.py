#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    blank = []

    for i in matrix:
        for j in i:
            blank.append(j*j)

    slicer = len(blank) ** (1/2)
    new = [blank[i:i+int(slicer)] for i in range(0, len(blank), int(slicer))]

    return new

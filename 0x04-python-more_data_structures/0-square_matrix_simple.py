#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    blank = []
    a = []
    for x in range(len(matrix)):
        a += matrix[x]

    for i in range(len(a)):
        exp = a[i] ** 2
        blank.append(exp)

    new = [blank[i:i+3] for i in range(0, len(blank), 3)]
    return new

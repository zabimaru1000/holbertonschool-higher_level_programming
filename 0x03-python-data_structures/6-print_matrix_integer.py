#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        digit_count = 0

        for j in i:
            if digit_count < len(i) - 1:
                print("{:d}".format(j), end=" ")

            else:
                print("{:d}".format(j), end="")

            digit_count = digit_count + 1

        print("")

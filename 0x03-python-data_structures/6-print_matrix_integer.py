#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        sep = 0
        for j in i:
            if sep == len(i) - 1:
                print("{:d}".format(j), end="")

            else:
                print("{:d}".format(j), end=" ")

            sep += 1

        print("")

#!/usr/bin/python3
"""
Function read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    reads a file and prints it
    """
    with open(filename, "r") as f:
        if nb_lines <= 0:
            print(f.read(), end="")

        lines = 0
        for i in f:
            if lines < nb_lines:
                print(i, end="")
                lines = lines + 1

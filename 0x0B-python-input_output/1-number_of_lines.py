#!/usr/bin/python3
"""
Function number_of_lines
"""


def number_of_lines(filename=""):
    """
    reads a file and prints it
    """
    with open(filename, "r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

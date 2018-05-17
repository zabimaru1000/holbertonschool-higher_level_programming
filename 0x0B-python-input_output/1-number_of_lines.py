#!/usr/bin/python3
"""
Function number_of_lines
"""


def number_of_lines(filename=""):
    """
    reads a file and prints it
    """
    lines = 0
    with open(filename, "r") as f:
        for i in f:
            lines = lines + 1
    return lines

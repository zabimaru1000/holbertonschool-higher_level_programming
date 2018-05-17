#!/usr/bin/python3
"""
Function read_file
"""


def read_file(filename=""):
    """
    reads a file and prints it
    """
    with open(filename, "r") as f:
        print(f.read(), end="")

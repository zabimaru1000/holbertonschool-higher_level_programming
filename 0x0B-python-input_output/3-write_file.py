#!/usr/bin/python3
"""
Function read_file
"""


def write_file(filename="", text=""):
    """
    reads a file and prints it
    """
    with open(filename, "w") as f:
        f.write(text)
    return len(text)

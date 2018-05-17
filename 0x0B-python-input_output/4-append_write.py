#!/usr/bin/python3
"""
Function read_file
"""


def append_write(filename="", text=""):
    """
    reads a file and prints it
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)

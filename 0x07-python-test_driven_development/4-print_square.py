#!/usr/bin/python3
"""
Module for print_square
Uses one function to print square
"""


def print_square(size):
    """
    Prints square
    """

    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

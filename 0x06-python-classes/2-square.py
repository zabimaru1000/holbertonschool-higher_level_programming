#!/usr/bin/python3
"""2-square.py: Makes a class called Square that checks if size is an int"""


class Square:
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        except TypeError:
            if type(size) != int:
                raise TypeError("size must be an integer")

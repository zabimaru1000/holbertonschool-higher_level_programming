#!/usr/bin/python3
"""3-square.py: Makes a class Square that gets the area of a size"""


class Square:
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size

        except TypeError:
                raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

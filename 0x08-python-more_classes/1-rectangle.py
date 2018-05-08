#!/usr/bin/python3
"""
Creates a class Rectangle
"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Method that initiates height and width
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Gets property for height
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Method to set height
        """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Method to set width
        """
        return self.width

    @width.setter
    def width(self, value):
        """
        Method to get width
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

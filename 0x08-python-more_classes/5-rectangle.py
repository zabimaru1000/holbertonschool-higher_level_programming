#!/usr/bin/python3
"""
Creates class Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Method that initiates height and width
        """
        self.__height = height
        self.__width = width

    def __str__(self):
        """
        Method to return string representation
        """
        string = ""
        if self.__height is 0 and self.__width is 0:
            return string
        for col in range(self.__height):
            for row in range(self.__width):
                string += "#"
            if col < self.__height - 1:
                string += "\n"

        return string

    def __repr__(self):
        """
        Method to return string representation
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.height)

    def __del__(self):
        """
        Method to delete instance
        """
        print("Bye rectangle...")

    @property
    def height(self):
        """
        Method to get height
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

    def area(self):
        """
        Method to return total area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to return total perimeter
        """
        return self.__width * 2 + self.__height * 2

#!/usr/bin/python3
"""
Class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Class inheriting from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor init
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets our width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets our width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets our height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets our height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

#!/usr/bin/python3
"""
Class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Class inheriting from class Base
    """
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
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor init that calls a super class: id
        Assigns private attributes to respective arguments
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

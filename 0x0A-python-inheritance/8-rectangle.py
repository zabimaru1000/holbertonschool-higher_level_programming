#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        w_inherit = self.integer_validator("width", width)
        h_inherit = self.integer_validator("height", height)
        self.__width = w_inherit
        self.__height = h_inherit

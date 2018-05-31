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
        Instantiation of above arguments and calls from Base
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """
        Returns string representation
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

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

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints hashes to stdout depending on area
        """
        for y in range(self.y):
            print()
        for col in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Updates the rectangle class
        """
        attr = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for i, value in enumerate(args):
                setattr(self, attr[i], value)
        if len(kwargs) > 0:
            for i, value in kwargs.items():
                setattr(self, i, value)

    def to_dictionary(self):
        """
        Returns dict representation of rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

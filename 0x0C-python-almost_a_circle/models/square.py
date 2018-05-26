#!/usr/bin/python3
"""
Class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of above arguments, calls from Rectangle
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Str representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        """
        Gets size and returns width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets size to width and height
        """
        self.width = value
        self.height = value

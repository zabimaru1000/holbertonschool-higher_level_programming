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

    def update(self, *args, **kwargs):
        """
        Updates the square class
        """
        attr = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i, value in enumerate(args):
                setattr(self, attr[i], value)
        if len(kwargs) > 0:
            for i, value in kwargs.items():
                setattr(self, i, value)

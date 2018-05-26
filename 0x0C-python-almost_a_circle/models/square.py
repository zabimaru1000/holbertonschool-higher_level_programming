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
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Str representation
        """
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y,
                                                       self.size)

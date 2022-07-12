#!/usr/bin/python3
"""
Defines a class square that inherits from class rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructore for a square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Update the height and width of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of a square
        Args:
            *args: New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """
        Return the print() and str() rep of a Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

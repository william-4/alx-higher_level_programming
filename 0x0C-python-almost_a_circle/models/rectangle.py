#!/usr/bin/python3
"""
A module that defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes each instance of Rectangle
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, w):
        """
        Sets the width of the rectangle
        """
        if type(w) != int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, h):
        """
        Sets the height of the rectangle
        """
        if type(h) != int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """
        Returns the x-coordinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returns the y-coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of a rectangle using args

        Args:
        *args: New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.__width, self.__height, self.__x,
                                      self.__y)
                    else:
                        self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle
        """
        return {
            "id": self.id
            "width": self.__width
            "height": self.__height
            "x": self.__x
            "y": self.__y
        }

    def __str__(self):
        """
        Overrides the __str__method so that it returns a custom string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

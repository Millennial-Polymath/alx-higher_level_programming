#!/usr/bin/python3
""" contains class Rectangle """
Base = __import__("base").Base

class Rectangle(Base):
    """
    Inherits from class Base
    Attributes:
             width (int)
             height (int)
             x (int)
             y (int)
             id (int)
    Methods:
          __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialises class attributes
        Argss:
            width
            height
            x
            y
            id
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise ValueError("x must be an integer")
        if not isinstance(y, int):
            raise ValueError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints out the Rectangle instance with the character #
        """
        for i in range(self.__height):
            print("#" * self.__width)
        print()
    def __str__(self):
        """
        Returns a string fromat of the rectangle
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.__x, self.__y,
                                                 self.__width, self.__height))
    def display(self):
        """
        Prints in stdout the Rectangle instance with the character by taking
        care of x and y
        """
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Assigns a key/valye argumenys to attributes
        Args:
            args: No key-word arument
            Kwargs: Keyword arguments
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        try:
            self.__id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        return {'id': getattr(self, 'id'),
                'width': getattr(self, 'width'),
                'height': getattr(self, 'height'),
                'x': getattr(self, 'x'),
                'y': getattr(self, 'y')}

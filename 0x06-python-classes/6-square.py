#!/usr/bin/python3
""" Module contains: Class Square """


class Square:
    """
    Square: defines a square
    Attributes:
        size: size of the square.
    Method:
        __init__: Initialises size attribute in  each of class instance
        area: calculates area of a square
        my_print: prints in the stdout the square with the character '#'
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter method for the private attribute size
            Args: self
            Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the private attribute size
            Args: self
            Return: None
        """
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ Getter function for private attribute position
            Args: self
            Return: position
        """
        return self.__position

    @position.setter
    def position(self, tu_value):
        """ Setter method for the private attribute position
            Args: self, tu_value(tuple)
            Return: None
        """
        if isinstance(tu_value, tuple) and len(value) == 2:
            for item in tu_value:
                if isinstance(item, int) and item >= 0:
                    self.__position = tu_value
        else:
            raise TypeError("position must be \
            a tuple of 2 positive integers")

    def area(self):
        """ Public instance method to calc. the area of a square
            Args: self
            Return: Area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Public instance method to print square with char. '#'
            Args: self
            Return: None
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], "#" * self.__size))

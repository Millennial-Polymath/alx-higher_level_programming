#!/usr/bin/python3
""" Module contains: Class Square """


class Square:
        """
        Square: defines a square
        Attributes:
            size: size of the square.
        Method:
    __init__: initialialises size attribute in each of class instances
    """
        def __init__(self, size=0):
                self.__size = size

        @property
        def size(self):
                """ Getter function for the private attribute size
                Returns:
                     size
                """
                return self.__size

        @size.setter
        def size(self, value):
                """setter function for private attribute size.
            Args:
                value: value to be set.
            Return:
                Returns nothing """
                if isinstance(value, int):
                        self.__size = value
                        if value < 0:
                                raise ValueError("size must be >= 0")
                else:
                        raise TypeError("size must be an integer")

        def area(self):
                """
                area of the square
                Returns:
                square of size(area)
                """
                return self.__size * self.__size

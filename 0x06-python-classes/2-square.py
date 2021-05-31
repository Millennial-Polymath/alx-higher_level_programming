#!usr/bin/python3
""" Module contains: class Square """


class Square:
    """
        Square: defines a square.
        Attributes:
                 size : size of the square

        Method:
            __init__: initialise size attribute of each class instance
    """

    def __init__(self, size=0):
        """ Initialisation of attributes for class instances
            Args:
                 size: size of the square
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

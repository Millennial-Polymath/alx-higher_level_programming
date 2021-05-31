#!/usr/bin/python3
""" Module 5  contains: class square """


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
        """ getter function for private attribute size
            Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter function for private attribute size
            Args:
                value: the value to be assigned to size
            Return: Nothing
        """
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ public instance method calculates the area of a square
            args: None
            Return: current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """ Public instance method to print to stdout the square with "#"
            Args: None
            Return: None
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
                print("#" * self.__size, end='')
                print()

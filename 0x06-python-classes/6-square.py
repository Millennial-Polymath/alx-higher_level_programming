#!/usr/bin/python3
""" Module contains: Class Square """


class Square:
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
        for item in tu_value:
            if not isinstance(item, int):
                raise TypeError("position must be \
                a tuple of 2 positive integers")
        self.__position = tu_value

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

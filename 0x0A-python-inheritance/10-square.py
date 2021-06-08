#!/usr/bin/python3
""" 10-square: class Square """
Rectangle = __import__("9-rectangle").Rectangle
class Square(Rectangle):
    """
    Square - inherits from Rectangle
    Attributes:
            size: size of the rectangle
    Methods:
          area() - calculates the area of the rectangle
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size


    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle",
                                    self.__size,
                                    self.__size))

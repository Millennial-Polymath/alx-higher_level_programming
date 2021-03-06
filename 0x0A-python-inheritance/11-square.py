#!/usr/bin/python3
""" 11-square: class square"""
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size))

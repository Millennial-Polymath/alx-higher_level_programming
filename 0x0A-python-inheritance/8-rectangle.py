#!/usr/bin/python3

""" 8-rectangle: class Rectangle """
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle inherits from BaseGeometry
    Attributes:
             width: width of rectangle
             height: Height of the rectangle
    Methods:
            __init__ - initialises the Rectangle instance
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

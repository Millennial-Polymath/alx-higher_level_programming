#!/usr/bin/python3
"""
contains class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialiases the attributes
        """
       super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        public getter for attribute size
        """
        return self.width
    @size.setter
    def size(self, value):
        """
        public setter for attribute size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assign args to attributes
        """
        if len(args) ==  0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
        returns string version of the attributes
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))


    def get_to_dictionary(self):
        """
        Returns the dictionary representation of a square
        """
        return {'id': getattr(self, 'id'),
                'size': getattr(self, 'size'),
                'x': getattr(self, 'x'),
                'y': getattr(self, 'y')}

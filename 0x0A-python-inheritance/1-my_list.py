#!/usr/bin/python3
""" Module contains class: MyList """

class MyList(list):
    def print_sorted(self):
        """
           prints a list in ascending order
        """
        print(sorted(self))

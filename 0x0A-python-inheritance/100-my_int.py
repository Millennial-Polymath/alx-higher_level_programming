#!/usr/bin/python3
""" 100-my_int: Class MyInt """
class MyInt(int):
    def __init__(self, number):
        self.number = number
    def __eq__(self, value):
        return (self.number != value)
    def __ne__(self, value):
        return self.number == value

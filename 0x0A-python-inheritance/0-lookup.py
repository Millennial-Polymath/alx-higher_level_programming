#!/usr/bin/python3

""" Module contains a function:lookup """

def lookup(obj):
    """ Function: lookup
        args: class instance(object)
        return: list of available attributes and methods of an object
    """
    return dir(obj)

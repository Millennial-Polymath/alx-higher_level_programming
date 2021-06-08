#!/usr/bin/python3
""" 4-inherits_from: inherits_from """

def inherits_from(obj, a_class):
    """
    Returns true if the object is an instance of a sub-class,oherwise, false
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False

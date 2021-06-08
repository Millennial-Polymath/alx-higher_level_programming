#!/usr/bin/python3

""" 2-is_same_class : is_same_class"""


def is_same_class(obj, a_class):
    """
       is_same_class: Returns true if the object is exactly an instanec of \
    specified class; otherwise False
    """

    if type(obj) is a_class:
        return True
    else:
        return False


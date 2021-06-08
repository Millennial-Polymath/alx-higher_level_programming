#!/usr/bin/python3
""" 101-ad_attribute: Function that adds a new atribute to an object """

def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

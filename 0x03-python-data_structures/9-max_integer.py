#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        y = 0
        for x in my_list:
            if x > y:
                y = x
        return y
    else:
        return None

#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = [x for x in dict.fromkeys(my_list)]
    sumTotal = 0
    for i in unique:
        sumTotal += i

    return sumTotal

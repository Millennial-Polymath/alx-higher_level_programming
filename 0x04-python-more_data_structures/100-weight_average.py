#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_final = 0
        wght = 0
        for i in my_list:
            b = [tp for tp in i]
            product = b[0] * b[1]
            wght += b[1]
            sum_final += product
            average = sum_final / wght
        return average

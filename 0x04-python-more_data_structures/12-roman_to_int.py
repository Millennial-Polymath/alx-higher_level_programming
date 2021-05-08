#!/usr/bin/python3
def roman_to_int(roman_string):
    numb = 0
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in range(len(roman_string)-1, -1, -1):
        num = roman[roman_string[i]]
        if 4 * num < numb:
            numb -= num
        else:
            numb += num
    return numb

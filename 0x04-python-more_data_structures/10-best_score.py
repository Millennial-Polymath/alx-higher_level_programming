#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big = 0
        for key, value in a_dictionary.items():
            if value > big:
                big = value

    if a_dictionary:
        for k, val in a_dictionary.items():
            if val == big:
                return k

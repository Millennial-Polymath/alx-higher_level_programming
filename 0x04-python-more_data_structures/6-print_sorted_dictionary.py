#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.keys())
    for key in sorted_list:
        print("{:s}: {}".format(key, a_dictionary[key]))
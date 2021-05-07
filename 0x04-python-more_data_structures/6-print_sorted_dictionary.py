#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_items = a_dictionary.items() # call items to return key-value pairs
    sorted_dict = dict(sorted(dict_items, key=lambda kv: kv[0].upper())) # returns tuples
    for key, value in sorted_dict.items():
        print(key, ':', value)

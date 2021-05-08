#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    if value in a_dictionary.values():
        for key, v in a_dictionary.items():
            if value == v:
                del_list.append(key)

        for item in del_list:
            del a_dictionary[item]

    return a_dictionary

#!/usr/bin
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        if len(tuple_a) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_b[1]
        elif len(tuple_b) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1]
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + tuple_b[1]

    else:
        if len(tuple_a) == 0 and tuple_b:
            a = tuple_b[0]
            b = tuple_b[1]
        elif len(tuple_b) == 0 and tuple_a:
            a = tuple_a[0]
            b = tuple_a[1]
        else:
            a = 0
            b = 0
    tuple_result = a,b
    return tuple_result

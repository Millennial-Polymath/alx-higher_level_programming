#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        quot = a / b
        return quot
    except ZeroDivisionError:
        return None
    finally:
        print("Inside Result: {}".format(quot if b != 0 else None))

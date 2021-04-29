#!/usr/bin/python3
import sys
if __name__ == "__main__":
    str_len = len(sys.argv)
    if (str_len - 1 == 1):
        args = "argument:"
    elif (str_len == 1):
        args = "arguments."
    else:
        args = "arguments:"
    print("{:d} {:s}".format(str_len - 1, args))

    for i in range(1, str_len):
        print("{:d}: {:s}".format(i, sys.argv[i]))

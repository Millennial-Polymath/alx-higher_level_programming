#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    some_list = []

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    funcs = dir(calculator_1)
    for fun in funcs:
        if not fun.startswith("__"):
            f = getattr(calculator_1, fun)
            some_list.append(f)

#    print(some_list[0](int(a), int(b)))


    if (operator == '+'):
        print("{:d} + {:d} = {:d}".format(int(a), int(b), some_list[0](int(a), int(b))))
    elif operator == '-':
        print("{} - {} = {:d}".format(a, b, some_list[1](int(a), int(b))))
    elif operator == '*':
        print("{} * {} = {:d}".format(a, b, some_list[2](int(a), int(b))))
    elif operator == '/':
        print("{} / {} = {:d}".format(a, b, some_list[3](int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

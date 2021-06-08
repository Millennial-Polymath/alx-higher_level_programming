#!/usr/bin/python3

import sys
from print import print_hello

for args in sys.argv:
    print(args, end=' ')
    print()


print_hello()

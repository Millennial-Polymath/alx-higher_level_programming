#!/usr/bin/python3
def remove_char_at(str, n):
    s = list(str)
    for i in range(len(s)):
        if i == n + 1:
            s[n] = ""
            return s

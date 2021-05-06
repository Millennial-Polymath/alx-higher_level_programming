#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        tuple_a = (len(sentence), sentence[0])
    else:
        tuple_a = (len(sentence), None)
    return tuple_a

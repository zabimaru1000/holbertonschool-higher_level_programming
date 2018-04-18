#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        letter = None

    else:
        letter = sentence[0]

    tup1 = (len(sentence), letter)
    return tup1

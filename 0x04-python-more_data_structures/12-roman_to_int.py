#!/usr/bin/python3
def roman_to_int(roman_string):
    rdict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    prev = 1001
    total = 0

    if roman_string is not None:
        for i in roman_string:
            if rdict[i] > prev:
                total += rdict[i] - (prev * 2)
            else:
                total += rdict[i]
                prev = rdict[i]

        return total

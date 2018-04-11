#!/usr/bin/python3
def uppercase(str):
    upper = ""

    for i in str:
        if 'a' <= i and i <= 'z':
            strIndex = ord(i) - ord('a')
            ordVal = strIndex + ord('A')
            i = chr(ordVal)
        upper = upper + i

    print(upper, end="\n")

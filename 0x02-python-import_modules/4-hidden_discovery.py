#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    a = dir(hidden_4)
    b = "__"

    for i in range(0, 11):
        if a[i][0:2] != b:
            print("{}".format(a[i]))

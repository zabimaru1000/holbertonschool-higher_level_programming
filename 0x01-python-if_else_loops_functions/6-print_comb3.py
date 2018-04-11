#!/usr/bin/python3
for i in range(1, 90):
    if i < 89:
        if i % 11 != 0 and i % 10 != 0:
            print("{:02d}".format(i), end=", ")

    else:
        print(i)

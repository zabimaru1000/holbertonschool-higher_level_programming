#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv)

    if ac == 1:
        print("0")

    elif ac > 1:
        sum = 0
        for i in range(1, ac):
            sum = sum + int(sys.argv[i])

        print("{:d}".format(sum))

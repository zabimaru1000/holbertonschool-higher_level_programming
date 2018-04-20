#!/usr/bin/python3
def uniq_add(my_list=[]):
    cmp_list = []
    sum = 0

    for i in my_list:
        if i not in cmp_list:
            cmp_list.append(i)
            sum += i

    return sum

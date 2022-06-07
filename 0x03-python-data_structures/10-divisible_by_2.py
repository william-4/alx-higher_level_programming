#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if my_list:
        for i in my_list:
            new.append(False if elm % 2 else True)
    return (new)

#!/usr/bin/python3
def max_integer(my_list=[]):
    if not bool(my_list):
        return ("None")
    else:
        maxim = my_list[0]
        for num in my_list:
            if num > maxim:
                maxim = num
        return (maxim)

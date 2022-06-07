#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[l]))
        l -= 1

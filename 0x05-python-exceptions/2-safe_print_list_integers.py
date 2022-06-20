#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            if (isinstance(my_list[i], int)):
                print("{:d}".format(my_list[i]), end="")
            i += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (i)

#!/usr/bin/python3
def uppercase(str):
    for char in str:
        j = ord(char)
        if j in range(97, 123):
            j -= 32
        print("{:c}".format(j), end="")
    print()

#!/usr/bin/python3
"""
This module contains the function text_indentation
which prints 2 new lines after '.', '?', ':'

"""
def text_indentation(text):
    """
    this function adds two new lines after '.', '?' or ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    check = 0
    for i in text:
        if check == 0:
            if i == ' ':
                continue
            else:
                check = 1
        if check == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                check = 0
            else:
                print(i, end="")

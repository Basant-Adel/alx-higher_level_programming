#!/usr/bin/python3
def no_c(my_string):
    no_c_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            no_c_string += ch
    return no_c_string

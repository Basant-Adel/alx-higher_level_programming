#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_add = 0
    for n in set(my_list):
        n_add += n
    return n_add

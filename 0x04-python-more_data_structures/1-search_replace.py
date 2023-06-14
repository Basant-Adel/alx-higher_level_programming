#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for n in my_list:
        if n == search:
            n_list.append(replace)
        else:
            n_list.append(n)
    return n_list

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = a_dictionary.copy()
    for n in n_dictionary:
        n_dictionary[n] = n_dictionary[n] * 2
    return (n_dictionary)

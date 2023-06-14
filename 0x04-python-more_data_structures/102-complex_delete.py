#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a in list(a_dictionary):
        if value == a_dictionary.get(a):
            del a_dictionary[a]
    return (a_dictionary)

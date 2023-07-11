#!/usr/bin/python3
''' A function that writes an Object to a text file '''
import json


def save_to_json_file(my_obj, filename):
    '''
    Save To JSON File
    '''

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))

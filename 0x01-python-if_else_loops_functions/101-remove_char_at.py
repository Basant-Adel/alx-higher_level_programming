#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    for ch in range(len(str)):
        if ch != n:
            new += str[ch]
    return (new)

#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write File -> Return Number of characters
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

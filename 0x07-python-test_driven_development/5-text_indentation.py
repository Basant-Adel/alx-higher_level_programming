#!/usr/bin/python3
"""
Write a function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ Text Indentation """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in ".?:":
        list = text.split(i)
        text = ""
        for j in list:
            text += j.strip(" ")
            if j is not list[-1]:
                text += i + "\n\n"
    print(text, end="")
    """ Print Text """

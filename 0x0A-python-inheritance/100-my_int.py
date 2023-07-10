#!/usr/bin/python3
""" 100-my_int """


class MyInt(int):
    """ Write a class My Int that inherits from int """

    def __eq__(self, value):
        """ Override == """

        return self.real != value

    def __ne__(self, value):
        """ Override != """

        return self.real == value

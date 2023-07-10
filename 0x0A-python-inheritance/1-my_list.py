#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    My List
    """

    def print_sorted(self):
        """
        Public instance method:
        prints the list,
        but sorted (ascending sort)
        """

        print(sorted(self))

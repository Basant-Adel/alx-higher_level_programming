#!/usr/bin/python3
""" Write a class Student that defines a student """


class Student:
    """ Student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ To JSON """

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)

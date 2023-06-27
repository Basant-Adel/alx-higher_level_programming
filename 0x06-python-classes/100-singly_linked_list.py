#!/usr/bin/python3
""" Defines Linked List """


class Node:
    """ Linked List """

    def __init__(self, data, next_node=None):
        """ Private instance attribute: data """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Data """

        return (self.__data)

    @data.setter
    def data(self, value):
        """ Data """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """ Next Node """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Next Node """

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """ Singly Linked List """

    def __init__(self):
        """ Init """

        self.head = None

    def __str__(self):
        """ Prints List """

        printsll = ""
        location = self.head

        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """ Inserts Sorted """

        new = Node(value)

        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        location = self.head

        while location.next_node and location.next_node.data < value:
            location = location.next_node

        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new

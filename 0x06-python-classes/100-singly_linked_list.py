#!/usr/bin/python3
"""Singly linked list implementation"""


class Node:
    """Node class"""

    def __init__(self, n, nxt_n=None):
        """constructor"""
        if type(n) is not int:
            raise TypeError('data must be an integer')
        self.__data = n
        if nxt_n is not None and type(nxt_n) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = nxt_n

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, n):
        """data setter"""
        if type(n) is not int:
            raise TypeError('data must be an integer')
        self.__data = n

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """next_node setter"""
        if node is not None and type(node) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = node


class SinglyLinkedList:
    """ Single linked list class"""

    def __init__(self):
        """constructor"""
        self.__head: Node = None

    def __str__(self):
        """to string method"""
        s = []
        node: Node = self.__head
        while node is not None:
            s.append(str(node.data))
            node = node.next_node
        return '\n'.join(s)

    def sorted_insert(self, value):
        """public method that insert a new node to the list in sorted way"""
        new_node: Node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        node = self.__head
        while node.next_node is not None and value > node.next_node.data:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node

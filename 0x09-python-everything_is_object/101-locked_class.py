#!/usr/bin/python3
"""
for preventing dynamic attributes creation

"""


class LockedClass():
    """class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """constructor"""
        pass

#!/usr/bin/python3
"""int module"""


class MyInt(int):
    """MyInt inherits int"""

    def __eq__(self, other):
        """override == operator with != behavior"""
        return self.real != other

    def __ne__(self, other):
        """override != operator with == behavior"""
        return self.real == other

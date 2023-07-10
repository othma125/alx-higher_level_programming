#!/usr/bin/python3
"""list module"""


class MyList(list):
    """MyList inherits list"""

    def print_sorted(self):
        """
        sort before print
        :return:
        :rtype:
        """
        print(sorted(self))

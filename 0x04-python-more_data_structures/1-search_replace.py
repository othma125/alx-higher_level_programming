#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return [replace if x is search else x for x in my_list]

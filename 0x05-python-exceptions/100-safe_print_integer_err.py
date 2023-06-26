#!/usr/bin/python3
def safe_print_integer_err(v):
    try:
        print("{:d}".format(v))
    except Exception as e:
        from sys import stderr
        stderr.write('Exception: {}\n'.format(e))
        return False
    else:
        return True

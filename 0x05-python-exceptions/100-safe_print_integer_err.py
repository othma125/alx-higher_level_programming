#!/usr/bin/python3
def safe_print_integer_err(v):
    import sys
    try:
        print("{:d}".format(v))
    except Exception as e:
        sys.stderr.write('Exception: {}\n'.format(e))
        return False
    else:
        return True

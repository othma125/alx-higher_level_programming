#!/usr/bin/python3
if __name__ == '__main__':
    """
    How to make a script dynamic
    """
    from sys import argv
    print("{} {}{}{}".format(len(argv) - 1,
                             "argument", "s" if len(argv) - 1 != 1 else "",
                             ":" if len(argv) - 1 > 0 else "."))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

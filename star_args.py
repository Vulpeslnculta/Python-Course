from __future__ import print_function


def average(*args):
    """Basic function for calculating mean from an indefinite string of arguments"""

    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))


def build_tuple(*args):
    """ Simple function packing any other type of data into a form of tuple"""
    return args


"""
Module containing utility functions
"""
import operator


def remap(x, in_min, in_max, out_min, out_max):
    """
    Map input value (knowing minimum and maximum values that it can take) to another range

    :param x: value to be mapped
    :param in_min: minimum value of input
    :param in_max: maximum value of input
    :param out_min: minimum value of output
    :param out_max: maximum value of output
    :return: changed value
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def constrain(value, max_val, min_val=0):
    """
    Constrain given value in given boundries

    :param value: value to be constrained
    :param max_val: value cannot be more than this
    :param min_val: returned value won't be lower than this
    :return: constrained value
    """
    if max_val < min_val:
        max_val, min_val = min_val, max_val
    return max(min_val, min(value, max_val))


def add_tuples(a: tuple, b: tuple) -> tuple:
    """
    Add subsequent elements of a tuple to each other.

    :param a: first tuple
    :param b: second tuple
    :return: result tuple
    """
    return tuple(map(operator.add, a, b))


def sub_tuples(a: tuple, b: tuple) -> tuple:
    """
    Subtract subsequent elements of a tuple from each other.
    a - b

    :param a: first tuple
    :param b: second tuple
    :return: result tuple
    """
    return tuple(map(operator.sub, a, b))


def merge_dicts(*dicts_to_merge):
    """
    Merge multiple dictionaries into one.
    Leaves originals unchanged.

    :param dicts_to_merge: dictionaries to be merged. Multiple dictionaries can be provided.
    :return: copy of merged dictionary (originals are left unchanged).
    """
    result = {}
    for dictionary in dicts_to_merge:
        result.update(dictionary)

    return result

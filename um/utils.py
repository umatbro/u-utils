"""
Module containing utility functions
"""
import sys
import operator
import functools
from time import time
from contextlib import contextmanager
from io import StringIO
from typing import Union, Hashable


def remap(x: Union[float, int], in_min: Union[float, int], in_max: Union[float, int], out_min: Union[float, int],
          out_max: Union[float, int]) -> float:
    """
    Map input value (knowing minimum and maximum values that it can take) to another range.

    :param x: value to be mapped
    :param in_min: minimum value of input
    :param in_max: maximum value of input
    :param out_min: minimum value of output
    :param out_max: maximum value of output
    :return: value mapped to a new range
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def constrain(value: Union[int, float], max_val: Union[float, int], min_val: Union[float, int]=0):
    """
    Constrain given value in given boundaries.

    :param value: value to be constrained
    :param max_val: value cannot be more than this
    :param min_val: returned value won't be lower than this
    :return: value constrained within given range
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


def merge_dicts(*dicts_to_merge: dict):
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


def timer(func):
    """
    Decorator function.
    Prints function execution time to console.

    :param func: function to be measured
    :return: function result (unchanged)
    """
    @functools.wraps(func)
    def timing(*args, **kwargs):
        start = time()
        func_result = func(*args, **kwargs)
        stop = time()
        print('Function \'{}\' executed in: {}s'.format(func.__name__, stop - start))
        return func_result

    return timing


@contextmanager
def captured_output():
    """
    Context manager to capture function output to console.

    Example usage:

    .. code-block:: python

        with captured_output() as (out, err):
            foo()
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()

    :return:
    """
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def memoize(function):
    """
    Decorator that stores in cache results from previous function calls
    (it can be used to boost performance).
    """
    function.cache = {}  # init function results cache

    class hashdict(dict):
        """Hashable dict - class to help hash kwargs"""
        def __hash__(self):
            return hash(tuple(sorted(self.items())))

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        hkwargs = hashdict(kwargs)
        # store function return value in cache if it is not stored already and return cached result
        if (args, hkwargs) not in function.cache:
            function.cache[(args, hkwargs)] = function(*args, **kwargs)

        return function.cache[(args, hkwargs)]

    return wrapper


def find_nested_key_value(dictionary: dict, key: Hashable):
    pass

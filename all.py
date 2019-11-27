"""more docstrings"""
#from typing import Callable, Iterable, Any, List
import functools


def new_all(initial_list):
    """docstring"""
    return functools.reduce(lambda x, y: (x and y) is True, initial_list)

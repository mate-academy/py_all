"""docstring"""
from typing import Iterable
import functools


def all_(iterable: Iterable[bool]) -> bool:
    """
    Returns True if all elements in the iterable are True
    otherwise, returns False
    :param iterable: Iterable[bool]
    :return: bool
    """
    return functools.reduce(lambda a, b: a and b, iterable)

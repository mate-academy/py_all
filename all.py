"""Create your own implementation of built-in all() function using reduce()."""
from typing import Iterable
from functools import reduce


def all_(array: Iterable[bool]) -> bool:
    """Return True if all elements of the iterable are true"""
    return reduce(lambda x, y: x and y, array)

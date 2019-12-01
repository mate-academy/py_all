"""Own implementation of built-in all() function using reduce()"""

from typing import Iterable
from functools import reduce


def all_(arr: Iterable[bool]) -> bool:
    """Return True if all elements of iterable are True,
    else return False
    """
    return reduce(lambda x, y: x and y, arr)

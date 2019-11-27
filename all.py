"""
module all
"""

from typing import Iterable
from functools import reduce


def all_(lst: Iterable[bool]) -> bool:
    """
    Implementation of built-in all() function using reduce().
    :param lst: Iterable[bool]
    :return: bool
    """
    return reduce(lambda x, y: x and y is True, lst)

"""
docstring
"""
from typing import Iterable
from functools import reduce


def all_(lst: Iterable[bool]) -> bool:
    """

    :param lst:
    :return:
    """
    return reduce(lambda x, y: x & y, lst)

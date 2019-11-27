"""
all
"""
from typing import Iterable
import functools


def all_(items: Iterable[bool]) -> bool:
    """
    :param items: list
    :return: is all items true
    """
    return functools.reduce(lambda _, y: bool(y), items)

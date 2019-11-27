"""Custom function all module"""
from typing import Iterable
from functools import reduce


def all_(lst: Iterable[bool]) -> bool:
    """
    Custom function all
    :param lst: list for check
    :return: True or False
    """
    return reduce(lambda x, y: x and y, lst)

"""import"""
from typing import Iterable
from functools import reduce


def all_(lst: Iterable[bool]) -> bool:
    """all"""
    return reduce(lambda first, second: first and second, lst)

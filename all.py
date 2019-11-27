"""
Create your own implementation of built-in all() function using
"""


from typing import Iterable
import functools


def all_(lst: Iterable[bool]) -> bool:
    """My function all()"""
    return functools.reduce(lambda first, second: first and second, lst)

"""docstring"""
from typing import Iterable
from functools import reduce


def all_item(list_item: Iterable[bool]) -> bool:
    """return true if only all items is true"""

    return reduce(lambda x, y: x and y, list_item)

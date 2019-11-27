"""import"""
from typing import Iterable


def all_(lst: Iterable[bool]) -> bool:
    """all"""
    for ele in lst:
        if not ele:
            return False
    return True

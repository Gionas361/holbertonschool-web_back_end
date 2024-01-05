#!/usr/bin/env python3
"""
Takes takes a string 'k' and an int or float 'v' and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns an tuple of an string and an float"""
    return (k, v * v)

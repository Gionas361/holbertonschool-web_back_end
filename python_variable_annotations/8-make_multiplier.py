#!/usr/bin/env python3
"""
Takes 2 float variables and returns the sum of both of them.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiples a float by multiplier"""

    def multi(m: float) -> float:
        """Returns the multiplication of multiplier and the float m"""
        return (multiplier * m)

    return (multi)

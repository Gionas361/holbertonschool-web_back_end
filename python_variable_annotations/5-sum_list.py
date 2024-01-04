#!/usr/bin/env python3
"""
Takes a float list of floats and returns the sum
of all the values stored inside of it.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the all the values"""
    s = 0
    int: i
    i = 0

    for j in input_list:
        s += input_list[i]
        i += 1
    
    return (s)

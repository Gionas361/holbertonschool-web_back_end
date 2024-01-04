#!/usr/bin/env python3
"""
Takes a list with a mix of integers
and floats and sums they're values.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the mixed values"""
    suma = 0
    int: i
    i = 0

    for c in mxd_lst:
        suma += float(mxd_lst[i])
        i += 1
    
    return (float(suma))

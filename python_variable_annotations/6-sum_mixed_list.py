#!/usr/bin/env python3
"""
Takes a list with a mix of integers
and floats and sums they're values.
"""


def sum_mixed_list(mxd_lst: list) -> float:
    """Returns the sum of the mixed values"""
    suma = 0
    int: i
    i = 0

    for c in mxd_lst:
        suma += float(mxd_lst[i])
        i += 1
    
    return (float(suma))

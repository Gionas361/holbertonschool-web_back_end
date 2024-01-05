#!/usr/bin/env python3
"""
Takes 2 float variables and returns the sum of both of them.
"""
from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of Tuples, each tuple contains
    the element and lenght of the list."""
    return [(i, len(i)) for i in lst]
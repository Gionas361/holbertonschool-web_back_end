#!/usr/bin/env python3
"""
This is an coroutine that takes no arguments and
returns a list of the 10 random numbers.
"""
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Gives out a list of 10 random numbers.
    """
    return ([i async for i in async_generator()])
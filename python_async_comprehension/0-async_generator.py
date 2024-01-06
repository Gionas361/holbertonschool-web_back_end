#!/usr/bin/env python3
"""
This function contains a coroutine that will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    It will loop 10 times each with an interval of 1 second
    each time generating a number between 1 and 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

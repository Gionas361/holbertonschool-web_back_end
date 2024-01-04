#!/usr/bin/env python3
"""
An async routine that's called wait_n that receives two int arguments:
n and max_delay. It will spawn wait_random n times with
the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Spawns wait_random n times with the specified max_delay."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

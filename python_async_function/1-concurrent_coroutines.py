#!/usr/bin/env python3
"""
Asynchronous coroutine that spawns wait_random
n times with the specified max_delay.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay allowed.

    Returns:
        List[float]: List of all the delays
        (float values) in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)


if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))


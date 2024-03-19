#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay allowed. Defaults to 10.

    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))

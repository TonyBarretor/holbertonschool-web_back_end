#!/usr/bin/env python3
"""
Module to define a function task_wait_n.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create and return a list of asyncio.
    Tasks for wait_random coroutine.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay allowed.

    Returns:
        List[float]: List of all the delays
        (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))

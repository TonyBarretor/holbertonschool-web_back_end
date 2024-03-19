#!/usr/bin/env python3
"""
Module to define a regular function task_wait_random.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random coroutine.

    Args:
        max_delay (int): The maximum delay allowed.

    Returns:
        asyncio.Task: Task for wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))

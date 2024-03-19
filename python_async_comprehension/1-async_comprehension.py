#!/usr/bin/env python3
"""
Async Comprehension Module
"""

from typing import List
from random import uniform
from asyncio import gather

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers asynchronously.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [num async for num in async_generator()]


if __name__ == "__main__":
    import asyncio

    async def main():
        print(await async_comprehension())

    asyncio.run(main())

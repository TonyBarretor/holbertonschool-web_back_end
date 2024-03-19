#!/usr/bin/env python3
"""
Async Generator Module
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that generates random numbers asynchronously.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    import asyncio

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())

#!/usr/bin/env python3
"""
Measure Runtime Module
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    return end_time - start_time


if __name__ == "__main__":
    import asyncio

    async def main():
        return await measure_runtime()

    print(asyncio.run(main()))

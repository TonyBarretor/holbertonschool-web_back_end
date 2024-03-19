#!/usr/bin/env python3
"""
Module to measure the runtime of wait_n function.
"""
import time
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return total_time / n.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): The maximum delay allowed.

    Returns:
        float: Average execution time per call.
    """
    start_time = time.time()

    async def main():
        await __import__('1-concurrent_coroutines').wait_n(n, max_delay)

    asyncio.run(main())

    total_time = time.time() - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))


#!/usr/bin/env python3
"""Defines measure_time"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Calculates the runtime of wait_n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n

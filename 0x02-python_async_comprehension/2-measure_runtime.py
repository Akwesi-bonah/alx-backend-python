#!/usr/bin/env python3
"""Defines measure_runtime"""
import asyncio
from time import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of parallel coroutines"""
    start = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time() - start

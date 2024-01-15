#!/usr/bin/env python3
"""Defines task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times"""
    wait_list = await asyncio.gather(*tuple(map(lambda _: task_wait_random(
        max_delay), range(n))))
    sort_ = sorted(wait_list)
    return sort_

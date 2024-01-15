#!/usr/bin/env python3
"""Defines the basic async syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async syntax"""
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait

#!/usr/bin/env python3
"""Defines async_generator"""
from random import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Yield a random integer 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10

#!/usr/bin/env python3
"""Defines async_comprehension"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Create a list of 10 floats from async_generator"""
    return [i async for i in async_generator()]

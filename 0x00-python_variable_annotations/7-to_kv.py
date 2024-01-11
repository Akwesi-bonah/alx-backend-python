#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple """
    return (k, v * v)


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))

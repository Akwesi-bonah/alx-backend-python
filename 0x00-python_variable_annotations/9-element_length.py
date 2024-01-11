#!/usr/bin/env python3
""" annotations - let's duck type an iterable object """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples, each containing an element and its length """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length.__annotations__)

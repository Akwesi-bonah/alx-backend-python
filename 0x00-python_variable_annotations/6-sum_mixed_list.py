#!/usr/bin/env python3
""" Basic annotations  - mixed list"""

from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns the sum of all elements of a list """
    return sum(mxd_list)


if __name__ == "__main__":

    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}"
          .format(ans, type(ans)))

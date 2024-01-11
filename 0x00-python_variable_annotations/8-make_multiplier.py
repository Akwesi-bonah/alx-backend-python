#!/usr/bin/env python3
""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def multiply_by_multiplier(n: float) -> float:
        """ Returns the product of multiplier and n """
        return n * multiplier
    return multiply_by_multiplier


if __name__ == "__main__":
    make_multiplier = __import__('8-make_multiplier').make_multiplier
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))

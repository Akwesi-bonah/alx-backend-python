#!/usr/bin/env python3
""" Basic annotations - add """


def add(a: float, b: float) -> float:
    """ Returns the sum of two floats """
    return a + b


if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
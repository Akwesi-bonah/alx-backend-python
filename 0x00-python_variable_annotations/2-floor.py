#!/usr/bin/env python3
""" Basic annotations - floor """

def floor(n:float) -> int:
    """ Returns the floor of a float """
    return int(n)


if __name__ == "__main__":
    import math
    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

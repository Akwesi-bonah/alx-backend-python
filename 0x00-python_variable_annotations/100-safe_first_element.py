#!/usr/bin/env python3
""" annotations - first element of a sequence """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == '__main__':
    print(safe_first_element.__annotations__)

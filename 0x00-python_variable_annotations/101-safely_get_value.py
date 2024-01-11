#!/usr/bin/env python3
""" annotations - involved type annotations """

from typing import Any, Union, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """ Returns the value of a key in a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == '__main__':
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print(("{}: {}".format(k, v)))

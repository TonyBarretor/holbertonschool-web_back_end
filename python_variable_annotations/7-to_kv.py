#!/usr/bin/env python3
"""
Module: 7-to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element
    and the square of
    the int/float v as the second element (annotated as float).

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v.
    """
    return (k, v ** 2)

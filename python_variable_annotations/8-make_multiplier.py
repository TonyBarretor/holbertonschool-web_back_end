#!/usr/bin/env python3
"""
Module: 8-make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a
        float argument and
        returns the product of the input float and the multiplier.
    """
    def multiplier_function(num: float) -> float:
        """
        Inner function that multiplies a float by the multiplier.

        Args:
            num (float): The input float number.

        Returns:
            float: The product of num and multiplier.
        """
        return num * multiplier
    return multiplier_function

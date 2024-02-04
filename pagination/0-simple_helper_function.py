#!/usr/bin/env python3


"""
Module with a simple helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:

    """
    Return a tuple of start and end indices for pagination.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
    Tuple[int, int]:
    Start and end indices for the given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

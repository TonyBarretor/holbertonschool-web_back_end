#!/usr/bin/env python3

"""
Module with a simple helper function
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset.

        Args:
            page (int): Current page number (default is 1).
            page_size (int): Number of items per page (default is 10).

        Returns:
            List[List]: Paginated data.
        """
        assert isinstance(page, int) and page > 0, "Page must be a pos int"
        assert isinstance(page_size, int) and page_size > 0, "be a pos int"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return information about the current dataset page in a dictionary.

        Args:
            page (int): Current page number (default is 1).
            page_size (int): Number of items per page (default is 10).

        Returns:
            dict: Dictionary containing information about the dataset page.
        """

        assert isinstance(page, int) and page > 0, "Page must be a pos intr"
        assert isinstance(page_size, int) and page_size > 0, " be a pos int"

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page':
            page + 1 if page * page_size < len(self.dataset()) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

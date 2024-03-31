#!/usr/bin/env python3

"""
Module: 0-simple_helper_function
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end indx

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing
    """	
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

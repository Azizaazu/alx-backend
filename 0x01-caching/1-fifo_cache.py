#!/usr/bin/env python3
"""This module defines FIFOCache class"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    and implements a caching system using FIFO algorithm.
    """

    def __init__(self):
        """
        Initializes the FIFOCache object.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns item value to the dictionary self.cache_data
        for the given key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the given key in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
